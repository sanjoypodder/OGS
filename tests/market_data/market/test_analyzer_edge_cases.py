"""
Tests for Market analyzer edge cases.
"""

from ogs.market_data.market import (
    MarketAnalyzer,
    MarketCollection,
)


def test_empty_collection():

    analyzer = MarketAnalyzer(
        MarketCollection()
    )

    result = analyzer.analyze()

    assert result["summary"]["count"] == 0
    assert result["market_analysis"]["exchange_count"] == 0


def test_empty_distribution():

    analyzer = MarketAnalyzer(
        MarketCollection()
    )

    distribution = analyzer.distribution_analysis()

    assert distribution["status"] == {}