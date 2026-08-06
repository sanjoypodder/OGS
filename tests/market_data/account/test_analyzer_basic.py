"""
Tests for Account analyzer (basic).
"""

from ogs.market_data.account import (
    Account,
    AccountAnalyzer,
    AccountCollection,
)


def test_analyzer():

    collection = AccountCollection()

    collection.add(
        Account(
            account_id="ACC001",
            name="Primary",
        )
    )

    analyzer = AccountAnalyzer(collection)

    result = analyzer.analyze()

    assert isinstance(result, dict)
    assert "summary" in result
    assert "account_analysis" in result
    assert "distribution_analysis" in result


def test_summary():

    collection = AccountCollection()

    collection.add(
        Account(
            account_id="ACC001",
            name="Primary",
        )
    )

    analyzer = AccountAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["count"] == 1