---
id: pub-02-jurix2026-figure-design
title: "Figure design — Publication 02"
type: publication
status: draft
created: 2026-07-29
updated: 2026-07-29
tags: [jurix, figures, publication-02]
source: planning/jurix-specification.md
---

## Figure design

Planned figures from the specification. **No graphics generated**—design notes only.

---

### Figure 1 — System State vs Decision Knowledge

#### Purpose

Make the §2 contrast visually immediate for JURIX readers.

#### Information conveyed

- Left: mutable system state (live prompts, current retrieval index, current tools, current model, current policies).
- Right: Decision Knowledge components retained for a past decision.
- Crossed or broken arrows showing that “current state” does not equal “what was known/used then.”

#### Required elements

- Two panels labelled **System state (now)** and **Decision Knowledge (then)**.
- Icons/boxes for: prompt, retrieval, tools, model version, policy constraints, human rationale, legal criteria.
- Time marker (`t_decision` vs `t_review`).

#### Relationship to argument

Supports thesis clause: engineering preserves state; accountability needs decision knowledge.

#### Rough layout

```text
[ t_decision ]                         [ t_review ]
System produces decision               Reviewer asks "why?"
        |                                     |
        v                                     v
+------------------+                 +------------------+
| System state     |  --X does not-> | Needed DK        |
| (overwritable)   |                 | (structured)     |
+------------------+                 +------------------+
```

---

### Figure 2 — Knowledge Continuity across the AI lifecycle

#### Purpose

Show Knowledge Continuity as a property spanning lifecycle stages (§5 contribution 4).

#### Information conveyed

- Lifecycle stages (design → data/prompting → inference/tools → human gate → deployment change → later review).
- What must be captured at each stage.
- Continuity strand linking stages to a preserved Decision Knowledge artifact.

#### Required elements

- Horizontal lifecycle.
- Vertical “preservation” bar or thread labelled Knowledge Continuity.
- Break points matching §2 failure modes (model update, tool change, etc.).

#### Relationship to argument

Operationalises contribution 3–4; previews principles “design preservation before deployment.”

#### Rough layout

```text
Design -> Build -> Decide -> Change -> Review
  |        |         |         |         |
  +--------+- capture DK ------+------> retained DK
            Knowledge Continuity thread
```

---

### Figure 3 — Conceptual model of decision knowledge preservation

#### Purpose

Summarise §5 principles and concepts without implying a product architecture.

#### Information conveyed

- Principles as outer requirements.
- Concepts (decision object, evidence object, dependencies, review context, governance primitive, lifecycle, audit chain / knowledge graph) as inner vocabulary.
- Arrow to legal functions (explain, justify, review, contest).

#### Required elements

- Clear “conceptual — not implementation” caption.
- Spec concept set (may group for readability).
- No vendor logos / project names.

#### Relationship to argument

Visual carrier of contribution 4.

#### Rough layout

```text
        [ Legal functions ]
                 ^
                 |
     [ Preservation principles ]
                 ^
                 |
     [ Conceptual objects & links ]
```

---

### Figure 4 — Relationship between decision, evidence, rationale, policy constraints and review context

#### Purpose

Show internal structure of Decision Knowledge (§4 components) as relations, not a flat checklist.

#### Information conveyed

- Decision node at centre.
- Linked nodes: evidence, rationale, policy constraints, review context (plus optional model/tool/prompt as satellites).
- Edges labelled (supports / constrains / authorises / records).

#### Required elements

- Centre: Decision.
- Spec-named relations among evidence, rationale, policy, review context.
- Optional uncertainty annotation.

#### Relationship to argument

Makes “structured set of information” literal; supports evidentiary reconstruction discussion in §6.

#### Rough layout

```text
     Evidence         Policy constraints
         \               /
          \             /
           > Decision <
          /             \
         /               \
   Human rationale    Review context
```

---

### Production notes

- Prefer simple line diagrams (IOS/LNCS-friendly).
- Captions must restate non-claims (“conceptual model”).
- Draw only after §4–§5 terminology is locked.
