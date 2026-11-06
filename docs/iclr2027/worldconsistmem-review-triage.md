# ICLR 2027 — WorldConsistMem review triage and rebuttal evidence

Submission: **49130**. Source: official OpenReview review text pasted on 2026-11-06. This is a working review-triage note, **not** an official rebuttal or a claim that outstanding issues have been resolved.

## Decision status

| Reviewer | Rating | Soundness | Main objection |
|---|---|---|---|
| Rkeo | 1 — Clear rejection | 1 | Presentation/typesetting, single-model synthetic evaluation, parser/scorer and post-result factorization, evidence sufficiency |
| vfz3 | 1 — Clear rejection | 1 | Generic F0 answer contract is unfair against strict tuple scoring; 77/150 sufficiency-label changes |
| EdSa | 2 — Weak rejection | 2 | Semantic grading independent of output schema, cross-model F0–F3 replication, generic-baseline rationale, impossible document cases |

## Highest-priority rebuttal work

1. **Task-aligned semantic rescoring of frozen F0/F2 raw responses.** Reviewer vfz3 specifically cites the scalar answer `21` for a “When ...?” question being marked wrong because the gold tuple contains extra fields. EdSa independently requests semantic evaluation ignoring output structure. The existing forensic audit's “0 format-only M5 wins” does **not** settle this broader construct-validity objection. Define and disclose a grading rubric, evaluate frozen predictions without changing model outputs, and report both relaxed semantic accuracy and strict tuple accuracy by subtype.
2. **Re-audit evidence sufficiency for all 150 packs, particularly 34 document cases.** The original labels change for 77/150 on re-audit. S2 is exactly collinear with the document subtype (34 cases), which scores 0/34 across all arms. Distinguish truly missing version identifiers from entailed but unexpressed resulting states. Do not describe unsupported cases as reasoning failures.
3. **Cross-model replication of F0–F3**, only after approving the model, budget, protocol, and execution. EdSa explicitly requests at least one additional model; Rkeo also flags single-snapshot external validity. Prepared Gemini protocol is not equivalent to executed replication.
4. **Explain the F0 interface and the precise task contract.** Was F0 intended as a realistic memory-system interface or an intentionally generic baseline? The original generic prompt did not necessarily request all gold fields.
5. **Clean manuscript presentation** (fonts, malformed symbols, figure baseline label 0/150 vs scorer-v2 13/150, bibliography floats, table/figure labels), as requested by Rkeo.
6. **Disclose F3 parser recovery and factorization asymmetries.** Frozen raw F3 responses were bare canonical JSON; the original online wrapper parser misclassified them. F1/F2 retained the generic wrapper, F3 did not. This is a remaining factorization confound.

## Verified existing results (do not overclaim)

| Arm | Intervention | Correct / 150 |
|---|---|---|
| F0 | Generic interface | 13/150 (8.67%) |
| F1 | Canonical schema only | 90/150 (60.00%) |
| F2 | Explicit prev/event/next representation only | 39/150 (26.00%) |
| F3 | Bundled schema + representation | 109/150 (72.67%) |

- F3–F1: **+19/150 = +12.67 percentage points**, 95% reported bundle-cluster bootstrap CI **[+7.33, +18.00] pp**, McNemar p ≈ **3.81×10⁻⁶**; 19 F3-only wins and 0 F1-only wins.
- Original S1 (59): F3 52/59 vs F1 39/59, +22.03 pp, reported 95% CI [+11.86, +32.20] pp.
- Original S1+S2 (93): F3 52/93 vs F1 39/93, +13.98 pp, reported 95% CI [+7.53, +21.51] pp.
- Interaction (F3−F1)−(F2−F0): **−4.67 pp**, 95% CI [−10.67, +1.33] pp. No established positive synergy.
- F1/F2 are **prospective post-result** interventions, not preregistered primary confirmatory arms.
- F3–F1 wins demonstrate better selection of explicit transitions in several inspected cases; they do **not** alone prove inference of latent states.
- Check the reported bootstrap `n_bundles = n` against actual grouping; several transition query IDs share world/bundle prefixes, and the intended clustering unit must be verified.
- Subtype heterogeneity matters: CEO F0 13/30, F1 10/30, F2 26/30, F3 23/30 (schema harms CEO by 3/30); document 0/34 all arms; ownership ceiling can explain the aggregate negative interaction.

## Reviewer-specific questions to answer

**Rkeo:** (1) Show subtype schema derivation using only public query-id slots, excluding gold leakage. (2) Specify which prompts, samples, seeds, and evaluation choices were frozen before post-result F1/F2 execution. (3) Show outcomes under original v1 scorer and online parser separately from corrected offline scoring. (4) Determine whether document/S2 target identifiers are present in evidence. (5) Fix typography in camera-ready manuscript.

**vfz3:** (1) Does complete F0 prompt request every field required by strict gold tuple? (2) Which conclusions survive task-aligned semantic grading? (3) How does corrected sufficiency classification change interpretation of errors?

**EdSa:** (1) Rescore F0 for underlying prev/event/next content independently of exact output structure. (2) Run full F0–F3 on at least one additional model. (3) Explain how and why generic F0 was selected. (4) Quantify impossible-vs-unsolved document/S2 examples.

## Operational guardrails

- Do not change experimental data, predictions, existing paper text, or evaluation code without explicit approval.
- Do not initiate paid API calls or submit OpenReview rebuttal without explicit approval.
- Treat review excerpts and program-chair automated feedback as distinct sources; automated PAT feedback is not an official human review.
- Deadline noted in discussion: **2026-11-18 AoE**; verify in OpenReview before submission.
