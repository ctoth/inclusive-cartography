"""Build the calibration pre-flight test set.

Positives: 13 inclusive-cartography seed papers in this repo (abstract.md) plus
real arXiv papers retrieved via the arXiv query API for additional positives.
Negatives: arXiv papers from cs.CG / cs.GR / cs.CV / stat.ML + CrossRef general
cartography / general accessibility papers. Every item is a REAL published paper
with a REAL abstract — no fabrication.

Output: test_set.jsonl, one JSON object per line with fields:
  id, title, abstract, ground_truth (rq1|rq2|rq3|excluded), source, justification
"""

from __future__ import annotations

import json
import re
import time
from pathlib import Path
from urllib.parse import quote_plus

import httpx

REPO = Path(__file__).resolve().parents[2]
PAPERS = REPO / "papers"
OUT = Path(__file__).resolve().parent / "test_set.jsonl"

# ----- seed-paper -> RQ mapping (hand-assigned from reading index.md) -----
# RQ1: design principles / methods for diverse perceptual/cognitive abilities
# RQ2: technologies/tools/media (3D printing, haptics, sonification, adaptive interfaces)
# RQ3: transferability of inclusive cartographic practice across user groups
SEED_LABELS: dict[str, tuple[str, str]] = {
    # name: (rq, justification)
    "Brock_2015_InteractiveMapsUsability": (
        "rq2",
        "Compares interactive audio-tactile map technology (multi-touch + overlay + TTS) vs. classical raised-line map — directly about tools/media for accessibility.",
    ),
    "Brulé_2016_MapSenseMulti-SensoryInteractiveMaps": (
        "rq1",
        "Participatory design process and four design guidelines for multi-sensory interactive maps for visually impaired children — design principles for inclusive cartography.",
    ),
    "Ducasse_2018_AccessibleInteractiveMapsVisually": (
        "rq2",
        "Three-decade survey and DIM/HIM taxonomy of accessible interactive map technologies — technologies/tools/media comparison.",
    ),
    "Gual_2015_EffectVolumetric3DTactile": (
        "rq2",
        "Empirical comparison of flat microcapsule vs. 3D-printed volumetric symbol tactile maps — a technology/media evaluation.",
    ),
    "Götzelmann_2016_LucentMaps3DPrintedAudiovisual": (
        "rq2",
        "3D-printed translucent tactile overlays with capacitive CapCode IDs for consumer tablets — a tools/technology contribution for accessible cartography.",
    ),
    "Holloway_2018_AccessibleMapsBlindComparing": (
        "rq2",
        "Comparison of 3D-printed relief maps vs. swell-paper tactile graphics and an audio-label prototype — tools/technology evaluation.",
    ),
    "Palivcová_2020_InteractiveTactileMapTool": (
        "rq3",
        "Transfers tactile-map design principles to a new user group (visually impaired older adults in residential care), directly testing cross-group transferability.",
    ),
    "Papadopoulos_2018_OrientationMobilityAidsIndividuals": (
        "rq2",
        "Within-subjects comparison of audio-only verbal description vs. embossed audio-tactile map for O&M — a media/tools evaluation.",
    ),
    "Perkins_2002_CartographyProgressTactileMapping": (
        "rq1",
        "Progress review of tactile-mapping research across design, standards, production, substitutes and ethics — design principles and methods survey.",
    ),
    "Rowell_2003_WorldTouchResultsInternational": (
        "rq2",
        "International survey of tactile-map production technologies, media and symbol categories — tools/technologies adoption baseline.",
    ),
    "Rowell_Ungar_2003_WorldTouchProduction": (
        "rq2",
        "Companion production-side World Touch survey of tactile-map production technologies.",
    ),
    "Taylor_2016_Customizable3DPrintedTactile": (
        "rq2",
        "End-to-end OSM-to-conductive-PLA tactile map pipeline with Android audio-label app — tools/technology contribution.",
    ),
    "Wabinski_2022_GuidelinesStandardizingTactileMaps": (
        "rq1",
        "Consolidates measurable design guidelines (symbols, dimensions, generalization rules) for tactile maps — design principles reference.",
    ),
}

EXCLUDE_DIRS = {
    "Wabiski_2026_CognitiveReviewProtocol",  # the protocol itself
    "Kadavath_2022_LanguageModelsMostlyKnow",
    "Lin_2022_TeachingModelsExpressUncertainty",
    "Tian_2023_JustAskCalibrationStrategies",
    "Xiong_2024_LLMUncertaintyConfidenceElicitation",
}


def read_abstract(paper_dir: Path) -> tuple[str, str]:
    """Return (title, original_abstract_text) for a paper dir.

    Title is taken from metadata.json; abstract is the verbatim text under the
    'Original Text (Verbatim)' heading in abstract.md.
    """
    meta = json.loads((paper_dir / "metadata.json").read_text(encoding="utf-8"))
    title = meta.get("title", paper_dir.name)
    text = (paper_dir / "abstract.md").read_text(encoding="utf-8")
    # Grab text between "Original Text (Verbatim)" and the next '---' or '## '
    m = re.search(
        r"##\s+Original Text.*?\n(.*?)(?:\n---|\n##\s+|\Z)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not m:
        raise RuntimeError(f"no verbatim abstract in {paper_dir}")
    abstract = m.group(1).strip()
    # Collapse internal whitespace but keep paragraph breaks
    abstract = re.sub(r"[ \t]+", " ", abstract)
    return title, abstract


def load_seed_positives() -> list[dict]:
    items = []
    for name, (rq, just) in SEED_LABELS.items():
        pdir = PAPERS / name
        if not pdir.exists():
            raise FileNotFoundError(pdir)
        title, abstract = read_abstract(pdir)
        items.append(
            {
                "id": f"seed::{name}",
                "title": title,
                "abstract": abstract,
                "ground_truth": rq,
                "source": "repo-seed",
                "justification": just,
            }
        )
    return items


# ----- arXiv query helper -----
ARXIV_URL = "http://export.arxiv.org/api/query"


def arxiv_query(search: str, max_results: int = 10) -> list[dict]:
    params = {
        "search_query": search,
        "start": 0,
        "max_results": max_results,
        "sortBy": "relevance",
        "sortOrder": "descending",
    }
    for attempt in range(4):
        try:
            r = httpx.get(
                ARXIV_URL, params=params, timeout=30.0, follow_redirects=True
            )
            if r.status_code == 429:
                time.sleep(6.0 * (attempt + 1))
                continue
            r.raise_for_status()
            text = r.text
            break
        except httpx.HTTPError:
            if attempt == 3:
                raise
            time.sleep(4.0)
    else:
        return []
    # Minimal Atom parsing — avoid extra deps.
    entries = re.findall(r"<entry>(.*?)</entry>", text, re.DOTALL)
    out = []
    for e in entries:
        id_match = re.search(r"<id>(.*?)</id>", e, re.DOTALL)
        title_match = re.search(r"<title>(.*?)</title>", e, re.DOTALL)
        summary_match = re.search(r"<summary>(.*?)</summary>", e, re.DOTALL)
        if not (id_match and title_match and summary_match):
            continue
        out.append(
            {
                "arxiv_id": id_match.group(1).strip(),
                "title": re.sub(r"\s+", " ", title_match.group(1).strip()),
                "abstract": re.sub(r"\s+", " ", summary_match.group(1).strip()),
            }
        )
    return out


def fetch_arxiv_positives() -> list[dict]:
    """Search arXiv for likely positive-label accessibility / tactile map papers.

    The LLM still makes the call, but the ground-truth label is set based on
    the query the paper was retrieved by. Entries that obviously don't fit are
    dropped.
    """
    queries = [
        # RQ1: design principles / inclusive design for diverse abilities
        ("all:\"tactile map\" AND all:\"design guidelines\"", "rq1", 6),
        ("all:\"accessible map\" AND all:\"participatory design\"", "rq1", 6),
        ("all:\"inclusive design\" AND all:cartography", "rq1", 6),
        # RQ2: technologies, tools, media
        ("all:\"tactile map\" AND all:\"3D printing\"", "rq2", 6),
        ("all:\"accessible map\" AND all:haptic", "rq2", 6),
        ("all:sonification AND all:map AND all:blind", "rq2", 6),
        ("all:\"audio-tactile\" AND all:map", "rq2", 6),
        # RQ3: transferability across user groups
        ("all:\"tactile map\" AND all:children", "rq3", 6),
        ("all:\"accessible map\" AND all:\"older adults\"", "rq3", 6),
        ("all:\"tactile graphic\" AND all:autism", "rq3", 6),
    ]
    items = []
    seen = set()
    for q, rq, n in queries:
        try:
            results = arxiv_query(q, max_results=n)
        except Exception as exc:  # noqa: BLE001
            print(f"  arxiv query failed: {q}: {exc}")
            continue
        for r in results:
            if r["arxiv_id"] in seen:
                continue
            text_l = (r["title"] + " " + r["abstract"]).lower()
            # Light relevance gate: must mention map/tactile/accessibility
            if not any(
                k in text_l for k in ("map", "tactile", "haptic", "sonification")
            ):
                continue
            if not any(
                k in text_l for k in ("accessib", "blind", "visually", "disab", "inclus")
            ):
                continue
            seen.add(r["arxiv_id"])
            items.append(
                {
                    "id": f"arxiv-pos::{r['arxiv_id'].rsplit('/', 1)[-1]}",
                    "title": r["title"],
                    "abstract": r["abstract"],
                    "ground_truth": rq,
                    "source": f"arxiv-query:{q}",
                    "justification": f"Retrieved via arXiv query '{q}' targeting {rq}.",
                }
            )
        time.sleep(3.0)  # be polite
    return items


def fetch_arxiv_negatives() -> list[dict]:
    """Search arXiv for clearly-out-of-scope negatives.

    Negatives are items the Wabiski protocol SHOULD exclude: wrong topic, not
    about inclusive cartography at all, or 'hard negatives' that mention
    'map'/'accessibility' in a non-cartographic sense.
    """
    queries = [
        # easy negatives — computational geometry, vision, stat-ML with zero
        # accessibility relevance
        ("cat:cs.CG AND all:mesh AND all:algorithm", "excluded-topic", 6),
        ("cat:cs.GR AND all:rendering AND all:shader", "excluded-topic", 6),
        ("cat:cs.CV AND all:\"object detection\" AND all:benchmark", "excluded-topic", 6),
        ("cat:stat.ML AND all:\"variational inference\"", "excluded-topic", 5),
        # hard negatives — 'map' in data-structure sense, or 'accessibility' in
        # web-dev sense, with no inclusive-cartography content
        ("all:\"self-organizing map\" AND cat:stat.ML", "excluded-hard", 4),
        ("all:\"web accessibility\" AND all:WCAG", "excluded-hard", 4),
        ("all:\"graph neural network\" AND all:\"node classification\"", "excluded-topic", 4),
    ]
    items = []
    seen = set()
    for q, src, n in queries:
        try:
            results = arxiv_query(q, max_results=n)
        except Exception as exc:  # noqa: BLE001
            print(f"  arxiv query failed: {q}: {exc}")
            continue
        for r in results:
            if r["arxiv_id"] in seen:
                continue
            text_l = (r["title"] + " " + r["abstract"]).lower()
            # Reject anything that does mention tactile maps / blind users —
            # those might be actual positives that slipped in
            if "tactile map" in text_l:
                continue
            if "visually impaired" in text_l and "map" in text_l:
                continue
            seen.add(r["arxiv_id"])
            items.append(
                {
                    "id": f"arxiv-neg::{r['arxiv_id'].rsplit('/', 1)[-1]}",
                    "title": r["title"],
                    "abstract": r["abstract"],
                    "ground_truth": "excluded",
                    "source": f"arxiv-query:{q}",
                    "justification": f"Out of scope — retrieved from {src} query '{q}'; not about inclusive cartography.",
                }
            )
        time.sleep(1.0)
    return items


def main() -> None:
    print("Loading seed positives from repo ...")
    pos = load_seed_positives()
    print(f"  {len(pos)} seed positives")

    print("Fetching arXiv positives ...")
    arxiv_pos = fetch_arxiv_positives()
    print(f"  {len(arxiv_pos)} arXiv positives")

    print("Fetching arXiv negatives ...")
    negs = fetch_arxiv_negatives()
    print(f"  {len(negs)} arXiv negatives")

    all_items = pos + arxiv_pos + negs

    # Cap total
    if len(all_items) > 80:
        # keep all seed positives, subsample arxiv positives to ~20 and negs to ~30
        keep_pos = pos + arxiv_pos[:20]
        keep_neg = negs[:30]
        all_items = keep_pos + keep_neg

    print(f"TOTAL {len(all_items)} items")

    with OUT.open("w", encoding="utf-8") as fh:
        for it in all_items:
            fh.write(json.dumps(it, ensure_ascii=False) + "\n")

    # Print summary
    from collections import Counter

    c = Counter(it["ground_truth"] for it in all_items)
    print("Label distribution:", dict(c))


if __name__ == "__main__":
    main()
