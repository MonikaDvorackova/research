# OOL (out-of-language discovery) results — Phase 22

Protocol: `topics/bostrom-world-models/world-models-programme/23-...md` (commit bcf9c9c, before the runs). Experiments/analysis: docs 22, 24, 25. Development-stage evidence only.

Reproduce (eid venv = torch + pysindy 2.1.0 + pandas; eid-pysr venv = pysr 2.7.2 + Julia in `~/.venvs/eid-pysr`):
1. `scripts/ool_detectability.py results/ool_dev/detectability.json`
2. `scripts/ool_tune_base.py --out results/ool_dev/baseline_tuning.json` (tuning seeds 310-312)
3. `scripts/ool_run.py --split calib --ns 29000 --n 12 --variants L0_falsify --out results/ool_dev/calibration_ns29000.pkl`; `scripts/ool_mkcal.py in.pkl calibration_ns29000.json`
4. `scripts/ool_run.py --split dev --ns 30000 --n 10 --cal results/ool_dev/calibration_ns29000.json --out results/ool_dev/dev_ns30000.pkl`; `scripts/ool_run.py --split holdout --ns 31000 --n 10 ... holdout_ns31000.pkl`
5. PySR (eid-pysr python): `scripts/ool_pysr.py <run>.pkl <run>_pysr.pkl --workers 7` (3 instances hung Julia and are absent: dev thresh 0 and 3, holdout saw 9)
6. `scripts/ool_report.py --run ... --pysr ... --cal ... --out ...` ; `scripts/ool_stress.sh`, `scripts/ool_stress_report.py`
Files: `ool_dev/*_report.md` (all tables), `*_long.pkl` (per-instance rows), `stress_*_ns32000.pkl`, `calibration_ns29000.json` (thresholds), `baseline_tuning.json`. `MANIFEST_ool.sha256` lists hashes. Benchmark manifest sha256 f8a09dea01ca1d3807237bd4b041d8ab354c5a78378758a62cbaf40ccbced1d2.
Note: `results/ool_dev/baseline_tuning.log` is the log of the final tuning run; an earlier duplicated launch's output was overwritten.
