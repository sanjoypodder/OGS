"""
Tests for Market analyzer detection.
"""

from ogs.market_data.market import (
    Market,
    MarketAnalyzer,
    MarketCollection,
    MarketStatus,
)


def test_distribution():

    collection = MarketCollection()

    collection.add(
        Market(
            market_id="INDIA",
            name="Indian Equity Market",
            status=MarketStatus.OPEN,
        )
    )

    collection.add(
        Market(
            market_id="USA",
            name="US Equity Market",
            status=MarketStatus.CLOSED,
        )
    )

    analyzer = MarketAnalyzer(collection)

    distribution = analyzer.distribution_analysis()

    assert distribution["status"]["OPEN"] == 1
    assert distribution["status"]["CLOSED"] == 1


def test_market_analysis():

    collection = MarketCollection()

    collection.add(
        Market(
            market_id="INDIA",
            name="Indian Equity Market",
        )
    )

    analyzer = MarketAnalyzer(collection)

    result = analyzer.market_analysis()

    assert result["exchange_count"] == 0
    assert result["broker_count"] == 0
    assert result["account_count"] == 0
    assert result["total_equity"] == 0.0
    assert result["total_cash"] == 0.0