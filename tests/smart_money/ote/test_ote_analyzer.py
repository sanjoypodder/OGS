"""
OGS FinOS

Unit Tests

OTE Analyzer
"""

from decimal import Decimal

from ogs.smart_money.dealing_range.domain import (
    DealingRange,
)
from ogs.smart_money.dealing_range.enums import (
    DealingRangeDirection,
)
from ogs.smart_money.ote.analyzer import (
    OTEAnalyzer,
)
from ogs.smart_money.ote.collection import (
    OTECollection,
)
from ogs.smart_money.ote.enums import (
    OTEDirection,
)


def create_bullish_range():

    return DealingRange(
        range_high=Decimal("2100"),
        range_low=Decimal("2000"),
        equilibrium=Decimal("2050"),
        direction=DealingRangeDirection.BULLISH,
        start_index=10,
        end_index=20,
    )


def create_bearish_range():

    return DealingRange(
        range_high=Decimal("2100"),
        range_low=Decimal("2000"),
        equilibrium=Decimal("2050"),
        direction=DealingRangeDirection.BEARISH,
        start_index=10,
        end_index=20,
    )


def test_analyze_returns_collection():

    analyzer = OTEAnalyzer()

    collection = analyzer.analyze(
        create_bullish_range()
    )

    assert isinstance(
        collection,
        OTECollection,
    )


def test_collection_contains_one_ote():

    analyzer = OTEAnalyzer()

    collection = analyzer.analyze(
        create_bullish_range()
    )

    assert len(collection) == 1


def test_bullish_direction():

    analyzer = OTEAnalyzer()

    collection = analyzer.analyze(
        create_bullish_range()
    )

    ote = collection.latest()

    assert ote is not None
    assert (
        ote.direction
        == OTEDirection.BULLISH
    )


def test_bearish_direction():

    analyzer = OTEAnalyzer()

    collection = analyzer.analyze(
        create_bearish_range()
    )

    ote = collection.latest()

    assert ote is not None
    assert (
        ote.direction
        == OTEDirection.BEARISH
    )


def test_bullish_levels():

    analyzer = OTEAnalyzer()

    collection = analyzer.analyze(
        create_bullish_range()
    )

    ote = collection.latest()

    assert ote is not None

    assert ote.level_62 == Decimal("2038.00")
    assert ote.level_705 == Decimal("2029.500")
    assert ote.level_79 == Decimal("2021.00")


def test_bearish_levels():

    analyzer = OTEAnalyzer()

    collection = analyzer.analyze(
        create_bearish_range()
    )

    ote = collection.latest()

    assert ote is not None

    assert ote.level_62 == Decimal("2062.00")
    assert ote.level_705 == Decimal("2070.500")
    assert ote.level_79 == Decimal("2079.00")


def test_zone_values():

    analyzer = OTEAnalyzer()

    collection = analyzer.analyze(
        create_bullish_range()
    )

    ote = collection.latest()

    assert ote is not None

    assert ote.zone_low == Decimal("2021.00")
    assert ote.zone_high == Decimal("2038.00")


def test_private_bullish_level():

    analyzer = OTEAnalyzer()

    value = analyzer._bullish_level(
        Decimal("2100"),
        Decimal("2000"),
        Decimal("0.62"),
    )

    assert value == Decimal("2038.00")


def test_private_bearish_level():

    analyzer = OTEAnalyzer()

    value = analyzer._bearish_level(
        Decimal("2100"),
        Decimal("2000"),
        Decimal("0.62"),
    )

    assert value == Decimal("2062.00")