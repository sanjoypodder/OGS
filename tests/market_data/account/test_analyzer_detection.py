"""
Tests for Account analyzer detection.
"""

from ogs.market_data.account import (
    Account,
    AccountAnalyzer,
    AccountCollection,
    AccountStatus,
    AccountType,
)


def test_distribution():

    collection = AccountCollection()

    collection.add(
        Account(
            account_id="1",
            name="Live",
            account_type=AccountType.LIVE,
            status=AccountStatus.ACTIVE,
        )
    )

    collection.add(
        Account(
            account_id="2",
            name="Paper",
            account_type=AccountType.PAPER,
            status=AccountStatus.INACTIVE,
        )
    )

    analyzer = AccountAnalyzer(collection)

    result = analyzer.distribution_analysis()

    assert result["status"]["ACTIVE"] == 1
    assert result["status"]["INACTIVE"] == 1
    assert result["types"]["LIVE"] == 1
    assert result["types"]["PAPER"] == 1


def test_account_analysis():

    collection = AccountCollection()

    collection.add(
        Account(
            account_id="1",
            name="Live",
        )
    )

    analyzer = AccountAnalyzer(collection)

    result = analyzer.account_analysis()

    assert result["total_equity"] == 0.0
    assert result["total_cash"] == 0.0