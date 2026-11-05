# Parametric three-state separation for hidden periodic signals

**2026-11-05 — exact symbolic derivation; not claimed novel.** This note strengthens `exact-three-state-hidden-phase-separation.md` from a single numerical parameter to every signal bias c in (0,1/2), for K=2 and K=3.

## Model and automaton

Hypotheses h=± have informative signal probabilities p_±=1/2±c at one phase of a hidden deterministic K-cycle; all other phases produce an independent fair bit. The clockless, time-homogeneous three-state observer always probes and updates memory i∈{0,1,2} by i←min(i+1,2) after Y=1 and i←max(i−1,0) after Y=0. It makes its decision from the current memory only. The performance criterion is the total variation distance between the **phase-averaged stationary memory laws** under the two hypotheses, with equal priors.

For row vectors, define
[
T(p)=\begin{pmatrix}
1-p&p&0\\
1-p&0&p\\
0&1-p&p
\end{pmatrix},quad A_\pm=T(1/2\pm c),quad B=T(1/2).
]
The stationary row vector v_± at the beginning of an informative phase satisfies v_±=v_±A_±B^{K-1}, v_±1=1. The phase-averaged distribution is
[
\bar v_\pm=\frac1K\sum_{j=0}^{K-1}v_\pm A_\pm B^j.
]
These are finite rational systems and are solved exactly, not estimated by simulation.

## Theorem A: strict separation for K=2, every c

For every 0<c<1/2, exact symbolic solution gives
[
\bar v_+ -\bar v_- =
\left(-\frac{12c}{9-4c^2},\;0,\;\frac{12c}{9-4c^2}\right).
]
Thus
[
\mathrm{TV}_3(c;K=2)=\frac{12c}{9-4c^2}.
]
The proven two-state optimum from `proof-note-two-state-hidden-phase.md` is 2c/K=c. Consequently
[
\mathrm{TV}_3(c;2)-\mathrm{TV}_{2,\mathrm{opt}}(c;2)
=\frac{c(3+4c^2)}{9-4c^2}>0.
]
The constructed three-state automaton therefore strictly outperforms *every* admissible irreducible two-state time-homogeneous observer, throughout the full signal-bias range. This is an **achievability separation**, not an m=3 optimality theorem.

## Theorem B: strict separation for K=3, every c

Exact symbolic solution gives
[
\bar v_+ -\bar v_- =
\left(-\frac{56c}{63+4c^2},\;0,\;\frac{56c}{63+4c^2}\right),
]
hence
[
\mathrm{TV}_3(c;K=3)=\frac{56c}{63+4c^2}.
]
Against the two-state optimum 2c/3, the gap is
[
\frac{56c}{63+4c^2}-\frac{2c}{3}
=\frac{2c(21-4c^2)}{3(63+4c^2)}>0
]
for every 0<c<1/2.

## Proof method and exact reproducibility

For each K, form P_±=A_±B^{K-1}. Solve the three linear equations from v_±P_±=v_± and normalization v_±1=1, then substitute into the phase average. Rational-function simplification yields the displayed identities. Positivity follows directly from 0<c<1/2. The proof is an exact symbolic matrix calculation; a separate, expanded hand algebra proof could improve independent auditability.

Reproducibility with SymPy:
```python
import sympy as s
c=s.symbols('c', positive=True)
def T(p):
    return s.Matrix([[1-p,p,0],[1-p,0,p],[0,1-p,p]])
for K in (2,3):
    laws=[]
    for p in (s.Rational(1,2)+c,s.Rational(1,2)-c):
        A,B=T(p),T(s.Rational(1,2))
        P=A*B**(K-1)
        z=s.symbols('z0:3')
        v=s.Matrix(1,3,z)
        sol=s.solve(list(v*P-v)+[sum(z)-1],z)
        v=s.Matrix(1,3,[sol[x] for x in z])
        laws.append(sum((v*A*B**j for j in range(K)),s.zeros(1,3))/K)
    print(K,[s.factor(laws[0][i]-laws[1][i]) for i in range(3)])
```

## Interpretation and scope

The observer does not know the phase or time. Its third memory state permits an evidence accumulator unavailable to the optimal two-state automaton. The result is strict for both K=2 and K=3 across all nonzero biases; at c=0 the hypotheses coincide. The result says nothing about simulation detection or physical host substrate identification.

**Novelty not established.** Compare with original Hellman–Cover finite-memory hypothesis-testing results and subsequent periodic/nonstationary finite-state detector literature. Do not describe these identities as new to mathematics without that gate.

## Next research questions

1. Determine whether the same reflecting-walk observer strictly exceeds 2c/K for all K≥2 and 0<c<1/2, or find a counterexample.
2. Derive a certified upper bound or exact optimum for all 3-state stochastic automata at K=2.
3. Investigate memory-size m and period K scaling without confusing phase-averaged stationary risk with terminal-time or phase-aware risk.
4. Audit the 2-state theorem and the literature independently.

**Verdict: CONTINUE.** A nontrivial parametric constructive separation is now established in the chosen model, but its originality and publication value are open.
