"""
Tests for PortfolioValidator.
"""

from datetime import datetime

import pytest

from ogs.market_data.portfolio import (
    Portfolio,
    PortfolioStatus,
    PortfolioType,
    PortfolioValidator,
)
from ogs.market_data.position import (
    PositionCollection,
)


validator = PortfolioValidator()


def test_validator_accepts_valid_portfolio():

    portfolio = Portfolio(
        portfolio_id="PORT1",
        name="Main Portfolio",
    )

    assert validator(portfolio)


def test_validator_rejects_non_portfolio():

    with pytest.raises(TypeError):
        validator("invalid")


def test_validator_rejects_empty_id():

    with pytest.raises(ValueError):
        validator(
            Portfolio(
                name="Main"
            )
        )


def test_validator_rejects_empty_name():

    with pytest.raises(ValueError):
        validator(
            Portfolio(
                portfolio_id="PORT1"
            )
        )


def test_invalid_portfolio_type():

    portfolio = Portfolio(
        portfolio_id="PORT1",
        name="Main",
    )

    portfolio.portfolio_type = "LIVE"

    with pytest.raises(ValueError):
        validator(portfolio)


def test_invalid_status():

    portfolio = Portfolio(
        portfolio_id="PORT1",
        name="Main",
    )

    portfolio.status = "ACTIVE"

    with pytest.raises(ValueError):
        validator(portfolio)


def test_invalid_position_collection():

    portfolio = Portfolio(
        portfolio_id="PORT1",
        name="Main",
    )

    portfolio.positions = []

    with pytest.raises(ValueError):
        validator(portfolio)


def test_negative_initial_capital():

    with pytest.raises(ValueError):
        validator(
            Portfolio(
                portfolio_id="PORT1",
                name="Main",
                initial_capital=-1,
            )
        )


def test_negative_cash():

    with pytest.raises(ValueError):
        validator(
            Portfolio(
                portfolio_id="PORT1",
                name="Main",
                cash_balance=-1,
            )
        )


def test_negative_buying_power():

    with pytest.raises(ValueError):
        validator(
            Portfolio(
                portfolio_id="PORT1",
                name="Main",
                buying_power=-1,
            )
        )


def test_negative_margin():

    with pytest.raises(ValueError):
        validator(
            Portfolio(
                portfolio_id="PORT1",
                name="Main",
                margin_used=-1,
            )
        )


def test_invalid_created_at():

    portfolio = Portfolio(
        portfolio_id="PORT1",
        name="Main",
    )

    portfolio.created_at = "today"

    with pytest.raises(ValueError):
        validator(portfolio)


def test_invalid_updated_at():

    portfolio = Portfolio(
        portfolio_id="PORT1",
        name="Main",
    )

    portfolio.updated_at = "today"

    with pytest.raises(ValueError):
        validator(portfolio)


def test_callable_validator():

    portfolio = Portfolio(
        portfolio_id="PORT1",
        name="Main",
    )

    assert validator(portfolio)


def test_valid_enums():

    assert isinstance(
        PortfolioType.LIVE,
        PortfolioType,
    )

    assert isinstance(
        PortfolioStatus.ACTIVE,
        PortfolioStatus,
    )


def test_valid_collection():

    assert isinstance(
        PositionCollection(),
        PositionCollection,
    )


def test_valid_datetime():

    assert isinstance(
        datetime.now(),
        datetime,
    )