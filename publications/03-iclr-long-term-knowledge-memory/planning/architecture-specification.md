---
id: pub-03-architecture-specification
title: "Hierarchical LTKM architecture specification"
type: research-notes
status: draft-spec
created: 2026-08-02
updated: 2026-08-02
---

# Hierarchical Long-Term Knowledge Memory — architecture specification

Conceptual five-component system for WorldConsistMem experiments. Cognitive labels are **operational**, not metaphors.

## Components

| Component | Stored object types | Write conditions | Update behavior | Retrieval role | Persistence | Metadata | Consistency link |
|---|---|---|---|---|---|---|---|
| **Working Memory** | Active turn buffer; scratch bindings | Every new observation | Overwrite/FIFO within window | Immediate context for reader | Ephemeral (session-scoped) | turn_id, tokens | Reduces local omission; not primary for historical Consistency |
| **Session Memory** | Session summaries / episode digests | End of session or token threshold | Merge within session; promote out | Recent-episode retrieval | Medium (across turns, cleared or archived at session end) | session_id, time_span | Near-term transition cues |
| **Long-Term Memory** | Durable facts/assertions with validity intervals | Promotion from session; high-confidence writes | Upsert by entity+attribute; supersession on update events | Semantic/keyword retrieval of current+valid facts | Long-lived | entity_id, attr, valid_from, valid_to, confidence | Current/historical/validity constraints |
| **Knowledge Graph** | Entities, typed relations, time-stamped edges | On structured extraction / explicit relations | Edge add/end; no silent overwrite of history | Multi-hop / relational traversal | Long-lived | edge_id, rel_type, t_start, t_end | Relational + transitive consistency |
| **Archive** | Immutable event/document versions; superseded snapshots | On supersession, conflict, or promotion policy | Append-only; never rewrite past versions | Historical, transition, provenance lookup | Permanent (within retention policy) | event_id, version, source, timestamp | Historical, transition, provenance |

## Interfaces (minimal)

```text
ingest(observation) -> write_plan
promote(session_items) -> LTM/KG/Archive writes
query(q, t_query?) -> evidence_pack
explain(assertion) -> provenance_links
```

Evidence packs may draw from multiple stores; reader is frozen or matched across systems for fair comparison.

## Knowledge lifecycle (concrete)

1. **Insertion** — observe → Working; extract candidates.  
2. **Promotion** — session → LTM/KG when durable.  
3. **Update** — new value with `valid_from`; close prior interval.  
4. **Conflict detection** — overlapping exclusive intervals / contradictory edges.  
5. **Supersession** — mark prior assertion superseded; keep Archive copy.  
6. **Archival** — event/doc versions + closed intervals to Archive.  
7. **Forgetting** — optional capacity policy (score/time); must be logged for ablations.  
8. **Retrieval** — typed routers: current vs historical vs graph path vs archive provenance.  
9. **Provenance tracking** — every LTM/KG write links to supporting event_id(s).

## Predicted H4 mapping

| Ablation / component | Expected consistency dimension |
|---|---|
| Archive | Historical + transition |
| Graph | Relational + multi-hop |
| Temporal validity metadata | Conflict-validity / temporal |
| Provenance links | Provenance consistency |
| Conflict handling | Contradiction consistency |
| Hierarchy / promotion | Bundle-level ConsAcc under evolution |
