# Post-S1 Research Question Selection (Critical)

**Status:** S1 CLOSED (Phase A NO-GO final).  
**Date:** 2026-07-31  
**Inputs:** [`research-question-search.md`](research-question-search.md); [`../../../experiments/archive-pareto-pilot/outputs/archive_pareto_pilot/go_nogo.md`](../../../experiments/archive-pareto-pilot/outputs/archive_pareto_pilot/go_nogo.md)  
**Forbidden:** rescue/rephrase S1; architecture-as-contribution; “our system is better.”

---

## Lessons from Phase A that bind all survivors

1. **Capacity splits can move metrics without creating a scientific trade-off.** \(\alpha\) moved \(A_c\) and \(A_h\) a lot, but Spearman \(=+1\): joint degradation, not Pareto.
2. **\(\alpha=0\) / recency dominated both axes.** Funding archive by starving active memory bought nothing.
3. **“Historical accuracy” without retained supersession can be fake** — unchanged facts answered from current store.
4. Therefore any RQ that is secretly “give history more slots by taking current slots” is **empirically poisoned** unless it predicts a *qualitatively different* dissociation than S1 and survives a kill pilot that forbids capacity confounds.
5. Literature since the original search further occupies consolidation / retain-vs-consolidate (*Retain or Consolidate?* arXiv:2607.17545; *Useful Memories Become Faulty…* arXiv:2605.12978; TiMem).

---

## Evaluation of every former survivor (S1 excluded)

For each: RQ → claim → why it “survives” S1 mechanically → literature → measured phenomenon → minimal experiment → rejection risks → **decision**.

### S2 — Promotion-criterion × task-family dominance

1. **RQ:** Which promotion criterion (recurrence / importance / conflict / semantic-shift / recency) dominates accuracy across task families in an evolving world?  
2. **Claim:** Criterion × task-family interaction; no universal winner.  
3. **Why survives S1 failure:** IV is *selection rule*, not archive budget \(\alpha\).  
4. **Closest literature:** RecMem (recurrence-triggered consolidation); MemCon (learned ops); GAM (semantic-shift consolidation); *Retain or Consolidate?* (operator selection under budget).  
5. **Phenomenon measured:** relative accuracy of fixed heuristic scorers under matched capacity.  
6. **Minimal experiment:** swap scorer only; freeze \(B\), \(k\), tiers; multi-family labels.  
7. **Rejection risks:** reads as systems ablation sweep; occupied by operator-selection papers; positive result = “task-dependent heuristics” (weak ICLR object); negative = null interaction. Phase A shows capacity/policy changes often produce monotone collapse, not interesting regimes.

**Decision: REJECT.** Engineering factorial, not a distinctive scientific phenomenon. Occupancy high.

---

### S3 — Lifecycle-operation dominance on evolving-world tasks

1. **RQ:** Which lifecycle operation dominates on historical/conflict evolving-world tasks—does retrieval still dominate as on LoCoMo?  
2. **Claim:** Regime-dependent op dominance (possibly falsifying retrieval-dominance transfer).  
3. **Why survives S1:** IV is op ablation, not \(\alpha\)-Pareto.  
4. **Closest literature:** *Diagnosing Retrieval vs Utilization* (retrieval dominates on LoCoMo); MemoryData; MemCon.  
5. **Phenomenon:** \(\Delta\)accuracy from matched ablations of retrieve/update/promote/forget.  
6. **Minimal experiment:** 2×2 write×retrieve upgrade on evolving world + LoCoMo transfer cell.  
7. **Rejection risks:** Most likely **reconfirms** retrieval dominance → incremental note, not ICLR oral/poster core; if archive/update “dominate,” Phase A warns this may be capacity starvation misread as op importance; still close to “which module matters” architecture-adjacent framing.

**Decision: REJECT as primary.** At best a secondary diagnostic; not a strong publishable claim if it agrees with LoCoMo, and hard to trust if it disagrees without ironclad capacity controls (S1 taught this).

---

### S4 — Consolidation lossiness destroys temporal/conflict cues

1. **RQ:** Does increasing consolidation lossiness causally destroy temporal/conflict cues required for historical and conflicting tasks?  
2. **Claim:** Dose–response selective cue destruction (temporal/conflict collapse faster than single-hop current facts) under matched storage of consolidated units.  
3. **Why survives S1:** IV is **lossy transform of content**, not archive/active split. Can hold \(B\) fixed and vary compression.  
4. **Closest literature:** MemoryData (chronological cue loss under consolidation); Infini (summaries miss fine facts); *Useful Memories Become Faulty…* (continuous consolidation degrades); *Retain or Consolidate?* (consolidation vs retention under budget—**direct neighbor**); TiMem (temporal consolidation architecture).  
5. **Phenomenon:** selective information destruction under compression.  
6. **Minimal experiment:** lossiness ladder (identity → drop-fields → coarse buckets → summary); white-box cue probes + black-box task accuracies; matched slot/token budget.  
7. **Rejection risks:** **“Obvious that compression loses information”**; neighbor papers already establish consolidation harm and budget-dependent retain/consolidate; Area Chair may score as delayed rediscovery; does not need LTKM (undermines collaborative platform story without strengthening novelty).

**Decision: REJECT as primary.** Best *remaining* scientific object on paper, but **novelty bar fails** after 2026 consolidation literature. Not ICLR-competitive as stated.

---

### S5 — Archive tier necessity

1. **RQ:** Is an explicit archive tier necessary for historical queries under matched storage?  
2. **Claim:** Archive on vs off causes historical drop not recoverable by expanding LTM.  
3. **Why survives S1 mechanically:** tier presence vs \(\alpha\) continuum.  
4. **Literature / Phase A:** Near-identical to S1; Phase A found more archive capacity **hurts** historical net score.  
5. **Phenomenon:** tier necessity.  
6. **Experiment:** archive on/off, matched \(B\).  
7. **Risks:** S1 sibling; likely another NO-GO; hierarchy ablation optics.

**Decision: REJECT.** Poisoned by Phase A.

---

### S6 — When promotion helps vs hurts

1. **RQ:** Is the effect of promotion aggressiveness non-monotonic?  
2. **Claim:** U-shaped accuracy vs promotion rate.  
3. **Why survives S1:** rate dial ≠ archive Pareto (but often correlates with how much leaves hot store).  
4. **Literature:** RecMem/MemCon/GAM; Phase A monotone collapse under related capacity moves.  
5. **Phenomenon:** help/hurt regimes for promotion volume.  
6. **Experiment:** threshold sweep; fixed \(B\).  
7. **Risks:** Confounded with S1-style starvation; systems paper; may be monotone again.

**Decision: REJECT.** High confound overlap with closed S1; weak novelty.

---

### S7 — Hierarchy × conflict-density interaction

1. **RQ:** Does hierarchy’s benefit increase with conflict density?  
2. **Claim:** Interaction effect.  
3. **Why survives S1:** different IV (conflict × structure).  
4. **Literature:** MemConflict; hierarchy ablations (HiMem/GAM/…).  
5. **Phenomenon:** structure×conflict interaction.  
6. **Experiment:** 2×3 flat vs hierarchical × conflict levels.  
7. **Risks:** **Architecture is the factor** — forbidden by task rules.

**Decision: REJECT.** Architecture-as-IV.

---

### S8 — White-box / black-box dissociation under lifecycle IV

1. **RQ:** Do update/retrieval correctness and answers dissociate under lifecycle interventions?  
2. **Claim:** Dissociation under ops.  
3. **Why survives S1:** measurement dissociation ≠ archive Pareto.  
4. **Literature:** **MemConflict** already shows answer vs retrieval dissociation.  
5. **Phenomenon:** metric dissociation.  
6. **Experiment:** intervene on one op; white-box + black-box.  
7. **Risks:** Occupied; evaluation-methodology paper unless tiny novelty wedge.

**Decision: REJECT.**

---

### S9 — Transfer of lifecycle effects across worlds

1. **RQ:** Do lifecycle intervention rankings transfer from LoCoMo/LongMemEval to synthetic evolving world?  
2. **Claim:** External validity / rank correlation.  
3. **Why survives S1:** transfer science.  
4. **Literature:** every memory paper that reports multiple benchmarks; MemoryData workload dependence.  
5. **Phenomenon:** non-transfer of effect rankings.  
6. **Experiment:** same interventions on two worlds.  
7. **Risks:** Secondary validity study; weak standalone ICLR claim; “benchmark paper” optics.

**Decision: REJECT as primary.**

---

### S10 — Transfer across backends

1. **RQ:** Do lifecycle-operation effects transfer across memory backends?  
2. **Claim:** Backend-agnostic op effects.  
3. **Why survives S1:** architecture disposable — good.  
4. **Literature:** MemCon (backend-agnostic control).  
5. **Phenomenon:** generality of op effects.  
6. **Experiment:** wrap ≥2 backends with identical policies.  
7. **Risks:** Occupied spirit; expensive; still “ops matter” engineering.

**Decision: REJECT as primary.**

---

### S11 — Failure-mode ordering as horizon grows

1. **RQ:** As horizon grows, which failure mode appears first under controlled lifecycle settings?  
2. **Claim:** Ordered degradation (e.g. retrieval miss ≺ cue loss ≺ update failure).  
3. **Why survives S1:** mechanism ordering ≠ archive allocation.  
4. **Literature:** BEAM scale drops; MemoryData long-horizon degradation; STALE/MemConflict failure diagnostics.  
5. **Phenomenon:** temporal ordering of labeled failure modes.  
6. **Experiment:** horizon sweep; pre-registered taxonomy; white-box labels.  
7. **Rejection risks:** Post-hoc taxonomy; descriptive atlas rather than causal claim; hard to beat “things get worse with length”; may not need LTKM; ICLR may call it diagnostic appendix material.

**Decision: REJECT as primary.** Interesting engineering diagnostic; not a sharp enough scientific object for ICLR after scrutiny.

---

### S12 — Soft invalidation vs hard deletion

1. **RQ:** Soft invalidate vs hard delete under matched budget for historical vs current tasks?  
2. **Claim:** Task-family trade-off from deletion semantics.  
3. **Why survives S1:** semantics ≠ \(\alpha\) (but retains history vs not — **S1-adjacent**).  
4. **Literature:** Engram invalidate-not-delete; Zep bitemporal; Phase A retention-without-capacity.  
5. **Phenomenon:** delete-semantics trade-off.  
6. **Experiment:** two semantics × budget × task family.  
7. **Risks:** Occupied; S1-adjacent NO-GO likely; “our delete operator” optics.

**Decision: REJECT.**

---

### S13 — Write-after-act vs dialogue-only

1. **RQ:** Does action-grounded writing change optimal promotion vs dialogue-only?  
2. **Claim:** Interaction-sourced writes change promotion optima.  
3. **Why survives S1:** different IV.  
4. **Literature:** thinner; generative agents; tool-use memory.  
5. **Phenomenon:** write-channel effect on promotion.  
6. **Experiment:** dialogue-only vs act-coupled writes.  
7. **Risks:** **Agent loop not in hand**; execution blocker; not “existing LTKM platform” ready.

**Decision: REJECT** (not realistically executable now).

---

### S14 — Emergent cue survival under consolidation

Fold of S4. **REJECT** (same occupancy as S4).

---

### S15 — Tier capacity–accuracy Pareto

S1 sibling (allocation across tiers). Phase A killed the cleanest instance. **REJECT.**

---

## Ranking after S1 kill (critical)

| Rank | ID | Status | One-line reason |
|---|---|---|---|
| — | S1 | **CLOSED** | Phase A NO-GO |
| 1 | S4 | Best *object*, still **not publishable enough** | Occupied by 2026 consolidation / retain-vs-consolidate literature; “compression loses cues” too obvious |
| 2 | S11 | Weak | Descriptive failure atlas |
| 3 | S3 | Weak | Likely reconfirm retrieval dominance |
| 4 | S2 / S6 | Weak | Heuristic sweeps; S1 confounds |
| 5 | S10 / S9 | Weak | Transfer/generality secondary |
| — | S5, S7, S8, S12, S13, S14, S15 | **Rejected** | S1-poisoned, architecture, occupied, or inexecutable |

**No candidate clears all required bars simultaneously:**

| Required bar | Who fails |
|---|---|
| Empirical + falsifiable | All could in principle |
| Architecture-independent | S7 fails; S2/S5/S15 flirt |
| Novel vs current memory literature | **S4/S2/S3/S6/S11 fail hard** after 2026 wave |
| Executable on existing LTKM platform | S13 fails; others ok |
| Not S1 reword / not “system better” / not benchmark-only | S5/S12/S15/S9 fail |
| Survives Phase A lessons (no fake trade-offs / capacity confounds) | S5/S6/S12/S15 fail |

---

## Final recommendation

# ABANDON the current research direction

**Conclusion:** There is **no** remaining survivor from S2–S15 that is simultaneously (i) a sharp scientific phenomenon, (ii) novel relative to mid/late-2026 agent-memory literature, (iii) free of architecture-as-claim, (iv) not a covert S1 rewording, and (v) realistically executable on the present LTKM platform with a decisive kill pilot.

**What failed:**

| Program element | Outcome |
|---|---|
| Outline RQ-A (hierarchy improves consistency) | Architecture claim; occupied |
| CR-Gap | Closed negative/inconclusive |
| Information-Access | Occupied |
| S1 archive Pareto | Phase A **NO-GO** (joint degradation; \(\alpha=0\) dominates) |
| S2–S15 | All rejected under post-S1 critical gate |

**What this does *not* claim:** that hierarchical memory is useless as engineering, or that no agent-memory paper can ever be written. It claims that **this collaborative LTKM platform, used as infrastructure to hunt an ICLR empirical phenomenon from the enumerated survivors, has no viable scientific question left.**

### If the team continues anyway (not recommended)

The least-bad *object* would have been **S4** (consolidation lossiness → selective cue destruction), but it should be treated as **literature-dominated** and unlikely to clear ICLR novelty review against *Retain or Consolidate?*, *Useful Memories Become Faulty…*, MemoryData, and TiMem. Do **not** adopt S4 as a “rescue” of the program without an independent novelty audit that finds a **non-obvious, pre-registered dissociation** those papers did not already measure—and even then, expect Area Chair skepticism that the claim is obvious.

### Recommended programme actions

1. **Close Publication 03 ICLR track** under hierarchical LTKM / survivor RQs (record as abandoned scientific hunt).  
2. Keep `experiments/archive-pareto-pilot/` as a **negative result artefact** (allocation under fixed \(B\) produced no Pareto).  
3. Do **not** start another pilot on S2–S15 hoping for a different outcome without a *new* scientific object outside this list.  
4. Separate decision (out of scope here): whether collaborators still want a **systems/demo** paper at a non-ICLR venue—explicitly not an empirical ICLR claim.

---

## Explicit non-deliverable

No “best candidate” full protocol (H0/H1/IVs/…) is provided for adoption, because **none survive**. Providing one would violate the instruction to reject architecture/engineering/S1-reword papers and would falsely imply a green light.

---

## Files

- Created: `planning/post-s1-rq-selection.md` (this document)  
- Should update: `project-status.md` → direction abandoned
