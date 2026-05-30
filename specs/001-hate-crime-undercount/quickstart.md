# Quickstart: Hate Crime Undercount Analysis

These steps validate the planned project from a fresh clone.

## 1. Create an environment

```bash
cd hate-crime-undercount
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## 2. Run the notebook end-to-end

```bash
jupyter nbconvert --to notebook --execute notebook.ipynb --output notebook.executed.ipynb
```

Expected generated files:

```text
data/processed/fbi_2013_summary.csv
data/processed/bjs_funnel.csv
data/processed/bias_breakdown.csv
figures/funnel.png
figures/bias_breakdown.png
```

## 3. Run validation tests

```bash
pytest
```

Expected checks:
- Required processed CSVs exist and match their schemas.
- Funnel values are exactly `204600`, `101900`, `45600`, `15200`, and `7500`.
- Bias breakdown percentages match the required NCVS/UCR pairs.
- Required figure files exist.
- Notebook execution succeeds from a clean kernel.

## 4. Review narrative outputs

Open `notebook.executed.ipynb` and confirm:
- Sections follow the requested story order.
- Funnel chart shows five descending steps with loss labels.
- Bias chart shows side-by-side NCVS/UCR bars for all five categories.
- Final writeup is under 500 words and includes the unit-comparison caveat.
