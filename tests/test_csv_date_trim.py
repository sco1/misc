import datetime as dt
from pathlib import Path

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
