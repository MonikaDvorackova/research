# Joint memory–period phase diagram: rigorous vanishing and consistency regimes

**2026-11-05. Status:** two proved sufficient regimes, using the exact phase-averaged Poisson identity and an exponential drift argument. Novelty not established. **This supersedes the suggestion that K≈m² is a nontrivial discrimination crossover:** in that regime TV→0 for this construction.

## Model

Use the m-state reflecting-walk observer and hidden K-period Bernoulli observation model from `arbitrary-memory-rare-phase-asymptotics.md`. Fix c∈(0,1/2). Under hypotheses h=± the informative bit has p=1/2±c and other K−1 bits are fair. The observer updates i∈{0,…,m−1} by reflecting ±1 increments, without phase or clock. Let μ_± be the stationary phase-averaged memory laws, TV_m(K,c)=TV(μ_+,μ_-).

## Theorem A: information vanishes whenever m/K→0

For all m≥2, K≥2 and 0<c<1/2,

[
\boxed{\operatorname{TV}_m(K,c)\le\min\{1,\;4cm/K\}.}
]

In particular, for any joint sequence m,K→∞ with m/K→0, TV_m(K,c)→0. This includes K/m²→α∈(0,∞), and all K≫m.

**Proof.** Let B be the fair reflecting transition, D the derivative with respect to the Bernoulli parameter, π uniform, Π=1π, Z=(I−B+Π)^{-1}. From the exact balance identity proved in `arbitrary-memory-rare-phase-asymptotics.md`,

[
\mu_+-\mu_-=(c/K)(v_++v_-)DZ,
]

where v_± are probability rows at the informative phase. We bound the induced ∞→∞ norm of DZ on test functions.

Let f∈R^m with ||f||_∞≤1, let g=Zf, and put \bar f=m^{-1}\sum_j f_j. Then (I−B)g=f−\bar f\mathbf1. At the left boundary,

[
g_1-g_0=-2(f_0-\bar f).
]

At each interior state, discrete integration gives

[
\boxed{g_{j+1}-g_j=-2\sum_{r=0}^j(f_r-\bar f),\quad j=0,\ldots,m-2.}
]

Because |f_r−\bar f|≤2, each nearest-neighbor difference obeys |g_{j+1}−g_j|≤4m. In fact using cancellation of the centered sum yields |g_{j+1}−g_j|≤4 min(j+1,m−j−1)≤2m. Every row of D acts on g as g_{min(i+1,m−1)}−g_{max(i−1,0)}, a sum of at most two neighboring differences, so

[
\boxed{\|DZf\|_\infty\le4m.}
]

By l1/linf duality, each row of DZ has l1 norm ≤4m. Since v_++v_- is a nonnegative row with total mass 2,

[
\|(v_++v_-)DZ\|_1\le8m.
]

Therefore TV_m=(1/2)||μ_+−μ_-||_1≤4cm/K. The bound TV≤1 is automatic. ∎

This is a deliberately conservative constant. Numerical matrix inspection suggests the sharp maximum row l1 norm of DZ is 2(m−1), which would improve 4cm/K to 2c(m−1)/K; the sharper statement is not used or claimed here.

## Theorem B: consistency whenever K log K / m→0

For all m≥2, K≥2 and 0<c<1/2,

[
\boxed{
1-\operatorname{TV}_m(K,c)
\le \frac{2Ke^{6c}}{c^2}
\exp\!\left(-\frac{c(m-1)}{K}\right).
}
]

Thus for fixed c>0 and joint m,K→∞ satisfying K log K /m→0, TV_m(K,c)→1. The inequality may be vacuous for moderate sizes but is asymptotically informative.

**Proof.** Under h=+, define distance d=m−1−i to the upper reflecting boundary and V(d)=e^{td}. Observe the chain only at the beginnings of informative phases, with stationary law v_+. Choose t=2c/K.

For d≥K, no upper reflection can occur in the next K steps, while any lower reflection can only reduce d relative to the unrestricted walk. The moment-generating factor for the K increments in distance is

[
q(t)=[(1/2+c)e^{-t}+(1/2-c)e^t](\cosh t)^{K-1}.
]

Hoeffding's lemma for ±1 random variables gives

[
q(t)\le\exp(-2ct+Kt^2/2)=\exp(-2c^2/K)<1.
]

For d<K, after K steps d'<2K, so e^{td'}≤e^{2tK}. Stationarity and splitting into d≥K and d<K yield

[
\mathbb E_{v_+}e^{td}\le\frac{e^{2tK}}{1-q(t)}.
]

Since 0<2c²/K≤1/4, 1−e^{-2c²/K}≥c²/K. At every intermediate phase, d can increase by at most K, hence the phase-averaged μ_+ satisfies

[
\mathbb E_{\mu_+}e^{td}\le\frac{Ke^{3tK}}{c^2}
=\frac{Ke^{6c}}{c^2}.
]

Markov's inequality implies

[
\mu_+\{i\le(m-1)/2\}
\le (Ke^{6c}/c^2)e^{-t(m-1)/2}.
]

By reflecting the memory states and swapping the signal labels, the h=− law obeys the same bound on the opposite side. Using the midpoint threshold event to lower-bound TV,

[
1-\operatorname{TV}_m\le2(Ke^{6c}/c^2)e^{-t(m-1)/2}
=(2Ke^{6c}/c^2)e^{-c(m-1)/K}.
]

This proves the claimed finite-size inequality. If m/(K log K)→∞, its right-hand side tends to zero for fixed c>0. ∎

## Consequences and interpretation

- If K≈αm² with α>0, then m/K≈1/(αm)→0, so TV_m→0. This **resolves** the previous question about this scaling: it is a vanishing-discrimination regime, not a nontrivial crossover for this observer.
- If K=o(m/log m), TV_m→1.
- The **remaining open window** lies between K on the order of m/log m and K on the order of m. The logarithmic gap may be an artifact of the exponential-moment bound. The natural conjecture is that K/m→α∈(0,∞) yields a nontrivial continuum reflected-drift limit, but that is not proved.
- The results are constructive for the reflecting-walk family, not universal lower or upper bounds for all possible m-state observers. The fixed-m two-state optimum is a separate theorem under its own assumptions.
- This does not bear on physical universe simulation detection. The novelty of these bounds relative to standard drift criteria and Markov Poisson equations remains unverified.

## Next work

1. Tighten the Lyapunov estimate to remove the logarithmic gap, perhaps via stationary occupation bounds or coupling.
2. Derive a continuum limit when K/m→α>0; inspect how the periodic informative impulse affects stationary reflected drift.
3. Find an exact formula for the row l1 norm of DZ and improve the finite-size upper bound.
4. Check all model assumptions and primary prior art before publication.

**Verdict: CONTINUE, but focus on the K~m window, not K~m².**
