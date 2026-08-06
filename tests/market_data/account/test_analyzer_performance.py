"""
Performance tests for Account analyzer.
"""

from ogs.market_data.account import (
    Account,
    AccountAnalyzer,
    AccountCollection,
)


def test_large_collection():

    collection = AccountCollection()

    for i in range(1000):

        collection.add(
            Account(
                account_id=f"A{i}",
                name=f"Account {i}",
            )
        )

    analyzer = AccountAnalyzer(collection)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 1000


def test_summary_speed():

    collection = AccountCollection()

    for i in range(500):

        collection.add(
            Account(
                account_id=str(i),
                name="Account",
            )
        )

    analyzer = AccountAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["count"] == 500