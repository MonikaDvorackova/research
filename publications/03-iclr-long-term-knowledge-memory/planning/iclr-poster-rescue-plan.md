---
id: pub-03-iclr-poster-rescue-plan
title: "ICLR 2027 poster rescue plan — WorldConsistMem"
type: planning
status: active
created: 2026-09-07
updated: 2026-09-07
---

# ICLR 2027 poster rescue plan — WorldConsistMem

**Venue:** ICLR 2027 (abstract 2026-09-18 AOE; paper 2026-09-25 AOE).  
**Main-text limit:** ≤9 pages at submission (desk-reject if exceeded).  
**Paper shape:** benchmark + evaluation methodology (architecture claim closed).  
**Authoritative freeze:** `/Users/monikadvorackova/worldconsistmem-experiments/results/scaled/FINAL_EXPERIMENT_STATUS.md`  
**Note:** The research repo path `experiments/worldconsistmem/` is empty; runnable code and frozen CSVs live in the external experiment repo above. Do not invent numbers; do not mutate the frozen Option A artefacts.

---

## A. Current strengths

1. **Clear measurement gap.** Acc vs joint world-history consistency is concrete, with a minimal CEO-transition counterexample already in the draft.
2. **Defensible residual novelty** vs LongMemEval / V2 / MemoryAgentBench / DynamicMem / WorldMemArena / MemConflict **and** vs SetCons / LogicVault (memory + evolving gold world + world-history-derived Φ, not SMT/case-file SAT alone). Audited in `planning/final-novelty-audit.md`.
3. **Metric suite is operational.** Acc, BCR, CSR, ConsAcc/PConsAcc, Gap_query/Gap_bundle are implemented, tested (92 pytest passed), and frozen.
4. **Strong dissociation evidence already exists:**
   - Corruption suite: high Acc + BCR=0 and low Acc + BCR=1 both occur.
   - Symbolic scaled (102 / 1,088 / 7,140): B4 Acc 0.929 vs BCR 0.591 (Gap_query 0.338); B3 Acc 0.567 vs BCR 0.0625.
   - Qwen H4: Acc > 0 with BCR = 0 for all four systems; mean CSR still separates systems (0.258–0.329).
5. **BCR-floor diagnostics already exist** in `partial_consistency_findings.md` (transition fails on 192/192 bundles; multi-violation fractions; Acc–CSR correlations).
6. **Honest negative architecture result** is already written correctly (do not revive).
7. **World-level bootstrap CIs already computed** in CSVs but underused in the PDF tables.
8. **Tier / difficulty stratification already computed** (`difficulty_results.csv`; Fig.~5) and shows Acc–BCR divergence under history-length proxies (small/medium/large).

---

## B. ICLR reviewer risks (ranked by severity)

| Rank | Risk | Severity | Why it kills posters |
|---|---|---|---|
| R1 | **Main text > 9 pages** | Critical (desk reject) | Current PDF: scientific body through Conclusion ≈ pages 1–13; refs start p.14. Ethics/Repro do not count, but Conclusion still sits past p.9. |
| R2 | **Wrong venue year / missing ICLR 2027 requirements** | Critical | PDF header says “ICLR 2026”; style is `iclr2026_*`; ICLR 2027 requires 2027 style files + mandatory AI-use statement. |
| R3 | **BCR = 0 read as broken metric / parser** | High | Reviewers may dismiss the LLM study if floor is unexplained; paper already has the rebuttal pieces but they are scattered. |
| R4 | **Incremental novelty vs SetCons/LogicVault + LTM Acc suites** | High | Residual is real but must stay sharp; Related Work is short in main text (good) but appendix table can look like scoreboard marketing. |
| R5 | **Synthetic benchmark validity / ecological overclaim** | High | Controlled synthetic worlds are necessary for Φ; reviewers punish any “real-world memory” tone. |
| R6 | **Weak LLM reader (3B Qwen) + high abstention** | High | Limits external credibility; must keep scoped and use CSR diagnostics honestly. |
| R7 | **CSR resolution doubted when BCR floors** | Medium–High | Need distributions, family hits, CIs—not only mean CSR. |
| R8 | **CIs mentioned but not shown** | Medium | Protocol claims world-level bootstrap CIs; tables omit them → reproducibility / completeness hit. |
| R9 | **Baseline fairness / compact-flat saturation** | Medium | Compact BCR=1 under symbolic can look like a setup artifact; already caveated—must remain visible after compression. |
| R10 | **Artifact path mismatch / empty `experiments/worldconsistmem/` in research repo** | Medium | Reproducibility statement claims release; research tree lacks code; must package anonymized supplementary correctly. |
| R11 | **Presentation density before Results** | Medium | Results currently start ~p.9; formal sections eat the budget. |
| R12 | **Manuscript/table rounding drift** | Low (fixable) | Canonical display: B3 BCR **0.063** (raw 0.0625), H0 Abs **0.483** (raw 0.4825). Markdown tables still show 0.062 / 0.482. |

---

## C. Exact evidence needed for each risk

| Risk | Evidence needed | Status in artefacts |
|---|---|---|
| R1 | Compress to ≤9 main pages; verify with compile | Action required |
| R2 | Swap to ICLR 2027 style; add AI Use Statement; retarget header | Action required |
| R3 | Gold Acc=BCR=1 (smoke + preferably H4-subset gold); symbolic non-zero BCR; Qwen multi-violation + transition 192/192; abstention/malformed rates; reader_fail_on_evidence | Mostly present; H4 gold recheck recommended as labelled sanity |
| R4 | Keep dual contrast; no “first consistency”; Table closest-work stays appendix | Present |
| R5 | Explicit “what we test / do not claim” in Discussion | Present; keep under compression |
| R6 | Scope to single local reader; report Abs/Mal; no human-level claim | Present |
| R7 | Report mean/median CSR, mean viol., multi-viol. frac, family hits, Acc–CSR r, CSR world CIs | Present in `partial_consistency_*`; under-surfaced in PDF |
| R8 | Put Acc/BCR (and CSR where available) world CIs into tables or caption | CSV columns exist |
| R9 | Keep compact-padding fairness sentence in main text | Present |
| R10 | Anonymized code+data zip from experiment repo; no identifying paths | Partial |
| R11 | Move formal detail / extended failures to appendix | Action required |
| R12 | Sync markdown tables to half-up display rule | Action required |

**Numerical audit (frozen CSV ↔ submission LaTeX, half-up 3 decimals):** PASS for headline Acc/BCR/CSR/Abs/Mal after the OpenReview rounding rule in `submission/NONSCIENTIFIC_CHANGELOG.md`. Raw: B3 BCR 0.0625; H0 Acc 0.1849; H0 Abs 0.4825; B4 Acc 0.1484; CSR means 0.2581 / 0.2581 / 0.3291 / 0.2844.

---

## D. Experiments realistically completable before deadline

### D0 — No new inference (do first; hours)

| ID | Action | Runtime | Output use |
|---|---|---|---|
| E0a | Surface existing world-level CIs in main tables / captions | minutes | R8 |
| E0b | Surface Qwen BCR-floor diagnostics (violations, family hits, Acc–CSR r) already in partial findings | minutes | R3, R7 |
| E0c | Surface symbolic tier Acc/BCR for B3/B4 from `difficulty_results.csv` (history-length proxy) | minutes | R5/generalization |
| E0d | Re-run pytest in experiment repo | ~4s | reproducibility check |
| E0e | Offline H4-subset **gold** prediction evaluate → expect BCR=1 | minutes | BCR sanity (new labelled status, not mutating Option A) |

### D1 — Symbolic robustness (new labelled runs; do not overwrite freeze)

| ID | Action | Feasibility | Notes |
|---|---|---|---|
| E1a | Alternate seed symbolic mini-study (e.g. seeds 101–103, fewer worlds/tier) | High; code supports `seed` / `worlds_per_tier` | Tests seed sensitivity of Gap_query |
| E1b | Relation-density / event-volume already proxied by tier; report frozen tier table rather than new generator knobs | Prefer E0c | `relation_density` exists in generator but no frozen density sweep |
| E1c | Bundle-size / constraint-density dedicated sweep | Medium | Would need generator changes → **defer** unless trivial |
| E1d | Extra corruption rates | Low value | Smoke suite already separates Acc≠Φ |

### D2 — Additional LLM reader (optional P2)

| ID | Action | Feasibility | Decision |
|---|---|---|---|
| E2a | Phi / larger Qwen / cloud | Code has hooks; hours–days; freeze forbids Phi for Option A | **Do not block submission**; only if time remains and clearly labelled as supplementary |

**Priority order for execution:** E0a–E0e → E1a if time → never revive architecture claim → E2 only as optional appendix.

---

## E. Changes that should not be attempted

1. **Revive H0 / hierarchy superiority** as a contribution.
2. **Mutate frozen Option A predictions** or “optimize” BCR by prompt hacking.
3. **Claim real-world / legal / production generality.**
4. **Run large multi-model LLM campaigns** that risk incomplete tables at deadline.
5. **Convert paper into an architecture paper** or add untested memory designs.
6. **Invent CIs, significance tests, or external-benchmark transfer results.**
7. **Silent author-list changes** or single-author conversion.
8. **Touch JURIX or other publication trees.**
9. **Commit / push** unless explicitly requested.
10. **Cosmetic rewriting without page-cut** — presentation polish after ≤9 pages is locked.

---

## F. Final acceptance-readiness checklist

### Desk-reject hygiene
- [ ] Main text ≤ 9 pages (ICLR 2027 style)
- [ ] ICLR 2027 style files in use; header not “2026”
- [ ] Mandatory AI Use Statement present (outside page limit)
- [ ] Ethics + Reproducibility present (outside page limit)
- [ ] Double-blind: no names, emails, identifying paths, coauthor-identifying URLs
- [ ] No placeholder / duplicate abstract

### Scientific story (one narrative)
- [ ] Individual answers can look correct
- [ ] Bundle can still be inconsistent
- [ ] WorldConsistMem measures this (bundles + Φ)
- [ ] Acc, BCR, CSR expose different failure modes
- [ ] Effect survives controlled scaling / corruption (frozen + any new labelled runs)
- [ ] Architecture superiority unsupported (explicit)

### Evidence integrity
- [ ] Every headline number traceable to frozen CSV or clearly labelled new experiment status
- [ ] Abstract / tables / figures / conclusion agree
- [ ] BCR=0 explained with multi-violation + gold/symbolic satisfiability
- [ ] CSR diagnostics visible when BCR floors
- [ ] Limitations include synthetic scope, reader, exact-match, fairness

### Poster readiness
- [ ] Fig.~1 or Fig.~2 as dominant evaluation-object visual
- [ ] Fig.~3 as dominant Acc/BCR/CSR divergence visual
- [ ] Captions state takeaway
- [ ] Tables readable after compression
- [ ] Anonymized code/data supplementary prepared from experiment repo

### Subjective gate (poster)
Submit only if: (i) ≤9 pages, (ii) BCR floor defended, (iii) residual novelty sharp, (iv) no architecture overclaim, (v) artefact package exists. Otherwise delay or redirect (e.g. workshop / extended tech report) rather than desk-reject or underpowered LLM-only story.

---

## Implementation sequence for this rescue pass

1. Write this plan (done).
2. **P0 page cut + ICLR 2027 packaging + claim sync + CI/BCR-floor surfacing from existing artefacts.**
3. **P1:** H4 gold BCR sanity + optional alternate-seed symbolic mini-study if runtime allows; label outputs separately from freeze.
4. Compile PDF; verify page count; sync OpenReview package.
5. Write `planning/iclr-poster-rescue-report.md` with recommendation.
