"""
Tests for Broker analyzer detection.
"""

from ogs.market_data.broker import (
    Broker,
    BrokerAnalyzer,
    BrokerCollection,
    BrokerStatus,
)


def test_distribution():

    collection = BrokerCollection()

    collection.add(
        Broker(
            broker_id="1",
            name="Broker One",
            status=BrokerStatus.ACTIVE,
        )
    )

    collection.add(
        Broker(
            broker_id="2",
            name="Broker Two",
            status=BrokerStatus.INACTIVE,
        )
    )

    analyzer = BrokerAnalyzer(collection)

    distribution = analyzer.distribution_analysis()

    assert distribution["status"]["ACTIVE"] == 1
    assert distribution["status"]["INACTIVE"] == 1


def test_broker_analysis():

    collection = BrokerCollection()

    collection.add(
        Broker(
            broker_id="1",
            name="Broker",
        )
    )

    analyzer = BrokerAnalyzer(collection)

    result = analyzer.broker_analysis()

    assert result["total_accounts"] == 0
    assert result["total_equity"] == 0.0
    assert result["total_cash"] == 0.0