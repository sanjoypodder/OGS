"""
Tests for PortfolioStatistics.
"""

from ogs.market_data.portfolio import (
    PortfolioCollection,
    PortfolioStatistics,
    PortfolioStatus,
    PortfolioType,
)
from ogs.market_data.portfolio.domain import Portfolio


def make_portfolio(
    portfolio_id,
    portfolio_type=PortfolioType.LIVE,
    status=PortfolioStatus.ACTIVE,
):

    return Portfolio(
        portfolio_id=portfolio_id,
        name=f"Portfolio {portfolio_id}",
        portfolio_type=portfolio_type,
        status=status,
        initial_capital=1000,
        cash_balance=1000,
    )


def test_count():

    collection = PortfolioCollection()

    collection.add(make_portfolio("A"))

    stats = PortfolioStatistics(collection)

    assert stats.count == 1


def test_active_inactive_count():

    collection = PortfolioCollection()

    collection.add(make_portfolio("A"))
    collection.add(
        make_portfolio(
            "B",
            status=PortfolioStatus.INACTIVE,
        )
    )

    stats = PortfolioStatistics(collection)

    assert stats.active_count == 1
    assert stats.inactive_count == 1


def test_type_counts():

    collection = PortfolioCollection()

    collection.add(make_portfolio("A"))

    collection.add(
        make_portfolio(
            "B",
            portfolio_type=PortfolioType.PAPER,
        )
    )

    collection.add(
        make_portfolio(
            "C",
            portfolio_type=PortfolioType.BACKTEST,
        )
    )

    stats = PortfolioStatistics(collection)

    assert stats.live_count == 1
    assert stats.paper_count == 1
    assert stats.backtest_count == 1


def test_total_cash():

    collection = PortfolioCollection()

    collection.add(make_portfolio("A"))
    collection.add(make_portfolio("B"))

    stats = PortfolioStatistics(collection)

    assert stats.total_cash == 2000


def test_average_return():

    collection = PortfolioCollection()

    collection.add(make_portfolio("A"))

    stats = PortfolioStatistics(collection)

    assert stats.average_return == 0.0


def test_status_distribution():

    collection = PortfolioCollection()

    collection.add(make_portfolio("A"))

    stats = PortfolioStatistics(collection)

    assert stats.status_distribution["ACTIVE"] == 1


def test_type_distribution():

    collection = PortfolioCollection()

    collection.add(make_portfolio("A"))

    stats = PortfolioStatistics(collection)

    assert stats.type_distribution["LIVE"] == 1


def test_summary():

    collection = PortfolioCollection()

    collection.add(make_portfolio("A"))

    stats = PortfolioStatistics(collection)

    summary = stats.summary()

    assert summary["count"] == 1