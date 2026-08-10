---
id: pub-03-pbind-go-nogo
title: "P-Bind go / no-go criteria"
type: research-notes
status: provisional
created: 2026-08-01
updated: 2026-08-01
---

# P-Bind go / no-go

**Applies to:** kill pilot in [`p-bind-kill-pilot-protocol.md`](p-bind-kill-pilot-protocol.md)  
**Novelty precondition:** [`p-bind-novelty-audit.md`](p-bind-novelty-audit.md) = PARTIALLY OPEN (not OCCUPIED)

---

## Quantitative thresholds (pre-registered)

| Symbol | Meaning | Value |
|---|---|---|
| \(\Delta_{\mathrm{bind}}\) | Binding-error rate at ρ=3 minus ρ=0 (or ρ=1 if ρ=0 is oracle-only) on C0 | **≥ 0.10** absolute |
| Mono | Binding-error vs ρ on C0 | Monotonic or near-monotonic (at most one adjacent inversion ≤0.03) |
| SwapShare | Among errors that appear at ρ=3 but not explained by ρ=0 error baseline: fraction labeled entity_swap or attribute_swap | **≥ 0.50** |
| PersistPos | Primary middle-rank effect also holds within 0.05 of \(\Delta_{\mathrm{bind}}\) on length-matched controls | Required |
| PersistLen | Effect remains after length matching (by construction) | Required |
| TwoModels | Both model families show \(\Delta_{\mathrm{bind}}\ge 0.10\) with same sign | Required |
| PromptKill | C3 (binding scratchpad) at ρ=3 vs C0 at ρ=3: binding-error reduction | If C3 brings binding-error to within **0.05** of C0@ρ=0 **and** accuracy within 0.05 of C4, → **NO-GO** (prompt sensitivity) |
| Seeds | Generation seeds | 42 and 43; qualitative replication of dose–response sign |
| CIs | Report Wilson or bootstrap 95% CIs on rates | Required in tables |

Use \(N\ge 100\) per model on C0 for primary rates.

---

## Continue (GO) — all required

1. Binding-error rate increases monotonically / near-monotonically with \(\rho\) on C0.  
2. \(\Delta_{\mathrm{bind}} \ge 0.10\).  
3. Effect under fixed context length and fixed gold rank (primary).  
4. Reproduces on ≥2 model families (\(\Delta_{\mathrm{bind}}\ge 0.10\) each).  
5. SwapShare \(\ge 0.50\).  
6. Explicit binding-table prompting (C3) does **not** fully eliminate the effect (fails PromptKill NO-GO).  
7. Novelty residual still holds (no newly found paper meeting OCCUPIED criterion before write-up).

---

## Stop / reframe (NO-GO) — any triggers

1. Accuracy falls with \(\rho\) but **swap** rates do not rise (\(\Delta_{\mathrm{bind}} < 0.10\)).  
2. Effect disappears after length or position matching / position-only explanation.  
3. Only the smallest / one family shows the effect.  
4. Structured prompting (C3 or C1) closes gap to within 5 points of low-ρ / oracle (PromptKill).  
5. Errors are ordinary omissions / malformed / unsupported despite gold-present (SwapShare < 0.50).  
6. A near-duplicate paper is found that already reports the same controlled dose–response (reclassify OCCUPIED).

---

## Fastest empirical kill

**Single experiment:** C0, fixed middle gold rank, matched length, ρ∈{0,3} only, one strong model, N=100.

- **Continue signal:** binding-error(ρ=3) − binding-error(ρ=0) ≥ 0.10 and SwapShare ≥ 0.50.  
- **End direction:** \(\Delta_{\mathrm{bind}} < 0.05\) or SwapShare < 0.30 or C3 eliminates gap.

Then expand to full ρ ladder + second model only if continue signal holds.

---

## Exact result that justifies continuation

On C0, across two model families, with matched length and fixed gold rank:

\[
\text{binding-error}(\rho{=}3) - \text{binding-error}(\rho{=}0) \ge 0.10,
\]

near-monotonic in \(\rho\), SwapShare ≥ 0.50, and C3 does not wipe the effect (<5pp of low-ρ).

## Exact result that ends the direction

Any of: no swap dose–response; position/length confound explains all; single-model-only; prompt closure; or OCCUPIED reclassification.

---

## ICLR-fit verdict (honest)

| Strongest plausible outcome | ICLR adequacy |
|---|---|
| Mechanistic capability finding: gold-present misbinding scales with ρ | **Conditional yes** — if effect is large, multi-model, not prompt-trivial, clearly distinguished from LitM |
| Evaluation-methodology only | Weak as sole ICLR story |
| RAG benchmark bake-off | Insufficient |
| Prompt sensitivity only | **No** |

**Overall:** P-Bind is **not** automatically ICLR-worthy. It becomes plausible **only if** the kill pilot delivers the surprising residual: *correct fact present → systematic binding swaps ↑ with ρ*. Otherwise stop.
