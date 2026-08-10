---
id: pub-03-benchmark-specification
title: "WorldConsistMem benchmark specification"
type: research-notes
status: draft-spec
created: 2026-08-02
updated: 2026-08-02
---

# WorldConsistMem — benchmark specification

**Primary name:** WorldConsistMem  
**Working alias:** EvolvingWorldMem  
**Rationale:** Name foregrounds the residual (cross-query **consistency** over an evolving world), not merely that the world changes.

## 1. Formal world

- Latent evolving world: \(W_0,\ldots,W_T\) where each \(W_t\) is a structured state over entities and relations.  
- Event log: \(E_{1:T}\) with deterministic transitions \(W_t = \mathrm{Apply}(W_{t-1}, E_t)\).  
- Memory system state after ingesting observations of \(E_{1:T}\): \(M_T\).  
- Query set / bundle: \(Q=\{q_1,\ldots,q_n\}\).  
- Gold answers: \(Y^*=\{y_1^*,\ldots,y_n^*\}\) derived only from \((W_{0:T}, E_{1:T})\).  
- Predictions: \(\hat Y=\{\hat y_1,\ldots,\hat y_n\}\) from a reader conditioned on \(M_T\) (and optional retrieved evidence).  
- Constraint family: \(\mathcal{C}(W_{0:T}, E_{1:T})\) — machine-checkable predicates over answer sets.

### Entity types (minimum)

persons, organizations, projects, documents, locations, roles, ownership, employment/membership, dependencies, events, explicit state transitions (start/end/transfer/update).

### Generator requirements

- Fully deterministic given seed.  
- Preserves **full gold history** (all \(W_t\) and \(E_t\) retained for scoring; systems never see gold \(W\) directly—only an observation stream).  
- Emits **query bundles**, not only isolated questions.  
- Every constraint in \(\mathcal{C}\) must be auto-derivable from the generated world.

## 2. Per-query accuracy vs cross-query consistency

### Per-query accuracy

For each \(q_i\), \(\mathrm{Acc}_i = \mathbf{1}[\hat y_i \equiv y_i^*]\) under structured equality (IDs, times, relation slots).

Mean accuracy: \(\mathrm{Acc}(Q)=\frac{1}{|Q|}\sum_i \mathrm{Acc}_i\).

### Cross-query consistency

Let \(\Phi(\hat Y; \mathcal{C}_Q)\) be 1 iff \(\hat Y\) satisfies all applicable constraints \(\mathcal{C}_Q\subseteq\mathcal{C}\) for bundle \(Q\).

A system may achieve high \(\mathrm{Acc}\) while \(\Phi=0\).

### Concrete examples

**Example A — temporal inconsistency with high accuracy.**  
\(q_1\): “Who is CEO of Acme at \(T\)?” → correct: Dana.  
\(q_2\): “Who was CEO of Acme at \(t<T\)?” → correct: Blake.  
\(q_3\): “When did leadership change?” → wrong date, but still names Blake→Dana.  
If \(q_1,q_2\) alone are scored, Acc can be high; adding transition/provenance constraints fails if the asserted change time contradicts the event log.

**Example B — mutually inconsistent correct-looking answers.**  
\(q_1\): “Who owns Project Orion at \(T\)?” → Acme (correct).  
\(q_2\): “Which organization employs Rivera at \(T\)?” → Globex (correct if true).  
\(q_3\): “Does Rivera lead Orion at \(T\)?” → Yes (incorrect given employment).  
Individually, \(q_1\) and \(q_2\) may pass; the bundle violates relational/transitive consistency.

**Example C — conflict-validity vs current-state clash.**  
\(q_1\) (current): role = Manager.  
\(q_2\) (conflict-validity at earlier interval): role = Intern, correctly.  
\(q_3\) (provenance): cites a document version that only supports Manager.  
Acc on \(q_1,q_2\) can be high while provenance consistency fails.

**Example D — multi-hop disagrees with components.**  
Component facts retrieved correctly in isolation; multi-hop answer asserts a path that contradicts those facts → transitive consistency failure.

## 3. Query families (minimum)

| # | Family | Probe |
|---|---|---|
| 1 | Current-state | What is true at \(T\)? |
| 2 | Historical-state | What was true at \(t<T\)? |
| 3 | Transition | What changed, when, from→to? |
| 4 | Conflict-validity | Which assertion is valid for specified time/context? |
| 5 | Multi-hop relational | Linked facts across entities |
| 6 | Provenance | Which event/source supports a fact? |
| 7 | Counterfactual consistency check | Which candidate answer would contradict known history? |
| 8 | Cross-query bundles | Groups of interdependent questions sharing \(\mathcal{C}_Q\) |

## 4. Bundle design

Each bundle \(B\) is tied to one **focal subgraph** (e.g., one org + related people/projects over a time window) and includes:

- ≥1 current-state query  
- ≥1 historical-state query  
- ≥1 transition **or** conflict-validity query  
- ≥1 multi-hop **or** provenance query  
- Optional counterfactual check item  

Gold answers and \(\mathcal{C}_B\) are emitted together. Scoring uses both Acc and \(\Phi\).

## 5. Consistency constraint families

All auto-derived from \((W_{0:T},E_{1:T})\):

1. **Uniqueness** — mutually exclusive roles/values cannot co-hold on overlapping validity intervals unless the world explicitly allows.  
2. **Temporal ordering** — successor intervals respect predecessor ends / recorded overlaps.  
3. **State-transition consistency** — current/historical answers must match the event sequence.  
4. **Relational consistency** — ownership, employment, membership, document links align.  
5. **Provenance consistency** — claimed facts supported by the cited event/version.  
6. **Transitive consistency** — multi-hop answers agree with component edge facts.  
7. **Contradiction consistency** — exclusive values not both asserted for the same interval.

## 6. Empirical hypotheses (falsifiable)

- **H1:** High per-query accuracy does not guarantee high cross-query consistency.  
- **H2:** Flat / retrieval-centric systems show distinct consistency failure modes under world evolution.  
- **H3:** Explicit separation of current state, historical records, relational structure, and provenance improves bundle-level consistency under matched model and retrieval budgets.  
- **H4:** Components map to dimensions — archive→historical/transition; graph→relational/multi-hop; temporal metadata→validity; provenance links→source; conflict handling→contradiction.

## 7. Observation stream (system input)

Systems receive a chronological stream of **observations** (dialogue turns, documents, or structured event notices)—not the latent \(W_t\). Gold \(W\) and \(E\) remain evaluator-only.
