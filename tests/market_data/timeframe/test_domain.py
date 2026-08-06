"""
Tests for Timeframe domain.
"""

from datetime import timedelta

from ogs.market_data.timeframe import (
    Timeframe,
    TimeframeType,
)


def test_create_timeframe():

    timeframe = Timeframe(
        value=TimeframeType.M15,
    )

    assert timeframe.value is TimeframeType.M15


def test_duration():

    timeframe = Timeframe(
        value=TimeframeType.H1,
    )

    assert timeframe.duration == timedelta(hours=1)


def test_minutes():

    timeframe = Timeframe(
        value=TimeframeType.H4,
    )

    assert timeframe.minutes == 240


def test_seconds():

    timeframe = Timeframe(
        value=TimeframeType.M5,
    )

    assert timeframe.seconds == 300


def test_label():

    timeframe = Timeframe(
        value=TimeframeType.D1,
    )

    assert timeframe.label == "D1"


def test_intraday():

    timeframe = Timeframe(
        value=TimeframeType.H1,
    )

    assert timeframe.is_intraday
    assert not timeframe.is_daily_or_higher


def test_daily():

    timeframe = Timeframe(
        value=TimeframeType.D1,
    )

    assert timeframe.is_daily_or_higher
    assert not timeframe.is_intraday


def test_weekly():

    timeframe = Timeframe(
        value=TimeframeType.W1,
    )

    assert timeframe.is_daily_or_higher


def test_monthly():

    timeframe = Timeframe(
        value=TimeframeType.MN1,
    )

    assert timeframe.is_daily_or_higher