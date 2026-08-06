"""
Tests for Calendar domain.
"""

from datetime import date

from ogs.market_data.calendar import (
    Calendar,
    CalendarStatus,
    CalendarType,
)


def test_default():

    obj = Calendar()

    assert obj.calendar_id == ""
    assert obj.exchange == ""
    assert obj.market == ""
    assert obj.trading_date is None

    assert obj.calendar_type == CalendarType.UNKNOWN
    assert obj.status == CalendarStatus.CLOSED

    assert obj.active

    assert not obj.is_valid
    assert not obj.is_trading_day


def test_valid():

    obj = Calendar(
        calendar_id="CAL001",
        exchange="NSE",
        market="Cash",
        trading_date=date.today(),
    )

    assert obj.is_valid


def test_trading_day():

    obj = Calendar(
        calendar_id="CAL001",
        exchange="NSE",
        market="Cash",
        trading_date=date.today(),
        calendar_type=CalendarType.TRADING_DAY,
        status=CalendarStatus.OPEN,
    )

    assert obj.is_trading_day


def test_to_dict():

    obj = Calendar()

    data = obj.to_dict()

    assert isinstance(data, dict)

    assert "calendar_id" in data
    assert "trading_date" in data


def test_string():

    obj = Calendar()

    assert "Calendar" in str(obj)