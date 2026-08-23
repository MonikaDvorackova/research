---
id: note-article-01-decision-level-control-spine
title: "Article 1 Spine — Decision-Level Control"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-21
updated: 2026-08-21
tags: [article-planning, spine, decision-level-control, running-example]
refs: []
---

## Article 1 Spine (Task D) + Running Example (Task E)

Target: ~1,650–2,000 words across 7 sections. Written so prose drafting is
mechanical — each section states its own claim, evidence, and boundary; no
section needs outside decisions made at drafting time.

---

### Running example (Task E) — used throughout

**The Model Promotion Gate.** A team trains model candidates and wants to
promote a new candidate to serve production traffic. Instead of promotion
happening the moment a candidate "looks good," promotion is treated as a
decision that must be supported and gated:

- **Output:** the trained candidate plus its raw evaluation numbers
  (accuracy, latency, fairness/safety metrics as applicable).
- **Proposed decision:** "Promote candidate model vN to serve production
  traffic."
- **Evidence:** the evaluation report, the dataset/version used to produce
  it, the metric values, and a reference to which policy version they were
  checked against.
- **Gate:** a deterministic rule evaluator reads the evidence and the
  declared policy (e.g., minimum accuracy threshold, required fairness
  checks, required sign-offs for high-risk categories) and returns one of
  three outcomes: **allow**, **block**, or **escalate**.
- **Escalate → human approval:** borderline cases go to a named approver,
  whose approval or denial is itself a recorded, attributed decision — not
  an informal exception to the pipeline.
- **Production action:** only an *allowed* (or human-approved, formerly
  escalated) decision actually flips traffic routing to the new candidate.

This mirrors Source B's own proposed structure (Ch. 3 outputs→decisions,
Ch. 4 evidence, Ch. 6–7 enforcement/CI gates, Ch. 8 approval) using a
scenario any engineer with CI/CD experience already has intuition for.
**AIGov Core mapping:** Source A §7 states AIGov Core was "originally
conceived as an AI governance and auditability runtime" that "treats
governance decisions themselves as engineering artifacts" — this is the kind
of problem the example is built around. The source material gives no
concrete API, schema, or enforcement mechanics for AIGov Core, so the
example must be written as a generic pattern, with at most one sentence
noting it is the kind of problem AIGov Core originated from (per `evidence.md`,
claim 11/12) — not a description of AIGov Core's actual internals.

---

### Section 1 — The gap (≈150–200 words)

- **Purpose:** hook the reader with a concrete, familiar failure shape.
- **Central claim:** in most production AI systems, a model's output flows
  directly into a consequential action with no structural checkpoint in
  between — this is an architecture gap, not a data-quality problem.
- **Supporting example/evidence:** open with a compressed version of the
  Model Promotion Gate scenario *without* the gate — "candidate looks good
  on the dashboard, someone flips the flag" — to make the missing
  checkpoint visible before naming it.
- **Word budget:** 150–200.
- **Transition:** to see exactly what's missing, we need to separate two
  things that are usually treated as one: the output and the decision.
- **Must NOT leak:** no mention of reconstruction-over-time, capability vs.
  understanding, or the historical software-engineering analogy.

### Section 2 — Outputs vs. decisions (≈250–300 words)

- **Purpose:** establish the article's core vocabulary.
- **Central claim:** an *output* is a raw model artifact; a *decision* is an
  authorized, consequential commitment to act. Systems that conflate them
  let outputs act as if they were already validated decisions (evidence.md
  claim 3).
- **Supporting example/evidence:** the Model Promotion Gate's "candidate
  looks good" (output) vs. "candidate is promoted to serve traffic"
  (decision) distinction.
- **Word budget:** 250–300.
- **Transition:** once a decision is a distinct object, what does it need to
  be defensible?
- **Must NOT leak:** do not frame this as "so it can be explained/audited
  later" (Article 2/3 territory) — frame it as "so it can be checked before
  it happens" (decision-time control only).
- **Boundary-safe bridge (one sentence, permitted here):** "This article is
  only about whether a decision was properly supported and gated at the
  moment it was made — whether that support still means anything six months
  later, once the systems around it have changed, is a separate and deeper
  problem this article does not take on." Mark this explicitly as a bridge,
  not a developed claim — do not elaborate further in this section.

### Section 3 — What a decision needs (≈300–350 words)

- **Purpose:** define the supporting conditions a decision must carry.
- **Central claim:** a production decision should have explicit supporting
  conditions: what evidence supports it, which evaluation established
  readiness, which policy/requirement applies, who or what has authority to
  approve it, and whether the required evidence is actually present
  (evidence.md claim 4).
- **Supporting example/evidence:** enumerate these five conditions against
  the Model Promotion Gate: evaluation report (evidence), the eval suite run
  (evaluation), the policy version referenced (policy), the approver role
  for escalations (authority), and a presence-check step (is evidence
  actually attached, not just claimed).
- **Word budget:** 300–350.
- **Transition:** having these conditions recorded is necessary — but
  recording them doesn't yet do anything on its own.
- **Must NOT leak:** no discussion of whether these records survive context
  drift, model updates, or policy revisions — that's Article 2.

### Section 4 — Recording is not enforcing (≈250–300 words)

- **Purpose:** the article's first real turn — documentation vs. control.
- **Central claim:** a system can be fully documented and still execute a
  decision that violates its own stated requirements; governance becomes
  operational only when requirements can block, permit, or escalate a
  decision (evidence.md claim 5, stated in its logical form, not as an
  unsupported empirical verdict).
- **Supporting example/evidence:** a promotion that proceeds even though the
  evaluation report shows a fairness metric below threshold — nothing
  stopped it, because nothing was watching for it at the point of action,
  only recording it after.
- **Word budget:** 250–300.
- **Transition:** this motivates a decision architecture built around
  enforcement, not paperwork.
- **Must NOT leak:** nothing here about long-term reconstruction; the
  failure mode described is "nothing blocked it," not "nothing can explain
  it later."

### Section 5 — The gate pattern (≈400–450 words) — technical core

- **Purpose:** walk through the concrete mechanism, using the running
  example end-to-end.
- **Central claim:** a CI-style deterministic gate is one concrete pattern
  for coupling evidence to production decisions: evidence enters, rules
  evaluate it against policy, the gate produces allow/block/escalate, and
  only allowed decisions proceed (evidence.md claims 6, 12).
- **Supporting example/evidence:** the full Model Promotion Gate walk-
  through: output → proposed decision → evidence attached → gate reads
  evidence + policy → allow/block/escalate → production action (or none,
  on block). Include the escalate branch explicitly: human approval is
  presented as a formal, attributed branch of the gate outcome (evidence.md
  claim 7), not an informal side channel that bypasses the pipeline.
- **Word budget:** 400–450 (longest section — this is where the diagram in
  `diagram-spec.md` is placed).
- **Transition:** what does building this actually get you — and what
  doesn't it get you?
- **Must NOT leak:** describe the gate as a generic architecture pattern;
  the one permitted AIGov Core sentence stays anecdotal/originating-problem
  only (see running-example note above), no invented AIGov functionality.

### Section 6 — What this buys you (and doesn't) (≈200–250 words)

- **Purpose:** state the narrower, defensible claim and explicitly avoid
  overclaiming.
- **Central claim:** the result is not "compliant AI by construction" — the
  narrower and correct claim is that production AI becomes more auditable
  and controllable when decision evidence and enforcement are native
  architectural components rather than external documentation (matches
  Task B thesis (1), avoids Task B thesis (3)'s overclaim).
- **Supporting example/evidence:** contrast the gated Model Promotion
  pipeline against the un-gated version from Section 1 — same model, same
  evaluation numbers, different architectural guarantee.
- **Word budget:** 200–250.
- **Transition:** into the closing takeaway.
- **Must NOT leak:** this is where the single permitted boundary-safe
  foreshadow sentence to Articles 2/3 belongs (in addition to, not instead
  of, the one in Section 2): "Evidence existing and being checked at the
  moment of decision is a different question from whether that evidence
  still means anything after the surrounding system has moved on — that
  question is out of scope here." Mark explicitly as a bridge; do not
  develop reconstructability, state/knowledge, or the historical
  software-engineering pattern.

### Section 7 — Closing takeaway (≈100–150 words)

- **Purpose:** leave the reader with a portable mental model.
- **Central claim:** if it's consequential, it's a decision, not an output;
  if it's a decision, it needs evidence and a gate.
- **Supporting example/evidence:** one-line callback to the Model Promotion
  Gate as the pattern to reuse elsewhere (approvals, autonomous agent
  actions, content moderation actions, etc. — named only as pattern
  analogues, not developed).
- **Word budget:** 100–150.
- **Transition:** none — end of article.
- **Must NOT leak:** no forward reference beyond what Section 6 already
  flagged; do not name "Article 2" or "Article 3" or preview their content.

---

**Total word budget check:** 175 + 275 + 325 + 275 + 425 + 225 + 125 ≈
**1,825 words** (midpoint estimates), inside the 1,500–2,000 target range.
