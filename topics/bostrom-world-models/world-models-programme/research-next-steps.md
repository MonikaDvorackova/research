# Research next steps (embedded observers)

Based on the mathematical findings in `candidate-theorems-and-counterexamples.md`, not on a project summary. Decision gates are explicit; every step can end the line.

## Where the mathematics stands
Embedding adds no identifiability structure beyond known theory in the sequentially factored finite model, except the **finite, time-homogeneous (clockless) memory** restriction. The only exact new-candidate result is Theorem 3 (m = 2). The strongest remaining unresolved question is the general-m version under hidden structure.

## Step 1 — close the literature on finite-memory testing (gate G1; ≈ 2–3 weeks, reading only)
Read in full the originals that could not be obtained: Hellman & Cover (1970), Cover (1969), Hellman–Cover on memory saved by randomisation, Wilson (2014) and Leung (arXiv:2009.11917 full proofs); Gold (1967), Angluin (1987) (need a text-layer copy), Kelly (1996, chs. 3–4); Hsu–Kontorovich–Szepesvári (2015); Groz et al. (2015); Chase on the separating-words problem (check that the link in the prior-art file is real). For each, record the exact theorem and whether Theorem 3 or the m-state identity is a corollary.
**G1 decision:** if Theorem 3 (any m=2 hidden-phase statement) already appears, record it and **STOP** the finite-memory line; otherwise continue to Step 2.

## Step 2 — write out and prove the general-m identity (≈ 1 week)
State Lemma 2 for m states: S = k Z with Z = (I − B + 1π)⁻¹, k = 2c x̂₀ D, D = Q(T_1 − T_0), TV = ½‖S‖₁/K; the proof is Lemma 2 with matrices (zero-sum k). Cross-check on exact rational examples (the numeric check is `scripts/embedded_general_m_identity_check.py`).

## Step 3 — the exact optimisation for m = 3 (≈ 3–4 weeks)
Question: TV*(3, K) for symmetric binary signals. Approach: (i) reduce the maximisation of ‖x̂₀DZ‖₁ over 3-state automata to a finite-dimensional polynomial optimisation (parameters: B ∈ stochastic 3×3, D with row constraints, q); (ii) certify upper bounds by semidefinite relaxation (moment/SOS) or by cylindrical decomposition on a reduced parameterisation; (iii) compare with the random-phase dilution value 1/(1+λ′²) and with the exact m = 3, K = 1 Hellman–Cover value 1/(1+λ²). *Success:* a closed form or a certified bound showing strictly better-than-dilution performance by persistence (m = 3) or equality. *Failure:* the optimum equals the dilution value (then the hidden-phase structure is exploitable only with a clock: conjecture C-clock) or the problem reduces to Hellman–Cover with effective λ′ (then record as a corollary and stop).
The earlier stochastic optimiser does not converge for m ≥ 3 (boundary optima); do not rely on it. Any computation must be exact or certified.

## Step 4 — clock cost (only if Step 3 yields a pattern)
Define the *clock cost*: the smallest m such that an m-state clockless automaton matches the performance of an unbounded-memory observer up to ε on the hidden periodic phase of period K. Conjecture (U): it grows linearly with K for fixed ε, with persistence changing the constant only. Prove a lower bound by the memory-label argument (E3) plus the phase-ambiguity argument, or find a counterexample (a clever sticky automaton). This would be a statement about **what finite embedded memory can know about the temporal structure of its world**, the nearest thing found to a distinctive embedding result.

## Step 5 — decision gate G2 (after Step 3–4)
Continue to a paper only if (a) a general (m, K) statement or a sharp lower bound is proved, (b) it is not a corollary of the Step-1 literature, and (c) an external specialist in learning theory or information theory has checked the proof. The target would be a short theoretical note on **finite-memory identification under hidden periodic structure**, framed honestly as a result in finite-memory hypothesis testing with a motivation from embedded observers — **not** as a theorem about simulations or about whether the universe is simulated. If (a) or (b) fails, **STOP** and archive the embedded-observer programme as: reductions proved, one narrow exact result, no original theorem.

## What not to do
No new agents, benchmarks, neural networks, symbolic-regression pipelines or confirmatory studies. No manuscript until the originality gate (Step 5) is passed. No claim about simulation, and no use of toy-system results as evidence about the physical universe.

## Verdict by direction (carried from the log)
A self-reference — STOP. B endogenous interventions — STOP. C resource coupling / finite homogeneous memory — narrow CONTINUE (Steps 1–4), conditional on gate G1. D counterfactual access without replay — STOP. E learned world models — STOP.
