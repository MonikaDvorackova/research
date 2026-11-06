---
id: topic-bostrom-world-models-phase7-integrity
title: "Experiment-integrity report and frozen-protocol verification (X1 confirmatory run)"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [integrity, preregistration, X1]
---

# Experiment-integrity report

**Verdict: all ten integrity conditions pass. The X1 results are confirmatory for the preregistered hypotheses H1–H5.** Any analysis not listed in `03-preregistration-X1.md` is labelled exploratory below and in the results.

## Run recovery (Part 2)
| Fact | Evidence |
|---|---|
| The original process was recovered, not restarted. | At session resumption the process (parent PID 54645 and 11 workers, elapsed ≈ 6.5 min at 13:08, 80–90 % CPU each) was still running `python -m eid.run_x1 --config configs/x1_confirm.yaml --out results/x1_confirm --workers 11`. It was left untouched. It writes its output only at the end, so no partial outcomes existed to inspect. |
| One confirmatory run only. | No second launch of `run_x1` on the confirmatory config occurred. Development runs (`x1_dev`, `x1_dev_v0_5policies`) predate the freeze. |
| Completion. | `results/x1_confirm/meta.json` and `runs.jsonl` appeared at 13:26; wall time 1468 s; Python 3.12.1, numpy 2.5.4, macOS 26.2 arm64. Nothing failed. |

## The ten conditions (Part 1)
| # | Condition | Result | Evidence |
|---|---|---|---|
| 1 | Commit `02bad01` exists | pass | `02bad015a10e14215d47033dac7b78986f6dcca9` |
| 2 | Timestamp and contents | pass | committer date 2026-11-03T13:01:50+01:00; 24 files: preregistration, config, analysis code, run code, tests, dev data |
| 3 | Preregistration committed before the confirmatory execution | pass | commit 13:01:50; the run was launched at 13:01:59 (shell `date` at launch); `runs.jsonl` was created 13:26 |
| 4 | Exact configuration | pass | `meta.json` config is identical (parsed and compared) to `git show 02bad01:…/configs/x1_confirm.yaml` |
| 5 | Confirmatory seeds | pass | 600–629 (30 seeds), R = 20, N = 3000, T = 4, α = 0.05 |
| 6 | Disjoint from development seeds | pass | development: 500–505; overlap = ∅ (also disjoint from every earlier phase: 200, 300–311, 400–405) |
| 7 | No tuning after the freeze | pass | `git diff 02bad01` for `src/`, `configs/x1_confirm.yaml` and the preregistration is empty; the working tree was clean at launch. Files added after the freeze (audit, supplementary and integrity scripts, manifests) do not alter the run or the frozen analysis. |
| 8 | Analysis script matches the preregistered analysis | pass | `src/eid/analyze_x1.py` unchanged since `02bad01`; its thresholds (1.5, 0.07, 0.05, 0.8, 1500) equal the preregistered ones; it was executed unmodified |
| 9 | Incomplete, duplicated, corrupted runs | pass | 36 000 expected = 36 000 read; 0 unparsable lines; 0 duplicates; 0 missing; 0 unexpected keys; 0 non-finite values; `reject_episode ∈ [1, N+1]`; exact field set (`results/x1_confirm/integrity_check.txt`) |
| 10 | Policies received the intended information and budgets | pass | see `04-information-access-matrix.md`; the action-selection spy (audit check 4) shows P0 never plays action 2, P1 plays it ≈ 2 %, P2 is uniform, each run having the full 1200-step budget in the check; all 36 000 runs used the same N = 3000 cap; the observer code contains no reference to the truth (source-inspection test) |

## Raw-data manifest (checksums recorded before analysis)
```
7398b5b20559821021eff56bcc38c6aa10cb1d4f0b3b3ac3df8c5e2aab03cd8d  runs.jsonl
fd5fba0ddb5d580d18cb692947e05e30a84ea312c79ec09f33869473d9988d5e  meta.json
7e39a3cda3d02b2984e4e4fd577366c2aaed75f107d3426f9dd10b9013e5c16d  integrity_check.txt
```
Guard: `tests/test_x1_manifest.py` recomputes these hashes. Files: `results/x1_confirm/MANIFEST_raw.sha256`.

## Disclosures that qualify the "confirmatory" label
1. **Development exposure.** The preregistration was written after seeing development results on seeds 500–505 and states this. In particular H4c's and H4b's expected outcomes were predicted from development data; H4a and H5 were predicted as borderline/supported. The preregistered hypotheses and thresholds were not changed after confirmatory outcomes existed.
2. **Same author.** The preregistration, code, analysis and audit were produced by one agent; the "independent" checks are second implementations by the same author, not an external audit. An external reviewer is still outstanding.
3. **No timestamps beyond git/shell dates.** The ordering proof is the commit date and shell timestamps on one machine; it is not a cryptographic timestamp. The commit was pushed (remote receipt) before analysis.
4. **Run-to-run reproducibility of the confirmatory run itself** (a second full execution) was not performed: the brief forbids a second confirmatory run. Determinism is supported by the unit test (identical outputs for identical stream keys) and by deterministic integer-keyed streams.
