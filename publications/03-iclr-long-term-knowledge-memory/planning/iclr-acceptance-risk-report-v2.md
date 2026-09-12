---
id: pub-03-iclr-acceptance-risk-report-v2
title: "ICLR 2027 acceptance-risk report v2 — WorldConsistMem"
type: planning
status: final
created: 2026-09-07
updated: 2026-09-07
---

# ICLR 2027 acceptance-risk report (v2)

**PDF:** `submission/worldconsistmem.pdf` — 13 pages total; Conclusion p.7; References p.8 (**main text ≤9**).  
**Audit plan:** `planning/iclr-hostile-reviewer-audit-v2.md`  
**Labelled NEW artefacts:** `planning/rescue_p1_artifacts/`, `planning/rescue_p2_artifacts/`  
**Option A freeze:** unchanged.

---

## Completed vs pending vs blocked

### Completed (this rescue)
| Item | Status |
|---|---|
| Hostile-reviewer audit + prioritized plan | Done |
| Abstract/intro rewrite around Acc–BCR failure mode | Done |
| Explicit Acc vs Φ mathematics | Done |
| Threat-to-validity subsection | Done |
| Robustness subsection + labelled tables | Done |
| Surface frozen H0 ablations | Done |
| Seed sweep 100–105 (symbolic B3/B4, wpt=6) | Done (labelled NEW) |
| Relation-density sweep (medium, 8 worlds) | Done (labelled NEW) |
| Distractor on/off | Done — **null result** (labelled NEW) |
| Shortcut baselines (empty / majority / shuffle / gold) | Done (labelled NEW) |
| H4 gold BCR=1 sanity | Done (prior labelled NEW) |
| PDF rebuild + anonymity check | Done |
| Pytest (experiment repo) | 92 passed |

### Blocked / not completed
| Item | Reason |
|---|---|
| Stronger LLM reader (Phi / larger Qwen) | `mlx_lm` not installed; disk ≈2.1 GiB free; **not reported as run** |
| Full 34-world/tier multi-seed regeneration | Deferred; wpt=6 used instead |
| Contradiction-depth / dependency-depth generator surgery | Not implemented (would require generator redesign) |
| External transfer to other Acc suites | Not run |
| Anonymized code/data OpenReview zip from experiment repo | **Still manual** (research `experiments/worldconsistmem/` empty) |

---

## Strongest claim (supported)

WorldConsistMem isolates a failure mode in which a system can answer individual questions correctly (Acc) while failing joint world-history constraints (Φ/BCR), yielding a measurable gap $\Gapq=\Acc-\BCR$ that is a different evaluation object from Acc.

## Strongest evidence
1. **Corruption suite (frozen):** high Acc + BCR=0 and low Acc + BCR=1 both occur.
2. **Symbolic scaled (frozen):** B4 Acc 0.929 vs BCR 0.591 ($\Gapq=0.338$) with world BCR CI $[0.586,0.596]$.
3. **Shortcut baselines (NEW):** family-majority Acc 0.352 with BCR 0.000; gold Acc=BCR=1.
4. **Qwen Option A (frozen):** BCR=0 for all; CSR still separates; gold H4 BCR=1.
5. **H0 ablations (frozen):** archive/temporal removals → Acc 0.876, BCR 0.375 ($\Gapq=0.501$).

---

## Remaining fatal / high weaknesses
1. **Incremental novelty** vs SetCons/LogicVault + LTM Acc suites (residual real but narrow).
2. **Synthetic-only** diagnostic; no external transfer.
3. **Single weak LLM reader** (3B Qwen; high abstention); stronger reader blocked.
4. **Limited seed diversity** under wpt=6 (B3 identical across seeds 100–105) — reported honestly.
5. **Empty research experiment path** — reproducibility depends on packaging `~/worldconsistmem-experiments`.
6. **Distractor null** and **density weakly effective** — generator knobs may be less powerful than hoped (reported).

---

## Reviewer-by-reviewer objections and rebuttals

### Reviewer 1 (novelty)
| Objection | Rebuttal |
|---|---|
| “Consistency already exists (SetCons/LogicVault).” | Those target logical/case-file SAT, not persistent memory over evolving multi-entity gold worlds with world-history-derived Φ. Residual stated explicitly; we do not claim consistency is new in general. |
| “BCR is Acc rebranded.” | Different domain (bundles vs queries) and predicate (joint $\Phi$ vs pointwise match). Corruption + majority Acc=0.35/BCR=0 + consistent-wrong-world Acc=0.39/BCR=1 refute rebranding. |
| “Synthetic diagnostic is insignificant.” | Framed as controlled instrument, not ecological proxy; contribution is measurement isolation of Acc–BCR failure mode. |

### Reviewer 2 (validity)
| Objection | Rebuttal |
|---|---|
| “Leakage / shortcuts.” | Prompt leakage asserts; majority/shuffle/empty/gold controls; gold BCR=1 on H4. |
| “Generator artifact.” | Gaps persist across tiers, density settings, seeds (with limited diversity disclosed); distractor null disclosed. |
| “Weak reader drives BCR=0.” | Symbolic non-zero BCR; gold BCR=1; Qwen multi-violation (not single brittle constraint). Stronger reader absent — acknowledged. |
| “Compact flat BCR=1 is setup gaming.” | Fairness caveat explicit; not used as architecture win. |

### Reviewer 3 (reproducibility / strength)
| Objection | Rebuttal |
|---|---|
| “Cannot reproduce.” | Freeze checksums + tests; must upload anonymized experiment repo. |
| “Only 3B Qwen.” | Honest limitation; stronger reader blocked in this environment. |
| “Seed study too weak.” | Extended to 100–105; disclose B3 identity / limited diversity. |

---

## Estimated acceptance probability

| Stage | Subjective P(poster+) |
|---|---|
| Before this rescue (overlength + thin robustness narrative) | ~15–25% (with desk-reject risk) |
| After prior page-cut rescue | ~25–40% |
| **After this v2 rescue** | **~35–50%** |

**Why up:** clearer failure-mode spine; Acc≠BCR math; shortcut proof; ablations surfaced; threats/robustness sections; honest nulls.  
**Why not higher:** still synthetic; still 3B-only LLM; novelty incremental; code packaging incomplete.

---

## Final recommendation

**Submit** after:
1. Packaging anonymized `worldconsistmem-experiments` as supplementary.
2. Coauthor review of AI Use Statement and OpenReview quotas.
3. Optional (if environment fixed before 2026-09-25): labelled Phi/stronger-reader H4 — appendix only, never mixed with Option A.

Do **not** delay solely for stronger readers if packaging is ready; do **not** claim architecture superiority; do **not** hide the distractor null or limited seed diversity.

---

## Changed files (v2)
- `planning/iclr-hostile-reviewer-audit-v2.md`
- `planning/iclr-acceptance-risk-report-v2.md` (this file)
- `planning/rescue_p2_artifacts/*`
- `submission/latex/worldconsistmem.tex`, `sec_intro.tex`, `sec_object.tex`, `sec_metrics.tex`, `sec_results.tex`, `sec_failures.tex`, `sec_discussion.tex`, `sec_conclusion.tex`, `sec_appendix.tex`
- `submission/worldconsistmem.pdf`, OpenReview zip refreshed

No commits. JURIX untouched. Option A freeze untouched.
