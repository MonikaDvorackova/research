---
id: pub-03-c4-consolidation-novelty-audit
title: "C4 consolidation novelty audit"
type: research-notes
status: audit-complete
created: 2026-08-02
updated: 2026-08-02
---

# C4 novelty audit — task-conditioned sufficiency / irreversible consolidation collapse

**Provisional RQ:** When a memory consolidation representation is learned for one task distribution, under what conditions does it irreversibly discard information that becomes necessary after a task or query-distribution shift?

**Intended object:** task-conditioned sufficiency and irreversible representation collapse in learned memory consolidation under distribution shift — **not** “compression loses information,” summary omissions, larger-is-better, or architecture bakeoffs.

## 1. Distinction from closed S4

Closed **S4** ([`post-s1-rq-selection.md`](post-s1-rq-selection.md)): consolidation **lossiness** selectively destroys temporal/conflict cues (dose–response; descriptive information destruction). Rejected as occupied/obvious vs *Retain or Consolidate?*, *Useful Memories…*, MemoryData, TiMem.

| Criterion for C4 survival | Result |
|---|---|
| Representation learned under \(\mathcal{T}_1\) | Framing yes; literature already has learned/LLM consolidators |
| Sufficient for \(\mathcal{T}_1\) | Standard IB / abstraction goal |
| Shift to \(\mathcal{T}_2\) | Standard transfer / reward-change setting |
| Irreversible removal; retrained \(d_2\) fails | Classical SS consequence if \(H\) discarded |
| Alternative objective could have preserved transferable SS | Classical multi-task / task-agnostic compression |

**Verdict on distinction:** **Not scientifically substantive.** C4 is a **learning-theoretic rephrase** of S4’s information-destruction neighborhood plus textbook state abstraction. Hostile reading: S4 with an encoder and a decoder-retrain control.

## 2. Novelty classification

### Primary: `STANDARD STATE-ABSTRACTION RESULT APPLIED TO MEMORY`

Twin labels that also apply:

- `STANDARD INFORMATION-BOTTLENECK RESULT APPLIED TO MEMORY` (claim B / transfer radius)
- `TOO OBVIOUS` for claim A (“\(\mathcal{T}_1\)-optimal compression can erase \(\mathcal{T}_2\) factors”)
- Empirically **adjacent / partially OCCUPIED** by *Useful Memories Become Faulty…* for path-dependent irreversible consolidation failures

Not `OPEN`. Not `PARTIALLY OPEN` for Pub-03 survival. Not `NOT FEASIBLE` locally — feasibility is irrelevant once novelty fails.

## 3. Closest occupying work

1. **State abstraction / bisimulation / MDP homomorphism** — task-conditioned sufficiency; failure under reward/task change (classical).  
2. **IB zero-shot transfer theory** — compression–transfer frontier, encoder diagnostics.  
3. **Useful Memories Become Faulty…** — continuous consolidation irreversibly harms reuse; applicability stripping; task-switch overwrite; keep raw episodes.  
4. **Retain or Consolidate?** — consolidation vs raw under budget; query-critical detail loss (**S4**).  
5. **MCMA** — learned abstraction aimed at **transfer success** (opposite polarity).

## 4. Exact residual

A synthetic demo that \(\mathcal{T}_1\)-trained bottlenecks fail \(\mathcal{T}_2\) after discarding \(H\), with gap scaling in SS overlap, **after** retraining \(d_2\).

That residual is **exactly what standard theory predicts** and what hostile reviewers will call “obvious.” Empirically, Useful Memories already shows consolidation can permanently damage later performance relative to retaining episodes.

**No distinct Pub-03 scientific object remains.**

## 5. Claim recommendation

**None.** A–D all fail (obvious / standard / S1-like / occupied).

## 6. ICLR test

| Question | Answer |
|---|---|
| Representation-learning paper? | Only as textbook SS/IB application |
| Continual-learning paper? | Path dependence occupied by Useful Memories; else CF |
| State-abstraction paper? | **Yes — and already done outside “memory” branding** |
| Memory-system application only? | **Yes, if pursued** |

Strongest viable shape would need items 1–3 (new structural theorem + controlled env + predicted collapse). **Item 1 fails.** Therefore **not ICLR-viable**.

## 7. Decision

**ABANDON C4.**

Do not implement a pilot.  
Do not rebrand S4 as C4.
