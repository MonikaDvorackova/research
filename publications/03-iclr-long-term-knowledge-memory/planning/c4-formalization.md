---
id: pub-03-c4-formalization
title: "C4 formalization — task-conditioned sufficiency and irreversible collapse"
type: research-notes
status: audit-complete
created: 2026-08-02
updated: 2026-08-02
---

# C4 formalization

## Objects

| Symbol | Meaning |
|---|---|
| \(H\) | Interaction history (possibly non-replayable after consolidation) |
| \(Z=g_\theta(H)\) | Consolidated representation / bottleneck state |
| \(\mathcal{T}_1,\mathcal{T}_2\) | Training and shifted task families |
| \(Y_1,Y_2\) | Target variables for \(\mathcal{T}_1,\mathcal{T}_2\) |
| \(d_1\) | Decoder / policy head for \(\mathcal{T}_1\) |
| \(d_2^\star\) | Optimal (or strongly trained) decoder for \(\mathcal{T}_2\) given only \(Z\) |
| \(h_2^\star\) | Optimal decoder given full \(H\) |

## \(\mathcal{T}_1\)-sufficiency

Exact (information): \(Y_1 \perp H \mid Z\).

Operational finite-task equivalent: there exists \(d_1\) such that
\(\mathbb{E}[\ell(d_1(Z),Y_1)] \le \inf_{h}\mathbb{E}[\ell(h(H),Y_1)]+\varepsilon_1\).

## Transfer insufficiency (irreversible representational loss)

\[
\inf_{d_2}\mathbb{E}[\ell(d_2(Z),Y_2)]
\;>\;
\inf_{h_2}\mathbb{E}[\ell(h_2(H),Y_2)]+\varepsilon.
\]

**Critical clause:** the gap must remain after training \(d_2\) with adequate labeled \(\mathcal{T}_2\) data **without access to \(H\)**.  
If retraining \(d_2\) closes the gap, the failure is **decoder mismatch**, not irreversible collapse.

## Distinction from closed S4

| | Closed S4 | Intended C4 |
|---|---|---|
| Object | Selective cue destruction under consolidation lossiness | Learned \(\mathcal{T}_1\)-sufficient \(Z\) that is \(\mathcal{T}_2\)-insufficient after irreversible discard of \(H\) |
| IV | Lossiness ladder / compression severity | Task-statistic overlap, consolidation objective, timing, capacity vs selective discard |
| Controls | Cue probes vs single-hop | Retrained \(d_2^\star\) vs raw-history oracle; capacity-matched multi-task baselines |
| Learning? | Transform severity (often non-learned) | Encoder trained under \(\mathcal{T}_1\) objective |

**Audit finding:** the distinction is **rhetorically real** but **not scientifically substantive enough** for a new ICLR object. Once \(H\) is discarded, C4’s predicted gap is the classical fact that a \(\mathcal{T}_1\)-sufficient statistic need not be \(\mathcal{T}_2\)-sufficient — standard state-abstraction / sufficient-statistic theory — dressed as agent memory consolidation.

## Candidate claims — evaluation

### A. Task-optimal consolidation can be maximally non-transferable
Construct \(s=(u,v)\), \(\mathcal{T}_1\) needs \(u\) only, bottleneck dim 1, \(g\) keeps \(u\), \(\mathcal{T}_2\) needs \(v\).  
**Reject as main claim:** **TOO OBVIOUS** construction.

### B. Transfer failure follows task-overlap structure
Gap scales with overlap of sufficient statistics / shared latent factors.  
**Theoretically real**, **standard** (state abstraction, IB transfer radius, bisimulation under reward change). Memory nouns add no new structure.

### C. Multi-objective consolidation creates a transfer frontier
Trade current compression vs future-task recoverability under unknown future mixture.  
**Reject for Pub-03:** collapses toward capacity / rate–distortion Pareto (S1-adjacent optics) unless a new non-Pareto mechanism appears — not found.

### D. Consolidation timing creates irreversible path dependence
Early \(\mathcal{T}_1\)-specific consolidation prevents later recovery even if objective later changes.  
**Closest to memory-specific** (online, irreversible, non-replayable \(H\)).  
**Empirically occupied** by *Useful Memories Become Faulty…* (stream vs static; task-switch overwrite; applicability stripping). Distinct from parametric catastrophic forgetting only if parameters frozen and only \(Z\) changes — still not a new law beyond “discarded bits stay discarded.”

**Recommended claim:** **none.** Do not advance A–D as Pub-03 primary.

## Strongest possible proposition

**Proposition (standard).**  
Let \(Z\) be a minimal sufficient statistic for \(Y_1\) given \(H\). If \(I(Y_2;H\mid Z)>0\) and \(H\) is unavailable at \(\mathcal{T}_2\) time, then
\(\inf_{d_2}\mathbb{E}[\ell(d_2(Z),Y_2)] > \inf_{h_2}\mathbb{E}[\ell(h_2(H),Y_2)]\)
under standard identifiability of the losses.  
**Status:** **standard sufficient-statistic / state-abstraction corollary.** Not new.

**Memory path-dependence corollary (also standard once stated):** repeated irreversible maps \(H\mapsto Z_1\mapsto Z_2\mapsto\cdots\) can strictly decrease \(I(Y_2;Z_k)\) even when each step is \(\mathcal{T}_1\)-optimal.  
**Status:** information processing inequality + task-specific optimality; empirically illustrated by Useful Memories. Not a new theorem.

## Assumptions that look “memory-specific” but do not rescue novelty

| Structure | Why insufficient alone |
|---|---|
| Online irreversible consolidation | Still IB/SS once \(H\) gone |
| Unknown future task at write time | Classical unknown-future / multi-task compression |
| Bounded persistent state | Rate–distortion / capacity |
| Non-replayable history | Makes irreversibility operational — does not create new math |
| Repeated consolidation | Composition of lossy maps — standard |
