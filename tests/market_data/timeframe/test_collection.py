"""
Tests for Timeframe collection.
"""

from ogs.market_data.timeframe import (
    TimeframeCollection,
    TimeframeFactory,
    TimeframeType,
)


def build_collection():

    collection = TimeframeCollection()

    collection.append(TimeframeFactory.create(TimeframeType.M15))
    collection.append(TimeframeFactory.create(TimeframeType.H1))
    collection.append(TimeframeFactory.create(TimeframeType.D1))
    collection.append(TimeframeFactory.create(TimeframeType.W1))

    return collection


def test_empty_collection():

    collection = TimeframeCollection()

    assert len(collection) == 0


def test_append():

    collection = TimeframeCollection()

    collection.append(
        TimeframeFactory.create(TimeframeType.M1)
    )

    assert len(collection) == 1


def test_by_type():

    collection = build_collection()

    result = collection.by_type(
        TimeframeType.H1,
    )

    assert len(result) == 1
    assert result[0].value is TimeframeType.H1


def test_intraday():

    collection = build_collection()

    result = collection.intraday()

    assert len(result) == 2


def test_higher_timeframes():

    collection = build_collection()

    result = collection.higher_timeframes()

    assert len(result) == 2


def test_shortest():

    collection = build_collection()

    timeframe = collection.shortest()

    assert timeframe.value is TimeframeType.M15


def test_longest():

    collection = build_collection()

    timeframe = collection.longest()

    assert timeframe.value is TimeframeType.W1