"""
Tests for Exchange analyzer detection.
"""

from ogs.market_data.exchange import (
    Exchange,
    ExchangeAnalyzer,
    ExchangeCollection,
    ExchangeStatus,
)


def test_distribution():

    collection = ExchangeCollection()

    collection.add(
        Exchange(
            exchange_id="NSE",
            name="NSE",
            status=ExchangeStatus.OPEN,
        )
    )

    collection.add(
        Exchange(
            exchange_id="BSE",
            name="BSE",
            status=ExchangeStatus.CLOSED,
        )
    )

    analyzer = ExchangeAnalyzer(collection)

    distribution = analyzer.distribution_analysis()

    assert distribution["status"]["OPEN"] == 1
    assert distribution["status"]["CLOSED"] == 1


def test_exchange_analysis():

    collection = ExchangeCollection()

    collection.add(
        Exchange(
            exchange_id="NSE",
            name="NSE",
        )
    )

    analyzer = ExchangeAnalyzer(collection)

    result = analyzer.exchange_analysis()

    assert result["total_brokers"] == 0
    assert result["total_accounts"] == 0
    assert result["total_equity"] == 0.0
    assert result["total_cash"] == 0.0