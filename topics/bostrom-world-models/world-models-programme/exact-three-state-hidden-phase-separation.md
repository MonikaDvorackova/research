# Exact three-state separation for a hidden periodic informative phase

**Date:** 2026-11-05. **Status:** Exact constructive result, independently calculated; not claimed novel. No global m=3 optimum is asserted.

## Statement

In the same hidden-phase binary hypothesis model as `proof-note-two-state-hidden-phase.md`, let K=2 and p_1=2/3, p_0=1/3 (c=1/6). Consider the deterministic, time-homogeneous, clockless three-state observer with memory i∈{0,1,2}. It always probes. On observing Y=1 it updates i to min(i+1,2); on Y=0 it updates i to max(i−1,0). Its final decision depends only on the memory state; the observer never observes the phase.

**Proposition (exact strict memory separation).** In the periodic stationary regime, after averaging uniformly over the unknown phase, the two hypotheses induce memory distributions

P_1(M=0,1,2) = (9/40, 13/40, 9/20),
P_0(M=0,1,2) = (9/20, 13/40, 9/40).

Thus TV(P_1,P_0)=9/40=0.225, and the equal-prior optimal Bayes error is (1−9/40)/2=31/80=0.3875.

By the two-state theorem in `proof-note-two-state-hidden-phase.md`, any irreducible clockless two-state observer has TV≤2c/K=1/6 and error≥5/12. Consequently the exhibited three-state observer achieves a **strict** 35% improvement in TV: (9/40)/(1/6)=27/20=1.35. Its error reduction is 5/12−31/80=7/240.

The proposition proves a separation between *two* and *three* memory states for this model. It does not prove that 9/40 is optimal among all three-state observers, nor that the separation is absent from existing finite-memory hypothesis testing literature.

## Reproducible algebra

Let the row-stochastic transition matrix for a step with P(Y=1)=p be

T(p) =
[ [1−p, p, 0],
  [1−p, 0, p],
  [0, 1−p, p] ].

At the informative phase, the transition is A_h=T(p_h); at the uninformative phase, it is B=T(1/2). A row distribution v at the start of the informative phase satisfies v=v A_h B. Solve this 3×3 stationary linear system, normalize v·1=1, and calculate the phase-averaged memory law as (v+v A_h)/2. Exact rational arithmetic gives the two distributions above.

To reproduce independently, solve the linear system using exact fractions or symbolic algebra; the result is not based on a floating-point optimizer.

The symmetry under p→1−p exchanges memory states 0 and 2. Hence the TV is |9/20−9/40|=9/40.

The Bayes decision is to guess h=0 at memory state 0 and h=1 at memory state 2; memory state 1 is uninformative under equal priors.

## Additional exact checks

For K=3, the same observer with p_1=2/3, p_0=1/3 has
P_1=(37/142,47/142,29/71),
P_0=(29/71,47/142,37/142),
so TV=21/142≈0.147887, exceeding the two-state ceiling 1/9≈0.111111.

These exact values are independently derived from the stationary matrix equations. They establish an explicit counterexample to the conjecture that the two-state 1/K optimum extends unchanged to three-state memory.

## Interpretation and boundaries

- The observer has no clock and no access to the hidden phase; its three states provide a bounded evidence accumulator.
- The theorem for two states remains consistent with this example.
- The phase-averaged output criterion is crucial. It is not the same as an observer allowed to know the phase or to access an unlimited transcript at decision time.
- The result is **not** a theorem about whether our universe is simulated.
- A strict finite-memory hierarchy may be well known from Hellman–Cover and related finite-state hypothesis-testing theory. The novelty gate must compare this **periodic hidden-phase** extension against primary literature before publication claims.

## Next mathematical obligations

1. Prove an upper bound for all three-state time-homogeneous stochastic observers at K=2, or establish a certified nontrivial bound.
2. Check whether the simple reflecting-walk construction remains strictly better than the two-state optimum for every c∈(0,1/2), and for which K.
3. Derive a general m-state expression for this explicit reflecting-walk family and compare it to Hellman–Cover bounds.
4. Verify the exact two-state proof independently, including its model restrictions and phase-averaged risk definition.
5. Read the original Hellman–Cover and subsequent finite-state hypothesis testing literature; no novelty claim before this check.

**Verdict:** CONTINUE mathematical research. The explicit separation is a real proved model-specific fact, but its novelty and broader significance are unresolved.
