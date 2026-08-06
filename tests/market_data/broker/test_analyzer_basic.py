"""
Tests for Broker analyzer (basic).
"""

from ogs.market_data.broker import (
    Broker,
    BrokerAnalyzer,
    BrokerCollection,
)


def test_analyzer():

    collection = BrokerCollection()

    collection.add(
        Broker(
            broker_id="BRK001",
            name="Broker One",
        )
    )

    analyzer = BrokerAnalyzer(collection)

    result = analyzer.analyze()

    assert isinstance(result, dict)
    assert "summary" in result
    assert "broker_analysis" in result
    assert "distribution_analysis" in result


def test_summary():

    collection = BrokerCollection()

    collection.add(
        Broker(
            broker_id="BRK001",
            name="Broker One",
        )
    )

    analyzer = BrokerAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["count"] == 1