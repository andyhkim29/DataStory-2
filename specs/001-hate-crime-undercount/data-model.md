# Data Model: Hate Crime Undercount Analysis

## Entity: Raw FBI Table

Represents a downloaded or committed FBI 2013 source CSV.

Fields:
- `source_name`: Human-readable source label, such as `FBI Hate Crime Statistics 2013 Table 1`.
- `source_url`: Raw URL used for retrieval.
- `local_path`: Repository path under `hate-crime-undercount/data/raw/`.
- `retrieved_at`: Date the file was downloaded or verified.
- `table_id`: FBI table identifier, such as `table1` or `table4`.

Validation rules:
- Required FBI raw files must exist before processing.
- Table 1 must contain the bias motivation rows needed for incidents, offenses,
  and victims by category.
- Table 4 must be available for source completeness and offense-by-bias context.

## Entity: FBI Bias Summary

Processed summary of FBI 2013 hate crime counts by bias category.

Fields:
- `year`: `2013`.
- `bias_category`: Canonical category name.
- `incidents`: FBI-reported incident count.
- `offenses`: FBI-reported offense count.
- `victims`: FBI-reported victim count.
- `source_table`: FBI source table identifier.
- `source_url`: Source URL or citation.

Validation rules:
- Must include bias categories needed for the comparison narrative.
- Numeric count fields must be non-negative integers.
- Known aggregate values used in notebook findings must match the source data.

## Entity: BJS Published Value

Raw, traceable transcription of a published BJS point estimate, percentage, or
confidence interval bound.

Fields:
- `source_name`: BJS report or briefing title.
- `source_url`: BJS PDF URL.
- `source_note`: Page, table, figure, or text note identifying where the value appears.
- `series`: `funnel`, `2013_specific`, or `bias_breakdown`.
- `measure`: Human-readable measure name.
- `value`: Numeric value.
- `unit`: `victimizations`, `percentage`, or other explicit unit.
- `ci_low`: Lower 95% confidence interval bound when verified; blank otherwise.
- `ci_high`: Upper 95% confidence interval bound when verified; blank otherwise.
- `ci_note`: Note explaining verified or unavailable CI bounds.

Validation rules:
- Required point estimates from the spec must be present.
- CI bounds may be blank only when `ci_note` documents that they were not
  verified in the cited BJS PDF.
- Percentage values may overlap and must not be forced to sum to 100%.

## Entity: BJS Funnel Step

Processed five-step annual-average reporting funnel.

Fields:
- `step_order`: Integer from 1 to 5.
- `step_label`: Narrative label for the funnel stage.
- `value`: Estimated count for the stage.
- `unit`: `victimizations`, `reported_to_police`, `confirmed_by_police`, or another explicit stage unit.
- `ci_low`: Lower 95% confidence interval bound when verified.
- `ci_high`: Upper 95% confidence interval bound when verified.
- `loss_from_previous`: Difference from the previous step; blank for step 1.
- `loss_percent_from_previous`: Percentage loss from the previous step; blank for step 1.
- `source_url`: BJS PDF URL.
- `source_note`: Page, figure, table, or note.
- `ci_note`: Confidence interval source or unavailability note.

Validation rules:
- Must contain exactly five rows.
- `step_order` must be unique and ordered from 1 to 5.
- Values must match 204600, 101900, 45600, 15200, and 7500.
- Values must be descending.

## Entity: Bias Breakdown Category

Processed comparison of NCVS and UCR bias-motivation percentages.

Fields:
- `bias_type`: One of `race_or_ethnicity`, `religion`, `gender`, `sexual_orientation`, `disability`.
- `display_label`: Label used in figures and tables.
- `ncvs_percent`: NCVS 2013-2017 annual-average percentage.
- `ucr_percent`: UCR 2013-2017 annual-average percentage.
- `gap_percentage_points`: `ncvs_percent - ucr_percent`.
- `source_url`: BJS PDF URL.
- `source_note`: Page, figure, table, or note.

Validation rules:
- Must contain exactly five rows, one per required category.
- Percent values must match 57/60, 8/19, 27/2, 26/18, and 16/1 for NCVS/UCR.
- Percentages can overlap; the dataset must not include a total-row check that
  requires sums to equal 100%.

## Entity: Exported Figure

Static visual output for the video story and notebook.

Fields:
- `figure_name`: `funnel` or `bias_breakdown`.
- `path`: Repository path under `hate-crime-undercount/figures/`.
- `source_dataset`: Processed CSV used to generate the figure.
- `required_labels`: Labels that must be visible in the exported figure.

Validation rules:
- Required figure files must exist after notebook execution.
- Funnel figure must show five descending bars and loss labels between steps.
- Bias breakdown figure must show paired NCVS/UCR values for all five categories.
