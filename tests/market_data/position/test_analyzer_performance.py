"""
Performance tests for PositionAnalyzer.
"""

from ogs.market_data.position import (
    Position,
    PositionAnalyzer,
    PositionCollection,
)


def test_large_collection():

    collection = PositionCollection()

    for i in range(1000):

        collection.add(
            Position(
                position_id=f"P{i}",
                quantity=10,
                average_entry_price=100,
                current_price=110,
            )
        )

    analyzer = PositionAnalyzer(collection)

    result = analyzer.summary()

    assert result["count"] == 1000


def test_large_analysis():

    collection = PositionCollection()

    for i in range(500):

        collection.add(
            Position(
                position_id=f"P{i}",
                quantity=20,
                average_entry_price=100,
                current_price=120,
            )
        )

    analyzer = PositionAnalyzer(collection)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 500
    assert result["position_analysis"]["total_market_value"] == 1200000
    assert result["position_analysis"]["average_return"] == 20.0