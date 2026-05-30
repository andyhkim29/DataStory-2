# Artifact Contracts: Hate Crime Undercount Analysis

This project has no web API or external service interface. Its public contract
is the set of files produced by the notebook.

## Required Processed CSVs

### `hate-crime-undercount/data/processed/fbi_2013_summary.csv`

Required columns:
- `year`
- `bias_category`
- `incidents`
- `offenses`
- `victims`
- `source_table`
- `source_url`

Rules:
- `year` is `2013` for all rows.
- Count columns are non-negative integers.
- Values used in notebook findings must be present in this file.

### `hate-crime-undercount/data/processed/bjs_funnel.csv`

Required columns:
- `step_order`
- `step_label`
- `value`
- `unit`
- `ci_low`
- `ci_high`
- `loss_from_previous`
- `loss_percent_from_previous`
- `source_url`
- `source_note`
- `ci_note`

Rules:
- Exactly five rows.
- `value` sequence is `204600`, `101900`, `45600`, `15200`, `7500`.
- Values are descending by `step_order`.
- `ci_low` and `ci_high` are populated only when verified in the cited BJS PDF.
- Blank CI bounds require a non-empty `ci_note`.

### `hate-crime-undercount/data/processed/bias_breakdown.csv`

Required columns:
- `bias_type`
- `display_label`
- `ncvs_percent`
- `ucr_percent`
- `gap_percentage_points`
- `source_url`
- `source_note`

Rules:
- Exactly five rows.
- Required `bias_type` values: `race_or_ethnicity`, `religion`, `gender`,
  `sexual_orientation`, `disability`.
- Required NCVS/UCR pairs: `57/60`, `8/19`, `27/2`, `26/18`, `16/1`.
- Percentages are allowed to overlap and are not summed to 100%.

## Required Figures

### `hate-crime-undercount/figures/funnel.png`

Rules:
- Static image generated from `bjs_funnel.csv`.
- Shows five descending bars in order.
- Labels each stage value.
- Labels loss between adjacent stages.
- Shows 95% confidence interval bounds where available and documents unavailable
  bounds in the notebook.

### `hate-crime-undercount/figures/bias_breakdown.png`

Rules:
- Static image generated from `bias_breakdown.csv`.
- Shows paired NCVS and UCR bars for all five bias types.
- Makes gender and disability gaps visually obvious.
- Uses readable labels suitable for notebook display and video editing.

## Required Narrative Files

### `hate-crime-undercount/notebook.ipynb`

Rules:
- Runs from a restarted kernel without manual intervention.
- Sections appear in this order: the two sources, loading and validation, the
  funnel, the bias breakdown, findings and caveats.
- Top comment block lists pinned package versions.
- Final writeup is under 500 words and includes required caveats.

### `hate-crime-undercount/README.md`

Rules:
- Includes a one-paragraph project description.
- Includes setup and run instructions for a fresh clone.
