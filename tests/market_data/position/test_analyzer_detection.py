"""
Detection tests for PositionAnalyzer.
"""

from ogs.market_data.position import (
    Position,
    PositionAnalyzer,
    PositionCollection,
    PositionSide,
)


def test_position_analysis():

    collection = PositionCollection()

    collection.add(
        Position(
            position_id="LONG1",
            side=PositionSide.LONG,
            quantity=10,
            average_entry_price=100,
            current_price=110,
        )
    )

    collection.add(
        Position(
            position_id="SHORT1",
            side=PositionSide.SHORT,
            quantity=5,
            average_entry_price=120,
            current_price=100,
        )
    )

    analyzer = PositionAnalyzer(collection)

    result = analyzer.position_analysis()

    assert result["long_count"] == 1
    assert result["short_count"] == 1


def test_distribution_analysis():

    collection = PositionCollection()

    collection.add(
        Position(
            position_id="P1",
            provider="NSE",
            symbol="NIFTY",
        )
    )

    analyzer = PositionAnalyzer(collection)

    result = analyzer.distribution_analysis()

    assert "providers" in result
    assert "symbols" in result


def test_total_market_value_detection():

    collection = PositionCollection()

    collection.add(
        Position(
            position_id="P1",
            quantity=10,
            current_price=120,
        )
    )

    analyzer = PositionAnalyzer(collection)

    result = analyzer.position_analysis()

    assert result["total_market_value"] == 1200