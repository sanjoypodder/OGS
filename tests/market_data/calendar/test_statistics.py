"""
Tests for Calendar statistics.
"""

from datetime import date

from ogs.market_data.calendar import (
    Calendar,
    CalendarCollection,
    CalendarStatistics,
    CalendarStatus,
    CalendarType,
)


def make(idx, calendar_type, status):

    return Calendar(
        calendar_id=str(idx),
        exchange="NSE",
        market="Cash",
        trading_date=date.today(),
        calendar_type=calendar_type,
        status=status,
    )


def build_collection():

    collection = CalendarCollection()

    collection.add(
        make(
            1,
            CalendarType.TRADING_DAY,
            CalendarStatus.OPEN,
        )
    )

    collection.add(
        make(
            2,
            CalendarType.HOLIDAY,
            CalendarStatus.CLOSED,
        )
    )

    collection.add(
        make(
            3,
            CalendarType.TRADING_DAY,
            CalendarStatus.OPEN,
        )
    )

    return collection


def test_counts():

    stats = CalendarStatistics(build_collection())

    assert stats.count == 3
    assert stats.trading_day_count == 2
    assert stats.holiday_count == 1
    assert stats.open_count == 2


def test_distribution():

    stats = CalendarStatistics(build_collection())

    distribution = stats.distribution()

    assert distribution["TRADING_DAY"] == 2
    assert distribution["HOLIDAY"] == 1


def test_summary():

    stats = CalendarStatistics(build_collection())

    summary = stats.summary()

    assert summary["count"] == 3
    assert summary["trading_days"] == 2
    assert summary["holidays"] == 1
    assert summary["open_days"] == 2