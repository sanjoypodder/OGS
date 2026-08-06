from ogs.core.config import CONFIG
from ogs.core.constants import (
    APP_NAME,
    CODENAME,
    COMPANY,
    DEFAULT_SYMBOL,
    DEFAULT_TIMEFRAME,
)


def test_application_name() -> None:
    assert CONFIG.app_name == APP_NAME


def test_company() -> None:
    assert CONFIG.company == COMPANY


def test_codename() -> None:
    assert CONFIG.codename == CODENAME


def test_default_symbol() -> None:
    assert CONFIG.default_symbol == DEFAULT_SYMBOL


def test_default_timeframe() -> None:
    assert CONFIG.default_timeframe == DEFAULT_TIMEFRAME


def test_debug_flag() -> None:
    assert isinstance(CONFIG.debug, bool)


def test_log_level() -> None:
    assert CONFIG.log_level in (
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    )
