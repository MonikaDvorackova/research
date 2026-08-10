---
id: pub-03-closed-negative-cycle-cr-gap
title: "Closed cycle — CR-Gap / historical reconstruction (negative / inconclusive)"
type: research-notes
status: closed
created: 2026-07-31
updated: 2026-07-31
tags: [iclr, negative-result, closed-cycle, cr-gap]
related_experiment: experiments/cr-gap-pilot
---

# Closed research cycle: CR-Gap / historical reconstruction

**Status:** `closed — negative / inconclusive research cycle`

**Explicit statement:** No publishable positive ICLR claim was established. Negative and inconclusive findings are recorded here as programme hygiene, not as a paper contribution.

---

## Original hypothesis

Instruction-following language models (and retrieval architectures over continually revised evidence) exhibit a large **current–retrospective gap**: they answer present-state queries well but fail to recover historically warranted states after updates, contradictions, resolutions, and reversions. Early framing treated **revision-aware retrieval** (and related non-destructive memory) as a candidate technical cause and contribution.

## Successive reformulations

1. **Overwrite vs revision-aware retrieval** as an ICLR-facing systems/representation claim.
2. **Keep-all vs revision-aware** under equalized query information (fair LLM validation) after recognizing overwrite ≫ revision-aware was partly by construction.
3. Rejection of the retrieval-structure claim; residual framed as **historical state reconstruction under conflicting evidence** with perfect retrieval (oracle / ordered history).
4. Model-ladder + conflict-density + length-matched controls to test whether residual errors are genuine conflict reasoning failures vs length/prompt confounds.

## Experiments performed

| Phase | Artefact | Result (summary) |
|---|---|---|
| Symbolic pilot | `experiments/cr-gap-pilot` extractive reader | Engineering gate only; large overwrite gap by construction |
| Fair LLM validation | equalized settings A/B, local MLX | Keep-all vs revision-aware ~2 pp when target info is explicit; earlier huge gap largely **reader-policy confound** |
| Reconstruction ladder | oracle minimal / full / distractors × 4 prompts × 3 MLX families | Absolute errors survive medium/strong models |
| Conflict × depth grid | controlled instances + unsupported cells | No clean conflict-density claim after controls |
| Length-matched controls | conflict vs non-conflict length-matched pairs | **Conflict gap does not survive length matching** |

Primary outputs (retained, not deleted):

- `experiments/cr-gap-pilot/outputs/reconstruction_findings.md` — verdict **INCONCLUSIVE**
- `reconstruction_model_ladder.csv`, `reconstruction_by_operation.csv`, `reconstruction_by_depth.csv`
- `reconstruction_by_conflict_density.csv`, `reconstruction_length_controls.csv`
- `reconstruction_predictions.jsonl`, `reconstruction_failures.csv`
- data: `reconstruction_instances.jsonl`, `reconstruction_unsupported.jsonl`
- code: `src/cr_gap/*`, tests under `tests/`

## Confounds discovered

1. **Diagnostic reader policy** inflated overwrite vs revision-aware differences.
2. **Unequal query information** across retrieval methods in early LLM runs.
3. **Conflict density confounded with prompt length / evidence-row count** until length-matched controls were added.
4. **Small per-cell n** and wide bootstrap intervals on depth×conflict grids.
5. **Model-tier label ≠ empirical strength** (Llama-3.2-3B outperformed Phi-3.5-mini on the primary cell).
6. Trajectory prompting introduced **malformed-output** mass in some models, mixing parsing with reasoning.

## Hypotheses rejected

- Revision-aware retrieval is required / is the ICLR contribution.
- Hierarchical agent memory / BCWR-style formulations as the path for this cycle.
- Current–retrospective trade-off as a clean, architecture-causal claim under fair conditions.
- Historical reconstruction under conflicting evidence as a **conflict-causal** phenomenon sufficient for ICLR continuation (length matching falsified the conflict-density criterion).

## Surviving observations (not claimed as contributions)

- Absolute historical-target errors can remain for local instruct models even with oracle evidence and explicit target revision.
- Fair keep-all vs revision-aware differences are small (~2 pp) when target information is equalized.
- Conflict-heavy items are **not** reliably harder than length-matched non-conflict controls in this suite.
- Trajectory reconstruction prompting does not close residual failure rates to abandon thresholds.

These are programme facts and cautionary notes. They do **not** constitute a positive scientific paper claim.

## Why the direction was stopped

Pre-registered abandon / reframe gates were applied. The cycle fails **reframe** (no length-controlled conflict/depth causal story) and fails **abandon-by-triviality** only in the weak sense that absolute errors remain—but without a controlled causal factor suitable for ICLR. Correct scientific status: **INCONCLUSIVE / NO-GO** for Publication-03 continuation of this topic.

## Reusable artefacts

- Deterministic symbolic world + query families.
- Fair validation harness (equalized query settings).
- Reconstruction suite generator with unsupported-cell logging and length-matched controls.
- Local MLX evaluation client, caches, and metric/CI pipeline.
- Error taxonomy and decision criteria templates (reuse the *method*, not the *claim*).

## Lessons for future topic selection

1. Pre-register length / information-equivalence controls before claiming operation-specific difficulty.
2. Prefer diagnostic dissociations over solution-first architectures.
3. Kill retrieval/systems claims early with equalized-information ablations.
4. Do not promote residual absolute error into a paper without a surviving causal factor.
5. Keep negative cycles documented; do not force a novelty narrative.

## Closure declaration

This cycle is **closed**. Do not reopen hierarchical agent memory, BCWR, revision-aware retrieval, current–retrospective trade-offs, or historical reconstruction under conflicting evidence unless materially new evidence identifies a *different* scientific question with controls that the present suite already falsified for conflict density.
