import datetime as dt
from pathlib import Path
from unittest import mock

from click.testing import CliRunner

from sco1_misc import csv_date_trim

CURRENT_DIR = Path()
DUMMY_LOG_FILEPATH = CURRENT_DIR / "best_log.csv"

TEST_DATE = dt.date(2022, 4, 20)


def test_date_convert_no_filename() -> None:
    out_filepath = csv_date_trim._build_output_filepath(DUMMY_LOG_FILEPATH, TEST_DATE, None)

    assert out_filepath == CURRENT_DIR / "best_log_2022-04-20.csv"


def test_date_convert_filename() -> None:
    out_filepath = csv_date_trim._build_output_filepath(
        DUMMY_LOG_FILEPATH, TEST_DATE, "taco_bell_4lyfe.csv"
    )

    assert out_filepath == CURRENT_DIR / "taco_bell_4lyfe.csv"


def test_same_path_raises() -> None:
    runner = CliRunner()
    result = runner.invoke(
        csv_date_trim.trim_cli, ["--log_filepath", "some_log.csv", "--out_filename", "some_log.csv"]
    )

    assert result.exit_code == 1


@mock.patch.object(csv_date_trim, "prompt_for_file", return_value=DUMMY_LOG_FILEPATH)
@mock.patch.object(csv_date_trim, "_trim_csv")
def test_no_log_path_prompts(mocked_trim: mock.MagicMock, mocked_prompt: mock.MagicMock) -> None:
    runner = CliRunner()
    result = runner.invoke(csv_date_trim.trim_cli)

    assert result.exit_code == 0
    mocked_prompt.assert_called()
    mocked_trim.assert_called()


@mock.patch.object(csv_date_trim, "prompt_for_file", side_effect=ValueError)
@mock.patch.object(csv_date_trim, "_trim_csv")
def test_no_log_path_prompt_selection_raises(
    mocked_trim: mock.MagicMock,
    mocked_prompt: mock.MagicMock,
) -> None:
    runner = CliRunner()
    result = runner.invoke(csv_date_trim.trim_cli)

    assert result.exit_code == 1
    mocked_prompt.assert_called()
    mocked_trim._trim_csv.assert_not_called()


@mock.patch.object(csv_date_trim, "_trim_csv")
def test_trim_pipeline_invoked(mocked_trim: mock.MagicMock) -> None:
    runner = CliRunner()
    result = runner.invoke(csv_date_trim.trim_cli, ["--log_filepath", "some_log.csv"])

    assert result.exit_code == 0
    mocked_trim.assert_called()
