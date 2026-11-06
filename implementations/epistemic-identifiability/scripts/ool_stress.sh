#!/bin/bash
cd "$(dirname "$0")/.."
V=adapt_sweepB,all_sweepB,L0_sweepB,oracle_struct
F=sin,rectsq,leak,bilin,thresh
PY=~/.venvs/eid/bin/python
$PY scripts/ool_run.py --split dev --ns 32000 --n 6 --fams $F --Bs 8,12 --variants $V --workers 5 --cal results/ool_dev/calibration_ns29000.json --noise 1.0 --out results/ool_dev/stress_noise1_ns32000.pkl > results/ool_dev/stress_noise1.log 2>&1
$PY scripts/ool_run.py --split dev --ns 32000 --n 6 --fams $F --Bs 8,12 --variants $V --workers 5 --cal results/ool_dev/calibration_ns29000.json --noise 2.0 --out results/ool_dev/stress_noise2_ns32000.pkl > results/ool_dev/stress_noise2.log 2>&1
$PY scripts/ool_run.py --split dev --ns 32000 --n 6 --fams $F --Bs 8,12 --variants $V --workers 5 --cal results/ool_dev/calibration_ns29000.json --noise 3.0 --out results/ool_dev/stress_noise3_ns32000.pkl > results/ool_dev/stress_noise3.log 2>&1
$PY scripts/ool_run.py --split dev --ns 32000 --n 6 --fams $F --Bs 8,12 --variants $V --workers 5 --cal results/ool_dev/calibration_ns29000.json --nou2 --out results/ool_dev/stress_nou2_ns32000.pkl > results/ool_dev/stress_nou2.log 2>&1
