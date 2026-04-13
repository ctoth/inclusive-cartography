"""Run the Wabiski §3.5.2 screening prompt against each test-set item via
OpenAI (GPT-5) and Google Gemini 2.5 Pro.

- Temperature 0 primary pass (single sample per item per provider).
- Optional temperature-1 N=5 secondary pass (set SECONDARY_SAMPLES=5 and
  re-run). Cached so re-runs are free.

The prompt uses the verbatim Wabiski §3.5.2 screening dictionary, wrapped in a
minimal instruction asking the model to emit structured JSON with keys:
    tag: one of screening:rq1 | screening:rq2 | screening:rq3 | screening:excluded
    confidence_score: float 0.0-1.0
    exclusion_reason: string or null
"""

from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
TEST_SET = HERE / "test_set.jsonl"
CACHE = HERE / "cache"

# Pulled verbatim from papers/Wabiski_2026_CognitiveReviewProtocol/notes.md §3.5.2
WABISKI_DICT = [
    {
        "tag": "screening:rq1",
        "label": "Relevant to RQ1",
        "definition": (
            "The study discusses design principles or methods used in "
            "inclusive cartography for users with diverse perceptual "
            "abilities (e.g., visually impaired, elderly, children, "
            "autistic individuals)."
        ),
        "example": (
            "The paper presents a participatory design process for tactile "
            "maps tailored to blind users."
        ),
        "confidence_score": "0.00-1.00",
    },
    {
        "tag": "screening:rq2",
        "label": "Relevant to RQ2",
        "definition": (
            "The study evaluates or describes technologies, tools, or media "
            "used to enhance map accessibility (e.g., 3D printing, haptics, "
            "sonification, adaptive interfaces)."
        ),
        "example": (
            "The article compares the effectiveness of haptic feedback and "
            "audio-tactile maps for visually impaired users."
        ),
        "confidence_score": "0.00-1.00",
    },
    {
        "tag": "screening:rq3",
        "label": "Relevant to RQ3",
        "definition": (
            "The study explores whether inclusive cartographic design "
            "practices are transferable across user groups or domains "
            "(e.g., applying tactile design principles to cognitive "
            "accessibility)."
        ),
        "example": (
            "The study analyzes how tactile mapping techniques developed "
            "for blind users can be adapted for children with cognitive "
            "challenges."
        ),
        "confidence_score": "0.00-1.00",
    },
    {
        "tag": "screening:excluded",
        "label": "Excluded",
        "definition": (
            "The study does not meet the inclusion criteria or is "
            "irrelevant to all research questions."
        ),
        "example": (
            "The citation is a theoretical paper on cartographic history "
            "with no mention of accessibility or user diversity."
        ),
        "confidence_score": "0.00-1.00",
        "exclusion_reasons": [
            {
                "reason": "date_out_of_range",
                "description": "Published outside 2001-2025.",
            },
            {
                "reason": "not_peer_reviewed",
                "description": "Not peer-reviewed (blog, editorial, etc.).",
            },
            {
                "reason": "language_not_supported",
                "description": "Language not supported by the review team.",
            },
            {
                "reason": "not_relevant_to_rqs",
                "description": "Does not address any of the three RQs.",
            },
            {
                "reason": "no_accessibility_focus",
                "description": "No accessibility / user-diversity focus.",
            },
        ],
    },
]

INSTRUCTION = (
    "You are the screening classifier from the Wabiski 2026 systematic-review "
    "protocol (§3.5.2). Use the following tag dictionary to classify an "
    "incoming citation's title + abstract into exactly one tag.\n\n"
    "TAG DICTIONARY (verbatim from Wabiski §3.5.2):\n"
    + json.dumps(WABISKI_DICT, indent=2)
    + "\n\n"
    "Inclusion criteria (Wabiski §3.5.1): date range 2001-2025; peer-reviewed; "
    "languages English/Spanish/Polish/German; must be related to at least one "
    "of the three research questions on inclusive cartography for users with "
    "diverse perceptual, cognitive and age-related abilities.\n\n"
    "Respond with ONLY a JSON object matching this exact schema:\n"
    "{\n"
    '  "tag": "screening:rq1" | "screening:rq2" | "screening:rq3" | "screening:excluded",\n'
    '  "confidence_score": <float between 0.00 and 1.00>,\n'
    '  "exclusion_reason": <string or null>\n'
    "}\n"
    "Do not include any commentary, markdown fences, or additional fields."
)


def build_user_prompt(item: dict) -> str:
    return (
        "TITLE: " + item["title"] + "\n\n" + "ABSTRACT: " + item["abstract"]
    )


JSON_OBJ_RE = re.compile(r"\{.*\}", re.DOTALL)


def parse_response(text: str) -> dict[str, Any]:
    """Best-effort parse of model JSON output."""
    text = text.strip()
    # Strip code fences if present
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n?|```$", "", text, flags=re.MULTILINE)
        text = text.strip()
    try:
        return json.loads(text)
    except Exception:
        pass
    m = JSON_OBJ_RE.search(text)
    if m:
        try:
            return json.loads(m.group(0))
        except Exception:
            pass
    return {"tag": None, "confidence_score": None, "exclusion_reason": None, "_parse_error": text[:500]}


# ----- OpenAI -----

def run_openai(item: dict, model: str, temperature: float, sample_idx: int = 0) -> dict:
    cache_dir = CACHE / "openai" / model
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_file = cache_dir / f"{item['id'].replace('::', '__').replace('/', '_')}__t{temperature}__n{sample_idx}.json"
    if cache_file.exists():
        return json.loads(cache_file.read_text(encoding="utf-8"))

    from openai import OpenAI

    client = OpenAI()
    user_prompt = build_user_prompt(item)

    # GPT-5 models may not accept temperature param in chat.completions; use responses API
    kwargs: dict[str, Any] = {
        "model": model,
        "input": [
            {"role": "system", "content": INSTRUCTION},
            {"role": "user", "content": user_prompt},
        ],
    }
    # GPT-5 only accepts default temperature; don't pass it. For non-gpt-5 models,
    # pass the requested temperature. GPT-5 sampling diversity across N samples
    # is still present because the model's default is non-deterministic.
    if not model.startswith("gpt-5"):
        kwargs["temperature"] = temperature

    t0 = time.time()
    resp = client.responses.create(**kwargs)
    wall = time.time() - t0

    text = ""
    try:
        text = resp.output_text
    except Exception:
        # Fallback: concatenate output text
        for out in getattr(resp, "output", []) or []:
            for c in getattr(out, "content", []) or []:
                t = getattr(c, "text", None)
                if t:
                    text += t

    parsed = parse_response(text)
    usage = getattr(resp, "usage", None)
    record = {
        "provider": "openai",
        "model": model,
        "temperature": temperature,
        "sample_idx": sample_idx,
        "item_id": item["id"],
        "raw_text": text,
        "parsed": parsed,
        "wall_s": wall,
        "usage": {
            "input_tokens": getattr(usage, "input_tokens", None) if usage else None,
            "output_tokens": getattr(usage, "output_tokens", None) if usage else None,
            "total_tokens": getattr(usage, "total_tokens", None) if usage else None,
        },
    }
    cache_file.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    return record


# ----- Gemini -----

def run_gemini(item: dict, model: str, temperature: float, sample_idx: int = 0) -> dict:
    cache_dir = CACHE / "gemini" / model
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_file = cache_dir / f"{item['id'].replace('::', '__').replace('/', '_')}__t{temperature}__n{sample_idx}.json"
    if cache_file.exists():
        return json.loads(cache_file.read_text(encoding="utf-8"))

    from google import genai
    from google.genai import types

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    user_prompt = build_user_prompt(item)
    cfg = types.GenerateContentConfig(
        system_instruction=INSTRUCTION,
        temperature=temperature,
        response_mime_type="application/json",
    )

    t0 = time.time()
    resp = client.models.generate_content(
        model=model,
        contents=user_prompt,
        config=cfg,
    )
    wall = time.time() - t0

    text = ""
    try:
        text = resp.text or ""
    except Exception:
        text = ""
    parsed = parse_response(text)
    usage = getattr(resp, "usage_metadata", None)
    record = {
        "provider": "gemini",
        "model": model,
        "temperature": temperature,
        "sample_idx": sample_idx,
        "item_id": item["id"],
        "raw_text": text,
        "parsed": parsed,
        "wall_s": wall,
        "usage": {
            "input_tokens": getattr(usage, "prompt_token_count", None) if usage else None,
            "output_tokens": getattr(usage, "candidates_token_count", None) if usage else None,
            "total_tokens": getattr(usage, "total_token_count", None) if usage else None,
        },
    }
    cache_file.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    return record


def load_items() -> list[dict]:
    return [json.loads(l) for l in TEST_SET.read_text(encoding="utf-8").splitlines() if l.strip()]


PROVIDERS = [
    ("openai", "gpt-5", run_openai),
    ("gemini", "gemini-2.5-pro", run_gemini),
]


def run_pass(items: list[dict], temperature: float, n_samples: int) -> None:
    for provider_name, model, runner in PROVIDERS:
        print(f"\n=== {provider_name} / {model} / T={temperature} / N={n_samples} ===")
        for i, item in enumerate(items):
            for s in range(n_samples):
                try:
                    rec = runner(item, model, temperature, sample_idx=s)
                    tag = rec["parsed"].get("tag")
                    conf = rec["parsed"].get("confidence_score")
                    print(f"  [{i+1}/{len(items)}] s{s} {item['id'][:45]:45s} -> {tag} conf={conf}")
                except Exception as exc:  # noqa: BLE001
                    print(f"  [{i+1}/{len(items)}] ERROR: {exc}")
                    time.sleep(2.0)


def main() -> None:
    items = load_items()
    print(f"Loaded {len(items)} items.")

    # Primary temperature-0 pass
    run_pass(items, temperature=0.0, n_samples=1)

    # Secondary temp=1 N=5 (opt-in via env var to stay inside budget)
    if os.environ.get("RUN_SECONDARY", "0") == "1":
        run_pass(items, temperature=1.0, n_samples=5)


if __name__ == "__main__":
    main()
