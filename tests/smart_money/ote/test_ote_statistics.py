"""
OGS FinOS

Unit Tests

OTE Statistics
"""

from decimal import Decimal

from ogs.smart_money.ote.collection import (
    OTECollection,
)
from ogs.smart_money.ote.domain import (
    OTE,
)
from ogs.smart_money.ote.enums import (
    OTEDirection,
)
from ogs.smart_money.ote.statistics import (
    OTEStatistics,
)


def create_ote(
    high,
    low,
    direction,
):

    high = Decimal(high)
    low = Decimal(low)

    return OTE(
        range_high=high,
        range_low=low,
        level_62=high - Decimal("62"),
        level_705=high - Decimal("70.5"),
        level_79=high - Decimal("79"),
        zone_low=high - Decimal("79"),
        zone_high=high - Decimal("62"),
        direction=direction,
    )


def test_total():

    collection = OTECollection()

    collection.add(
        create_ote(
            "2100",
            "2000",
            OTEDirection.BULLISH,
        )
    )

    stats = OTEStatistics(collection)

    assert stats.total == 1


def test_direction_counts():

    collection = OTECollection()

    collection.add(
        create_ote(
            "2100",
            "2000",
            OTEDirection.BULLISH,
        )
    )

    collection.add(
        create_ote(
            "2200",
            "2100",
            OTEDirection.BEARISH,
        )
    )

    stats = OTEStatistics(collection)

    assert stats.bullish == 1
    assert stats.bearish == 1


def test_average_zone_size():

    collection = OTECollection()

    collection.add(
        create_ote(
            "2100",
            "2000",
            OTEDirection.BULLISH,
        )
    )

    collection.add(
        create_ote(
            "2200",
            "2100",
            OTEDirection.BEARISH,
        )
    )

    stats = OTEStatistics(collection)

    expected = (
        Decimal("17")
        + Decimal("17")
    ) / Decimal("2")

    assert (
        stats.average_zone_size
        == expected
    )


def test_maximum_zone_size():

    collection = OTECollection()

    collection.add(
        create_ote(
            "2100",
            "2000",
            OTEDirection.BULLISH,
        )
    )

    stats = OTEStatistics(collection)

    assert (
        stats.maximum_zone_size
        == Decimal("17")
    )


def test_minimum_zone_size():

    collection = OTECollection()

    collection.add(
        create_ote(
            "2100",
            "2000",
            OTEDirection.BULLISH,
        )
    )

    stats = OTEStatistics(collection)

    assert (
        stats.minimum_zone_size
        == Decimal("17")
    )


def test_average_levels():

    collection = OTECollection()

    collection.add(
        create_ote(
            "2100",
            "2000",
            OTEDirection.BULLISH,
        )
    )

    stats = OTEStatistics(collection)

    assert (
        stats.average_level_62
        == Decimal("2038")
    )

    assert (
        stats.average_level_705
        == Decimal("2029.5")
    )

    assert (
        stats.average_level_79
        == Decimal("2021")
    )


def test_empty_collection():

    stats = OTEStatistics(
        OTECollection()
    )

    assert stats.total == 0

    assert (
        stats.average_zone_size
        == Decimal("0")
    )

    assert (
        stats.maximum_zone_size
        == Decimal("0")
    )

    assert (
        stats.minimum_zone_size
        == Decimal("0")
    )


def test_summary():

    collection = OTECollection()

    collection.add(
        create_ote(
            "2100",
            "2000",
            OTEDirection.BULLISH,
        )
    )

    summary = OTEStatistics(
        collection
    ).summary()

    assert summary["total"] == 1

    assert summary["bullish"] == 1