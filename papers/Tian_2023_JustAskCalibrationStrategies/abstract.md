# Abstract

## Original Text (Verbatim)

A trustworthy real-world prediction system should produce well-calibrated confidence scores; that is, its confidence in an answer should be indicative of the likelihood that the answer is correct, enabling deferral to an expert in cases of low-confidence predictions. Recent studies have shown that unsupervised pre-training produces large language models (LMs) whose conditional probabilities are remarkably well-calibrated. However, the most widely-used LMs are fine-tuned with reinforcement learning from human feedback (RLHF-LMs), and some studies have suggested that RLHF-LMs produce conditional probabilities that are very poorly calibrated. In light of this perceived weakness, we conduct a broad evaluation of methods for extracting confidence scores from RLHF-LMs. For RLHF-LMs such as ChatGPT, GPT-4, and Claude, we find that verbalized confidences emitted as output tokens are typically better-calibrated than the model's conditional probabilities on the TriviaQA, SciQ, TruthfulQA, and TruthfulQA benchmarks, often reducing the expected calibration error by a relative 50%.

---

## Our Interpretation

Tian et al. show empirically that for RLHF-fine-tuned chatbots (GPT-4, ChatGPT, Claude-1/2, Llama-2-70B-chat) the model's own conditional token probabilities are unreliable as confidence signals, but simply asking the model to verbalize a probability (either numerically or via a fixed linguistic phrase menu) — especially in a two-step or top-k protocol — recovers calibration that is roughly 50% better in ECE than logit-based baselines on TriviaQA, SciQ, and TruthfulQA. No fine-tuning, labeled calibration data, or logit access is required, making the method the only practically viable calibration approach for closed-API RLHF-LMs. For this project, the result bounds what "LM-reported confidence" can and cannot mean inside Wabinski 2026's confidence-threshold screening rule and supplies the concrete protocol improvements (2-step, top-k) the critique can recommend.
