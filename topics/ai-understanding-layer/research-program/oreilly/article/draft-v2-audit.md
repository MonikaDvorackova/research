---
id: note-oreilly-article-draft-v2-audit
title: "O'Reilly Article draft-v2 — Self-Audit"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [oreilly, article, audit, v2]
refs: [draft-v2.md, editorial-notes-v2.md, review/VERDICT.md]
---

Independent self-audit against the 17 checks specified for this
drafting task and against `review/revision-plan-v2.md`'s exact required
changes. PASS / WARN / FAIL. No substantive problem found below has been
silently left unfixed in draft-v2 itself; anything not fully resolved
is stated as such, not hidden.

## 1. Section 4 (now "Reconstructing a Decision Later") no longer contradicts Article 2

**PASS.** Grep-confirmed: the phrase "assembled after the fact" (the
absolute claim draft-v1 made) does not appear anywhere in draft-v2. The
rewritten paragraph states the property as "informational, not
representational" and explicitly: "Explicit decision-time recording is
one way to guarantee this property holds. It is not the only way, and
this article does not claim it's required" — matching
`contribution-02/article/draft-v2.md` line 43 ("not the only way")
directly.

## 2. Representation-neutral reconstruction claim

**PASS.** The requirement is stated as preserving "enough evidence to
identify the consumed context uniquely," satisfiable via "an explicit
binding... or... reliably derivable afterward, from provenance edges,
event records, execution traces, or a sufficiently precise temporal
history" — no storage technology or schema is claimed necessary.

## 3. Bitemporal correctness

**PASS.** States directly: "A correctly designed bitemporal database or
a well-instrumented event log can already preserve everything needed,
if it's instrumented to capture the right relationship." No claim that
bitemporal databases are insufficient or that explicit custom binding is
always required.

## 4. No unsupported prevalence

**PASS.** Grep-confirmed zero occurrences of "most systems," "most ML
pipelines," or "most production AI systems." A fourth, related instance
("more heterogeneous inputs than most of the systems...") was found and
corrected during this session's pre-audit pass (`editorial-notes-v2.md`)
— not one of the three originally flagged instances, but caught on
sight rather than left in. The one remaining "most" in the article
("edge cases most likely to matter later," Section 3) is a superlative
intensifier, not a prevalence/quantifier claim, and requires no change.

## 5. No deterministic "will eventually" claims

**PASS.** Grep-confirmed zero occurrences of "will, sooner or later" or
"will eventually." Replaced with: "that design creates pressure to
collapse ambiguity into a specific answer that looks the same as a
determined one" — a design-necessity argument, not a prediction about
future system behavior.

## 6. Reconstruction outcome separated from persisted data

**PASS.** Section 7 is explicitly split into "What to preserve around
the decision" (four decision-time categories) and "What a
reconstruction process should be able to return" (identified/ambiguous/
unavailable), with the reason stated in-line: "not persisted at decision
time, because it isn't known at decision time."

## 7. Citations complete

**PASS, with one disclosed caveat.** Nine citations, all present in both
body and References, no dangling or unused entries (grep-verified: [1]
through [9] each appear at least once in body text and exactly once in
References). Five new citations added per the required plan: Kubernetes
admission controllers, XACML/PDP-PEP, in-toto, SLSA, and Buneman/Khanna/
Tan (ICDT 2001, previously verified elsewhere in this programme). The
four infrastructure citations (Kubernetes, XACML, in-toto, SLSA) rely on
high-confidence, well-known canonical URLs rather than a fresh
same-session verification fetch — disclosed in `editorial-notes-v2.md`
and flagged for the acceptance gate's judgment, not hidden. No author
list was fabricated anywhere; citation [9] retains "et al." exactly as
before.

## 8. Dynamic assurance acknowledged fairly

**PASS.** Section 6 now states directly: "Of everything cited here,
dynamic and continuous assurance cases come closest to this article's
own combined concern... and it wasn't invented here" — a direct,
unhedged concession, stronger than draft-v1's implicit treatment.

## 9. Synthesis stronger than concatenation

**PASS.** The explicit pivot paragraph ("Authorization asks...
Reconstruction asks... A system can satisfy either property while
failing the other") now opens the reconstruction section directly,
sharpening the moment `review/reviewer-report.md` §13 already found
present but implicit in draft-v1's lines 51–53.

## 10. AI specificity honest

**PASS.** Section 6's closing paragraph states plainly "none of this is
unique to AI" and names the specific, evidenced reason AI-mediated
decisions matter more (heterogeneous inputs: model version, prompt/
configuration, retrieval, tool state, dataset, policy, human/service
authority — all seven items from the drafting task's required list are
present) without any prevalence claim.

## 11. C3 subordinate

**PASS.** Section 5 ("When the Record Can't Decide") is 381 words,
within the 300–400 target. No case IDs, regime names, or metric names
(Trajectory Identifiability, Dependency Edge Accuracy, False Global
Confidence) appear anywhere — grep-verified. The trajectory-level
extension is one sentence, using only the already-established
identified/ambiguous/unavailable vocabulary, not new terminology.

## 12. Title accurate

**PASS.** "Authorized Now, Reconstructable Later" — matches the
required title exactly. Covers both halves of the article (unlike
draft-v1's title, which represented only reconstruction) and contains
no false dichotomy.

## 13. Terminology uses reconstructable

**PASS.** Grep-confirmed: "explain"/"explainable" appears exactly twice
in the entire article, both within the single disambiguation sentence in
Section 1. Every section heading, the title, and the dek use
"authorized"/"reconstructable."

## 14. No XAI ambiguity

**PASS.** The disambiguation sentence is present, tightened, and placed
immediately after the section's punchline (per `editorial-notes-v2.md`);
given "reconstructable" is now the article's primary term throughout,
the XAI-misreading risk that motivated this check in draft-v1's review
is substantially reduced independent of the disambiguation sentence
itself.

## 15. No retired concepts

**PASS.** Grep-confirmed zero occurrences of "Understanding Layer" or
"capability vs. understanding" anywhere in draft-v2.

## 16. Word count

**PASS.** Body (title, dek, eight sections, excluding References):
**3,783 words** — within the 3,500–4,300 target, and tighter than
draft-v1's 3,882 without cutting required content (the reduction comes
primarily from compressing the retroactive-correction example from a
full paragraph to one sentence, per the drafting task's explicit
instruction).

## 17. Practical value

**PASS.** The Section 7 checklist is retained and structurally improved
— an engineer following it now has an unambiguous answer to "what do I
populate now vs. what does a later process produce," which directly
resolves the practical confusion draft-v1's review flagged as its most
consequential structural issue after the P0 finding.

## Overall

**17/17 PASS. No blocking technical issue found.** No item required
deferral to a hypothetical v3. The one disclosed, non-blocking item
(citation-URL verification confidence for the four new infrastructure
citations) is a judgment call appropriately left to the acceptance gate,
not a substantive defect in the article's argument or evidence.
