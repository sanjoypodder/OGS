"""
Tests for Account statistics.
"""

from ogs.market_data.account import (
    Account,
    AccountCollection,
    AccountStatistics,
    AccountStatus,
    AccountType,
)


def make_collection():

    c = AccountCollection()

    c.add(
        Account(
            account_id="1",
            name="Live",
            account_type=AccountType.LIVE,
            status=AccountStatus.ACTIVE,
        )
    )

    c.add(
        Account(
            account_id="2",
            name="Paper",
            account_type=AccountType.PAPER,
            status=AccountStatus.INACTIVE,
        )
    )

    return c


def test_statistics_counts():

    stats = AccountStatistics(make_collection())

    assert stats.count == 2
    assert stats.active_count == 1
    assert stats.inactive_count == 1
    assert stats.live_count == 1
    assert stats.paper_count == 1
    assert stats.backtest_count == 0


def test_statistics_totals():

    stats = AccountStatistics(make_collection())

    assert stats.total_equity == 0.0
    assert stats.total_cash == 0.0
    assert stats.total_market_value == 0.0
    assert stats.total_realized_pnl == 0.0
    assert stats.total_unrealized_pnl == 0.0
    assert stats.total_pnl == 0.0


def test_summary():

    stats = AccountStatistics(make_collection())

    summary = stats.summary()

    assert isinstance(summary, dict)
    assert summary["count"] == 2
    assert summary["active_count"] == 1


def test_distribution():

    stats = AccountStatistics(make_collection())

    assert stats.status_distribution["ACTIVE"] == 1
    assert stats.status_distribution["INACTIVE"] == 1

    assert stats.type_distribution["LIVE"] == 1
    assert stats.type_distribution["PAPER"] == 1