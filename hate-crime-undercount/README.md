# Hate Crime Undercount

A reproducible data analysis comparing FBI UCR 2013 hate crime statistics with BJS NCVS hate crime victimization estimates for 2013 and the 2013-2017 annual average. The notebook builds a reporting funnel from estimated victimizations to FBI-published victims, compares NCVS and UCR bias-motivation shares, exports static figures for a 3-4 minute video story, and documents the unit and source caveats behind the comparison.

## Run

```bash
cd hate-crime-undercount
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
jupyter nbconvert --to notebook --execute notebook.ipynb --output notebook.executed.ipynb
pytest
```

Expected outputs:

```text
data/processed/fbi_2013_summary.csv
data/processed/bjs_funnel.csv
data/processed/bias_breakdown.csv
figures/funnel.png
figures/bias_breakdown.png
```

Raw source files are included because the required data is well under 10 MB. The notebook also records the official FBI and BJS source URLs for traceability.
