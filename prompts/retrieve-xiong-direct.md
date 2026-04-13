# Task: Retrieve Xiong 2024 via direct arXiv PDF — stalled-agent recovery

A previous worker for this paper stalled in a Semantic Scholar 429 rate-limit loop on `/graph/v1/paper/ArXiv:2306.13063`. Your job is to retrieve and process the same paper by **bypassing** the S2 metadata path and going directly to arXiv.

## Base instructions
Follow `prompts/retrieve-and-process-paper.md` for the general flow (retrieve → process → verify → commit → report). All the parallel-swarm rules still apply: only touch your own paper directory, do not edit `papers/index.md`, do not touch other workers' directories, one commit scoped to your paper dir.

## PAPER_SPEC
```
label: Xiong_2024
title: Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs
authors: Miao Xiong, Zhiyuan Hu, Xinyang Lu, Yifei Li, Jie Fu, Junxian He, Bryan Hooi
year: 2024
venue: ICLR 2024
identifier: https://arxiv.org/pdf/2306.13063.pdf
fallback_identifier: https://arxiv.org/pdf/2306.13063v3.pdf
report_path: reports/retrieve-Xiong_2024.md
```

## Critical retrieval rules (differ from the master prompt)

1. **Do NOT hit `api.semanticscholar.org`** for this paper. The previous worker got stuck in a 429 loop on that endpoint. If the `research-papers:paper-retriever` skill tries to hit S2 first, intercept and go direct.
2. **Direct arXiv download is the primary path.** Use `curl`, `wget`, or the `claude-in-chrome` MCP to GET `https://arxiv.org/pdf/2306.13063.pdf` straight to disk. The PDF lives at that URL unconditionally — no metadata lookup needed.
3. **If `research-papers:paper-retriever` will not accept a raw URL**, bypass it entirely: download the PDF yourself to `papers/xiong-2024.pdf`, then invoke `research-papers:paper-reader` directly on that file. The reader does not need S2 metadata.
4. **If the reader-skill demands metadata**, fill it in by hand from the arXiv abstract page HTML (`https://arxiv.org/abs/2306.13063`) — parse title/authors/year from the landing page, do not hit S2.
5. **Do not install or upgrade packages.** If the retriever script has a baked-in S2 call path, skip the script and do manual download.
6. **Timeout budget:** 8 minutes. If you're not done in 8 minutes, stop, write a `failed` report with exact failure point, and exit. Do NOT spin on retries.

## What to return

Short final message (≤5 sentences) summarising status and pointing at `reports/retrieve-Xiong_2024.md`. Include:
- Which retrieval path worked (direct arXiv / Chrome / other)
- Whether S2 was touched at all
- Commit hash
- Any cross-citations relevant to the Wabiski LLM-confidence critique (Xiong's paper is being retrieved to back the critique — any findings on verbalised confidence calibration under distribution shift are high-value for Q's meeting).
