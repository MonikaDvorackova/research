# Originality and proof status (embedded observers)

Assessment of every substantive statement produced or used. Labels: **P** proved (proof in the cited file), **K** known (source), **E** elementary, **C** conjecture, **O** computational observation, **U** unsupported. Novelty: **L** low / **M** medium / **U** uncertain. "Publishable alone?" means as the main claim of a peer-reviewed theoretical paper. This assessment is internal; no external specialist has checked any result.

| id | statement | status | where | novelty | publishable alone? |
|---|---|---|---|---|---|
| T1 | Embedded finite observer in a sequentially factored host = finite-state controller of a POMDP (Theorem 1) | P (+ O exact check) | formal model §2 | L (standard FSC–POMDP identification) | no |
| T2 | Without SF1 there are hosts with equal observer-visible laws and different interventional laws (Theorem 2) | P (+ O) | formal model §3 | L (= Causal Hierarchy Theorem / IV) | no |
| T3 | Latency d ⇒ delayed POMDP (Prop. 3) | E | formal model §4 | L | no |
| T4 | Factorization non-uniqueness ⇒ targets must be invariant (minimal realisation of the visible process) (Prop. 4) | E | formal model §5 | L | no |
| E3 | Final conclusions of an m-state observer take ≤ m values ⇒ identifying K behaviourally distinct hypotheses needs m ≥ K | E | log | L | no |
| E4 | Strict memory hierarchy (combination lock) | E | log | L | no |
| E6 | No finite-state self-reference barrier beyond reachability + memory bound | E (negative result) | log | L | no |
| E8 | Pinsker-type bound E_a[TV²] ≤ I(A;U)/2 for the bias from dependence of action and hidden variable | P (elementary) | log | L | no |
| E9 | Persistent latent ⇒ cross-time coupling identified by Kruskal-type conditions; same-noise coupling not | E + K (Allman et al.) | log | L | no |
| E10 | Resource-coupled indistinguishability reduces to PRG/PRF theory | E + K | log | L | no |
| K1 | Hellman–Cover: m-state time-invariant automaton, i.i.d. hypothesis testing, optimal error 1/(1+λ^{m−1}) | K (S + secondary restatement; original not read) | formal model §6 | — | — |
| **Thm 3** | Two-state time-homogeneous observer, hidden period-K informative phase: optimal asymptotic error ½ − c/K, attained by the memoryless automaton; persistence cannot be exploited | **P** (complete argument + O) | proof note | **U, probably L**: special-case calculation containing the m = 2, K = 1 Hellman–Cover value | **no**: too narrow, relevance to identification of generative structure is indirect |
| Id-m | General-m exact identity: TV = (1/K)·½‖2c x̂₀ D Z‖₁ with Z the fundamental matrix of the uninformative kernel | O (checked to 9×10⁻¹³ on 300 automata); proof = Lemma 2 with matrices, **not written out** | `results/embedded/general_m_identity_check.json` | U | no |
| C-m | For m ≥ 3 persistence is slightly exploitable (error below the random-phase dilution value) | U (searches unreliable) | proof note remark | U | no |

## Strongest result obtained
**Theorem 3** is the only statement for which I did not find the result among the sources I could access, and it is proved. Its content: for a finite, time-homogeneous, clockless embedded observer with **two** memory states, a hidden periodic informative phase of period K dilutes the best achievable discriminability between two simple hypotheses by exactly 1/K, and the optimum is the memoryless "last signal" automaton. It is **not** a result about identifying generative structure in general, is special (m = 2, symmetric binary signals, periodic phase), and its K = 1 case is the two-state Hellman–Cover optimum. I assess its originality as *uncertain, probably low*, and its significance for the central question as *small*: it quantifies, in one tractable case, a genuine embedding constraint (no external clock, finite homogeneous memory), but it is not a theorem a journal would take as the main contribution.

## What the investigation established about the central question
1. **Embedding reduces, in the natural model, to known structures.** A physically embedded finite-state observer in a sequentially factored host is a POMDP controlled by a finite-state controller (Theorem 1). Nothing about identifiability changes except the policy class. The one restriction that is genuinely *not* a restriction on reach is **finite, time-homogeneous memory**, whose consequences (irreducible error floors for noisy mechanisms; dependence on a clock) are the classical Cover/Hellman–Cover theory.
2. **Where embedding creates a distinct feature, the feature is known:** shared noise between actuator and environment (confounded POMDP/instrument; Causal Hierarchy Theorem; Bell-type measurement dependence), non-uniqueness of the factorization (realisation theory), self-inference limits (Wolpert), realizability failure (embedded agency/grain of truth).
3. **No evidence that embedding yields identifiability or impossibility results beyond those of standard system identification, causal inference, active learning and computational indistinguishability**, in the finite-state model studied. This is the negative answer to the directive's question as posed; it is limited to the models and attempts recorded.

## Ready for a genuine original paper?
**No.** No result passes the originality gate. The only new-candidate theorem (Theorem 3) is narrow and of uncertain novelty; the framework results are corollaries. A paper restating them would be expository. Not claimed: any new impossibility theorem for embedded observers; any evidence about whether our universe is simulated.

## Strongest remaining unresolved question
**General finite memory under hidden structure:** for an m-state time-homogeneous observer-controller and two hypotheses that differ only in a hidden periodic phase (or hidden Markov context) of the environment, what is the optimal asymptotic discriminability TV*(m, K)? The exact identity (Id-m) reduces it to maximising ‖x̂₀ D Z‖₁ over automata. m = 2 is solved (Theorem 3); m ≥ 3 is open and numerically suggests a slight gain from persistence. A related, literature-check-first lead (unverified): finite-memory identification of two long deterministic histories is the *separating words problem* of automata theory.

## Update 2026-11-06 (reflecting-walk programme)
See `mlr-and-single-crossing-theorem.md` (MLR and single crossing PROVED; strictly increasing phase-averaged mass function), `memory-hierarchy-and-walk-nonoptimality.md` (K = 2 even-m closed forms and hierarchy proved; reflecting-walk optimality DISPROVED by exact rational certificate) and `reflecting-walk-audit-and-literature-status.md` (independent audit: no formula errors found; literature classification). Novelty of every item remains unverified; the monotone-cone mechanism is elementary and likely related to Keilson–Kester monotone/unimodality-preservation theory (originals not accessed).
