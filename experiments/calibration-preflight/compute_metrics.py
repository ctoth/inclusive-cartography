"""Compute calibration metrics from cached screening results.

Outputs:
- metrics.json: all numeric results
- reliability-diagram.png: per-provider reliability diagrams
- confidence-histogram.png: per-provider verbalized-confidence histogram

Primary-run metrics computed per provider:
- confusion matrix (4 classes: rq1, rq2, rq3, excluded)
- per-class precision, recall, F1; overall accuracy
- ECE (correctness binary) — 10 equal-width bins
- ECE (include/exclude binary)
- AUROC on the include/exclude task using verbalized confidence
- reliability-diagram data
- threshold analysis at Wabiski's 0.70 / 0.90 cutoffs
- confidence histogram + clustering at multiples of 5
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support, roc_auc_score

HERE = Path(__file__).resolve().parent
TEST_SET = HERE / "test_set.jsonl"
CACHE = HERE / "cache"
OUT_JSON = HERE / "metrics.json"
OUT_REL = HERE / "reliability-diagram.png"
OUT_HIST = HERE / "confidence-histogram.png"

TAGS = ["screening:rq1", "screening:rq2", "screening:rq3", "screening:excluded"]
GT_TO_TAG = {
    "rq1": "screening:rq1",
    "rq2": "screening:rq2",
    "rq3": "screening:rq3",
    "excluded": "screening:excluded",
}


def load_items() -> list[dict]:
    return [json.loads(l) for l in TEST_SET.read_text(encoding="utf-8").splitlines() if l.strip()]


def load_cache(provider: str, model: str) -> list[dict]:
    d = CACHE / provider / model
    recs = []
    for f in sorted(d.glob("*.json")):
        r = json.loads(f.read_text(encoding="utf-8"))
        # Keep only the primary T=0 N=0 run
        if r.get("temperature") == 0 and r.get("sample_idx") == 0:
            recs.append(r)
    return recs


def expected_calibration_error(confidences: list[float], correct: list[int], n_bins: int = 10) -> tuple[float, list[dict]]:
    """Compute ECE with n equal-width bins. Returns (ece, bin_data)."""
    confidences = np.asarray(confidences, dtype=float)
    correct = np.asarray(correct, dtype=float)
    edges = np.linspace(0.0, 1.0, n_bins + 1)
    ece = 0.0
    N = len(confidences)
    bins = []
    for i in range(n_bins):
        lo, hi = edges[i], edges[i + 1]
        if i == n_bins - 1:
            mask = (confidences >= lo) & (confidences <= hi)
        else:
            mask = (confidences >= lo) & (confidences < hi)
        count = int(mask.sum())
        if count == 0:
            bins.append({"lo": float(lo), "hi": float(hi), "count": 0, "mean_conf": None, "acc": None})
            continue
        mean_conf = float(confidences[mask].mean())
        acc = float(correct[mask].mean())
        ece += (count / N) * abs(mean_conf - acc)
        bins.append({"lo": float(lo), "hi": float(hi), "count": count, "mean_conf": mean_conf, "acc": acc})
    return float(ece), bins


def analyse_provider(provider: str, model: str, items_by_id: dict) -> dict:
    recs = load_cache(provider, model)
    # Align records with items
    aligned = []
    missing = 0
    parse_errors = 0
    for r in recs:
        item = items_by_id.get(r["item_id"])
        if not item:
            continue
        parsed = r.get("parsed") or {}
        tag = parsed.get("tag")
        conf = parsed.get("confidence_score")
        if tag not in TAGS or conf is None:
            parse_errors += 1
            continue
        aligned.append(
            {
                "id": item["id"],
                "gt": GT_TO_TAG[item["ground_truth"]],
                "pred": tag,
                "conf": float(conf),
                "input_tokens": r.get("usage", {}).get("input_tokens") or 0,
                "output_tokens": r.get("usage", {}).get("output_tokens") or 0,
            }
        )
    missing = len(items_by_id) - len(aligned) - parse_errors

    if not aligned:
        return {"provider": provider, "model": model, "error": "no aligned records"}

    y_true = [a["gt"] for a in aligned]
    y_pred = [a["pred"] for a in aligned]
    confidences = [a["conf"] for a in aligned]

    # 4-class confusion matrix
    cm = confusion_matrix(y_true, y_pred, labels=TAGS).tolist()
    prec, rec, f1, support = precision_recall_fscore_support(y_true, y_pred, labels=TAGS, zero_division=0)
    per_class = [
        {"tag": TAGS[i], "precision": float(prec[i]), "recall": float(rec[i]), "f1": float(f1[i]), "support": int(support[i])}
        for i in range(len(TAGS))
    ]
    overall_acc = float(np.mean([yt == yp for yt, yp in zip(y_true, y_pred)]))

    # Binary correctness
    correct = [1 if yt == yp else 0 for yt, yp in zip(y_true, y_pred)]
    ece_corr, bins_corr = expected_calibration_error(confidences, correct, n_bins=10)

    # Include/exclude binary — include = not excluded
    y_true_incl = [1 if yt != "screening:excluded" else 0 for yt in y_true]
    y_pred_incl = [1 if yp != "screening:excluded" else 0 for yp in y_pred]
    # Correct on the include-vs-exclude task
    incl_correct = [1 if yt == yp else 0 for yt, yp in zip(y_true_incl, y_pred_incl)]
    ece_incl, _ = expected_calibration_error(confidences, incl_correct, n_bins=10)

    # Per-item "probability the item is an include" — LLM didn't give us this
    # directly, so we use: verbalized confidence if predicted include, else 1-conf
    incl_score = [
        c if yp != "screening:excluded" else (1.0 - c)
        for yp, c in zip(y_pred, confidences)
    ]
    try:
        auroc = float(roc_auc_score(y_true_incl, incl_score))
    except Exception:
        auroc = None

    # Threshold analysis — evaluated against CORRECTNESS of the prediction
    # (Wabiski's rule gates on verbalized confidence_score attached to the tag)
    auto_include = [(a, c) for a, c in zip(aligned, confidences) if c > 0.90]
    auto_exclude = [(a, c) for a, c in zip(aligned, confidences) if c < 0.70]
    human_review = [(a, c) for a, c in zip(aligned, confidences) if 0.70 <= c <= 0.90]
    ai_correct = sum(1 for a, c in auto_include if a["gt"] == a["pred"])
    ae_correct = sum(1 for a, c in auto_exclude if a["gt"] == a["pred"])
    # Also: how many of the auto-include band items are ACTUALLY positive
    # regardless of whether the tag matches exactly
    ai_actually_pos = sum(
        1 for a, c in auto_include if a["gt"] != "screening:excluded"
    )
    ae_actually_neg = sum(
        1 for a, c in auto_exclude if a["gt"] == "screening:excluded"
    )

    threshold_analysis = {
        "auto_include_gt_0.90": {
            "count": len(auto_include),
            "fraction_of_total": len(auto_include) / len(aligned),
            "tag_correct": ai_correct,
            "tag_correct_rate": (ai_correct / len(auto_include)) if auto_include else None,
            "actually_positive": ai_actually_pos,
            "actually_positive_rate": (ai_actually_pos / len(auto_include)) if auto_include else None,
        },
        "auto_exclude_lt_0.70": {
            "count": len(auto_exclude),
            "fraction_of_total": len(auto_exclude) / len(aligned),
            "tag_correct": ae_correct,
            "tag_correct_rate": (ae_correct / len(auto_exclude)) if auto_exclude else None,
            "actually_negative": ae_actually_neg,
            "actually_negative_rate": (ae_actually_neg / len(auto_exclude)) if auto_exclude else None,
        },
        "human_review_0.70_to_0.90": {
            "count": len(human_review),
            "fraction_of_total": len(human_review) / len(aligned),
        },
    }

    # Confidence histogram / clustering at multiples of 5 (Xiong 2024 check)
    rounded = [round(c * 100) / 100 for c in confidences]
    conf_counter = Counter(rounded)
    mode_value, mode_count = conf_counter.most_common(1)[0]
    # Multiples-of-5 clustering: fraction of predictions whose conf (in %) is
    # within 0.005 of a multiple of 0.05
    def near_mult5(c: float) -> bool:
        return abs((c * 20) - round(c * 20)) < 0.01
    mult5_count = sum(1 for c in confidences if near_mult5(c))
    mult5_fraction = mult5_count / len(confidences)

    # Token usage → cost estimate
    in_tok = sum(a["input_tokens"] for a in aligned)
    out_tok = sum(a["output_tokens"] for a in aligned)

    return {
        "provider": provider,
        "model": model,
        "n_items": len(aligned),
        "n_parse_errors": parse_errors,
        "n_missing": missing,
        "overall_accuracy": overall_acc,
        "per_class": per_class,
        "confusion_matrix": {"labels": TAGS, "matrix": cm},
        "ece_correctness": ece_corr,
        "ece_correctness_bins": bins_corr,
        "ece_include_binary": ece_incl,
        "auroc_include": auroc,
        "threshold_analysis": threshold_analysis,
        "confidence_distribution": {
            "modal_value": float(mode_value),
            "modal_count": int(mode_count),
            "mult5_count": int(mult5_count),
            "mult5_fraction": float(mult5_fraction),
            "all_values": confidences,
        },
        "usage": {"input_tokens": in_tok, "output_tokens": out_tok},
    }


def plot_reliability(metrics: list[dict]) -> None:
    fig, axes = plt.subplots(1, len(metrics), figsize=(5 * len(metrics), 5), squeeze=False)
    for ax, m in zip(axes[0], metrics):
        bins = m["ece_correctness_bins"]
        mids = [(b["lo"] + b["hi"]) / 2 for b in bins]
        accs = [b["acc"] if b["acc"] is not None else 0 for b in bins]
        counts = [b["count"] for b in bins]
        ax.bar(mids, accs, width=0.09, edgecolor="black", alpha=0.7, label="empirical accuracy")
        ax.plot([0, 1], [0, 1], "k--", label="perfect calibration")
        for mid, acc, cnt in zip(mids, accs, counts):
            if cnt > 0:
                ax.text(mid, acc + 0.02, str(cnt), ha="center", fontsize=8)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.05)
        ax.set_xlabel("Verbalized confidence")
        ax.set_ylabel("Empirical accuracy")
        ax.set_title(
            f"{m['provider']} / {m['model']}\n"
            f"ECE={m['ece_correctness']:.3f} | AUROC={m['auroc_include']:.3f}"
        )
        ax.legend(loc="lower right", fontsize=8)
    plt.tight_layout()
    plt.savefig(OUT_REL, dpi=150)
    plt.close()


def plot_histogram(metrics: list[dict]) -> None:
    fig, axes = plt.subplots(1, len(metrics), figsize=(5 * len(metrics), 4), squeeze=False)
    for ax, m in zip(axes[0], metrics):
        vals = m["confidence_distribution"]["all_values"]
        ax.hist(vals, bins=np.linspace(0, 1, 21), edgecolor="black")
        ax.set_xlim(0, 1)
        ax.set_xlabel("Verbalized confidence")
        ax.set_ylabel("Count")
        ax.set_title(
            f"{m['provider']} / {m['model']}\n"
            f"mode={m['confidence_distribution']['modal_value']} "
            f"mult5={m['confidence_distribution']['mult5_fraction']:.2f}"
        )
    plt.tight_layout()
    plt.savefig(OUT_HIST, dpi=150)
    plt.close()


def analyse_secondary(provider: str, model: str, items_by_id: dict) -> dict | None:
    d = CACHE / provider / model
    # group by item_id
    samples: dict[str, list[dict]] = defaultdict(list)
    for f in sorted(d.glob("*__t1.0__*.json")):
        r = json.loads(f.read_text(encoding="utf-8"))
        samples[r["item_id"]].append(r)
    if not samples:
        return None
    rows = []
    for item_id, srs in samples.items():
        item = items_by_id.get(item_id)
        if not item:
            continue
        tags = []
        confs = []
        for r in srs:
            parsed = r.get("parsed") or {}
            tag = parsed.get("tag")
            conf = parsed.get("confidence_score")
            if tag in TAGS and conf is not None:
                tags.append(tag)
                confs.append(float(conf))
        if not tags:
            continue
        modal_tag, modal_count = Counter(tags).most_common(1)[0]
        agreement = modal_count / len(tags)
        rows.append(
            {
                "id": item_id,
                "gt": GT_TO_TAG[item["ground_truth"]],
                "modal_tag": modal_tag,
                "n_samples": len(tags),
                "agreement": agreement,
                "mean_conf": float(np.mean(confs)),
            }
        )
    if not rows:
        return None
    correct = [1 if r["modal_tag"] == r["gt"] else 0 for r in rows]
    agreements = [r["agreement"] for r in rows]
    mean_confs = [r["mean_conf"] for r in rows]

    acc = float(np.mean(correct))
    ece_agreement, _ = expected_calibration_error(agreements, correct, n_bins=10)
    ece_mean_conf, _ = expected_calibration_error(mean_confs, correct, n_bins=10)

    y_true_incl = [1 if r["gt"] != "screening:excluded" else 0 for r in rows]
    y_pred_incl = [1 if r["modal_tag"] != "screening:excluded" else 0 for r in rows]
    incl_score_agree = [
        a if yp == 1 else (1.0 - a) for a, yp in zip(agreements, y_pred_incl)
    ]
    try:
        auroc_agreement = float(roc_auc_score(y_true_incl, incl_score_agree))
    except Exception:
        auroc_agreement = None

    return {
        "provider": provider,
        "model": model,
        "n_items": len(rows),
        "n_samples_per_item": max(r["n_samples"] for r in rows),
        "accuracy_modal": acc,
        "mean_agreement": float(np.mean(agreements)),
        "ece_using_agreement": ece_agreement,
        "ece_using_mean_verbalized": ece_mean_conf,
        "auroc_using_agreement": auroc_agreement,
    }


def main() -> None:
    items = load_items()
    items_by_id = {it["id"]: it for it in items}

    provider_specs = [
        ("openai", "gpt-5"),
        ("gemini", "gemini-2.5-pro"),
    ]

    metrics = []
    secondary = []
    for provider, model in provider_specs:
        sec = analyse_secondary(provider, model, items_by_id)
        if sec is not None:
            secondary.append(sec)
            print(f"\n== secondary {provider}/{model} ==")
            print(json.dumps(sec, indent=2))
        try:
            m = analyse_provider(provider, model, items_by_id)
        except Exception as exc:  # noqa: BLE001
            print(f"skip {provider}/{model}: {exc}")
            continue
        metrics.append(m)
        print(f"\n=== {provider} / {model} ===")
        print(f"  N = {m['n_items']}")
        print(f"  accuracy = {m['overall_accuracy']:.3f}")
        print(f"  ECE (correctness) = {m['ece_correctness']:.3f}")
        print(f"  ECE (include-binary) = {m['ece_include_binary']:.3f}")
        print(f"  AUROC (include) = {m['auroc_include']}")
        print(f"  threshold analysis: {json.dumps(m['threshold_analysis'], indent=4)}")
        print(f"  mult5 fraction = {m['confidence_distribution']['mult5_fraction']:.3f}")

    out = {"primary": metrics, "secondary": secondary}
    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    plot_reliability(metrics)
    plot_histogram(metrics)
    print(f"\nWrote {OUT_JSON}, {OUT_REL}, {OUT_HIST}")


if __name__ == "__main__":
    main()
