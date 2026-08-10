---
id: pub-03-aug-formal-definition
title: "AUG formal definition"
type: research-notes
status: audit
created: 2026-08-01
updated: 2026-08-01
---

# AUG formal definition

## Symbols

| Symbol | Meaning |
|---|---|
| \(T\) | Task identifier |
| \(x\) | Task input (query / prompt / decision request) |
| \(I\) | Available information state presented to the model (context, retrieved set, retained trace view, etc.) |
| \(y^*\) | Gold output under task \(T\) |
| \(f_T\) | Deterministic task semantics / oracle rule for \(T\) |
| \(M\) | Model (stochastic or deterministic map from \((x,I)\) to an output) |
| \(Y_T(x,I)\) | Set of outputs entailed by \(f_T\) given \((x,I)\) |

## Adequacy (model-independent)

**Definition (information adequacy).**  
\(I\) is **adequate** for \((T,x,y^*)\) if and only if

\[
f_T(x,I)=y^*
\]

when \(f_T\) is total and single-valued, or, more generally,

\[
Y_T(x,I)=\{y^*\}
\]

i.e. the task semantics uniquely entail \(y^*\) from \((x,I)\).

Adequacy is a property of \((T,x,I,f_T)\), **not** of \(M\).  
It is **forbidden** to define adequacy as “a stronger model can answer correctly.”

### Special cases of \(f_T\)

| Mode | Adequacy criterion | Operational? |
|---|---|---|
| **Logical** | \(y^*\) is the unique answer entailed by \(I\) under explicit logical rules | Yes, if rules and \(I\) are fully specified |
| **Programmatic** | A fixed deterministic program / lookup (e.g. extract value of attribute \(a\) for entity \(e\) from a triple table) returns \(y^*\) from \(I\) | Yes |
| **Probabilistic** | \(P(y^*\mid x,I)\) under a stated generative process exceeds a pre-registered threshold, or \(y^*\) is MAP-unique | Only with an agreed generative model; otherwise **ambiguous** |
| **Ambiguous** | Multiple answers remain consistent with \(I\) under \(f_T\) | Adequacy **fails** by definition (\(Y_T\) not singleton) |
| **Not operationally definable** | \(f_T\) appeals to unstated world knowledge, underspecified multi-hop norms, or autorater judgment without frozen criteria | Treat as **non-AUG-eligible** until \(f_T\) is fixed |

## AUG event

**Definition (AUG event).** An instance \((T,x,I,y^*,M)\) is an **Adequacy–Utilization Gap event** iff

\[
I \text{ is adequate for }(T,x,y^*)
\quad\land\quad
M(x,I)\neq y^*.
\]

(If \(M\) is stochastic, replace with a pre-registered decoding rule, e.g. temperature-0 output ≠ \(y^*\).)

## What AUG is not

- Retrieval miss (\(g\notin I\)) — adequacy fails.
- Ambiguous \(I\) — adequacy fails.
- Parametric guessing that happens to be wrong when \(I\) is insufficient — not AUG.
- “Model is weak” as a definition of insufficiency — circular; banned.

## Audit note

Open-domain QA “sufficient context” (Joren et al., ICLR 2025) operationalizes a close notion via human/LLM judgment that a *plausible* answer exists from \(C\) (not always uniqueness of \(y^*\)). That is related but **not identical** to unique entailment of a fixed gold \(y^*\). For this audit, AUG uses **unique entailment of \(y^*\)** under explicit \(f_T\).
