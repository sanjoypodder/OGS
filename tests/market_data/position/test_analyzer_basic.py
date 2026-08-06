"""
Tests for PositionAnalyzer basic functionality.
"""

from ogs.market_data.position import (
    Position,
    PositionAnalyzer,
    PositionCollection,
)


def make_position(position_id, quantity, entry, current):

    return Position(
        position_id=position_id,
        quantity=quantity,
        average_entry_price=entry,
        current_price=current,
    )


def test_analyzer_creation():

    collection = PositionCollection()

    analyzer = PositionAnalyzer(collection)

    assert analyzer.collection is collection


def test_summary():

    collection = PositionCollection()

    collection.add(make_position("P1", 10, 100, 110))
    collection.add(make_position("P2", 20, 200, 220))

    analyzer = PositionAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["count"] == 2


def test_analyze():

    collection = PositionCollection()

    collection.add(make_position("P1", 10, 100, 110))

    analyzer = PositionAnalyzer(collection)

    result = analyzer.analyze()

    assert "summary" in result
    assert "position_analysis" in result
    assert "distribution_analysis" in result