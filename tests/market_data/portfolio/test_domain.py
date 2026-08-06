"""
Tests for Portfolio domain.
"""

from datetime import UTC
from datetime import datetime

from ogs.market_data.portfolio import (
    Portfolio,
    PortfolioStatus,
)
from ogs.market_data.position import (
    Position,
)


def make_position():

    return Position(
        position_id="POS1",
        quantity=10,
        average_entry_price=100,
        current_price=110,
    )


def test_default_portfolio():

    portfolio = Portfolio()

    assert portfolio.portfolio_id == ""
    assert portfolio.name == ""
    assert portfolio.position_count == 0


def test_add_position():

    portfolio = Portfolio()

    portfolio.add_position(make_position())

    assert portfolio.position_count == 1


def test_market_value():

    portfolio = Portfolio()

    portfolio.add_position(make_position())

    assert portfolio.market_value == 1100


def test_cost_basis():

    portfolio = Portfolio()

    portfolio.add_position(make_position())

    assert portfolio.cost_basis == 1000


def test_total_unrealized_pnl():

    portfolio = Portfolio()

    portfolio.add_position(make_position())

    assert portfolio.total_unrealized_pnl == 100


def test_total_pnl():

    portfolio = Portfolio()

    portfolio.add_position(make_position())

    assert portfolio.total_pnl == 100


def test_equity():

    portfolio = Portfolio(
        cash_balance=500
    )

    portfolio.add_position(make_position())

    assert portfolio.equity == 1600


def test_return_percentage():

    portfolio = Portfolio(
        initial_capital=1000
    )

    portfolio.add_position(make_position())

    assert portfolio.return_percentage == 10.0


def test_is_active():

    portfolio = Portfolio(
        status=PortfolioStatus.ACTIVE
    )

    assert portfolio.is_active


def test_is_valid():

    portfolio = Portfolio()

    assert portfolio.is_valid


def test_to_dict():

    portfolio = Portfolio(
        portfolio_id="PORT1"
    )

    data = portfolio.to_dict()

    assert data["portfolio_id"] == "PORT1"


def test_created_at():

    portfolio = Portfolio()

    assert isinstance(
        portfolio.created_at,
        datetime,
    )


def test_custom_created_at():

    ts = datetime.now(UTC)

    portfolio = Portfolio(
        created_at=ts
    )

    assert portfolio.created_at == ts


def test_string():

    portfolio = Portfolio(
        portfolio_id="P001"
    )

    assert "P001" in str(portfolio)