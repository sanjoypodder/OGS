"""
Tests for Market analyzer (basic).
"""

from ogs.market_data.market import (
    Market,
    MarketAnalyzer,
    MarketCollection,
)


def test_analyzer():

    collection = MarketCollection()

    collection.add(
        Market(
            market_id="INDIA",
            name="Indian Equity Market",
        )
    )

    analyzer = MarketAnalyzer(collection)

    result = analyzer.analyze()

    assert isinstance(result, dict)
    assert "summary" in result
    assert "market_analysis" in result
    assert "distribution_analysis" in result


def test_summary():

    collection = MarketCollection()

    collection.add(
        Market(
            market_id="INDIA",
            name="Indian Equity Market",
        )
    )

    analyzer = MarketAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["count"] == 1