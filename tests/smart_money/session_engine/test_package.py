"""
Tests for the Session Engine package.
"""

from ogs.smart_money import session_engine
from ogs.smart_money.session_engine import (
    Session,
    SessionAnalyzer,
    SessionFactory,
    SessionSeries,
    SessionStatistics,
    SessionValidator,
    SessionState,
    SessionType,
    TimeZoneType,
    TradingDay,
)


def test_package_import():

    assert session_engine is not None


def test_session_class():

    assert Session is not None


def test_analyzer_class():

    assert SessionAnalyzer is not None


def test_factory_class():

    assert SessionFactory is not None


def test_validator_class():

    assert SessionValidator is not None


def test_collection_class():

    assert SessionSeries is not None


def test_statistics_class():

    assert SessionStatistics is not None


def test_session_type_enum():

    assert SessionType.ASIAN.value == "Asian"
    assert SessionType.LONDON.value == "London"
    assert SessionType.NEW_YORK.value == "New York"
    assert SessionType.LONDON_CLOSE.value == "London Close"
    assert SessionType.CUSTOM.value == "Custom"


def test_session_state_enum():

    assert SessionState.PRE_OPEN.value == "Pre Open"
    assert SessionState.ACTIVE.value == "Active"
    assert SessionState.CLOSING.value == "Closing"
    assert SessionState.CLOSED.value == "Closed"


def test_trading_day_enum():

    assert TradingDay.MONDAY.value == "Monday"
    assert TradingDay.TUESDAY.value == "Tuesday"
    assert TradingDay.WEDNESDAY.value == "Wednesday"
    assert TradingDay.THURSDAY.value == "Thursday"
    assert TradingDay.FRIDAY.value == "Friday"
    assert TradingDay.SATURDAY.value == "Saturday"
    assert TradingDay.SUNDAY.value == "Sunday"


def test_timezone_enum():

    assert TimeZoneType.UTC.value == "UTC"
    assert TimeZoneType.GMT.value == "GMT"
    assert TimeZoneType.IST.value == "IST"

    assert TimeZoneType.NEW_YORK.value == "America/New_York"
    assert TimeZoneType.LONDON.value == "Europe/London"
    assert TimeZoneType.TOKYO.value == "Asia/Tokyo"

    assert TimeZoneType.CUSTOM.value == "Custom"