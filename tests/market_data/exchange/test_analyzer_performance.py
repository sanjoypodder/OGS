"""
Performance tests for Exchange analyzer.
"""

from ogs.market_data.exchange import (
    Exchange,
    ExchangeAnalyzer,
    ExchangeCollection,
)


def test_large_collection():

    collection = ExchangeCollection()

    for i in range(1000):

        collection.add(
            Exchange(
                exchange_id=f"EX{i}",
                name=f"Exchange {i}",
            )
        )

    analyzer = ExchangeAnalyzer(collection)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 1000


def test_summary_speed():

    collection = ExchangeCollection()

    for i in range(500):

        collection.add(
            Exchange(
                exchange_id=str(i),
                name="Exchange",
            )
        )

    analyzer = ExchangeAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["count"] == 500