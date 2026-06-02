# Hate Crime Undercount

## Project Information

**Project name:** Hate Crime Undercount  
**Author:** Andy Kim  
**GitHub username:** [andyhkim29](https://github.com/andyhkim29)  
**Repository:** [andyhkim29/DataStory-2](https://github.com/andyhkim29/DataStory-2)

## Overview

This project asks: how much larger are hate crime victimization estimates from the Bureau of Justice Statistics' National Crime Victimization Survey than the hate crime counts published through the FBI's Uniform Crime Reporting Program, and where do cases drop out of the reporting pipeline? The analysis uses a reproducible Jupyter notebook to compare FBI UCR 2013 hate crime statistics with BJS NCVS estimates for 2013 and the 2013-2017 annual average. It builds a five-step reporting funnel, compares bias-motivation shares across federal data systems, exports static charts, and documents the caveats needed for a short data story.

**Approach:** The notebook loads small committed source CSVs, validates anchor values, creates processed datasets, and exports figures for the story. It treats NCVS and UCR as different measurement systems rather than exact one-to-one counts.

**Data used:** FBI Hate Crime Statistics 2013 Table 1 and Table 4, plus published BJS NCVS values from *Hate Crime Victimization, 2013-2017*.

**Tools used:** Python 3.10+, pandas, matplotlib, requests, Jupyter, nbconvert, nbclient, and pytest.

**Key findings:** BJS estimates 204,600 average annual hate crime victimizations in 2013-2017, while the UCR endpoint is about 7,500 hate crime victims, roughly 3.7% of the starting NCVS estimate. About half of estimated victimizations are reported to police, and far fewer are identified as hate crimes by victims or confirmed by police. Race or ethnicity shares are similar across sources, but gender and disability bias appear much more prominently in NCVS than in UCR.

## YouTube Link

5-minute data story video: <https://youtu.be/fMA7S3op0So>

## Data Links

The analyzed source files are included in [`hate-crime-undercount/data/raw/`](hate-crime-undercount/data/raw/) so the project can run without manual downloads.

- BJS briefing PDF: <https://bjs.ojp.gov/content/pub/pdf/hcs1317pp.pdf>
- FBI Hate Crime Statistics 2013 Table 1: <https://ucr.fbi.gov/hate-crime/2013/tables/1tabledatadecpdf>
- FBI Hate Crime Statistics 2013 Table 4: <https://ucr.fbi.gov/hate-crime/2013/tables/4tabledatadecpdf>
- Processed outputs: [`hate-crime-undercount/data/processed/`](hate-crime-undercount/data/processed/)
- Exported figures: [`hate-crime-undercount/figures/`](hate-crime-undercount/figures/)

## Running the Code

From a fresh clone, run:

```bash
cd hate-crime-undercount
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
jupyter nbconvert --to notebook --execute notebook.ipynb --output notebook.executed.ipynb
pytest
```

Expected generated or validated outputs:

```text
data/processed/fbi_2013_summary.csv
data/processed/bjs_funnel.csv
data/processed/bias_breakdown.csv
figures/funnel.png
figures/bias_breakdown.png
notebook.executed.ipynb
```

Open `hate-crime-undercount/notebook.executed.ipynb` to review the fully executed notebook narrative, summary table, charts, findings, and caveats.

## Contributing

Potential next steps:

- Add a carefully scoped year-to-year comparison once comparable NCVS and UCR values are available.
- Expand the caveats section with more detail about jurisdiction participation and UCR reporting coverage.
- Add clearer uncertainty visualization for every NCVS estimate where confidence intervals are available.
- Consider state-level or agency-level analysis, while keeping it separate from this national comparison.

Open questions and known issues:

- NCVS victimizations and FBI UCR incidents or victims are not identical units, so the funnel is a system comparison rather than a precise conversion rate.
- NCVS covers people age 12 or older in households; it does not cover businesses, organizations, institutions, or people outside household settings.
- FBI hate crime reporting is voluntary, and some jurisdictions report no hate crimes or do not participate fully.
- Bias categories can overlap, so category percentages should not be forced to sum to 100%.

## Acknowledgements and Citations

This project relies on public data from the Bureau of Justice Statistics and the FBI Uniform Crime Reporting Program.

- Bureau of Justice Statistics. *Hate Crime Victimization, 2013-2017*. <https://bjs.ojp.gov/content/pub/pdf/hcs1317pp.pdf>
- Federal Bureau of Investigation. *Hate Crime Statistics, 2013: Table 1*. <https://ucr.fbi.gov/hate-crime/2013/tables/1tabledatadecpdf>
- Federal Bureau of Investigation. *Hate Crime Statistics, 2013: Table 4*. <https://ucr.fbi.gov/hate-crime/2013/tables/4tabledatadecpdf>

