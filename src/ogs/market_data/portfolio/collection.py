"""
OGS Smart Money AI

Portfolio Collection
"""

from __future__ import annotations

from ogs.framework import BaseCollection

from .domain import Portfolio
from .enums import (
    PortfolioStatus,
    PortfolioType,
)


class PortfolioCollection(BaseCollection[Portfolio]):
    """
    Collection of Portfolio objects.
    """

    def __init__(self, items=None):
        super().__init__(items)

    @property
    def items(self) -> list[Portfolio]:
        """
        Compatibility property.
        """
        return self._items

    def add(
        self,
        portfolio: Portfolio,
    ) -> None:
        self.append(portfolio)

    def active(self) -> list[Portfolio]:
        return [
            portfolio
            for portfolio in self
            if portfolio.status == PortfolioStatus.ACTIVE
        ]

    def inactive(self) -> list[Portfolio]:
        return [
            portfolio
            for portfolio in self
            if portfolio.status == PortfolioStatus.INACTIVE
        ]

    def live(self) -> list[Portfolio]:
        return [
            portfolio
            for portfolio in self
            if portfolio.portfolio_type == PortfolioType.LIVE
        ]

    def paper(self) -> list[Portfolio]:
        return [
            portfolio
            for portfolio in self
            if portfolio.portfolio_type == PortfolioType.PAPER
        ]

    def backtest(self) -> list[Portfolio]:
        return [
            portfolio
            for portfolio in self
            if portfolio.portfolio_type == PortfolioType.BACKTEST
        ]

    def find(
        self,
        portfolio_id: str,
    ) -> Portfolio | None:

        return next(
            (
                portfolio
                for portfolio in self
                if portfolio.portfolio_id == portfolio_id
            ),
            None,
        )

    def total_equity(self) -> float:
        return sum(
            portfolio.equity
            for portfolio in self
        )

    def total_market_value(self) -> float:
        return sum(
            portfolio.market_value
            for portfolio in self
        )

    def total_cash(self) -> float:
        return sum(
            portfolio.cash_balance
            for portfolio in self
        )

    def total_realized_pnl(self) -> float:
        return sum(
            portfolio.total_realized_pnl
            for portfolio in self
        )

    def total_unrealized_pnl(self) -> float:
        return sum(
            portfolio.total_unrealized_pnl
            for portfolio in self
        )

    def total_pnl(self) -> float:
        return sum(
            portfolio.total_pnl
            for portfolio in self
        )

    def to_list(self) -> list[dict]:
        return [
            portfolio.to_dict()
            for portfolio in self
        ]