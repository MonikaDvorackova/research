---
id: pub-03-iclr-submission-readiness-audit
title: "ICLR final submission readiness audit (Area Chair inspection)"
type: planning
status: final
created: 2026-08-04
updated: 2026-08-04
---

# ICLR Area Chair — pre-submission inspection

**Manuscript:** `publications/03-iclr-long-term-knowledge-memory/manuscript/paper.md`  
**Role:** final inspection only; no scientific rewrite; no commit.

## A. ICLR readability

**One coherent story:** Yes. Motivation → gap (per-query Acc vs joint world-history coherence) → formal object → benchmark → metrics → reference systems → frozen results → limitations. Thesis is measurement, not architecture.

**Motivation:** Immediate by end of Abstract / first two intro paragraphs.

**Contribution hierarchy:** Clear (methodology → benchmark → metrics → empirical characterization). Explicitly demotes H0 to reference baseline.

**Section support:** §§3–5 define the object; §6–7 enable evaluation; §8–9 answer the RQ; §10 bounds claims. No scientific detours that reopen architecture superiority.

**Unnecessary detours (presentation, not science):** Related-work residual is repeated often; §8.3 H0/compact matched-budget discussion is long for a benchmark paper; assembly meta-sections at end are not paper content.

## B. Reviewer experience (by section)

| Section | Issues |
|---|---|
| Abstract | Clean; dense acronym load (BCR/CSR/ConsAcc) acceptable for ICLR. |
| §1 | Strong. Mild repetition of empirical headline vs Abstract. |
| §2 | Attention drop risk: long dense paragraphs; residual restated 4×. Necessary defensively, fatiguing. |
| §3 | Clear; good Figure 1–2 placement. |
| §4 | Scale numbers appear twice (prose + Table 2). Fine but redundant. |
| §5 | Terminology-heavy (ConsAcc / PConsAcc grid); justified. |
| §6 | Clear fairness caveats; H0 described carefully. |
| §7 | Repo-path / freeze-file language feels internal. |
| §8 | Strongest section. **Rounding inconsistency** (see C). Duplicate inline tables then formal Tables 3/4/7. **Figure 5 appears before Figure 4.** |
| §9 | Good localization; Table 5 “Source: csv” is lab note. |
| §10–11 | Scope hygiene excellent. |
| End matter | “Final figure/table list”, key-only References, process notes in Appendix A — not reviewer-facing. |

## C. Claim hygiene

**Supported claims:** Acc≠Φ (corruption + symbolic); high-Acc retrieval gaps; Qwen BCR=0; CSR discriminative; H0 Acc≠CSR win; architecture superiority unsupported.

**Watch sentences (not false, but interpretable as soft overclaim):**

- “Acc remains non-trivial” under Qwen Acc ≈ 0.09–0.19 — some reviewers will dispute “non-trivial.”
- Table 1 all-Yes row for this work — standard but can read as scoreboard marketing; mitigated by reading rule and §2.4 credit to SetCons/LogicVault.
- §9.4 “reader composition” causal flavor — mostly careful (“suggested… consistent with”), still slightly causal.

**No hidden architecture marketing** as contribution; negative result correctly framed.

**Internal inconsistency (must fix before PDF):** §8.2 lists B3 BCR **0.063** while Table 3 lists **0.062** (CSV 0.0625). §8.4 H0 Abs **0.483** vs Table 4 **0.482** (CSV 0.4825).

## D. Presentation

- Notation Acc/BCR/CSR/Φ/𝒞 mostly consistent; LTM used before explicit acronym expansion.
- Figures 1–5 and Tables 1–8 referenced.
- Equations unnumbered (Markdown); OK until LaTeX.
- Bibliography: keys only, not rendered entries.
- Appendix A/B present; B uses local repo paths.

## E. ICLR style / positioning match

Reads as **benchmark + evaluation methodology** (correct). Mild systems flavor in §6/§8.3 only as reference baselines — acceptable if kept demoted.

## F. OpenReview

| Item | Status |
|---|---|
| Author names in body | None found |
| Anonymity risk | Local paths, `planning/` refs, experiment tree paths |
| Supplementary / artifacts | Path list present; not anonymized release statement |
| Reproducibility | Appendix A present (needs cleanup of author process notes) |
| Limitations | Strong (§10, Table 8) |
| Ethics / broader impact | Absent (synthetic benchmark; usually brief N/A) |
| Submission PDF / ICLR style | Not produced |

## G. Decision inputs

Science freeze integrity: PASS.  
OpenReview upload readiness as currently assembled: FAIL (format + scaffolding + rounding sync).
