---
id: note-oreilly-submission-publication-qa
title: "O'Reilly Submission — Publication QA"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [oreilly, submission, qa]
refs: [article-submission.md, SUBMISSION-PACKAGE.md]
---

QA performed against `article-submission.md` (the publication-facing
copy), not `draft-v2.md` directly, though the two are substantively
identical apart from the disclosed publication-only edits.

| Check | Result |
|---|---|
| Title | **PASS** — "Authorized Now, Reconstructable Later," matches `SUBMISSION-PACKAGE.md`. |
| Dek | **PASS** — finalized, 18 words, no marketing language, states the core distinction directly. |
| Article body | **PASS** — reads coherently start to finish; verified by direct re-read this session. |
| Word count | **PASS** — 3,810 words (body, excluding "Further reading"), within the accepted 3,500–4,300 target. |
| Spelling | **PASS** — no misspellings found on direct re-read; no automated spellcheck tool was run, disclosed as a manual check only. |
| Broken citation markers | **PASS** — grep-confirmed zero stray `[n]` bracket markers remain; all citations converted to inline hyperlinks or short inline attributions per `references.md`. |
| URLs | **PASS, format-checked only** — all 9 URLs are well-formed and match `draft-v2.md`'s already-accepted References exactly (no new URLs introduced). Live resolution was not re-verified this session — flagged as a pre-submission task, not a blocker, since these are the same URLs already accepted in `draft-v2.md`. |
| Duplicate paragraphs | **PASS** — no duplicate prose paragraphs found; one heuristic false-positive (a repeated `|` character inside the ASCII diagram's box-drawing) is not a content duplication. |
| Heading hierarchy | **PASS** — one H1 (title), all eight sections plus "Further reading" as H2, no skipped levels. |
| Diagram references | **PASS** — the diagram appears once, in "What to Actually Build," matching `diagram-spec.md`'s specification exactly; no dangling reference to a diagram elsewhere in the text. |
| Bio accuracy | **PASS** — `SUBMISSION-PACKAGE.md`'s author bio (92 words) draws only from professional background material; no claim in it exceeds what's supportable. |
| No internal repo notes | **PASS** — `article-submission.md` contains no YAML frontmatter, no internal file-path references, no drafting-process commentary; grep-confirmed no research-programme internal vocabulary (Contribution numbers, regime names, T1/T2, metric names) anywhere in the body. |
| No personal information | **PASS** — see the dedicated privacy scan in this task's validation step; zero matches for mailing address, phone number, or personal email anywhere in the submission package. |
| No unsupported marketing claims | **PASS** — grep-confirmed zero occurrences of "revolutionary," "trustworthy AI," "responsible AI," or Source B's original unsupported claims ("most AI systems fail... not because of poor models," "every decision is validated, traceable, and enforceable"). |
| No research-program jargon | **PASS** — same scan as above; no contribution numbers, regime letters, or internal metric names found. |
| No TODOs | **PASS** — grep-confirmed zero occurrences of "TODO," "TBD," "XXX." |
| No placeholder citations | **PASS** — grep-confirmed zero "[citation needed]" or similar placeholders; all nine citations are complete and specific. |
| No "Understanding Layer" | **PASS** — grep-confirmed zero occurrences. |
| No capability-vs-understanding | **PASS** — grep-confirmed zero occurrences. |
| No book-proposal claims accidentally restored | **PASS** — same marketing-language scan; none of Source B's original unsupported claims appear. |

## Verdict

**PASS.**

No blocking issue found. The one non-blocking, disclosed item (live URL
resolution not re-verified this session) is a pre-submission task, not
a QA failure — the URLs themselves are unchanged from the already-
accepted `draft-v2.md` and were not newly introduced.
