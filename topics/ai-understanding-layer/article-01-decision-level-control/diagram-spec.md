---
id: note-article-01-decision-level-control-diagram-spec
title: "Article 1 Diagram Specification — Decision-Level Control"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-21
updated: 2026-08-21
tags: [article-planning, diagram-spec, decision-level-control]
refs: []
---

## Article 1 Diagram Specification (Task F)

Description only — no image generated at this stage. Sits in Section 5 of
`spine.md` ("The gate pattern"). Simple enough for an O'Reilly-Radar-style
practitioner piece: one flow, one contrast, no more than 7 nodes.

### Nodes

1. **Model Candidate / Output** — the trained model plus raw evaluation
   numbers (accuracy, latency, fairness/safety metrics).
2. **Proposed Decision** — "Promote candidate model vN to production."
3. **Evidence** — evaluation report, dataset/version reference, metric
   values, referenced policy version. *(Evidence enters the diagram here.)*
4. **Policy / Requirement** — the declared threshold set the gate checks
   evidence against (e.g., minimum accuracy, required fairness checks,
   required sign-off tier).
5. **Deterministic Gate** — reads Evidence + Policy, evaluates rules.
   *(Enforcement occurs here.)*
6. **Human Approval** — the escalation branch for borderline cases; approval
   or denial is itself a recorded, attributed decision. *(Human approval may
   occur here.)*
7. **Production Action** — the traffic-routing change / deployment that
   actually takes effect.

### Arrows and labels

```
Model Candidate / Output
        │
        ▼
Proposed Decision  ──requires──▶  Evidence
        │                            │
        │                            ▼
        │                     Policy / Requirement
        │                            │
        └───────────┬────────────────┘
                     ▼
             Deterministic Gate
                     │
        ┌────────────┼────────────────┐
        ▼            ▼                ▼
      allow        block          escalate
        │            │                │
        │      (no production   Human Approval
        │        action; logged)      │
        │                    ┌────────┴────────┐
        │                    ▼                 ▼
        │                approved           denied
        │                    │                 │
        └────────────────────┘                 ▼
                     │                   (no production
                     ▼                     action; logged)
              Production Action
```

- Label the **allow** arrow: "evidence satisfied policy."
- Label the **block** arrow: "evidence failed policy — nothing proceeds."
- Label the **escalate** arrow: "borderline — requires named approver."
- Label the **Evidence** node explicitly: **"Evidence enters here."**
- Label the **Deterministic Gate** node explicitly: **"Enforcement occurs
  here."**
- Label the **Human Approval** node explicitly: **"Human approval may occur
  here — as a formal branch, not an informal exception."**

### Contrast callout (what changes vs. a conventional ML pipeline)

Include a second, minimal path above or beside the main diagram, greyed out
or dashed, showing the conventional pipeline this replaces:

```
Model Candidate / Output ─ ─ ─ ─ ─ ─ ─▶ Production Action
        (no evidence checkpoint, no gate, no recorded decision)
```

Caption under the contrast callout: *"Conventional pipeline: output flows
directly into production action. No structural point exists at which
evidence is required, checked, or enforced."*

### Explicit exclusions (keep the diagram inside Article 1's boundary)

- Do not include any node representing historical/versioned context (prompt
  versions over time, retrieval corpus snapshots, policy version history) —
  that belongs to Article 2's diagrams, not this one.
- Do not label anything "understanding layer" or reference explainability/
  observability/interpretability as parallel boxes — that belongs to
  Article 3.
- Keep AIGov Core out of the diagram itself; it may be referenced only in
  surrounding prose per `evidence.md` and `spine.md`.
