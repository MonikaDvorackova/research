# Exact four-state hidden-phase discrimination for every K≥2

**2026-11-05. Status: complete constructive proof, algebraically checked. Novelty unverified.** This is a stronger exact result than the earlier large-K asymptotic statement.

## Statement

Use the same hidden-period binary signal model and phase-averaged stationary Bayes risk as `arbitrary-memory-rare-phase-asymptotics.md`. For each hypothesis h∈{+1,−1}, the informative signal has Bernoulli probability 1/2+h c, 0<c<1/2; the remaining K−1 signals are fair. The clockless, time-homogeneous observer has four memory states i=0,1,2,3; it always probes, increments after 1 and decrements after 0, reflecting at the boundaries. Let B be its fair-signal transition matrix and D=∂T(p)/∂p, so A_h=B+h c D.

**Theorem.** For every integer K≥2 and every 0<c<1/2, the observer achieves exactly

[
\boxed{\operatorname{TV}_4(K,c)=\frac{4c}{K},\qquad
P_{\mathrm{error},4}=\frac12-\frac{2c}{K}.}
]

This is exactly twice the **optimal two-state TV** 2c/K, under the same phase-averaged criterion. The theorem does not assert optimality among all four-state observers.

## Proof

The transition and derivative matrices are

[
B=\frac12\begin{pmatrix}1&1&0&0\\1&0&1&0\\0&1&0&1\\0&0&1&1\end{pmatrix},
\qquad
D=\begin{pmatrix}-1&1&0&0\\-1&0&1&0\\0&-1&0&1\\0&0&-1&1\end{pmatrix}.
]

Let π=(1/4,1/4,1/4,1/4). The row subspace V={(-a,-b,b,a): a,b∈R} is invariant under B. A direct multiplication establishes the **special cancellation identity**

[
\boxed{zDB=0\quad\text{for every }z\in V.}
]

Since πD=(-1/2,0,0,1/2) belongs to V, the zero-sum row

[
z=\pi D B^{K-1}(I-B^K+\Pi)^{-1},
\qquad \Pi=\mathbf1\pi,
]

also lies in V and satisfies z(I−B^K)=πD B^{K−1}. The inverse exists because B is irreducible and aperiodic, and the right-hand side has zero sum.

**Claim:** The phase-start stationary row under hypothesis h is exactly v_h=π+h c z.

Indeed, using K≥2 and the cancellation zDB^{K−1}=0,

[
(\pi+h c z)(B+h cD)B^{K-1}
=\pi+h c[zB^K+\pi D B^{K-1}]+c^2 zDB^{K-1}
=\pi+h c z.
]

This is a stationary probability row because the periodic product is a strictly mixing stochastic transition (and the solution is the unique stationary row); the algebraic expression therefore equals it. In particular v_++v_−=2π **exactly**, for every K≥2 and every c.

The exact phase-averaged response identity from `arbitrary-memory-rare-phase-asymptotics.md` states

[
\mu_+-\mu_- = \frac cK(v_++v_-)D(I-B+\Pi)^{-1}
=\frac{2c}{K}\pi D(I-B+\Pi)^{-1}.
]

The unique zero-sum Poisson solution w=πD(I−B+Π)^{-1} is

[
w=(-3/2,-1/2,1/2,3/2).
]

Consequently μ_+−μ_-=(2c/K)w and

[
\operatorname{TV}_4
=\frac12\|\mu_+-\mu_-\|_1
=\frac cK\|w\|_1
=\frac{4c}{K}.
]

Under equal priors, P_error=(1−TV)/2. ∎

## Why four states are special here

The nonlinear correction to v_h is killed after one uninformative step because zDB=0 on the antisymmetric subspace V. This is an **exact algebraic cancellation**, not a mixing approximation. It fails for general m (for example m=3 and m=6), so it cannot be extrapolated without proof.

## Reproducibility

The following exact SymPy checks were carried out independently for K=2,…,6:

- Solve v_h=v_h(B+h cD)B^{K−1}, v_h1=1.
- Verify v_++v_−=2π symbolically for every checked K.
- Verify the phase-averaged differences are (-3c/K,-c/K,c/K,3c/K), yielding TV=4c/K.

The general proof above covers **all** K≥2; the finite checks are only safeguards.

## Research status

This is a constructive exact result for a narrowly defined observer and observation criterion. Its novelty relative to finite-state hypothesis testing, Markov-chain perturbation, and periodic observation models is **not established**. It does not identify a simulator or provide evidence about the physical universe.

**Next:** investigate whether other memory sizes exhibit algebraic cancellations; characterize the subspaces satisfying zDB=0; compare the result against finite-state hypothesis-testing literature. The K≈m² critical-scaling limit for general m remains open.
