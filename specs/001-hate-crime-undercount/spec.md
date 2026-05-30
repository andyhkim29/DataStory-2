# Feature Specification: Hate Crime Undercount Analysis

**Feature Branch**: `001-hate-crime-undercount`  
**Created**: 2026-05-30  
**Status**: Draft  
**Input**: User description: "A reproducible data analysis comparing two federal sources of hate crime statistics: the FBI's Uniform Crime Reporting Program for 2013, and the Bureau of Justice Statistics' National Crime Victimization Survey for 2013 and the 2013-2017 average. The analysis quantifies the gap between FBI-reported hate crimes and BJS-estimated hate crime victimizations, and shows where in the reporting pipeline incidents are lost. The output supports a 3-4 minute video data story."

## Clarifications

### Session 2026-05-30

- Q: How should the analysis handle BJS 95% confidence interval bounds when the brief gives point estimates but not the bounds? -> A: Extract or transcribe 95% CI bounds from the cited BJS PDF where available; leave unavailable bounds blank with a note.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Reproduce the Headline Funnel (Priority: P1)

A data storyteller can run the project from a fresh clone and produce a five-step funnel showing how annual estimated hate crime victimizations narrow from the BJS 2013-2017 annual average to the FBI-published count.

**Why this priority**: The funnel is the headline visual and directly answers the primary question: what fraction of estimated victimizations reaches the FBI's published statistics, and where are incidents lost?

**Independent Test**: Can be tested by running the analysis from a clean checkout and confirming that the processed funnel data and exported funnel chart contain five descending steps with loss labels between adjacent steps.

**Acceptance Scenarios**:

1. **Given** a fresh clone with no manual downloads, **When** the analysis is run end-to-end, **Then** it creates a processed funnel dataset and an exported funnel chart.
2. **Given** the funnel chart, **When** a reviewer reads it, **Then** the chart shows all five values in descending order: 204,600, 101,900, 45,600, 15,200, and 7,500.
3. **Given** adjacent funnel steps, **When** a reviewer inspects the labels, **Then** each transition explicitly states the amount or share lost between those steps.
4. **Given** the cited BJS PDF provides uncertainty information for a step, **When** the funnel chart is rendered, **Then** the chart displays the verified 95% confidence interval bounds for that step and documents any unavailable bounds.

---

### User Story 2 - Compare Bias Categories Across Sources (Priority: P2)

A data storyteller can compare BJS NCVS and FBI UCR bias-motivation shares for race or ethnicity, religion, sexual orientation, gender, and disability, with the gender and disability disparities easy to see.

**Why this priority**: The second core question asks where the two sources agree and where FBI-reported statistics undercount most severely by motivation type.

**Independent Test**: Can be tested by reviewing the processed bias breakdown dataset and exported bias chart for all five requested categories, with side-by-side source values.

**Acceptance Scenarios**:

1. **Given** the processed bias breakdown dataset, **When** a reviewer checks each row, **Then** it includes both NCVS and UCR percentages for each of the five requested bias types.
2. **Given** the bias breakdown chart, **When** a reviewer compares paired values, **Then** it shows race or ethnicity at 57% versus 60%, religion at 8% versus 19%, gender at 27% versus 2%, sexual orientation at 26% versus 18%, and disability at 16% versus 1%.
3. **Given** the gender and disability categories, **When** the chart is viewed in the notebook or as an exported figure, **Then** the NCVS-versus-UCR gaps are visually obvious without requiring the reviewer to inspect raw data values.

---

### User Story 3 - Trace Findings to Source Data (Priority: P3)

A reviewer can trace every key number in the notebook narrative and final writeup back to a processed data file and cited federal source or source mirror.

**Why this priority**: The analysis supports a public-facing data story, so reproducibility, source traceability, and methodological caveats are required for credibility.

**Independent Test**: Can be tested by reading the notebook, processed CSVs, and final writeup and verifying that every quoted number appears in a data file and has a source citation.

**Acceptance Scenarios**:

1. **Given** the rendered summary table, **When** a reviewer checks the key values, **Then** the table includes the FBI 2013 values, the 2013 NCVS estimate, and the 2013-2017 annual-average funnel values.
2. **Given** the final notebook writeup, **When** a reviewer reads it, **Then** it is under 500 words and explicitly states that NCVS victimizations and FBI incidents or victims are not strictly the same unit.
3. **Given** the notebook caveats section, **When** a reviewer checks for methodological notes, **Then** it covers NCVS household and age coverage, FBI voluntary law-enforcement reporting, missing jurisdictions, and the distinction between victimizations, incidents, and victims.

---

### User Story 4 - Package the Analysis for a Short Video Story (Priority: P4)

A producer can use the notebook, exported figures, and concise findings to support a 3-4 minute video data story without additional data wrangling.

**Why this priority**: The deliverable is not only analysis, but an analysis package structured for a short narrative.

**Independent Test**: Can be tested by reviewing the project directory for the requested notebook, processed data, figures, and README and confirming that the notebook sections follow the requested narrative order.

**Acceptance Scenarios**:

1. **Given** the completed project, **When** a reviewer opens the notebook, **Then** sections appear in this order: the two sources, loading and validation, the funnel, the bias breakdown, findings and caveats.
2. **Given** the project README, **When** a reviewer reads it, **Then** it contains a one-paragraph description and clear run instructions.
3. **Given** the exported figures, **When** a video producer imports them into an editing workflow, **Then** the funnel and bias breakdown visuals are available as static image files with readable labels.

### Edge Cases

- Source downloads from the FBI mirror are unavailable or return an unexpected status.
- FBI source tables contain changed columns, renamed bias categories, or additional categories beyond the required summary.
- BJS values that are transcribed from PDFs do not have available 95% confidence interval bounds for every funnel step.
- Percentages by bias type can overlap because incidents or victimizations may involve more than one bias motivation; totals should not be forced to 100%.
- The FBI and NCVS units differ, so comparisons must avoid presenting victimizations and incidents as identical measures.
- Total raw data size exceeds the intended repository threshold.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The project MUST provide a reproducible analysis that runs end-to-end from a fresh clone without manual file downloads.
- **FR-002**: The analysis MUST compare the FBI UCR 2013 hate crime statistics with BJS NCVS hate crime victimization estimates for 2013 and the 2013-2017 annual average.
- **FR-003**: The analysis MUST use FBI Hate Crime Statistics 2013 source tables from the public GitHub mirror, including Table 1 for incidents, offenses, victims, and offenders by bias motivation and Table 4 for offenses by type and bias.
- **FR-004**: The analysis MUST use the BJS Hate Crime Victimization, 2013-2017 briefing values supplied in the feature brief, including the annual-average funnel, the 2013-specific NCVS estimate, and the NCVS-versus-UCR bias percentages.
- **FR-005**: The project MUST include source files directly when total data size is under 10 MB; otherwise, it MUST retrieve source data automatically on first run.
- **FR-006**: The project MUST produce `data/processed/fbi_2013_summary.csv` with incidents, offenses, and victims by bias category for 2013.
- **FR-007**: The project MUST produce `data/processed/bjs_funnel.csv` with the five funnel steps, values, and 95% confidence interval bounds extracted or transcribed from the cited BJS PDF where available; unavailable bounds MUST be left blank and documented.
- **FR-008**: The project MUST produce `data/processed/bias_breakdown.csv` with NCVS and UCR percentages by bias type for race or ethnicity, religion, gender, sexual orientation, and disability.
- **FR-009**: The project MUST produce a headline funnel figure in `figures/` showing five descending bars from approximately 205,000 to 7,500, with labels describing the losses between steps.
- **FR-010**: The project MUST produce a bias breakdown figure in `figures/` showing both NCVS and UCR values side by side for all five required bias categories.
- **FR-011**: The notebook MUST render a summary table containing the key values from both sources, including the 2013 NCVS estimate of 254,900 total victimizations, 88,400 reported to police, and 154,300 not reported.
- **FR-012**: Every notebook section MUST open with narrative markdown explaining what the section does and why it matters.
- **FR-013**: The notebook MUST follow this narrative order: the two sources; loading and validation; the funnel; the bias breakdown; findings and caveats.
- **FR-014**: The notebook MUST include a final markdown writeup under 500 words summarizing findings and caveats.
- **FR-015**: The notebook MUST explicitly state that NCVS counts victimizations while FBI data counts incidents and victims as classified by police, and that these are not strictly the same unit.
- **FR-016**: The notebook MUST state that NCVS surveys people age 12 and older living in households only, while FBI data can include crimes against businesses and organizations.
- **FR-017**: The notebook MUST state that FBI hate crime data is voluntarily reported by law enforcement and that many jurisdictions are missing entirely.
- **FR-018**: All key numbers in the final writeup MUST be traceable to a processed data file and a cited source.
- **FR-019**: The project MUST include a README with a one-paragraph project description and run instructions.

### Key Entities

- **FBI Bias Summary**: A 2013 source-derived summary of FBI-reported hate crime incidents, offenses, and victims by bias category.
- **BJS Funnel Step**: One stage in the BJS reporting pipeline, with label, value, order, and optional 95% confidence interval bounds.
- **Bias Breakdown Category**: A motivation category used to compare NCVS and UCR percentages: race or ethnicity, religion, gender, sexual orientation, or disability.
- **Source Citation**: A reference linking a processed value or narrative claim to its source table, briefing PDF, or source mirror.
- **Exported Figure**: A static visual artifact used by the notebook and the 3-4 minute video story.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A reviewer can run the complete analysis from a fresh clone in one pass without manual data downloads or manual data edits.
- **SC-002**: The project creates all three required processed CSVs and both required figure files in the specified directories.
- **SC-003**: The funnel figure contains exactly five ordered steps and correctly shows the 204,600-to-7,500 decline from the BJS annual-average estimate to the FBI-published count.
- **SC-004**: The bias breakdown figure shows both sources for all five required categories, and a reviewer can identify the gender and disability disparities in under 10 seconds.
- **SC-005**: The final writeup is under 500 words and includes all required methodological caveats.
- **SC-006**: Every numeric claim in the final writeup can be matched to a row in a processed CSV and to a cited source.
- **SC-007**: The analysis package supports a 3-4 minute story arc covering source differences, the reporting funnel, category disparities, and caveats.

## Assumptions

- The primary audience is a data-story producer or reviewer who needs a concise, reproducible analysis package rather than an interactive dashboard.
- The project focuses only on 2013 FBI UCR data, the 2013 NCVS estimate, and 2013-2017 NCVS annual-average values; trend analysis and state-by-state analysis are out of scope.
- The BJS values provided in the feature brief are authoritative transcriptions for the required analysis values, with source citations pointing to the BJS briefing PDF.
- If confidence interval bounds cannot be verified in the cited BJS PDF for a BJS funnel step, the processed funnel file may leave those bounds empty while documenting that they are unavailable.
- The comparison by bias type uses percentages from the BJS 2013-2017 briefing and should be interpreted as a source-comparison snapshot, not as a complete accounting of all motivations.
- The notebook template style should follow the storytelling-with-data demo structure while adapting section titles and outputs to this project.
