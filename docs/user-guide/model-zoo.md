# The pretrained model zoo

Trained models for direct use — imputation and short-term prediction —
whose **inference runs in the core via ONNX** (tract, pure Rust), so
Python, R and the CLI execute the same model with identical outputs.
Training lives in Python/torch (`zoo/ti360_zoo/`); weights are published
to the hub and fetched into a checksum-verified local cache
(`~/.cache/ti360/models`, `TI360_ZOO_CACHE` to override), fully offline
once cached. **Weights never live in git.**

## Cards are mandatory

Every model ships a card (`schemas/model_card.json`): training-data
provenance and license, the declared **domain fingerprint**, benchmark
metrics produced by the committed evaluation pipeline, intended use,
documented limits, and the expected zero-shot degradation. Read it:

```python
card = ti.zoo.model_card("ti360/impute-saits-mini")
print(card["limits"])
print(card["expected_zero_shot_degradation"])
```

The v0.1 weights are demonstration weights trained on the committed
synthetic generator — the cards say so verbatim. Production weights are
retrained on PeMS/UTD19-class archives with the same pipeline.

## Using a model

```python
model = ti.models.load_pretrained("ti360/impute-saits-mini")
filled, summary = model.impute("loops.csv")
# summary records id, version and sha256 — provenance, not trust-me
```

Honest runtime behavior: windows with no observed values are left
unfilled and **reported**, never invented; observed values are never
modified.

## The Advisor connection

The Advisor recommends a zoo model only when your dataset's fingerprint
falls **inside** a card's declared domain, and prescribes fine-tuning
when it is merely near it. The zoo never substitutes a model silently —
you opt in.

## Fine-tuning

Safetensors checkpoints ship alongside the ONNX artifacts (Python-only).
The step-by-step recipe — load checkpoint, fine-tune on local windows
with the runtime's exact normalization, evaluate against linear
interpolation before trusting it, export, distribute through a private
registry — is the runnable notebook
`notebooks/05_zoo_finetune_tutorial.ipynb`.
