"""
OGS Smart Money AI

Account Domain
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime

from ogs.market_data.portfolio import (
    Portfolio,
    PortfolioCollection,
)

from .enums import (
    AccountStatus,
    AccountType,
)


@dataclass(slots=True)
class Account:
    """
    Represents a brokerage trading account.
    """

    account_id: str = ""

    name: str = ""

    broker: str = ""

    account_number: str = ""

    account_type: AccountType = AccountType.UNKNOWN

    status: AccountStatus = AccountStatus.UNKNOWN

    base_currency: str = "USD"

    initial_balance: float = 0.0

    cash_balance: float = 0.0

    buying_power: float = 0.0

    margin_used: float = 0.0

    leverage: float = 1.0

    portfolios: PortfolioCollection = field(
        default_factory=PortfolioCollection
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def portfolio_count(self) -> int:
        return len(self.portfolios)

    @property
    def total_market_value(self) -> float:
        return sum(
            portfolio.market_value
            for portfolio in self.portfolios
        )

    @property
    def total_cash(self) -> float:
        return (
            self.cash_balance
            + sum(
                portfolio.cash_balance
                for portfolio in self.portfolios
            )
        )

    @property
    def total_equity(self) -> float:
        return (
            self.cash_balance
            + sum(
                portfolio.equity
                for portfolio in self.portfolios
            )
        )

    @property
    def total_realized_pnl(self) -> float:
        return sum(
            portfolio.total_realized_pnl
            for portfolio in self.portfolios
        )

    @property
    def total_unrealized_pnl(self) -> float:
        return sum(
            portfolio.total_unrealized_pnl
            for portfolio in self.portfolios
        )

    @property
    def total_pnl(self) -> float:
        return (
            self.total_realized_pnl
            + self.total_unrealized_pnl
        )

    @property
    def available_margin(self) -> float:
        return max(
            0.0,
            self.buying_power - self.margin_used,
        )

    @property
    def return_percentage(self) -> float:

        if self.initial_balance <= 0:
            return 0.0

        return (
            self.total_pnl
            / self.initial_balance
        ) * 100

    @property
    def is_active(self) -> bool:
        return self.status == AccountStatus.ACTIVE

    @property
    def is_valid(self) -> bool:
        return (
            self.initial_balance >= 0
            and self.cash_balance >= 0
            and self.buying_power >= 0
            and self.margin_used >= 0
            and self.leverage > 0
        )

    def add_portfolio(
        self,
        portfolio: Portfolio,
    ) -> None:
        self.portfolios.append(portfolio)

    def to_dict(self) -> dict:

        return {
            "account_id": self.account_id,
            "name": self.name,
            "broker": self.broker,
            "account_number": self.account_number,
            "account_type": self.account_type.value,
            "status": self.status.value,
            "base_currency": self.base_currency,
            "initial_balance": self.initial_balance,
            "cash_balance": self.cash_balance,
            "buying_power": self.buying_power,
            "margin_used": self.margin_used,
            "leverage": self.leverage,
            "portfolio_count": self.portfolio_count,
            "total_market_value": self.total_market_value,
            "total_cash": self.total_cash,
            "total_equity": self.total_equity,
            "total_realized_pnl": self.total_realized_pnl,
            "total_unrealized_pnl": self.total_unrealized_pnl,
            "total_pnl": self.total_pnl,
            "available_margin": self.available_margin,
            "return_percentage": self.return_percentage,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __str__(self) -> str:

        return (
            f"Account("
            f"id={self.account_id}, "
            f"name={self.name}, "
            f"broker={self.broker}, "
            f"portfolios={self.portfolio_count})"
        )