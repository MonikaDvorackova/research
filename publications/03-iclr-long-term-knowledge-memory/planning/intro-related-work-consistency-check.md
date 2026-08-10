---
id: pub-03-intro-related-work-consistency-check
title: "Intro / Related Work consistency check"
type: research-notes
status: complete
created: 2026-08-04
updated: 2026-08-04
---

# Intro / Related Work consistency check

Performed after drafting `01-introduction.md`, `02-related-work.md`, `tables/closest-work.md`, BibTeX append, and `final-citation-audit.md`. Frozen §§3–10 were **not** edited.

## Checks passed

| Check | Result |
|---|---|
| Intro RQ matches `final-positioning-lock.md` frozen RQ | **Pass** (verbatim) |
| Contribution list = methodology, benchmark, metrics, empirical+reference systems | **Pass** (4 bullets; no architecture contribution) |
| Related Work four-group structure matches locked structure | **Pass** (§2.1–2.4) |
| Dual neighbor contrast (LTM Acc suites + logical consistency) present | **Pass** |
| Novelty audit contrasts for DynamicMem / MemConflict / SetCons / LogicVault | **Pass** |
| No architecture marketing lead in §§1–2 | **Pass** (H0 as reference baseline only) |
| No new experimental claims beyond frozen §8 numbers | **Pass** |
| Qwen Acc/BCR/CSR values match frozen §8 table | **Pass** (Acc 0.185 / BCR 0 / CSR 0.329 BM25; Acc order preserved) |
| BCR/CSR definitions match §5 (strict vs partial; CSR complements BCR) | **Pass** |
| Terminology: dependent bundles, gold history, \(\Phi\), BCR, CSR, Gap_query | **Pass** vs §§3–5 |
| Every factual literature claim in §§1–2 has a citation key | **Pass** |
| Forbidden overclaim tokens avoided (`first`/`unprecedented`/`SOTA`/`no prior work` as novelty claims) | **Pass** after edit pass |
| `TODO(cite):` absent from §§1–2 | **Pass** |
| Closest-work table cells backed by citation audit | **Pass** (with footnotes for Partial) |
| LogicBench-Cross not given a fake independent bibliographic identity | **Pass** (cite via LogicVault) |

## Issues found and exact edits made

1. **Word-count shortfall** on first draft (Intro ~716; RW ~1073) → expanded motivation, residual framing, §2.1 closing sentence, §2.2 distinction paragraph, §2.3 grain contrast, §2.4 mandatory-positioning sentence, Intro roadmap sentence.
2. **Forbidden wording** in §2.3 (“unprecedented”, “first-class”) → rewritten to avoid those tokens while preserving meaning.
3. **“only” / “owns”** soft overclaim risk → Intro “released only as” → “released as”; §2.4 “already owns” → “already studies”.
4. **Forbidden wording** in §2.3 (“unprecedented”, “first-class”) → rewritten to avoid those tokens while preserving meaning.
5. **“only” / “owns”** soft overclaim risk → Intro “released only as” → “released as”; §2.4 “already owns” → “already studies”.
6. **EverMemBench title mismatch** (HTML alias vs arXiv title) → BibTeX uses official arXiv title; prose uses EverMemBench as benchmark name with citation.
7. **OpenReview bot wall** at final audit → LogicVault venue kept non-archival; confidence **M** recorded in citation audit.
8. **Deferred `TODO(cite):` in §§3 and 10** (SetCons/LogicVault line) → replaced with `@salla2026crossQueryContradictions; @chaudhry2026logicVault` (citation keys only; claims/numbers unchanged).

## Unresolved citation caveats

| Item | Status |
|---|---|
| `chaudhry2026logicVault` venue / archival status | **Open** — OpenReview HTML not re-confirmable this pass (bot wall); GitHub confirms project + LogicBench-Cross release |
| Most 2026 neighbors | Remain **arXiv preprints**; venues may change before camera-ready |
| `wu2025longMemEval` OpenReview HTML | Bot-walled; ICLR 2025 retained via arXiv comment + forum id |
| SetCons workshop acceptance | Supported by arXiv comment; still `@misc`, not archival proceedings entry |
| WorldMemArena instance counts | Not asserted in §§1–2 prose (avoid contested scale figures) |

## Architecture / evidence hygiene

- No restoration of hierarchy-superiority claims.
- No mutation of frozen experiment outputs, datasets, metrics, or §§3–10 numbers.
- No Abstract / Conclusion / title / camera-ready figures drafted (deferred).
