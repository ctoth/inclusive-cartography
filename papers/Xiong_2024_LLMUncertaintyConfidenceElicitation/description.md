---
tags: [llm-confidence, calibration, uncertainty-estimation, black-box-evaluation, benchmark]
---
Xiong et al. define a black-box framework for eliciting confidence from closed-source LLMs, decomposed into prompting, sampling, and aggregation strategies, and benchmark it on five LLMs across eight QA datasets.
The paper shows that vanilla verbalized confidence is severely overconfident (values cluster 80-100% in multiples of 5), that CoT/Top-K prompting reduces ECE mainly by raising accuracy rather than improving discrimination, and that Self-Random sampling with M=5 plus Avg-Conf or Pair-Rank aggregation is the most reliable configuration; the white-box/black-box AUROC gap is narrow (~0.522 to ~0.605).
This provides the empirical foundation for the Wabiski protocol LLM-confidence critique in inclusive-cartography: raw verbalized confidence is not trustworthy, ECE alone is an insufficient gate, and professional-knowledge domains defeat all current calibration methods.
