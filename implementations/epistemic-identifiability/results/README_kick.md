# kick-world / reassessment results — development only
* `kick_dev/runs/*/result.json` (29 runs; per-checkpoint detection curves, cross-environment validity, extraction/verification, replay), `kick_dev/kick_main_summary.txt`, `kick_dev/window_control.json` (P5 finite-context control).
* `kick_long/runs/*` 20,000-step follow-ups (n=8,10,12; instance 0).
* `gwb_dev/rssm_diag/` RSSM-vs-GRU controlled diagnostics (+ `summary.txt`).
* Reproduce: `scripts/kick_grid.sh` (≈45 min CPU), `scripts/kick_run.py --kind lfsr --n 8 --steps 20000 …`, `scripts/kick_window.py`, `scripts/gwb_rssm_diag.sh`, `scripts/kick_report.py results/kick_dev`.
* Interpretation: `topics/bostrom-world-models/world-models-programme/13`–`15`.
