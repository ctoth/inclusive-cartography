---
tags: [llm-calibration, verbalized-uncertainty, distribution-shift, gpt-3, finetuning]
---
Shows that GPT-3 can be supervised-finetuned on the CalibratedMath benchmark to emit a verbalized confidence estimate (numeric percentage or categorical word) alongside each answer, with the confidence remaining moderately calibrated under content and format distribution shift.
Verbalized confidence outperforms a temperature-scaled answer-logit baseline on format-shifted (Multi-answer) evaluation but loses to it on raw MSE for content-shifted (Multiply-divide) evaluation, and is only weakly correlated with answer-token logits, establishing that verbalized confidence is a distinct learned signal rather than a reparameterization of logits.
Directly relevant to inclusive-cartography's critique of Wabinski 2026's confidence-threshold rule: the paper quantifies how much (or little) a non-finetuned LM's self-reported confidence can be trusted, shows few-shot prompting does not substitute for finetuning, and gives the concrete MSE/MAD numbers (best-case ~15-22% calibration error on a synthetic arithmetic benchmark) that upper-bound what any in-context review protocol can expect.
