# Asymptotic memory advantage for rare informative phases

**2026-11-05. Status: proved corollary of the exact all-period three-state formula; novelty not established.**

## Setting

Use the exact model and reflecting-walk three-state automaton from `all-period-three-state-separation-theorem.md`. Let 0<c<1/2 be fixed, K≥2 an integer, x=2^{-(K-1)}, y=(-1/2)^{K-1}. The earlier result is

TV_3(K,c) = [8c(2−x)(2+y)]/[3K(4+(4c²−1)xy−2x+2y)].

The proven optimal two-state separation in the same model is TV_{2,opt}(K,c)=2c/K.

## Theorem: nonvanishing relative memory advantage

For every fixed 0<c<1/2,

lim_{K→∞} K·TV_3(K,c) = 8c/3,

lim_{K→∞} TV_3(K,c)/TV_{2,opt}(K,c) = 4/3,

and

TV_3(K,c) = 8c/(3K) + O(c·2^{-K}/K).

The O bound can be made uniform in c∈(0,1/2).

**Proof.** As K→∞, x→0, y→0 exponentially. In the exact rational expression, the numerator factor (2−x)(2+y)→4 and denominator factor 4+(4c²−1)xy−2x+2y→4. Hence K·TV_3→(8c/3)·(4/4)=8c/3, and division by 2c/K yields 4/3. For uniformity, set a=4c²−1∈(−1,0). Since |x|=|y|=2^{-(K−1)}, the numerator correction from 4 is 2y−2x−xy=O(2^{-K}) and denominator correction from 4 is axy−2x+2y=O(2^{-K}), uniformly in c. The denominator stays bounded away from zero for K≥2: using x≤1/2, |y|≤1/2, |a|≤1 gives 4+a xy−2x+2y ≥ 4−1/4−1−1=7/4. Standard difference-of-ratios algebra gives the stated uniform O bound. ∎

## Exact relative advantage and parity

Define R_K(c)=TV_3(K,c)/(2c/K). Then

R_K(c)=4(2−x)(2+y)/[3(4+(4c²−1)xy−2x+2y)].

For even K, y=−x, so

R_K(c)=4(4−4x+x²)/[3(4−4x+(1−4c²)x²)].

Thus R_K(c)>4/3 for even K because the denominator has the smaller x² coefficient.

For odd K≥3, y=x, so

R_K(c)=4(4−x²)/[3(4+(4c²−1)x²)].

Thus R_K(c)<4/3 for odd K (because 4+(4c²−1)x²−(4−x²)=4c²x²>0).

The ratios converge to 4/3 **from alternating sides** as the parity of K changes. At c→0, the odd-K ratio tends exactly 4/3, but c=0 itself has zero signal and the ratio of two TVs is undefined.

## Bayes-error consequence

Under equal priors, error_{2,opt}=1/2−c/K, while the exhibited three-state observer achieves error_3=1/2−TV_3/2 = 1/2−4c/(3K)+O(c·2^{-K}/K).

Thus its **absolute** Bayes-error improvement is c/(3K)+O(c·2^{-K}/K), tending to zero. The relative 4/3 improvement applies to TV (discrimination advantage), not to the total error rate.

## Interpretation

A third memory state yields a persistent 33.3% relative improvement in weak discrimination when informative observations are rare. This does not prevent the absolute information available to a clockless bounded-memory observer from vanishing as K increases. This result is specific to the chosen reflecting-walk automaton, and provides a lower bound for optimal three-state performance, **not** an optimal three-state value.

## Next tasks

- Seek a rigorous m=3 upper bound and determine whether the reflecting-walk automaton is optimal.
- Study m-state reflecting walks and the K→∞ rare-informative-phase limit using stationary linear response of the uninformative transition.
- Compare this asymptotic gain with existing finite-state detection and periodically modulated observation literature.
- Independently audit the prior two-state theorem and all-period spectral derivation.

**Novelty status: unverified. Publication readiness: no.**
