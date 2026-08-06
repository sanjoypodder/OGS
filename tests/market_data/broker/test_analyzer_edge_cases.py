"""
Tests for Broker analyzer edge cases.
"""

from ogs.market_data.broker import (
    BrokerAnalyzer,
    BrokerCollection,
)


def test_empty_collection():

    analyzer = BrokerAnalyzer(
        BrokerCollection()
    )

    result = analyzer.analyze()

    assert result["summary"]["count"] == 0
    assert result["broker_analysis"]["total_accounts"] == 0


def test_empty_distribution():

    analyzer = BrokerAnalyzer(
        BrokerCollection()
    )

    distribution = analyzer.distribution_analysis()

    assert distribution["status"] == {}