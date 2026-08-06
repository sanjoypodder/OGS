"""
Tests for PortfolioFactory.
"""

import pytest

from ogs.market_data.portfolio import (
    Portfolio,
    PortfolioFactory,
    PortfolioStatus,
    PortfolioType,
)


def test_create():

    portfolio = PortfolioFactory.create(
        portfolio_id="PORT1",
        name="Main",
    )

    assert isinstance(portfolio, Portfolio)


def test_live_factory():

    portfolio = PortfolioFactory.live(
        portfolio_id="PORT1",
        name="Live Portfolio",
    )

    assert portfolio.portfolio_type == PortfolioType.LIVE
    assert portfolio.status == PortfolioStatus.ACTIVE


def test_paper_factory():

    portfolio = PortfolioFactory.paper(
        portfolio_id="PORT2",
        name="Paper Portfolio",
    )

    assert portfolio.portfolio_type == PortfolioType.PAPER
    assert portfolio.status == PortfolioStatus.ACTIVE


def test_backtest_factory():

    portfolio = PortfolioFactory.backtest(
        portfolio_id="PORT3",
        name="Backtest Portfolio",
    )

    assert portfolio.portfolio_type == PortfolioType.BACKTEST
    assert portfolio.status == PortfolioStatus.ACTIVE


def test_clone():

    portfolio = PortfolioFactory.create(
        portfolio_id="PORT1",
        name="Main",
    )

    clone = PortfolioFactory.clone(portfolio)

    assert clone == portfolio
    assert clone is not portfolio


def test_clone_independent():

    portfolio = PortfolioFactory.create(
        portfolio_id="PORT1",
        name="Main",
    )

    clone = PortfolioFactory.clone(portfolio)

    clone.name = "Changed"

    assert portfolio.name == "Main"


def test_factory_validation():

    with pytest.raises(ValueError):

        PortfolioFactory.create(
            portfolio_id="",
            name="Main",
        )