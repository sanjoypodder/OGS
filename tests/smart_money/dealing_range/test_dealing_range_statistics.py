"""
OGS FinOS

Unit Tests

Dealing Range Statistics
"""

from decimal import Decimal

from ogs.smart_money.dealing_range.collection import (
    DealingRangeCollection,
)
from ogs.smart_money.dealing_range.domain import (
    DealingRange,
)
from ogs.smart_money.dealing_range.enums import (
    DealingRangeDirection,
)
from ogs.smart_money.dealing_range.statistics import (
    DealingRangeStatistics,
)


def create_range(
    high: str,
    low: str,
    direction: DealingRangeDirection,
) -> DealingRange:

    return DealingRange(
        range_high=Decimal(high),
        range_low=Decimal(low),
        equilibrium=(
            Decimal(high) + Decimal(low)
        ) / Decimal("2"),
        direction=direction,
        start_index=1,
        end_index=2,
    )


def test_total():

    collection = DealingRangeCollection()

    collection.add(
        create_range(
            "2100",
            "2000",
            DealingRangeDirection.BULLISH,
        )
    )

    stats = DealingRangeStatistics(collection)

    assert stats.total == 1


def test_direction_counts():

    collection = DealingRangeCollection()

    collection.add(
        create_range(
            "2100",
            "2000",
            DealingRangeDirection.BULLISH,
        )
    )

    collection.add(
        create_range(
            "2200",
            "2100",
            DealingRangeDirection.BEARISH,
        )
    )

    collection.add(
        create_range(
            "2300",
            "2200",
            DealingRangeDirection.SIDEWAYS,
        )
    )

    stats = DealingRangeStatistics(collection)

    assert stats.bullish == 1
    assert stats.bearish == 1
    assert stats.sideways == 1


def test_average_range():

    collection = DealingRangeCollection()

    collection.add(
        create_range(
            "2100",
            "2000",
            DealingRangeDirection.BULLISH,
        )
    )

    collection.add(
        create_range(
            "2200",
            "2000",
            DealingRangeDirection.BEARISH,
        )
    )

    stats = DealingRangeStatistics(collection)

    assert stats.average_range_size == Decimal("150")


def test_maximum_range():

    collection = DealingRangeCollection()

    collection.add(
        create_range(
            "2100",
            "2000",
            DealingRangeDirection.BULLISH,
        )
    )

    collection.add(
        create_range(
            "2400",
            "2000",
            DealingRangeDirection.BEARISH,
        )
    )

    stats = DealingRangeStatistics(collection)

    assert stats.maximum_range == Decimal("400")


def test_minimum_range():

    collection = DealingRangeCollection()

    collection.add(
        create_range(
            "2100",
            "2000",
            DealingRangeDirection.BULLISH,
        )
    )

    collection.add(
        create_range(
            "2400",
            "2000",
            DealingRangeDirection.BEARISH,
        )
    )

    stats = DealingRangeStatistics(collection)

    assert stats.minimum_range == Decimal("100")


def test_empty_collection():

    collection = DealingRangeCollection()

    stats = DealingRangeStatistics(collection)

    assert stats.total == 0
    assert stats.average_range_size == Decimal("0")
    assert stats.maximum_range == Decimal("0")
    assert stats.minimum_range == Decimal("0")


def test_summary():

    collection = DealingRangeCollection()

    collection.add(
        create_range(
            "2100",
            "2000",
            DealingRangeDirection.BULLISH,
        )
    )

    summary = DealingRangeStatistics(
        collection
    ).summary()

    assert summary["total"] == 1
    assert summary["bullish"] == 1