"""
Tests for Exchange analyzer (basic).
"""

from ogs.market_data.exchange import (
    Exchange,
    ExchangeAnalyzer,
    ExchangeCollection,
)


def test_analyzer():

    collection = ExchangeCollection()

    collection.add(
        Exchange(
            exchange_id="NSE",
            name="National Stock Exchange",
        )
    )

    analyzer = ExchangeAnalyzer(collection)

    result = analyzer.analyze()

    assert isinstance(result, dict)
    assert "summary" in result
    assert "exchange_analysis" in result
    assert "distribution_analysis" in result


def test_summary():

    collection = ExchangeCollection()

    collection.add(
        Exchange(
            exchange_id="NSE",
            name="National Stock Exchange",
        )
    )

    analyzer = ExchangeAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["count"] == 1