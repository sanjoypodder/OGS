"""
Tests for Exchange analyzer edge cases.
"""

from ogs.market_data.exchange import (
    ExchangeAnalyzer,
    ExchangeCollection,
)


def test_empty_collection():

    analyzer = ExchangeAnalyzer(
        ExchangeCollection()
    )

    result = analyzer.analyze()

    assert result["summary"]["count"] == 0
    assert result["exchange_analysis"]["total_brokers"] == 0


def test_empty_distribution():

    analyzer = ExchangeAnalyzer(
        ExchangeCollection()
    )

    distribution = analyzer.distribution_analysis()

    assert distribution["status"] == {}