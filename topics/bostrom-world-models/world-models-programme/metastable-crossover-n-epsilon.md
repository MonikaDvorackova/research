# Metastable crossover curve at n epsilon -> t

Date: 2026-11-06. Exact perturbative derivation for the explicit three-state family, independently checked numerically. Not a global stochastic optimum theorem.

## Model

For 0<c<1/2 and 0<epsilon<1, let
T0=[[1-epsilon,epsilon,0],[0,0,1],[0,0,1]],
T1=[[1,0,0],[1,0,0],[0,epsilon,1-epsilon]].
Define B=(T0+T1)/2, A_h=(1/2-h*c)T0+(1/2+h*c)T1, P_h=A_h B, h in {+1,-1}. Starting from u=(1/3,1/3,1/3), define v_h^(n,epsilon)=u P_h^n and phase-averaged memory law mu_h^(n,epsilon)=v_h^(n,epsilon)(I+A_h)/2.

## Theorem

For every fixed t>=0, every sequence epsilon -> 0+ and integers n=n(epsilon) with n>=1 and n*epsilon -> t,

\[
\boxed{\lim_{\epsilon\to0^+,\ n\epsilon\to t}\operatorname{TV}(\mu_+^{(n,\epsilon)},\mu_-^{(n,\epsilon)})=2c(1-\tfrac23 e^{-t}).}
\]

The restriction n>=1 matters at t=0 because the initial unprocessed distribution is uniform; the first-period boundary layer occurs before the slow scale.

## Derivation

At epsilon=0 the period transition is

\[
P_h(0)=\begin{pmatrix}
1&0&0\\
1/2+hc&0&1/2-hc\\
0&0&1
\end{pmatrix}.
\]

States 0 and 2 are absorbing, and state 1 is transient. One initial period sends the common uniform law to

\[
uP_h(0)=(1/2+hc/3,\ 0,\ 1/2-hc/3).
\]

To first order in epsilon, the effective 0 -> 2 transition probability per period is epsilon times

\[
(1/4-hc/2)+(1/2)(1/2-hc)=1/2-hc.
\]

The first summand is the direct P_h'(0) transition from 0 to 2; the second is the P_h'(0) transition from 0 to transient state 1, followed by its immediate absorption into state 2 under P_h(0). Similarly the effective 2 -> 0 transition rate is 1/2+hc. Hence the limiting two-state continuous-time generator, with states ordered (0,2), is

\[
Q_h=\begin{pmatrix}
-(1/2-hc)&1/2-hc\\
1/2+hc&-(1/2+hc)
\end{pmatrix}.
\]

Its unique invariant law is (1/2+hc,1/2-hc) and its nonzero eigenvalue is -1. Starting from the post-boundary-layer law, the probability of state 0 at scaled time t is

\[
x_h(t)=1/2+hc+(hc/3-hc)e^{-t}
=1/2+hc(1-\tfrac23e^{-t}).
\]

The transient-state probability vanishes as epsilon -> 0 for any n>=1 with n epsilon -> t, and A_h(0) fixes both absorbing states. Thus the phase average has the same limiting law, and the difference between the h=+ and h=- state-0 probabilities is 2c(1-2e^{-t}/3). State 2 has the opposite difference. Total variation equals the absolute state-0 difference.

The convergence can be justified by finite-dimensional singular perturbation: after the first step the transient component is O(epsilon); the effective two-state transition per period is I+epsilon Q_h+O(epsilon^2); then (I+epsilon Q_h+O(epsilon^2))^n -> exp(t Q_h). Uniformity holds for t in compact subsets of [0,infinity) after the initial one-period boundary layer.

## Quantitative implications

At c=1/5: F(t)=0.4-(4/15)e^{-t}. For any 0<delta<4c/3, to attain a limiting TV at least 2c-delta it suffices and is necessary on this crossover curve that

\[
t\ge\log\frac{4c}{3\delta},
\quad\text{or}\quad
n\gtrsim\epsilon^{-1}\log\frac{4c}{3\delta}.
\]

This is a within-family asymptotic time-to-accuracy statement, not a universal finite-sample lower bound.

Numerical check at c=0.2:
epsilon=0.002, t=1: TV=0.301683 versus limit 0.301899;
epsilon=0.0005, t=1: TV=0.301845 versus limit 0.301899.
At t=3: epsilon=0.0005 gives 0.386639 versus limit 0.386723.

## Scope

This derivation does not prove sup TV(3,2,c)=2c. It assumes phase-zero uniform initialization, phase-averaged readout, and the specific near-reducible stochastic family. Novelty versus finite-memory metastability literature remains unverified.
