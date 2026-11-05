# Noncommuting memory and hidden-period limits

**2026-11-05. Status: constructive theorem with an exponential Lyapunov proof. Novelty not established.** This resolves the *iterated* limits, but not the joint critical scaling K/m²→α.

## Model

Use the binary hidden-period model and reflecting-walk m-state clockless observer defined in `arbitrary-memory-rare-phase-asymptotics.md`. For h=+, the informative Bernoulli parameter is p=1/2+c; for h=− it is 1/2−c, with 0<c<1/2. The other K−1 steps per period have fair independent Bernoulli signals. Each signal 1 increments memory i∈{0,…,m−1} with reflection at m−1, and each 0 decrements with reflection at 0. Evaluate total variation of the two *phase-averaged periodic stationary* memory laws μ_±.

## Theorem: fixed-period consistency as memory grows

For every **fixed** integer K≥2 and fixed 0<c<1/2,

[
\boxed{\lim_{m\to\infty}\operatorname{TV}_m(K,c)=1.}
]

In fact, there exist constants C=C(K,c)<∞ and a=a(K,c)>0, independent of m, such that for all sufficiently large m,

[
\boxed{1-\operatorname{TV}_m(K,c)\le C e^{-a m}.}
]

Thus the equal-prior Bayes error of the displayed m-state observer decays exponentially with m at fixed K,c. This is an **achievability result**, not an optimality theorem over arbitrary m-state automata.

### Proof: exponential moment bound

Under h=+, write d=m−1−i for distance from the **upper** memory boundary. A signal 1 reduces d by one unless d=0; a signal 0 increases d by one unless d=m−1. Let v_+ be the stationary law at the beginning of the informative phase. Fix a sufficiently small t>0 and consider the exponential Lyapunov function V(d)=e^{td}.

Over a full period, when the starting distance d≥K, the upper reflecting boundary d=0 cannot be encountered in the next K updates. The lower reflecting boundary d=m−1 can only **decrease** the resulting distance relative to the unrestricted walk. Therefore, pathwise,

[
d_{\mathrm{after}}\le d_{\mathrm{before}}+\sum_{j=1}^K(1-2Y_j).
]

The K signals are independent conditional on h and phase; one has Bernoulli(1/2+c), the other K−1 are fair. Consequently

[
\mathbb E[V(d_{\mathrm{after}})\mid d_{\mathrm{before}}=d]
\le q(t)V(d),\quad d\ge K,
]
where
[
q(t)=\left[(\tfrac12+c)e^{-t}+(\tfrac12-c)e^t\right](\cosh t)^{K-1}.
]

Because q(0)=1 and q'(0)=−2c<0, there exists t=t(K,c)>0 such that q(t)<1.

When d<K, each update changes d by at most one, so d_after≤d+K<2K, and hence V(d_after)≤e^{2tK}. Taking expectation in the stationary phase-start law yields

[
\mathbb E_{v_+}V(d)
\le q(t)\mathbb E_{v_+}[V(d)\mathbf1_{d\ge K}]
+e^{2tK}\Pr_{v_+}(d<K)
\le q(t)\mathbb E_{v_+}V(d)+e^{2tK}.
]

Thus

[
\boxed{\mathbb E_{v_+}e^{td}\le \frac{e^{2tK}}{1-q(t)},}
]

uniformly over m.

At any of the K phases, d can increase by at most K relative to the beginning of the period, so the **phase-averaged** law μ_+ satisfies

[
\mathbb E_{\mu_+}e^{td}\le C_0:=\frac{e^{3tK}}{1-q(t)}.
]

By Markov's inequality, under h=+,

[
\mu_+\{i\le(m-1)/2\}
=\mu_+\{d\ge(m-1)/2\}
\le C_0e^{-t(m-1)/2}.
]

By reflecting memory states i↔m−1−i and exchanging signals 0↔1, the h=− law satisfies the symmetric bound

[
\mu_-\{i\ge(m-1)/2\}\le C_0e^{-t(m-1)/2}.
]

Choose a midpoint threshold set A={i>(m−1)/2}. Then μ_+(A)≥1−C_0e^{-t(m−1)/2}, while μ_−(A)≤C_0e^{-t(m−1)/2}. Total variation is the supremum over sets of the probability difference, so

[
\operatorname{TV}_m(K,c)\ge1-2C_0e^{-t(m-1)/2}.
]

Since TV≤1, the theorem follows, with a=t/2 and C=2C_0e^{t/2}. ∎

## Corollary: the iterated limits do not commute

The previously proved fixed-m rare-phase theorem gives TV_m(K,c)~cL_m/K→0 as K→∞. The theorem above gives TV_m(K,c)→1 as m→∞ at fixed K. Hence

[
\boxed{
\lim_{K\to\infty}\lim_{m\to\infty}\operatorname{TV}_m(K,c)=1,
\qquad
\lim_{m\to\infty}\lim_{K\to\infty}\operatorname{TV}_m(K,c)=0.
}
]

The order of limits is essential. No claim is made for simultaneous growth along arbitrary K=K(m). The Lyapunov constants depend on K and c and may deteriorate severely as K increases.

## Interpretation and limitations

A positive mean signal drift 2c per fixed-length period causes the reflecting-walk observer to concentrate near opposite memory boundaries under the two hypotheses as memory size grows. The stationary laws become asymptotically disjoint, yielding vanishing Bayes error. This does **not** show that an embedded observer can detect a simulated universe or infer its physical substrate. It is a narrow result about periodic binary observations and a particular finite-state decision mechanism.

This theorem uses standard exponential drift/Foster–Lyapunov ideas. **Originality is not established.** Check finite-state hypothesis testing, Markov-modulated queues, reflected random walks, and periodic Markov chains before claiming a novel theorem.

## Next questions

1. Find the sharp crossover in simultaneous m,K→∞, including K~αm².
2. Derive matching bounds on TV_m for intermediate growth rates and weak signal c→0.
3. Determine whether the reflecting-walk construction is optimal among all m-state observers.
4. Independently audit all exact spectral and two-state optimality results against primary literature.

**Verdict: CONTINUE.** The iterated-limit noncommutation is rigorously established for the construction; critical joint scaling remains open.
