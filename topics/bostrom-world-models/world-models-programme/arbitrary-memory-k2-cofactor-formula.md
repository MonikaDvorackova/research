# Exact finite-memory formula at K=2 via Markov-chain cofactors

**2026-11-05. Status:** general exact finite-dimensional formula for every m≥2, with a proof from the Markov-chain tree/cofactor identity. This is **not** a simplified scalar closed form, a monotonicity theorem, or an original theorem claim. It replaces ad hoc case-by-case stationary solves with a uniform construction.

## Model

Fix integer m≥2 and 0<c<1/2. The reflecting-walk observer has states 0,…,m−1. Define the row-stochastic matrices

B_{i,j}=(1/2)1_{j=max(i−1,0)}+(1/2)1_{j=min(i+1,m−1)},

D_{i,j}=1_{j=min(i+1,m−1)}−1_{j=max(i−1,0)},

A_+=B+cD, A_−=B−cD.

One step per hidden K=2 period uses A_h; the next uses B. Let P_h=A_h B. Let J be the m×m reversal permutation matrix, J_{i,m−1−i}=1. Then A_−=J A_+ J, B=JBJ, P_−=JP_+J.

## Theorem: cofactor formula for arbitrary m

Define for i=0,…,m−1

\[
\tau_i(c)=\det\left((I-P_+)_{\widehat i,\widehat i}\right),\qquad
S(c)=\sum_{i=0}^{m-1}\tau_i(c),
\]

where the subscript means delete row i and column i. Then all τ_i(c)>0 and S(c)>0, and the phase-start stationary distribution under h=+ is exactly

\[
v_+(c)_i=\frac{\tau_i(c)}{S(c)}.
\]

Define the row vector of polynomial numerators

\[
q(c)=\tau(c)(I+A_+),\qquad \tau(c)=(\tau_0(c),\ldots,\tau_{m-1}(c)).
\]

The **exact phase-averaged discrimination** of this particular m-state observer at K=2 is

\[
\boxed{
\operatorname{TV}_m(2,c)=
\frac{1}{4S(c)}
\sum_{i=0}^{m-1}\left|q_i(c)-q_{m-1-i}(c)\right|.
}
\]

This is an exact expression for **every integer m≥2**, requiring only (m−1)×(m−1) determinants and one matrix multiplication. Since P_+ is affine in c, τ_i is a polynomial of degree at most m−1, q_i is a polynomial of degree at most m, and S is a positive polynomial on the admissible interval. Hence TV_m(2,c) is piecewise rational in c. It becomes one rational function on any subinterval on which the signs of q_i−q_{m−1−i} are fixed.

### Proof

P_+ is irreducible and aperiodic for 0<c<1/2: every step has strictly positive probability of moving up or down, and the reflecting boundaries yield self-loops in its two-step product. The finite Markov-chain tree theorem (equivalently the adjugate identity for a simple zero eigenvalue of I−P_+) states that the stationary row has entries proportional to the principal cofactors of I−P_+. They are positive and yield the formula for v_+.

The phase-averaged stationary row is μ_+=v_+(I+A_+)/2=q/(2S). Reflection of the transition matrices gives v_−=v_+J and μ_−=μ_+J, by uniqueness of the stationary distribution. Therefore

TV(μ_+,μ_−)=1/2∑_i |μ_{+,i}−μ_{+,m−1−i}|
=1/(4S)∑_i|q_i−q_{m−1−i}|.

The degree bounds follow from determinants of matrices affine in c and the final multiplication by I+A_+. ∎

## What this proves and does not prove

This answers the question of whether there is a **uniform exact algebraic representation** for all m at K=2: yes. It does **not** give a low-complexity closed scalar formula, prove strict monotonicity in m, or prove that the reflecting-walk automaton is optimal among all m-state observers. A genuinely stronger theorem would establish the sign structure of q_i−q_{m−1−i} uniformly in m and c, and then simplify the determinant ratios or derive a recurrence.

## Independent numerical check

For c=0.17, direct stationary solves for m=3,4,5,6,7,8,10,20 yielded signed phase-average differences with a single crossing at the midpoint (negative on lower states, positive on upper states). This is **numerical evidence only** and is not used to remove the absolute values from the theorem. Exact rational checks at c=1/6 give TV_4=1/3, TV_5=51/130, TV_6=10/21, consistent with the earlier explicit formulas.

## Reproduction with exact arithmetic

~~~python
import sympy as s

def matrices(m, c):
    B, D = s.zeros(m), s.zeros(m)
    for i in range(m):
        B[i, max(0, i-1)] += s.Rational(1, 2)
        B[i, min(m-1, i+1)] += s.Rational(1, 2)
        D[i, max(0, i-1)] -= 1
        D[i, min(m-1, i+1)] += 1
    return B, D

def cofactor_phase_difference(m, c):
    B, D = matrices(m, c)
    A, P = B+c*D, (B+c*D)*B
    H = s.eye(m)-P
    tau = s.Matrix(1, m, [
        s.factor(H.minor_submatrix(i, i).det()) for i in range(m)
    ])
    S = sum(tau)
    q = tau*(s.eye(m)+A)
    # Difference μ_plus - reflected μ_plus, exactly
    return [s.factor((q[i]-q[m-1-i])/(2*S)) for i in range(m)]

c=s.Rational(1, 6)
for m, expected in [(4,s.Rational(1,3)),
                    (5,s.Rational(51,130)),
                    (6,s.Rational(10,21))]:
    delta=cofactor_phase_difference(m,c)
    tv=sum(abs(x) for x in delta)/2
    assert tv==expected, (m,tv,expected)
    print(m,tv)
~~~

**Next mathematical target:** Prove a uniform single-crossing sign theorem for the reflected phase-average laws and find a tractable recurrence for the cofactors. Independently check prior-art literature on finite-state binary hypothesis testing and stationary Markov-chain tree formulas. Novelty unverified.
