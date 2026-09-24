# NeurIPS 2026 rejection retrospective and v2 plan

**Paper:** *From Model Outputs to Auditable Decisions: Evidence-Gated Enforcement for AI Systems*  
**Venue:** NeurIPS 2026 Main Track  
**Decision:** Reject  
**Recorded:** 2026-09-24

## 1. Executive assessment

The rejection does **not** indicate that the core research problem was considered unimportant. Across the reviews and meta-review, reviewers consistently recognized decision-level auditability as a real, important, and underexplored problem. The rejection was driven primarily by insufficient technical and empirical support for the proposed solution.

The central lesson is therefore not to abandon the research question, but to redesign the scientific claim and evaluation.

### Consensus from the reviews

Positive signals:

- the problem was described as promising, important, underexplored, and potentially globally significant;
- the distinction between model correctness and decision justification was generally understandable;
- the auditability-gap framing was considered intuitive;
- the VALID / INVALID / BLOCKED taxonomy was clear;
- the framework's simplicity and interpretability were viewed positively.

Primary weaknesses:

1. evaluation was synthetic and insufficiently connected to real-world utility;
2. the principal policy-conformance experiment was close to self-fulfilling because the gate and expected oracle were derived from substantially the same policy assumptions;
3. reproducibility and experimental methodology were insufficiently documented;
4. the repository-prevalence study was not explained rigorously enough;
5. related work was incomplete and the novelty boundary was unclear;
6. the work did not sufficiently establish what is specifically AI-related rather than generic workflow/compliance enforcement;
7. there was no real-world deployment, independent audit ground truth, user study, operational audit dataset, or comparable practical evidence;
8. significance and originality therefore remained insufficiently demonstrated.

The meta-review agreed with the reviewers and concluded that these issues were too substantial to repair during the rebuttal period.

## 2. Process lesson: rebuttal

No author response was submitted during the NeurIPS discussion phase. The final meta-review explicitly records this.

This should become a process rule for future submissions:

> Always submit an author response/rebuttal when the venue permits one, even when the expected outcome is rejection.

A rebuttal probably would not have fixed this submission because the AC explicitly considered the concerns too large to address during rebuttal. However, it could have corrected factual misunderstandings, clarified the repository experiment and preserved a better discussion record.

## 3. Scientific reframing

The next version should not center its scientific claim on:

> EGDS agrees perfectly with a rubric derived from the same policy specification.

That is useful implementation verification, but weak evidence of scientific effectiveness.

The stronger central proposition is:

> **Predictive validity does not imply decision auditability.**

Formally, the paper should investigate the non-implication:

```
PredictiveValidity(M) ↛ DecisionAuditability(D)
```

The scientific task becomes:

1. define decision auditability precisely;
2. demonstrate empirically that it is distinct from predictive/model-level validity;
3. identify AI-specific mechanisms that cause auditability to fail;
4. show that evidence-gated enforcement detects/prevents these failures;
5. measure the operational costs and benefits of enforcing this property.

EGDS then becomes the enforcement mechanism supporting the scientific argument, rather than the scientific result by itself.

## 4. Reconsider the "auditability gap" metric

The current framing as a numerical difference between model performance and justification requires much stronger justification. Accuracy/performance and auditability are not obviously commensurable quantities.

Do not rely on a subtraction such as:

```
Gap = ModelPerformance - JustificationScore
```

unless a defensible measurement theory is established.

Prefer defining auditability as an independent property, e.g.:

```
A(D, E, P, t) ∈ {0, 1}
```

where:

- D = concrete operational decision;
- E = evidence set;
- P = governing policy/specification;
- t = relevant time/version state.

The key empirical question then becomes whether systems with acceptable predictive validity can nevertheless have A = 0.

Possible probabilistic analysis:

```
P(A(D)=1 | PredictivePerformance(M) >= τ)
```

This makes the relationship between performance and auditability an empirical question rather than assuming that two unlike quantities can simply be subtracted.

## 5. Make the contribution AI-specific

A major reviewer concern was that EGDS could be applied almost unchanged to conventional software testing or compliance workflows.

The v2 framework must therefore encode properties specific to deployed AI/ML systems.

Candidate AI-specific dependencies:

- exact model identity and version;
- relationship between evaluated and deployed model;
- training/evaluation dataset provenance;
- evaluation validity for the deployed model version;
- calibration / uncertainty evidence where relevant;
- distribution-shift and drift state;
- inference provenance;
- model/prompt/tool configuration for generative or agentic systems;
- policy/evaluation validity after model updates;
- evidence invalidation after data/model changes.

A particularly promising technical direction is **temporal and dependency-aware validity**.

A decision may satisfy:

```
Valid(D, t0) = 1
```

but after a relevant model, dataset, evaluation, policy, or evidence dependency changes:

```
Valid(D, t1) = 0
```

The framework should specify which dependency transitions invalidate which evidence and decisions.

This is materially stronger than a static approval workflow and provides a clearer AI-systems research contribution.

## 6. New research questions

Suggested RQs:

### RQ1 — Decoupling

Can an AI system satisfy conventional model-level validation while concrete downstream decisions remain unauditable?

### RQ2 — Detection

Can evidence-gated enforcement identify AI-specific evidence and provenance failures that model-level evaluation does not detect?

### RQ3 — Independent validity

How closely do EGDS decisions agree with independent human/auditor assessments when the ground truth is not generated from the EGDS policy implementation?

### RQ4 — Generalization

Do auditability failures occur in real open-source or deployed AI/ML pipelines rather than only in handcrafted synthetic scenarios?

### RQ5 — Operational utility

What latency, storage, false-blocking, integration and human-audit costs are introduced or reduced by EGDS?

### RQ6 — Temporal validity

Can dependency-aware invalidation correctly identify decisions whose supporting evidence becomes stale after model/data/policy changes?

## 7. Experimental redesign

### Experiment 1 — Policy-conformance verification

Retain the existing deterministic scenarios, failure injection and artifact replay.

Purpose must be explicitly limited to:

- implementation correctness;
- deterministic policy conformance;
- regression testing.

The existing 100% agreement / detection results belong here. They should not be presented as evidence that EGDS improves real-world auditability.

### Experiment 2 — Real AI pipeline failure injection

Use real, runnable ML/AI pipelines rather than only synthetic decision records.

Inject failures such as:

- model version mismatch;
- stale evaluation;
- evaluated/deployed model mismatch;
- missing model or dataset provenance;
- missing approval;
- artifact mutation;
- distribution-shift state without required re-evaluation;
- incomplete inference trace;
- policy/evaluation version mismatch.

Compare what remains invisible to ordinary model-level validation with what EGDS detects.

This directly tests the central proposition.

### Experiment 3 — Independent human audit

Create an audit protocol before evaluation.

Independent evaluators should assess the same systems without seeing EGDS verdicts.

Compare:

```
Human/Auditor Ground Truth ↔ EGDS
```

Report:

- precision;
- recall;
- F1;
- false acceptance;
- false blocking;
- inter-rater agreement;
- disagreement analysis.

Crucially, the independent ground truth must not simply reimplement the same oracle used internally by EGDS.

### Experiment 4 — Real-world repository study

Redesign the current 30-repository analysis as a reproducible empirical study.

Pre-register or explicitly document:

- repository inclusion/exclusion criteria;
- sampling strategy;
- date/version/commit analyzed;
- annotation protocol;
- evidence categories;
- handling of missing documentation;
- evaluator agreement;
- raw annotations;
- analysis scripts.

Possible evidence dimensions include:

- model provenance;
- evaluation provenance;
- evaluated/deployed artifact linkage;
- dataset/version evidence;
- approval or release evidence;
- inference-to-artifact traceability;
- monitoring/drift evidence;
- ability to reconstruct a concrete decision.

Do not equate missing public evidence automatically with absence in the organization's private production environment. Report precisely what the repository evidence permits concluding.

### Experiment 5 — Operational utility

Measure the cost of enforcement.

At minimum:

- gate latency;
- storage overhead;
- integration overhead;
- false-blocking rate.

Preferably add a controlled audit task:

```
T_manual-audit vs T_EGDS-assisted-audit
```

Measure both time and audit completeness/correctness.

This directly addresses the reviewers' question: does the framework deliver measurable practical value?

### Experiment 6 — Temporal/dependency invalidation

Create valid decisions and subsequently mutate relevant dependencies:

- model update;
- dataset update;
- evaluation expiration;
- policy update;
- artifact digest change;
- drift event.

Test whether only the appropriate dependent decisions/evidence become invalid.

This can become a distinctive technical contribution of v2.

## 8. Reproducibility requirements

Before resubmission, a fresh researcher should be able to reproduce every reported result from the repository without private knowledge.

Required package:

- exact environment and dependency lock;
- deterministic seeds where applicable;
- one-command or clearly documented experiment execution;
- scenario-generation code;
- complete definitions of rubrics and policies;
- raw experiment outputs;
- analysis scripts;
- scripts that generate every table and figure;
- repository-study sampling manifest;
- repository commit SHAs;
- annotation protocol;
- independent evaluator labels where publication permits;
- explicit mapping from paper result → command → artifact;
- README describing the full experimental pipeline.

A reproducibility test should be performed by someone who did not implement the experiment.

## 9. Related-work rebuild

Related work needs to be reconstructed systematically rather than incrementally patched.

Required areas:

- algorithmic and end-to-end AI auditing;
- internal algorithmic auditing;
- ML lifecycle governance;
- decision provenance and data provenance;
- AI assurance / assurance cases;
- model cards, datasheets and related documentation artifacts;
- ML supply-chain integrity;
- runtime policy enforcement;
- responsible AI governance;
- traceability and reproducibility;
- AI evaluation validity;
- safety cases / evidence-based assurance where applicable.

Raji et al. (2020) and related auditing literature explicitly raised by reviewers must be engaged substantively, not merely cited.

For every adjacent line of work, answer:

1. What property does prior work provide?
2. What does it not provide?
3. What exact property does EGDS add?
4. Is that difference demonstrated rather than asserted?

If the literature already provides the claimed property, narrow or change the novelty claim.

## 10. Paper architecture v2

Suggested structure:

1. Introduction and falsifiable claim
2. Related work and novelty boundary
3. Decision-auditability formalism
4. AI-specific evidence and dependency model
5. Evidence-gated enforcement mechanism
6. Experimental methodology
7. Policy-conformance verification
8. Real-pipeline failure-injection results
9. Independent audit evaluation
10. Real-world repository study
11. Operational overhead / utility
12. Temporal invalidation experiment
13. Limitations and threats to validity
14. Discussion
15. Conclusion

The paper should clearly separate:

- specification/definition;
- implementation verification;
- empirical scientific evidence;
- external-validity claims.

## 11. Figures and reporting

The next submission should contain actual visual analysis rather than primarily prose/table result reporting.

Candidate figures:

- model performance vs decision-auditability matrix;
- failure type × detection mechanism heatmap;
- human audit vs EGDS confusion matrix;
- audit time comparison;
- enforcement latency distribution;
- evidence/dependency graph;
- temporal invalidation example;
- repository-study prevalence with uncertainty and clearly stated denominator.

Avoid headline "100%" results unless the denominator, experimental construction and interpretation are explicit.

## 12. Submission strategy

### Immediate option: AISTATS 2027

Potential thematic fit exists for trustworthy ML / evaluation / robustness / safety-oriented work.

However, this should **not** become a rushed resubmission of the NeurIPS manuscript. The NeurIPS consensus requires substantial new experiments, a related-work rebuild and stronger technical framing. Submit only if the v2 evidence can actually be completed and independently reproduced before the deadline.

Known 2027 schedule considered on 2026-09-24:

- abstract deadline: 2026-09-29;
- full-paper deadline: 2026-10-06.

Decision rule: create an abstract only if the core real-pipeline experiment and the exact v2 contribution can be credibly defined immediately. Do not allow the deadline to force another under-validated submission.

### ICLR 2027

The abstract deadline has already passed for a new submission. Do not target this cycle unless a valid abstract for this work was already registered.

### AAAI-27 / AI Alignment track

The 2027 deadlines have passed. The AI Alignment track is nevertheless a strong thematic signal for future venue selection because its scope includes AI control/monitoring, auditing/assurance, governance, evaluation validity and safety constraints.

### Longer-horizon strategy

Prefer a venue whose audience accepts systems, auditing, assurance, governance and deployment contributions when supported by rigorous empirical evidence.

Venue selection should happen **after** the real-world/independent evaluation determines what the paper has become:

- if the main contribution becomes a formal/technical AI validity mechanism with strong experiments → target a top ML/AI venue;
- if the dominant contribution is AI systems/runtime enforcement → target an appropriate systems/ML-systems venue;
- if the dominant contribution is empirical auditing/governance methodology → target a responsible-AI / FAccT-style venue;
- if the work matures into a larger, deeper empirical study → consider a journal route.

Do not choose the venue solely by prestige. Match the final contribution type to the reviewing community.

## 13. Concrete execution plan

### Phase A — Formal repair

- replace or rigorously justify the numerical auditability-gap formulation;
- define decision auditability independently;
- define AI-specific evidence/dependency semantics;
- formalize temporal invalidation;
- state falsifiable hypotheses.

### Phase B — Literature repair

- systematic related-work search;
- novelty matrix;
- remove unsupported introduction claims;
- cite each substantive claim appropriately.

### Phase C — Empirical rebuild

- select real pipelines;
- design failure injections;
- freeze audit protocol before evaluation;
- recruit independent evaluators;
- redesign repository study;
- implement operational-overhead measurement.

### Phase D — Reproducibility

- produce one-command experiments;
- regenerate all results from clean environment;
- independent reproduction pass;
- publish raw/derived artifacts as permitted.

### Phase E — Manuscript v2

- rewrite methods before results;
- add visualizations;
- separate implementation verification from effectiveness;
- rewrite limitations/threats to validity;
- explicitly answer "why AI-specific?".

### Phase F — Submission

Before submission require all of:

- [ ] central claim supported by independent evidence;
- [ ] at least one realistic AI-pipeline experiment;
- [ ] no circular oracle as the primary validation;
- [ ] repository study reproducible;
- [ ] AI-specific novelty explicit;
- [ ] related work substantially complete;
- [ ] every headline number reproducible;
- [ ] independent reproduction completed;
- [ ] limitations accurately scoped;
- [ ] rebuttal dates entered into the submission calendar.

## 14. Bottom line

The NeurIPS reviews do not invalidate the research direction. They show that the current paper establishes an interesting problem and a working enforcement pattern, but does not yet establish a sufficiently novel, AI-specific, independently validated scientific result.

The v2 objective is therefore:

> Demonstrate that predictive validity and decision auditability are distinct properties in realistic AI systems, formalize the AI-specific evidence dependencies that determine auditability, and show through independent and reproducible experiments that evidence-gated enforcement detects or prevents failures that model-level validation does not.

That is the bar for the next submission.
