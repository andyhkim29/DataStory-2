from pathlib import Path

import pandas as pd


def test_funnel_schema_values_and_ci_notes(processed_dir: Path):
    path = processed_dir / "bjs_funnel.csv"
    assert path.exists()
    df = pd.read_csv(path)
    expected_columns = [
        "step_order",
        "step_label",
        "value",
        "unit",
        "ci_low",
        "ci_high",
        "loss_from_previous",
        "loss_percent_from_previous",
        "source_url",
        "source_note",
        "ci_note",
    ]
    assert list(df.columns) == expected_columns
    assert df["value"].tolist() == [204600, 101900, 45600, 15200, 7500]
    assert df["value"].is_monotonic_decreasing
    assert len(df) == 5
    blank_ci = df["ci_low"].isna() | df["ci_high"].isna()
    assert df.loc[blank_ci, "ci_note"].astype(str).str.len().gt(0).all()


def test_bias_breakdown_schema_and_values(processed_dir: Path):
    path = processed_dir / "bias_breakdown.csv"
    assert path.exists()
    df = pd.read_csv(path)
    assert list(df.columns) == [
        "bias_type",
        "display_label",
        "ncvs_percent",
        "ucr_percent",
        "gap_percentage_points",
        "source_url",
        "source_note",
    ]
    expected = {
        "race_or_ethnicity": (57.2, 59.8),
        "religion": (7.9, 19.2),
        "gender": (27.2, 1.8),
        "sexual_orientation": (25.7, 17.7),
        "disability": (16.0, 1.4),
    }
    assert set(df["bias_type"]) == set(expected)
    for bias_type, values in expected.items():
        row = df.set_index("bias_type").loc[bias_type]
        assert row["ncvs_percent"] == values[0]
        assert row["ucr_percent"] == values[1]


def test_fbi_summary_schema_and_counts(processed_dir: Path):
    path = processed_dir / "fbi_2013_summary.csv"
    assert path.exists()
    df = pd.read_csv(path)
    assert list(df.columns) == [
        "year",
        "bias_category",
        "incidents",
        "offenses",
        "victims",
        "source_table",
        "source_url",
    ]
    assert (df["year"] == 2013).all()
    assert (df[["incidents", "offenses", "victims"]] >= 0).all().all()
    total = df.set_index("bias_category").loc["Total"]
    assert total["incidents"] == 5928
    assert total["offenses"] == 6933
    assert total["victims"] == 7242


def test_source_citations_present(processed_dir: Path):
    for filename in ["fbi_2013_summary.csv", "bjs_funnel.csv", "bias_breakdown.csv"]:
        df = pd.read_csv(processed_dir / filename)
        assert df["source_url"].astype(str).str.startswith("https://").all()


def test_required_figures_exist(figures_dir: Path):
    assert (figures_dir / "funnel.png").exists()
    assert (figures_dir / "bias_breakdown.png").exists()


def test_readme_mentions_run_commands(project_root: Path):
    readme = (project_root / "README.md").read_text(encoding="utf-8")
    assert "jupyter nbconvert" in readme
    assert "pytest" in readme

