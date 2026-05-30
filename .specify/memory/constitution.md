<!--
Sync Impact Report
Version change: template -> 1.0.0
Modified principles:
- PRINCIPLE_1_NAME -> I. Reproducibility Is the Product
- PRINCIPLE_2_NAME -> II. Source Provenance and Traceability
- PRINCIPLE_3_NAME -> III. Narrative Before Ornament
- PRINCIPLE_4_NAME -> IV. Validation and Caveats
- PRINCIPLE_5_NAME -> V. Minimal, Auditable Scope
Added sections:
- Data Story Standards
- Workflow and Review Gates
Removed sections:
- None
Templates requiring updates:
- updated: .specify/templates/plan-template.md
- updated: .specify/templates/tasks-template.md
- updated: .specify/templates/spec-template.md
Follow-up TODOs:
- None
-->
# DataStory-2 Constitution

## Core Principles

### I. Reproducibility Is the Product
Every analysis MUST run end-to-end from a fresh clone without manual data edits,
manual downloads, or hidden local state. Inputs, transformations, outputs, and
run instructions MUST be committed or fetched by documented, repeatable steps.
Generated figures and processed data MUST be reproducible from the notebook or
analysis workflow. Rationale: the credibility of a data story depends on a
reviewer being able to recreate the evidence, not only view the final visuals.

### II. Source Provenance and Traceability
Every numeric claim used in a figure, table, or narrative finding MUST be
traceable to a source file, processed dataset, and citation. Manually
transcribed values MUST be isolated in clearly labeled data structures or files
with source page/table notes. Rationale: federal statistics and derived
comparisons can be misread if source units, collection methods, or transcription
steps are opaque.

### III. Narrative Before Ornament
Each feature MUST serve a clear story question and produce artifacts that
advance that question. Visuals MUST make the key comparison legible without
decorative clutter, and notebook sections MUST explain what is being shown and
why before presenting code or charts. Rationale: this repository exists to
support concise data stories, so analysis choices must be organized around
audience understanding rather than exploratory leftovers.

### IV. Validation and Caveats
Analyses MUST validate loaded data against expected row counts, categories,
totals, or known anchor values before using them in findings. Caveats about
units, coverage, uncertainty, missing data, and source limitations MUST appear
near the relevant results and in final findings. Rationale: public-interest data
work must surface uncertainty and comparability limits as part of the argument,
not as an afterthought.

### V. Minimal, Auditable Scope
Features MUST stay within the stated analysis scope and avoid adding unrelated
dashboards, models, data sources, or refactors. Dependencies SHOULD be kept
small and conventional for the analysis task. Any expansion beyond the approved
feature scope MUST be documented in the plan with a reason and a rejected simpler
alternative. Rationale: narrow scope keeps the work reviewable, reproducible,
and suitable for short-form storytelling.

## Data Story Standards

Project deliverables MUST include a narrative notebook or equivalent analysis
document, processed data outputs, exported figures when visuals are required,
and concise run instructions. Notebook sections MUST open with markdown that
states the purpose of the section and its role in the story. Final writeups MUST
distinguish source facts from analysis interpretation and MUST keep caveats close
to the claims they qualify.

Raw data SHOULD be committed when it is small enough for normal repository use.
When source data is too large or unsuitable for commit, the project MUST fetch it
automatically from stable public sources and document the fallback behavior.
Generated outputs MUST not depend on credentials, private services, or local file
paths outside the repository.

## Workflow and Review Gates

Before implementation planning, each feature MUST identify its story questions,
required outputs, source data, validation checks, and caveats. The plan MUST pass
a Constitution Check covering reproducibility, provenance, narrative fit,
validation, and scope control. Task lists MUST include verification tasks for
fresh-clone execution, processed-data generation, visual output generation, and
source traceability.

Reviews MUST treat failing reproducibility, missing citations, unvalidated
inputs, or omitted caveats as blocking issues. Changes that alter numeric
results MUST regenerate affected processed data and figures in the same change
set, or document why regeneration is intentionally deferred.

## Governance

This constitution supersedes conflicting repository practices. Amendments MUST
be made by editing this file, updating the Sync Impact Report, and checking
dependent Spec Kit templates for alignment. Versioning follows semantic
versioning: MAJOR for removing or redefining principles, MINOR for adding or
materially expanding principles or governance sections, and PATCH for wording
clarifications that do not change obligations.

Every Speckit plan MUST include a Constitution Check. Every implementation
review MUST verify compliance with the active constitution before considering a
feature complete. When a feature cannot comply with a principle, the plan MUST
document the violation, the reason it is necessary, and the simpler alternative
that was rejected.

**Version**: 1.0.0 | **Ratified**: 2026-05-30 | **Last Amended**: 2026-05-30
