# Tasks: Hate Crime Undercount Analysis

**Input**: Design documents from `/specs/001-hate-crime-undercount/`  
**Prerequisites**: [plan.md](plan.md), [spec.md](spec.md), [research.md](research.md), [data-model.md](data-model.md), [contracts/artifact-contracts.md](contracts/artifact-contracts.md), [quickstart.md](quickstart.md)

**Tests**: Included because the implementation plan requires notebook execution validation plus processed CSV schema and anchor-value checks.

**Organization**: Tasks are grouped by user story so each story can be implemented and tested independently.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel because it touches different files and has no dependency on incomplete tasks.
- **[Story]**: Which user story this task belongs to, used only in user-story phases.
- Every task includes an exact file path.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the requested project skeleton and dependency manifest.

- [x] T001 Create `hate-crime-undercount/` project directory structure with `data/raw/`, `data/processed/`, `figures/`, and `tests/`
- [x] T002 Create `hate-crime-undercount/requirements.txt` with pinned package versions for pandas, matplotlib, requests, jupyter, nbconvert, nbclient, ipykernel, and pytest
- [x] T003 Create placeholder `hate-crime-undercount/notebook.ipynb` with top package-version comment block and the required narrative section headings
- [x] T004 Create initial `hate-crime-undercount/README.md` with one-paragraph project description and quickstart run commands

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Establish shared source data, constants, and validation scaffolding needed by every user story.

**CRITICAL**: No user story work can begin until this phase is complete.

- [x] T005 Add FBI source metadata and download URLs for Table 1 and Table 4 in `hate-crime-undercount/notebook.ipynb`
- [x] T006 Add BJS source metadata, supplied 2013 values, 2013-2017 funnel values, and bias percentages in `hate-crime-undercount/data/raw/bjs_published_values.csv`
- [x] T007 Add reusable notebook helper cells for creating directories, fetching missing FBI raw CSVs, and saving outputs in `hate-crime-undercount/notebook.ipynb`
- [x] T008 Add shared validation helpers for required columns, non-negative numeric values, expected categories, and anchor values in `hate-crime-undercount/notebook.ipynb`
- [x] T009 Create pytest fixture utilities for locating project artifacts in `hate-crime-undercount/tests/conftest.py`

**Checkpoint**: Foundation ready; each user-story phase can use the same source metadata, raw value file, and validation helpers.

---

## Phase 3: User Story 1 - Reproduce the Headline Funnel (Priority: P1)

**Goal**: Produce the five-step BJS reporting funnel data and headline static funnel chart.

**Independent Test**: Run the notebook through the funnel section and confirm `bjs_funnel.csv` plus `figures/funnel.png` exist, contain five descending steps, and label losses between adjacent steps.

### Tests for User Story 1

- [x] T010 [P] [US1] Add processed funnel schema and anchor-value tests in `hate-crime-undercount/tests/test_processed_outputs.py`
- [x] T011 [P] [US1] Add figure existence test for `figures/funnel.png` in `hate-crime-undercount/tests/test_processed_outputs.py`

### Implementation for User Story 1

- [x] T012 [US1] Implement BJS funnel DataFrame construction from `data/raw/bjs_published_values.csv` in `hate-crime-undercount/notebook.ipynb`
- [x] T013 [US1] Calculate `loss_from_previous` and `loss_percent_from_previous` for all funnel transitions in `hate-crime-undercount/notebook.ipynb`
- [x] T014 [US1] Validate five-step descending order and required values `204600`, `101900`, `45600`, `15200`, and `7500` in `hate-crime-undercount/notebook.ipynb`
- [x] T015 [US1] Write `hate-crime-undercount/data/processed/bjs_funnel.csv` from the notebook
- [x] T016 [US1] Generate `hate-crime-undercount/figures/funnel.png` with five descending bars, stage labels, loss labels, and verified CI bounds where available
- [x] T017 [US1] Add funnel narrative markdown explaining source units, reporting-pipeline loss, CI handling, and missing-bound notes in `hate-crime-undercount/notebook.ipynb`

**Checkpoint**: User Story 1 is complete when the funnel CSV, funnel chart, and US1 tests pass independently.

---

## Phase 4: User Story 2 - Compare Bias Categories Across Sources (Priority: P2)

**Goal**: Produce the NCVS-versus-UCR bias breakdown data and paired-bar static chart for all five required categories.

**Independent Test**: Run the notebook through the bias breakdown section and confirm `bias_breakdown.csv` plus `figures/bias_breakdown.png` show all five paired categories with the required percentages.

### Tests for User Story 2

- [x] T018 [P] [US2] Add bias breakdown schema, category, and required percentage tests in `hate-crime-undercount/tests/test_processed_outputs.py`
- [x] T019 [P] [US2] Add figure existence test for `figures/bias_breakdown.png` in `hate-crime-undercount/tests/test_processed_outputs.py`

### Implementation for User Story 2

- [x] T020 [US2] Implement bias breakdown DataFrame construction from `data/raw/bjs_published_values.csv` in `hate-crime-undercount/notebook.ipynb`
- [x] T021 [US2] Calculate `gap_percentage_points` for each bias category in `hate-crime-undercount/notebook.ipynb`
- [x] T022 [US2] Validate required NCVS/UCR pairs `57/60`, `8/19`, `27/2`, `26/18`, and `16/1` in `hate-crime-undercount/notebook.ipynb`
- [x] T023 [US2] Write `hate-crime-undercount/data/processed/bias_breakdown.csv` from the notebook
- [x] T024 [US2] Generate `hate-crime-undercount/figures/bias_breakdown.png` with paired NCVS/UCR bars for all five categories
- [x] T025 [US2] Add bias breakdown narrative markdown emphasizing gender and disability disparities without forcing percentages to sum to 100 in `hate-crime-undercount/notebook.ipynb`

**Checkpoint**: User Story 2 is complete when the bias CSV, bias chart, and US2 tests pass independently.

---

## Phase 5: User Story 3 - Trace Findings to Source Data (Priority: P3)

**Goal**: Produce source-traceable FBI summary data, summary table, and final caveated writeup.

**Independent Test**: Review the notebook, processed CSVs, and final writeup to verify that each key number appears in a processed file and cites its FBI or BJS source.

### Tests for User Story 3

- [x] T026 [P] [US3] Add FBI summary schema and non-negative count tests in `hate-crime-undercount/tests/test_processed_outputs.py`
- [x] T027 [P] [US3] Add source citation non-empty tests for all processed CSVs in `hate-crime-undercount/tests/test_processed_outputs.py`

### Implementation for User Story 3

- [x] T028 [US3] Fetch or load FBI Table 1 and Table 4 raw CSVs into `hate-crime-undercount/data/raw/` from `hate-crime-undercount/notebook.ipynb`
- [x] T029 [US3] Transform FBI Table 1 into canonical 2013 bias summary rows in `hate-crime-undercount/notebook.ipynb`
- [x] T030 [US3] Validate FBI summary categories, numeric count fields, and source table references in `hate-crime-undercount/notebook.ipynb`
- [x] T031 [US3] Write `hate-crime-undercount/data/processed/fbi_2013_summary.csv` from the notebook
- [x] T032 [US3] Render a notebook summary table with FBI 2013 values, NCVS 2013 estimate `254900`, police-reported `88400`, not-reported `154300`, and 2013-2017 funnel values in `hate-crime-undercount/notebook.ipynb`
- [x] T033 [US3] Add final under-500-word findings and caveats writeup with unit-comparison, NCVS coverage, FBI voluntary-reporting, missing-jurisdiction, and CI caveats in `hate-crime-undercount/notebook.ipynb`

**Checkpoint**: User Story 3 is complete when the FBI summary CSV, summary table, traceability checks, and final writeup are present.

---

## Phase 6: User Story 4 - Package the Analysis for a Short Video Story (Priority: P4)

**Goal**: Make the notebook, figures, README, and run workflow usable as a compact 3-4 minute video-story package.

**Independent Test**: From the project directory, run the documented commands, open the executed notebook, and confirm the narrative order plus exported static visuals.

### Tests for User Story 4

- [x] T034 [P] [US4] Add notebook execution test using nbconvert or nbclient in `hate-crime-undercount/tests/test_notebook_execution.py`
- [x] T035 [P] [US4] Add README command smoke-check expectations in `hate-crime-undercount/tests/test_processed_outputs.py`

### Implementation for User Story 4

- [x] T036 [US4] Finalize notebook section order as the two sources, loading and validation, the funnel, the bias breakdown, findings and caveats in `hate-crime-undercount/notebook.ipynb`
- [x] T037 [US4] Ensure figure sizing, labels, and exported PNG readability are suitable for notebook display and video editing in `hate-crime-undercount/notebook.ipynb`
- [x] T038 [US4] Update `hate-crime-undercount/README.md` with complete fresh-clone setup, execution, testing, and output-location instructions
- [x] T039 [US4] Run the notebook end-to-end and save final generated outputs in `hate-crime-undercount/data/processed/` and `hate-crime-undercount/figures/`

**Checkpoint**: User Story 4 is complete when the documented workflow produces the full package from a fresh clone.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final verification across all user stories and constitution gates.

- [x] T040 Run `pytest` from `hate-crime-undercount/` and fix any failures in `hate-crime-undercount/tests/`
- [x] T041 Run `jupyter nbconvert --to notebook --execute notebook.ipynb --output notebook.executed.ipynb` from `hate-crime-undercount/`
- [x] T042 Verify every final numeric claim in `hate-crime-undercount/notebook.ipynb` traces to a processed CSV row and cited source
- [x] T043 Verify required caveats appear near results and in the final findings section of `hate-crime-undercount/notebook.ipynb`
- [x] T044 Confirm generated raw data size is under 10 MB or document first-run fetch behavior in `hate-crime-undercount/README.md`
- [x] T045 Review `hate-crime-undercount/figures/funnel.png` and `hate-crime-undercount/figures/bias_breakdown.png` for readable labels and no visual overlap
- [x] T046 Remove or ignore transient execution artifacts such as `hate-crime-undercount/notebook.executed.ipynb` if they are not part of the committed deliverable

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup completion and blocks all user stories.
- **User Story 1 (Phase 3)**: Depends on Foundational phase.
- **User Story 2 (Phase 4)**: Depends on Foundational phase and can run after or alongside US1 once shared BJS raw values exist.
- **User Story 3 (Phase 5)**: Depends on Foundational phase and benefits from US1/US2 processed outputs for the summary table.
- **User Story 4 (Phase 6)**: Depends on US1, US2, and US3 outputs.
- **Polish (Phase 7)**: Depends on all desired user stories being complete.

### User Story Dependencies

- **US1**: Independent MVP; produces headline funnel.
- **US2**: Independent of US1 after foundational BJS raw values exist; produces bias comparison.
- **US3**: Integrates source traceability and summary table; depends on processed outputs from US1 and US2 for complete summary table.
- **US4**: Packaging story; depends on complete notebook, figures, and processed data.

### Within Each User Story

- Tests are written before implementation tasks where practical.
- Data construction precedes validation.
- Validation precedes writing processed CSVs.
- Processed CSVs precede figure generation.
- Narrative markdown is completed before story checkpoint review.

## Parallel Opportunities

- T002, T003, and T004 can be worked after T001 by separate contributors.
- T010 and T011 can run in parallel before US1 implementation.
- T018 and T019 can run in parallel before US2 implementation.
- T026 and T027 can run in parallel before US3 implementation.
- T034 and T035 can run in parallel before US4 packaging.
- US1 and US2 can proceed in parallel after T006-T008 because they touch separate processed outputs and figures.

## Parallel Example: User Story 1

```bash
# Tests can be drafted together:
Task: "T010 [P] [US1] Add processed funnel schema and anchor-value tests in hate-crime-undercount/tests/test_processed_outputs.py"
Task: "T011 [P] [US1] Add figure existence test for figures/funnel.png in hate-crime-undercount/tests/test_processed_outputs.py"
```

## Parallel Example: User Story 2

```bash
# Bias tests can be drafted together:
Task: "T018 [P] [US2] Add bias breakdown schema, category, and required percentage tests in hate-crime-undercount/tests/test_processed_outputs.py"
Task: "T019 [P] [US2] Add figure existence test for figures/bias_breakdown.png in hate-crime-undercount/tests/test_processed_outputs.py"
```

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1 setup.
2. Complete Phase 2 foundational source metadata and validation helpers.
3. Complete Phase 3 User Story 1.
4. Stop and validate `data/processed/bjs_funnel.csv` and `figures/funnel.png`.

### Incremental Delivery

1. Deliver US1 headline funnel.
2. Add US2 bias breakdown comparison.
3. Add US3 source traceability, FBI summary, summary table, and caveated writeup.
4. Add US4 packaging and full fresh-clone validation.

### Final Validation

1. Run all tests with `pytest`.
2. Execute the notebook from a clean kernel.
3. Confirm all processed CSVs, figures, README instructions, and caveats match the artifact contracts.

## Notes

- [P] tasks touch different files or independent sections and can run in parallel.
- User-story labels map to the prioritized stories in `spec.md`.
- The first independently valuable deliverable is US1: the headline reporting funnel.
- Keep implementation inside `hate-crime-undercount/` unless updating Spec Kit planning artifacts.
