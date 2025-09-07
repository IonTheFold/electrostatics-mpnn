# IonTheFold

Electrostatically aware ProteinMPNN enhancements for charged protein–protein interfaces.
This repository contains notebooks, minimal utilities, and scripts to reproduce core experiments.

## Structure
```
IonTheFold/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ environment.yml
├─ Makefile
├─ notebooks/
├─ src/ionthefold/
├─ scripts/
├─ configs/
├─ data/
├─ results/
└─ docs/
```

## Quickstart
```bash
# create and activate env (conda/mamba)
mamba env create -f environment.yml || conda env create -f environment.yml
conda activate ionthefold

# run a quick smoke test
make test
```

## Notes
- Notebooks are numbered to reflect workflow order.
- `src/ionthefold` holds light-weight, testable helpers (stubs OK to start).
- APBS integration is optional initially; see `src/ionthefold/apbs.py`.
