# Research: Hate Crime Undercount Analysis

## Decision: Use a self-contained notebook project

**Rationale**: The deliverable is a reproducible data story, not a reusable
service. A notebook can combine narrative context, validation, tables, charts,
and final caveats in the requested order.

**Alternatives considered**: A command-line package would improve automation but
would add structure beyond the requested notebook. An interactive dashboard is
explicitly out of scope.

## Decision: Use pandas, matplotlib, and requests

**Rationale**: pandas is appropriate for small CSV wrangling, matplotlib creates
portable static figures for video editing, and requests supports first-run data
fetching if raw files are not already present. These choices match the feature's
tech constraints and keep dependencies conventional.

**Alternatives considered**: Plotly was rejected because the requested output is
static figures. Direct standard-library CSV handling was rejected because pandas
gives clearer validation and summarization with little overhead.

## Decision: Commit raw data when below 10 MB

**Rationale**: The FBI tables and manually transcribed BJS values are small, so
committing them supports fresh-clone reproducibility and avoids brittle network
dependence. The notebook can still include source-download logic for missing FBI
files to satisfy no-manual-download behavior.

**Alternatives considered**: Always downloading raw data was rejected because
public mirrors can be unavailable. Hosting externally is unnecessary unless the
data exceeds the size threshold.

## Decision: Treat BJS PDF values as traceable source data

**Rationale**: The required BJS values are few and supplied from published
briefing tables/figures. They should be encoded in a raw CSV with fields for
source document, page/table/figure note, measure, value, and confidence interval
bounds where verified.

**Alternatives considered**: PDF parsing was rejected as unnecessary and more
fragile than transcription for a small fixed set of values. Hard-coding values
only inside notebook code was rejected because it weakens traceability.

## Decision: Leave unverifiable confidence interval bounds blank

**Rationale**: The clarified requirement is to extract or transcribe 95% CI
bounds from the cited BJS PDF where available, and leave unavailable bounds
blank with a note. This avoids inventing uncertainty values while preserving the
chart's uncertainty support.

**Alternatives considered**: Omitting all confidence intervals would ignore the
clarification. Estimating bounds from point estimates would create unsupported
numbers.

## Decision: Validate with notebook execution and focused tests

**Rationale**: Acceptance depends on restart-and-run-all reproducibility plus
specific artifact schemas and anchor values. A notebook execution test and small
pytest checks catch the highest-risk failures without overbuilding.

**Alternatives considered**: Manual inspection only was rejected because it does
not satisfy reproducibility. Full pipeline packaging was rejected as unnecessary
for a small notebook project.
