---
id: pub-02-jurix2026-review-risks
title: "Review risks — Publication 02"
type: publication
status: draft
created: 2026-07-29
updated: 2026-07-29
tags: [jurix, review-risks, publication-02]
source: planning/jurix-specification.md
---

## Review risks

Scientific and venue risks for Publication 02 (planning stage).

### Risk register

| ID | Risk | Severity | Why it arises | Mitigation (writing stage) |
|---|---|---|---|---|
| R1 | “This is Cobbe reviewability under new names” | High | Strong conceptual overlap | Explicit differentiation table; cite Cobbe generously; claim engineering artifact/property, not invention of review |
| R2 | “PROV/logs/audit already suffice” | High | Spec thesis attacks reliance on logs/provenance alone | §2 failure modes where logs exist but decision knowledge does not |
| R3 | Conceptual-only / no evaluation | High | Spec is conceptual; future work lists formalisation/cases | State contribution class early; narrow claim (§7 author note) |
| R4 | Terminology inflation | Medium | Decision Knowledge / Knowledge Continuity not standard | Terminology section or early definitions; discuss alternatives |
| R5 | Unbounded component list | Medium | Spec “possible components” is open | Label as working inventory; define minimum for legal functions |
| R6 | AI Act overweight or underweight | Medium | Open question in spec | Keep Act as stress-test; legal author calibrates depth |
| R7 | Hidden product / AIGov pitch | Medium | Author responsibility mentions AIGov | Principles only; anonymise identifying project refs for submission |
| R8 | O’Reilly argument not scholarly | Medium | §2 author note | Re-argue with citable mechanisms; do not cite unpublished essay as proof |
| R9 | Format mismatch with live JURIX CFP | Medium | Spec LNCS/double-blind/16pp vs public IOS/single-blind/10pp | Resolve before writing to length (`manuscript/notes.md`) |
| R10 | Privacy / data minimisation conflict | Medium | §7 topics | Treat as first-class limitation, not afterthought |
| R11 | Insufficient AI & Law citations | Medium | CFP requirement | Use `literature-map.md`; Harašta leads consistency |
| R12 | Overclaiming legal compliance | High if occurs | Implications section temptation | “Necessary conditions for…” not “ensures compliance” |

### Venue fit

- **Positive:** Primary topics match JURIX; conceptual AI & Law papers are acceptable if literature-rich and precise.
- **Negative:** Systems reviewers may demand implementation; doctrinal reviewers may demand a case.

### Falsification exposure

Weakest thesis clause: “require explicit engineering mechanisms.” Strengthen by defining what would count as a counterexample (an existing stack that already preserves Decision Knowledge as defined).
