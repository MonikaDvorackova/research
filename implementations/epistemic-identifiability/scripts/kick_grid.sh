#!/bin/zsh
# Development grid for kick-world (determinism detection by learned world models). 3 concurrent jobs.
cd "$(dirname "$0")/.."; PY=$HOME/.venvs/eid/bin/python; R=results/kick_dev/runs
jobs=()
for n in 4 6 8 10 12 16; do for i in 0 1 2; do jobs+=("--kind lfsr --n $n --inst $i --H 128 --out $R/lfsr_n${n}_i${i}_H128"); done; done
for n in 6 8 10; do for i in 0 1; do jobs+=("--kind nlfsr --n $n --inst $i --H 128 --out $R/nlfsr_n${n}_i${i}_H128"); done; done
for i in 0 1 2; do jobs+=("--kind rand --n 0 --inst $i --H 128 --out $R/rand_i${i}_H128"); done
for n in 8 12; do jobs+=("--kind lfsr --n $n --inst 0 --H 32 --out $R/lfsr_n${n}_i0_H32"); done
printf '%s\n' "${jobs[@]}" | xargs -P 3 -I{} zsh -c "PYTHONPATH=src $PY scripts/kick_run.py --steps 4000 {} --threads 3 >> $R/grid.stdout 2>&1"
