from pathlib import Path

from ogs.core import constants


def test_project_root_exists() -> None:
    assert constants.PROJECT_ROOT.exists()
    assert constants.PROJECT_ROOT.is_dir()


def test_log_directory_name() -> None:
    assert constants.LOG_DIR.name == "logs"


def test_database_directory_name() -> None:
    assert constants.DATABASE_DIR.name == "database"


def test_default_symbol() -> None:
    assert constants.DEFAULT_SYMBOL == "XAUUSD"


def test_default_timeframe() -> None:
    assert constants.DEFAULT_TIMEFRAME == "5m"


def test_log_file_location() -> None:
    assert constants.LOG_FILE.parent == constants.LOG_DIR


def test_database_file_location() -> None:
    assert constants.DATABASE_FILE.parent == constants.DATABASE_DIR


def test_paths_are_path_objects() -> None:
    assert isinstance(constants.PROJECT_ROOT, Path)
    assert isinstance(constants.LOG_DIR, Path)
    assert isinstance(constants.DATABASE_DIR, Path)
