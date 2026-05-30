# Implementation Plan: Hate Crime Undercount Analysis

**Branch**: `main` | **Date**: 2026-05-30 | **Spec**: [spec.md](spec.md)  
**Input**: Feature specification from `/specs/001-hate-crime-undercount/spec.md`

## Summary

Build a reproducible notebook-based data story comparing FBI UCR 2013 hate crime
statistics with BJS NCVS 2013 and 2013-2017 hate crime victimization estimates.
The implementation will fetch or include small raw FBI source CSVs, encode the
few required BJS briefing values as traceable source data, validate known anchor
values, write three processed CSVs, export two static figures, and render a
notebook narrative suitable for a 3-4 minute video story.

## Technical Context

**Language/Version**: Python 3.10+  
**Primary Dependencies**: pandas for wrangling, matplotlib for static charts, requests for source downloads, Jupyter/nbclient tooling for notebook execution validation  
**Storage**: Repository files only: `data/raw/`, `data/processed/`, `figures/`, and `notebook.ipynb`  
**Testing**: Notebook restart-and-run-all validation plus lightweight pytest checks for processed CSV schemas and anchor values  
**Target Platform**: Local developer environment from a fresh clone on macOS/Linux-compatible Python  
**Project Type**: Reproducible data-analysis notebook and static artifact package  
**Performance Goals**: Full analysis completes in under 2 minutes on a typical laptop after dependencies are installed  
**Constraints**: No manual downloads; no private credentials; raw data included if under 10 MB; all final numeric claims trace to processed data and cited sources; notebook top includes a package-version comment block  
**Scale/Scope**: Small public datasets for 2013 FBI UCR data and published BJS point estimates/percentages only; no trend analysis, microdata analysis, dashboard, or state-by-state breakdown

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Reproducibility**: PASS. The plan uses repository-local raw/processed data
  directories, automatic source downloads where needed, deterministic processed
  CSVs, static figures, and quickstart instructions for fresh-clone execution.
- **Source Provenance**: PASS. Source URLs and BJS PDF citations are represented
  in raw/source metadata and reflected in processed datasets and notebook text.
  Manually transcribed BJS values remain isolated and labeled.
- **Narrative Fit**: PASS. Outputs map directly to the two story questions:
  reporting funnel and bias-category comparison. No dashboard or unrelated
  exploration is included.
- **Validation and Caveats**: PASS. The notebook validates known FBI/BJS anchor
  values, required categories, descending funnel order, and artifact schemas;
  caveats are required near results and in the final writeup.
- **Minimal Scope**: PASS. Dependencies are limited to conventional notebook
  analysis tools and small test utilities. No additional data sources or models
  are introduced beyond the approved spec.

## Project Structure

### Documentation (this feature)

```text
specs/001-hate-crime-undercount/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── artifact-contracts.md
└── tasks.md
```

### Source Code (repository root)

```text
hate-crime-undercount/
├── notebook.ipynb
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   │   ├── fbi_2013_table1.csv
│   │   ├── fbi_2013_table4.csv
│   │   └── bjs_published_values.csv
│   └── processed/
│       ├── fbi_2013_summary.csv
│       ├── bjs_funnel.csv
│       └── bias_breakdown.csv
├── figures/
│   ├── funnel.png
│   └── bias_breakdown.png
└── tests/
    ├── test_processed_outputs.py
    └── test_notebook_execution.py
```

**Structure Decision**: Use a single self-contained analysis directory named
`hate-crime-undercount/` to match the requested project structure while keeping
Spec Kit planning artifacts under `specs/001-hate-crime-undercount/`.

## Phase 0: Research Decisions

Research decisions are captured in [research.md](research.md). All technical
unknowns are resolved: static plotting with matplotlib, file-based data
contracts, small raw data committed when under 10 MB, notebook execution
validation with nbclient-compatible tooling, and explicit handling of unavailable
BJS confidence interval bounds.

## Phase 1: Design Artifacts

- Data model: [data-model.md](data-model.md)
- Artifact contracts: [contracts/artifact-contracts.md](contracts/artifact-contracts.md)
- Quickstart: [quickstart.md](quickstart.md)
- Agent context: [../../AGENTS.md](../../AGENTS.md)

## Post-Design Constitution Check

- **Reproducibility**: PASS. The quickstart defines fresh-clone setup and
  notebook execution; contracts define required generated files.
- **Source Provenance**: PASS. The data model includes source citation fields
  and source-note handling for manually transcribed BJS values.
- **Narrative Fit**: PASS. The data model and figure contracts are limited to
  the headline funnel, bias breakdown, summary table, and caveats.
- **Validation and Caveats**: PASS. Contracts specify anchor values, schema
  checks, missing-CI behavior, and required caveat coverage.
- **Minimal Scope**: PASS. No external service interface or dashboard is planned.

## Complexity Tracking

No constitution violations.
