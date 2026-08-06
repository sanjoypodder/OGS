"""
Tests for Calendar collection.
"""

from datetime import date

from ogs.market_data.calendar import (
    Calendar,
    CalendarCollection,
    CalendarStatus,
    CalendarType,
)


def make(
    calendar_id,
    calendar_type,
    status,
):

    return Calendar(
        calendar_id=calendar_id,
        exchange="NSE",
        market="Cash",
        trading_date=date.today(),
        calendar_type=calendar_type,
        status=status,
    )


def test_add():

    collection = CalendarCollection()

    collection.add(
        make(
            "1",
            CalendarType.TRADING_DAY,
            CalendarStatus.OPEN,
        )
    )

    assert len(collection) == 1


def test_find():

    collection = CalendarCollection()

    obj = make(
        "ABC",
        CalendarType.TRADING_DAY,
        CalendarStatus.OPEN,
    )

    collection.add(obj)

    assert collection.find("ABC") == obj

    assert collection.find("XYZ") is None


def test_filters():

    collection = CalendarCollection()

    collection.add(
        make(
            "1",
            CalendarType.TRADING_DAY,
            CalendarStatus.OPEN,
        )
    )

    collection.add(
        make(
            "2",
            CalendarType.HOLIDAY,
            CalendarStatus.CLOSED,
        )
    )

    assert len(collection.trading_days()) == 1

    assert len(collection.holidays()) == 1

    assert len(collection.open_days()) == 1


def test_to_list():

    collection = CalendarCollection()

    collection.add(
        make(
            "1",
            CalendarType.TRADING_DAY,
            CalendarStatus.OPEN,
        )
    )

    assert len(collection.to_list()) == 1