# Randomization Advantage in Finite-Memory Detection of Hidden Periodic Signals

**Working research manuscript — draft v0.1, 2026-11-06. Not submission-ready.**

## Abstract

We study binary hypothesis testing by time-homogeneous finite-state observers without access to the phase of a periodically informative binary observation process. Under two hypotheses, one observation in each two-step period is Bernoulli with parameter \(1/2\pm c\), while the other is fair. An observer has three memory states and updates its memory using either deterministic or randomized input-conditioned transitions. Starting from a common uniform memory distribution, we evaluate the total variation distance between the two memory laws after two complete periods, averaged over the observation phase. We prove by an exact finite enumeration certificate that the best deterministic observer achieves \(c(31+4c^2)/24\) for every \(0<c<1/2\). A fixed explicit randomized observer achieves \(c(6424571+563108c^2)/4800000\), exceeding the deterministic optimum by \(c(74857-78964c^2)/1600000>0\). The result is finite-horizon, nonasymptotic in the observation horizon, and valid throughout the entire admissible signal range. We additionally analyze a parameterized randomized family, deriving its stationary performance, an exact finite-horizon recurrence, and a metastable crossover as the transition probability tends to zero. We distinguish this specific separation from any claim of globally optimal randomized performance or novelty relative to the classical literature on finite-memory statistical decisions.

**Keywords:** finite-state hypothesis testing; randomized automata; hidden periodic signals; finite memory; total variation; metastability.

## 1. Introduction

Finite-memory observers face an information bottleneck: incoming observations must be compressed into a fixed number of internal states. In binary hypothesis testing, randomization can change the attainable performance of finite-state decision rules, as studied in the classical literature of Hellman and Cover. Here we consider a restricted but distinct setting in which the observation stream has a hidden period and the observer receives no external phase clock.

Our contribution is an exact finite-horizon separation. For three memory states and a period of two, a single explicit randomized rule beats every deterministic rule for all admissible signal strengths after two complete periods, under a specified common initialization and phase-averaged readout. We also quantify the transient behavior of a family that approaches high stationary discrimination as its transitions become rare.

The result concerns the mathematical distinguishability of two synthetic observation laws. It neither tests nor provides evidence for the philosophical simulation hypothesis.

### Contributions

1. An explicit phase-averaged finite-horizon testing model with a hidden informative phase.
2. An all-bias exact deterministic envelope for the three-state, two-period horizon.
3. A fixed randomized construction and an explicit strictly positive gap for all \(0<c<1/2\).
4. A separate analysis of near-reducible randomized observers: stationary performance, finite-horizon recurrence, and noncommuting long-time/small-noise limits.

## 2. Model and evaluation

Let \(h\in\{-1,+1\}\) denote the unknown hypothesis and \(0<c<1/2\). Observations are independent conditional on \(h\) and their phase, with one informative step per period of length \(K=2\):

\[
\Pr_h(Y=1\mid\text{informative phase})=\tfrac12+hc,\qquad
\Pr_h(Y=1\mid\text{uninformative phase})=\tfrac12.
\]

The observer has three memory states \(\{0,1,2\}\) and no phase clock. For each input \(y\in\{0,1\}\), a row-stochastic matrix \(T_y\) specifies the conditional memory transition. A deterministic observer is one for which each row of both matrices is a coordinate vector. There are \(3^6=729\) ordered deterministic observers.

Define

\[
B=\frac{T_0+T_1}{2},\quad
A_h=(\tfrac12-hc)T_0+(\tfrac12+hc)T_1,\quad
P_h=A_h B.
\]

The common phase-zero initial distribution is \(u=(1/3,1/3,1/3)\). After \(n\) complete periods, the phase-averaged readout is

\[
\mu_h^{(n)}=uP_h^n\frac{I+A_h}{2}.
\]

We measure distinguishability by

\[
D_n(T_0,T_1;c)=\operatorname{TV}(\mu_+^{(n)},\mu_-^{(n)})
=\frac12\sum_{i=0}^2|\mu_+^{(n)}(i)-\mu_-^{(n)}(i)|.
\]

The phase-averaged convention and uniform initialization are substantive modeling assumptions, not technical conveniences that can be dropped from the theorem.

## 3. Main result

**Theorem 1 (finite-horizon randomization advantage at every bias).**
For \(n=2\), \(m=3\), \(K=2\), the common uniform initialization and the phase-averaged readout defined above, the deterministic optimum satisfies

\[
\boxed{\max_{T_0,T_1\ {\rm deterministic}}D_2(T_0,T_1;c)
=\frac{c(31+4c^2)}{24}}
\quad(0<c<1/2).
\]

Consider the fixed randomized transition matrices

\[
R_0=\begin{pmatrix}3/10&7/10&0\\0&0&1\\0&0&1\end{pmatrix},
\quad
R_1=\begin{pmatrix}1&0&0\\1&0&0\\0&7/10&3/10\end{pmatrix}.
\]

They satisfy

\[
D_2(R_0,R_1;c)=\frac{c(6424571+563108c^2)}{4800000},
\]

and consequently

\[
\boxed{D_2(R_0,R_1;c)-\max_{\rm deterministic}D_2(c)
=\frac{c(74857-78964c^2)}{1600000}>0.}
\]

**Proof.**
For a deterministic pair \(T_0,T_1\), each coordinate of \(\mu_+^{(2)}-\mu_-^{(2)}\) is an odd polynomial in \(c\) of degree at most three. Indeed, the defining product contains three factors affine in \(hc\), and subtracting the two hypotheses eliminates all even powers. Writing \(x=c^2\), every signed subset sum divided by \(c\) is affine in \(x\).

For a zero-sum vector \(d\in\mathbb R^3\), its total variation is \(\max_{S\subseteq\{0,1,2\}}\sum_{i\in S}d_i\). Enumerate all \(27^2=729\) deterministic transition pairs and all six nonempty proper subsets \(S\). The exact rational certificate in the reproducibility supplement verifies, for each pair and subset, that the affine polynomial

\[
\frac{31+4x}{24}-\frac1c\sum_{i\in S}
\bigl(\mu_+^{(2)}(i)-\mu_-^{(2)}(i)\bigr)
\]

is nonnegative on \(x\in[0,1/4]\). It suffices to check both endpoints because each such polynomial is affine; this check is exact and finite. Thus every deterministic observer is bounded above by \(c(31+4c^2)/24\).

The deterministic reflecting walk specified by the destination maps \(f_0=(0,0,1)\) and \(f_1=(1,2,2)\) has signed law difference

\[
\mu_+^{(2)}-\mu_-^{(2)}
=\frac{c(31+4c^2)}{24}(-1,0,1),
\]

and attains the bound.

For \(R_0,R_1\), direct symbolic multiplication yields

\[
\mu_+^{(2)}-\mu_-^{(2)}
=\frac{c(6424571+563108c^2)}{4800000}(1,0,-1).
\]

Subtracting the deterministic bound gives the stated gap. Since \(c^2<1/4\), the numerator's parenthesis exceeds \(74857-78964/4=55116>0\). \(\square\)

**Remark (certificate implementation).** The earlier repository certificate uses a degree-two Bernstein nonnegativity check, which is conservative but sufficient for the actual affine polynomials. A minimal independent verification can simply evaluate each signed subset inequality at \(c^2=0\) and \(c^2=1/4\) with exact rational arithmetic. The full enumeration script must be preserved with the submission and rerun in a clean environment.

## 4. Near-reducible randomized family

For \(0<\varepsilon<1\), consider

\[
T_0(\varepsilon)=
\begin{pmatrix}1-\varepsilon&\varepsilon&0\\0&0&1\\0&0&1\end{pmatrix},
\quad
T_1(\varepsilon)=
\begin{pmatrix}1&0&0\\1&0&0\\0&\varepsilon&1-\varepsilon\end{pmatrix}.
\]

The stationary phase-averaged total variation is

\[
F(c,\varepsilon)=
\frac{4c(4-\varepsilon)}
{8+2\varepsilon-\varepsilon^2-8c^2\varepsilon+4c^2\varepsilon^2},
\qquad
\lim_{\varepsilon\downarrow0}F(c,\varepsilon)=2c.
\]

This is a lower bound on the supremum of stationary randomized performance; it is not a proof of global stochastic optimality.

### 4.1 Exact finite-horizon recurrence

Let \(d_n\) denote the signed state-zero difference after phase averaging. Reflection symmetry yields \(\mu_+^{(n)}-\mu_-^{(n)}=(d_n,0,-d_n)\), so \(D_n=|d_n|\). Put

\[
S=1-\varepsilon+\varepsilon^2/2,\qquad
Q=\varepsilon^2(2-\varepsilon)^2(1-4c^2)/16.
\]

The corrected characteristic polynomial of \(P_h\) is \((x-1)(x^2-Sx+Q)\), independent of \(h\). Hence

\[
d_{n+2}=S d_{n+1}-Qd_n+(1-S+Q)F,
\]

with

\[
d_0=c(1+\varepsilon)/3,\qquad
d_1=c(\varepsilon^3-5\varepsilon^2+7\varepsilon+4)/6.
\]

These formulas provide an exact finite-horizon calculation for this family.

### 4.2 Metastable scaling

At \(\varepsilon=0\), states 0 and 2 are absorbing, and the uniform initialization collapses after one period to \((1/2+hc/3,0,1/2-hc/3)\). For every \(\varepsilon>0\), the period chain has a unique stationary law, but its slow eigenvalue satisfies \(\lambda_2=1-\varepsilon+O_c(\varepsilon^2)\).

For integer \(n\ge1\), in the joint limit \(\varepsilon\downarrow0\), \(n\varepsilon\to t\ge0\), the phase-averaged distinguishability tends to

\[
\boxed{\lim D_n=2c\bigl(1-\tfrac23 e^{-t}\bigr).}
\]

In particular, the limits \(\varepsilon\to0\) and \(n\to\infty\) do not commute: their two orders yield \(2c/3\) and \(2c\), respectively. This result characterizes the specified family; it is not a general minimax sample-complexity theorem.

## 5. Discussion and limitations

Theorem 1 is a strict finite-horizon comparison over the complete deterministic class. Its proof does not assume irreducibility and does not invoke asymptotic stationary distributions. The result is conditional on the uniform initial distribution, hidden two-step period, phase-averaged readout, and three memory states. No claim is made that the exhibited randomized rule is optimal among all stochastic observers.

The near-reducible family exposes an important distinction between stationary performance and finite-horizon performance: approaching the stationary supremum may require an observation horizon diverging as the transition probability decreases.

Classical finite-memory testing already contains randomization advantages. The novelty question is therefore narrower: does the particular **hidden-periodic, phase-unaware, finite-horizon, all-bias exact separation** appear in prior literature? This must be resolved by targeted bibliographic review before claiming originality.

## 6. Conclusion

We establish an exact finite-horizon separation between randomized and deterministic three-state observers of a periodically informative binary source without phase information. A fixed randomized observer beats the deterministic optimum for every nonzero admissible signal strength. An explicit near-reducible family further reveals a metastable tradeoff between high stationary distinguishability and the time required to approach it.

## References — provisional, verify bibliographic details

- M. E. Hellman and T. M. Cover, “Learning with Finite Memory,” *Annals of Mathematical Statistics*, 1970. DOI: 10.1214/aoms/1177696958.
- M. E. Hellman and T. M. Cover, “On Memory Saved by Randomization,” 1971. Bibliographic venue, pages and stable DOI to be verified.
- Additional work on finite-state hypothesis testing, periodic hidden-state models, and randomized automata: **literature review pending**.

## Reproducibility and submission checklist

- [x] Explicit theorem with closed-form positive gap.
- [x] Exact exhaustive deterministic certificate committed separately.
- [x] Independent symbolic check of reflecting and randomized signed differences.
- [x] Corrected characteristic polynomial in original source note.
- [ ] Run a clean-room independent exact 729-rule endpoint audit and archive its machine-readable results.
- [ ] Verify finite-horizon recurrence and crossover against fresh simulations.
- [ ] Complete targeted prior-art search and bibliographic metadata.
- [ ] Prepare journal/conference LaTeX source, theorem numbering, proofs appendix, figure and code archive.
- [ ] External expert review of definitions, novelty and mathematical correctness.

**Research note:** this manuscript is a coherent first draft, not a validated submission or a claim of new discovery relative to all published work.
