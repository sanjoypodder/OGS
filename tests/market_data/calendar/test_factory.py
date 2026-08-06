"""
Tests for Calendar factory.
"""

from datetime import date

from ogs.market_data.calendar import (
    Calendar,
    CalendarFactory,
    CalendarStatus,
    CalendarType,
)


def test_create():

    obj = CalendarFactory.create(
        "CAL001",
        "NSE",
        "Cash",
        date.today(),
    )

    assert isinstance(obj, Calendar)


def test_trading_day():

    obj = CalendarFactory.trading_day(
        "CAL001",
        "NSE",
        "Cash",
        date.today(),
    )

    assert obj.calendar_type == CalendarType.TRADING_DAY

    assert obj.status == CalendarStatus.OPEN


def test_clone():

    obj = CalendarFactory.create(
        "CAL001",
        "NSE",
        "Cash",
        date.today(),
    )

    clone = CalendarFactory.clone(obj)

    assert clone == obj

    assert clone is not obj