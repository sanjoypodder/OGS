"""
OGS Smart Money AI

Portfolio Validator
"""

from __future__ import annotations

from datetime import datetime

from ogs.framework import BaseValidator
from ogs.market_data.position import PositionCollection

from .domain import Portfolio
from .enums import (
    PortfolioStatus,
    PortfolioType,
)


class PortfolioValidator(BaseValidator):
    """
    Validator for Portfolio objects.
    """

    def validate(
        self,
        portfolio: Portfolio,
    ) -> bool:

        if not isinstance(
            portfolio,
            Portfolio,
        ):
            raise TypeError(
                "Expected Portfolio."
            )

        if not portfolio.portfolio_id:
            raise ValueError(
                "Portfolio ID cannot be empty."
            )

        if not portfolio.name:
            raise ValueError(
                "Portfolio name cannot be empty."
            )

        if not isinstance(
            portfolio.portfolio_type,
            PortfolioType,
        ):
            raise ValueError(
                "Invalid PortfolioType."
            )

        if not isinstance(
            portfolio.status,
            PortfolioStatus,
        ):
            raise ValueError(
                "Invalid PortfolioStatus."
            )

        if not isinstance(
            portfolio.positions,
            PositionCollection,
        ):
            raise ValueError(
                "Invalid PositionCollection."
            )

        if portfolio.initial_capital < 0:
            raise ValueError(
                "Initial capital cannot be negative."
            )

        if portfolio.cash_balance < 0:
            raise ValueError(
                "Cash balance cannot be negative."
            )

        if portfolio.buying_power < 0:
            raise ValueError(
                "Buying power cannot be negative."
            )

        if portfolio.margin_used < 0:
            raise ValueError(
                "Margin used cannot be negative."
            )

        if not isinstance(
            portfolio.created_at,
            datetime,
        ):
            raise ValueError(
                "Invalid created_at."
            )

        if not isinstance(
            portfolio.updated_at,
            datetime,
        ):
            raise ValueError(
                "Invalid updated_at."
            )

        return True

    def __call__(
        self,
        portfolio: Portfolio,
    ) -> bool:

        return self.validate(portfolio)