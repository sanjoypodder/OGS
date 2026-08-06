"""
Tests for Timeframe factory.
"""

import pytest

from ogs.market_data.timeframe import (
    Timeframe,
    TimeframeFactory,
    TimeframeType,
)


def test_create():

    timeframe = TimeframeFactory.create(
        TimeframeType.H1,
    )

    assert isinstance(
        timeframe,
        Timeframe,
    )


def test_create_value():

    timeframe = TimeframeFactory.create(
        TimeframeType.M30,
    )

    assert timeframe.value is TimeframeType.M30


def test_from_string():

    timeframe = TimeframeFactory.from_string(
        "M15",
    )

    assert timeframe.value is TimeframeType.M15


def test_from_string_lowercase():

    timeframe = TimeframeFactory.from_string(
        "h4",
    )

    assert timeframe.value is TimeframeType.H4


def test_invalid_string():

    with pytest.raises(ValueError):

        TimeframeFactory.from_string(
            "ABC",
        )


def test_invalid_create():

    with pytest.raises(ValueError):

        TimeframeFactory.create(
            "H1",
        )