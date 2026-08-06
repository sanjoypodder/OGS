"""
Performance tests for Broker analyzer.
"""

from ogs.market_data.broker import (
    Broker,
    BrokerAnalyzer,
    BrokerCollection,
)


def test_large_collection():

    collection = BrokerCollection()

    for i in range(1000):

        collection.add(
            Broker(
                broker_id=f"B{i}",
                name=f"Broker {i}",
            )
        )

    analyzer = BrokerAnalyzer(collection)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 1000


def test_summary_speed():

    collection = BrokerCollection()

    for i in range(500):

        collection.add(
            Broker(
                broker_id=str(i),
                name="Broker",
            )
        )

    analyzer = BrokerAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["count"] == 500