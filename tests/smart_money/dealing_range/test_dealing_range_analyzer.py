"""
OGS FinOS

Unit Tests

Dealing Range Analyzer
"""

from decimal import Decimal

from ogs.smart_money.dealing_range.analyzer import (
    DealingRangeAnalyzer,
)
from ogs.smart_money.dealing_range.collection import (
    DealingRangeCollection,
)
from ogs.smart_money.dealing_range.enums import (
    DealingRangeDirection,
)


def test_analyze_returns_collection():

    analyzer = DealingRangeAnalyzer()

    collection = analyzer.analyze(
        swing_high=Decimal("2100"),
        swing_low=Decimal("2000"),
        start_index=10,
        end_index=20,
        direction=DealingRangeDirection.BULLISH,
    )

    assert isinstance(
        collection,
        DealingRangeCollection,
    )


def test_collection_contains_one_range():

    analyzer = DealingRangeAnalyzer()

    collection = analyzer.analyze(
        swing_high=Decimal("2100"),
        swing_low=Decimal("2000"),
        start_index=10,
        end_index=20,
        direction=DealingRangeDirection.BULLISH,
    )

    assert len(collection) == 1


def test_equilibrium_calculation():

    analyzer = DealingRangeAnalyzer()

    collection = analyzer.analyze(
        swing_high=Decimal("2100"),
        swing_low=Decimal("2000"),
        start_index=10,
        end_index=20,
        direction=DealingRangeDirection.BULLISH,
    )

    dealing_range = collection.latest()

    assert dealing_range is not None
    assert dealing_range.equilibrium == Decimal("2050")


def test_range_values():

    analyzer = DealingRangeAnalyzer()

    collection = analyzer.analyze(
        swing_high=Decimal("2100"),
        swing_low=Decimal("2000"),
        start_index=10,
        end_index=20,
        direction=DealingRangeDirection.BULLISH,
    )

    dealing_range = collection.latest()

    assert dealing_range is not None
    assert dealing_range.range_high == Decimal("2100")
    assert dealing_range.range_low == Decimal("2000")


def test_direction():

    analyzer = DealingRangeAnalyzer()

    collection = analyzer.analyze(
        swing_high=Decimal("2100"),
        swing_low=Decimal("2000"),
        start_index=10,
        end_index=20,
        direction=DealingRangeDirection.BULLISH,
    )

    dealing_range = collection.latest()

    assert dealing_range is not None
    assert (
        dealing_range.direction
        == DealingRangeDirection.BULLISH
    )


def test_private_equilibrium_method():

    analyzer = DealingRangeAnalyzer()

    equilibrium = analyzer._calculate_equilibrium(
        Decimal("2100"),
        Decimal("2000"),
    )

    assert equilibrium == Decimal("2050")