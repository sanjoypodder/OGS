"""
Edge case tests for PositionAnalyzer.
"""

from ogs.market_data.position import (
    Position,
    PositionAnalyzer,
    PositionCollection,
)


def test_empty_collection():

    collection = PositionCollection()

    analyzer = PositionAnalyzer(collection)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 0


def test_single_position():

    collection = PositionCollection()

    collection.add(
        Position(
            position_id="P1",
            quantity=1,
        )
    )

    analyzer = PositionAnalyzer(collection)

    assert analyzer.summary()["count"] == 1


def test_zero_market_value():

    collection = PositionCollection()

    collection.add(
        Position(
            position_id="P1",
            quantity=0,
            current_price=100,
        )
    )

    analyzer = PositionAnalyzer(collection)

    result = analyzer.position_analysis()

    assert result["total_market_value"] == 0


def test_zero_return():

    collection = PositionCollection()

    collection.add(
        Position(
            position_id="P1",
            quantity=10,
            average_entry_price=0,
            current_price=0,
        )
    )

    analyzer = PositionAnalyzer(collection)

    result = analyzer.position_analysis()

    assert result["average_return"] == 0