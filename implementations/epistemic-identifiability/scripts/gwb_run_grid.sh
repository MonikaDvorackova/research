#!/bin/zsh
# Final development grid: 2 archs x {pred, ICI(lam=1)} x seeds 1..3 (+ family holdouts, untrained controls). Max 4 concurrent jobs.
cd "$(dirname "$0")/.."
PY=${PY:-$HOME/.venvs/eid/bin/python}; R=results/gwb_final/runs
jobs=()
for s in 1 2 3; do for m in rssm det; do for lam in 0 1.0; do
  n=${m}_$([ "$lam" = "0" ] && echo pred || echo ici)_s$s
  jobs+=("--model $m --lam $lam --seed $s --out $R/$n")
done; done; done
for fam in A B; do for lam in 0 1.0; do
  n=det_$([ "$lam" = "0" ] && echo pred || echo ici)_only${fam}_s1
  jobs+=("--model det --lam $lam --seed 1 --family $fam --out $R/$n")
done; done
jobs+=("--model det --steps 0 --seed 1 --out $R/det_untrained_s1" "--model rssm --steps 0 --seed 1 --out $R/rssm_untrained_s1")
printf '%s\n' "${jobs[@]}" | xargs -P 4 -I{} zsh -c "PYTHONPATH=src $PY -m eid.gwb.train --steps 3000 {} --budget_s 1800 --threads 3 >> $R/grid.stdout 2>&1"
