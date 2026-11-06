# All-bias deterministic three-state optimum at hidden period two

**2026-11-06. Status:** Computer-assisted exact symbolic theorem, independently enumerated. Not externally reviewed; originality unverified.

## Theorem

For m=3, K=2 and every 0<c<1/2, consider clockless, always-probing **deterministic** update maps f_0,f_1:{0,1,2}→{0,1,2}. Require the two-step transition P_h=A_h B to be irreducible, with T_y(i,j)=1{f_y(i)=j}, B=(T_0+T_1)/2, A_h=(1/2−hc)T_0+(1/2+hc)T_1. Write v_h for the unique stationary row of A_hB, μ_h=v_h(I+A_h)/2. Then

\[
\boxed{\max_{\mathrm{irreducible\ deterministic}\ f_0,f_1}\mathrm{TV}(\mu_+,\mu_-)=\frac{12c}{9-4c^2}.}
\]

Exactly six labeled rules attain the maximum, the reflecting-walk rule under relabelings:

\`\`\`
(0,0,1; 1,2,2)
(0,2,0; 2,1,1)
(1,1,0; 2,0,2)
(1,2,2; 0,0,1)
(2,0,2; 1,1,0)
(2,1,1; 0,2,0)
\`\`\`

## Exhaustive symbolic certificate

Enumerate 3^6=729 deterministic pairs. Exactly 290 have strongly connected support graph for (T_0+T_1)^2; since 0<c<1/2 all transition support probabilities are positive, this is precisely the irreducibility condition for P_±. For each of these 290:

1. Build T_0,T_1,B,A_± as exact matrices over Q(c).
2. Solve the two stationary equations by replacing one row of (A_hB)^T−I with the normalization row.
3. Compute each coordinate difference δ_i(c)=μ_+(i)−μ_−(i) and certify that its numerator and denominator have no **interior** zeros on (0,1/2), using exact polynomial real-root counting. This justifies determining each sign at c=1/5, including cases with endpoint zeros.
4. Resolve absolute values, giving a rational TV function for each rule. Simplification produces exactly **19 distinct rational functions** among 290 rules.
5. For each function F(c), factor W(c)−F(c), W(c)=12c/(9−4c²). Exact root counting finds no interior sign-changing zeros and evaluation at c=1/5 gives W−F≥0; six rules have W−F identically zero.

This proves the claimed inequality throughout the interval, not just on a numerical grid. A separate check found 24 coordinate-difference expressions with a factor (2c−1), vanishing at the **excluded endpoint** c=1/2; none changes sign in the open interval.

At c=1/5 the runner-up score is 28c/(25−4c²), attained by twelve rules, and

\[
W(c)-\frac{28c}{25-4c^2}
=\frac{16c(4c^2+3)}{(9-4c^2)(25-4c^2)}>0.
\]

This expression is a useful exact cross-check, but the ordering of nonwinning rules need not be constant in c.

## Reproducible computation

Python/SymPy: iterate \`itertools.product(range(3),repeat=6)\`, construct deterministic 3×3 T_y, test reachability of \`(T0+T1)**2\`; use \`sympy.Matrix\`, \`sympy.Rational\`, \`sympy.factor\`, and exact stationary linear solves. For polynomial roots use \`sympy.Poly(...).count_roots(0,Rational(1,2))\` with explicit subtraction/checks of roots at interval endpoints, or isolate intervals with \`sympy.polys.polytools.intervals\`. Test sign at c=1/5 only **after** proving no interior zeros. The independent execution found 290 irreducible rules, 19 symbolic scores, and six global maximizers.

## Interpretation and boundaries

The reflecting walk is optimal for **irreducible deterministic three-state clockless observers** at K=2 for every 0<c<1/2. The stochastic sticky-decision counterexample remains strictly better at c=1/5, so this is not stochastic optimality. Reducible deterministic observers, initialization conventions, time-dependent/clocked rules, probe decisions, and global stochastic upper bounds remain outside the theorem. Prior-art novelty remains unverified.
