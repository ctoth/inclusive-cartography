# Abstract

## Original Text (Verbatim)

We show that a GPT-3 model can learn to express uncertainty about its own answers in natural language — without use of model logits. When given a question, the model generates both an answer and a level of confidence (e.g. "90% confidence" or "high confidence"). These levels map to probabilities that are well calibrated. The model also remains moderately calibrated under distribution shift, and is sensitive to uncertainty in its own answers, rather than imitating human examples. To our knowledge, this is the first time a model has been shown to express calibrated uncertainty about its own answers in natural language. For testing calibration, we introduce the CalibratedMath suite of tasks. We compare the calibration of uncertainty expressed in words ("verbalized probability") to uncertainty extracted from model logits. Both kinds of uncertainty are capable of generalizing calibration under distribution shift. We also provide evidence that GPT-3's ability to generalize calibration depends on pre-trained latent representations that correlate with epistemic uncertainty over its answers.

---

## Our Interpretation

The paper demonstrates, on the CalibratedMath benchmark, that supervised finetuning teaches GPT-3 to emit a verbalized confidence (either a numeric percentage or a categorical word) that tracks its own correctness *moderately* well on out-of-distribution evaluation — notably outperforming logit-based baselines on format-shifted tasks while being outperformed by them on content-shifted MSE. This matters for the Wabinski 2026 review protocol critique because it establishes, with quantitative error bars, that verbalized LM confidence is (a) learnable, (b) *not* interchangeable with output-token probabilities, (c) *not* reliably produced by few-shot prompting alone, and (d) still off-diagonal from perfect calibration even in the best finetuned case — so any fixed confidence-threshold rule built on top of raw verbal hedges from a non-finetuned model is unsupported by the evidence in this paper.
