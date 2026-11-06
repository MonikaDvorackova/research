---
id: topic-bostrom-world-models-review-mm
title: "Reviewer-style assessment for Minds and Machines (self-review, Phase 2)"
topic: bostrom-world-models
type: review
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [review, journal-fit]
---

## Reviewer-style assessment

Written by the research team against its own material, as a deliberately critical referee. It has not been checked against *Minds and Machines* author guidelines (not retrieved this session), so fit judgements are provisional.

### Summary of the submission as it stands

The paper would argue that detecting a discrepancy, identifying a generative mechanism, and concluding "simulation" are three distinct inferences with distinct premises; support this with elementary formal propositions on distinguishability and evidential bounds; and illustrate it with a toy experiment in which an agent testing consistency with its own learned theory fails to detect a learned world model and falsely flags the true environment under out-of-distribution interventions.

### Strengths

1. The three-way separation, with explicit bridge premises (artifact, reference, bridge to ancestor simulations), is clear and usable, and it is tied to propositions rather than asserted.
2. Honest treatment of the negative result: the experiment does not show detection succeeding; it shows how the agent's own theory becomes the weak point.
3. Reproducible code, seeds, tests, an equivalent negative control that is not exploited, and a documented post-hoc control.

### Weaknesses (major)

1. **Mathematical contribution is thin.** Propositions 3–6 are short consequences of the definition of total variation, the chain rule, and a change of measure. A mathematically trained referee will see them as framing. The paper must say so and must not present them as theorems of independent interest. The one place with some substance, the tightness of the c^t factor in Proposition 3(a), is an open obligation.
2. **Philosophical novelty is unestablished.** Theses T1–T3 (fidelity-indexed testability; asymmetry of detection; insulation of Bostrom's argument) resemble familiar points about underdetermination, falsifiability and the sceptical structure of the argument (Birch 2013 and others). Prior statements may exist that I have not found: the philosophical literature was checked at title/abstract level, Chalmers's book and several neighbours were not read, and the citation analysis is partial. A referee familiar with this literature could judge T1–T3 not new. The contribution would then rest on the quantitative form (Propositions 4–5) and the learned-model illustration.
3. **The experiment is far from the philosophical target.** A fully observed 2-D toy system, a theory built from the reference, one architecture family, and no partial observability. The step from the toy result to any claim about embedded observers is made by argument, not evidence. The key empirical finding (false alarms up to 1.000 under out-of-distribution interventions, W looking more theory-like than reality) may be an artifact of Q and W sharing architecture and training distribution; this was not tested.
4. **Post-hoc control and exploratory status.** AltOOD was added after seeing v1. This is documented, but it limits what can be claimed.

### Weaknesses (minor)

- Bootstrap intervals over ten seeds ignore within-seed variance; no multiple-comparison handling across the many cells.
- "Active" experimentation is an uncertainty proxy, not exact expected information gain; the claim that active selection "does not help" applies to this proxy and this detector only.
- Detector uses a single statistic with no tuning; negative detector results are not general.
- Several bibliographic items remain unverified (see verification log).

### Questions a referee would ask

1. What does the toy result add that Propositions 3(b) and 6 do not already say?
2. Does the agent's theory need to be learned? A symbolic or analytically correct theory would remove the Q-misfit effect: would detection then work, making the finding a statement about estimation error rather than epistemology?
3. Where is the connection to the observer-selection part of Bostrom's argument, beyond the claim that high fidelity insulates it?
4. Is "simulation" in T1 defined so that a fidelity-indexed hypothesis is a hypothesis about simulation at all, rather than about a particular model of physics?

### Journal fit (provisional)

- *Minds and Machines*: plausible audience for the epistemological argument and the AI link, provided the philosophical thesis is shown to be new relative to the literature and the formal part is positioned as supporting analysis. Risk: referees may see the experiment as decoration.
- *Philosophy & Technology*: similar fit, possibly more tolerant of a shorter technical part.

### Verdict at this stage

**Not ready to write as a manuscript.** The defensible path is to (a) close the literature gaps, (b) test thesis novelty against the philosophical literature, (c) strengthen the experiment with the architecture and "correct theory" ablations that questions 2 and the weakness 3 point to, and then reassess.


---

## Update after Phase 3 (literature, ablations, formal review)

### What changed

1. **Philosophical novelty has weakened.** Chalmers (2024) states the perfect-simulation epistemic thesis explicitly, distinguishes sceptical imperfect simulations, and uses a defeat argument by indifference that parallels Proposition 4. T1-T3 are known in qualitative form. The unread neighbours (Brogioli; the 2026 glitch paper; Edge; Kelly's definitions; the Glymour-Malament-Manchak-Norton papers; Weatherson's text) remain unread, so further overlap may exist.
2. **The experiment is more informative and more robust.** The failure of active detection is not caused by the active policy: with the true law or a theory covering the probed range, active detection is calibrated and perfect. It is not caused by a shared architecture alone: a ReLU theory reproduces the inversion. Coverage of the theory's training range is the best-supported cause. A different model class (polynomial) removes the inversion but not the false alarms.
3. **The formal part is correct but not original.** Review recorded in `notes/formal-framework.md` section 5. The wording of Prop. 5 was narrowed to the simple fidelity-indexed hypothesis.
4. **A candidate contribution has emerged** (T4, theory-relativity of detection), but it is the quantified instance of a classic point.

### Referee-style objections, revised

- **"This is Duhem-Quine plus a toy."** Likely. The reply must show that the quantification adds something a philosopher would care about: detectability is a property of the pair (environment, theory); coverage rather than architecture drives the failure; ranking and calibration can disagree (A2); and an observer cannot know its theory covers a regime it has never visited. Whether that persuades a *Minds and Machines* referee is uncertain.
- **"Why learned world models?"** Learned observers are the case in which theory-misfit is concrete and measurable, and the same setting realises a simulated environment (W). The link to the simulation hypothesis proper stays by analogy.
- **"The experiments do not test Bostrom."** Correct, and the manuscript must say so; they test a premise (detectability) that his argument leaves open.
- **"One toy environment, one W architecture, ten seeds."** Correct. A second environment (preferably partially observed) and a second W architecture would be needed to claim generality of G2/G5.
- **"Condition C hands the agent the answer."** It gives the agent experience over the probed range, which is the point: it identifies the premise (reference coverage) that detection needs. It does not show that such coverage is available to a real observer.

### Journal fit (provisional; author guidelines not checked)

- *Minds and Machines*: moderate at best for the reformulated paper. The AI link and the epistemological framing fit; the risk is that the philosophical thesis is judged not new and the technical part judged secondary.
- *Philosophy & Technology*: better fit for a technically grounded, methodological philosophy-of-AI paper whose main claim is T4.

### Verdict

**REVISE; do not submit to *Minds and Machines* as originally framed.** The original framing (T1-T3 as the contribution) is not defensible. The reformulated paper (T4/T5 with the supporting framework and ablations) is a defensible candidate, with *Philosophy & Technology* the more realistic first target, subject to (a) reading the remaining closest sources, (b) a second environment and a second W architecture, and (c) a check of whether the quantified theory-relativity claim has precedents in the philosophy-of-science and ML-evaluation literatures.
