"""
OGS Smart Money AI

Portfolio Domain
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime

from ogs.market_data.position import (
    Position,
    PositionCollection,
)

from .enums import (
    PortfolioStatus,
    PortfolioType,
)


@dataclass(slots=True)
class Portfolio:
    """
    Represents a trading portfolio.
    """

    portfolio_id: str = ""

    name: str = ""

    portfolio_type: PortfolioType = PortfolioType.UNKNOWN

    status: PortfolioStatus = PortfolioStatus.UNKNOWN

    base_currency: str = "USD"

    initial_capital: float = 0.0

    cash_balance: float = 0.0

    buying_power: float = 0.0

    margin_used: float = 0.0

    positions: PositionCollection = field(
        default_factory=PositionCollection
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def position_count(self) -> int:
        return len(self.positions)

    @property
    def market_value(self) -> float:
        return sum(
            position.market_value
            for position in self.positions
        )

    @property
    def cost_basis(self) -> float:
        return sum(
            position.cost_basis
            for position in self.positions
        )

    @property
    def total_realized_pnl(self) -> float:
        return sum(
            position.realized_pnl
            for position in self.positions
        )

    @property
    def total_unrealized_pnl(self) -> float:
        return sum(
            position.unrealized_pnl
            for position in self.positions
        )

    @property
    def total_pnl(self) -> float:
        return (
            self.total_realized_pnl
            + self.total_unrealized_pnl
        )

    @property
    def equity(self) -> float:
        return (
            self.cash_balance
            + self.market_value
        )

    @property
    def available_cash(self) -> float:
        return (
            self.cash_balance
            - self.margin_used
        )

    @property
    def margin_available(self) -> float:
        return max(
            0.0,
            self.buying_power - self.margin_used,
        )

    @property
    def gross_exposure(self) -> float:
        return sum(
            abs(position.market_value)
            for position in self.positions
        )

    @property
    def long_exposure(self) -> float:
        return sum(
            position.market_value
            for position in self.positions
            if position.is_long
        )

    @property
    def short_exposure(self) -> float:
        return sum(
            position.market_value
            for position in self.positions
            if position.is_short
        )

    @property
    def net_exposure(self) -> float:
        return (
            self.long_exposure
            - self.short_exposure
        )

    @property
    def return_percentage(self) -> float:

        if self.initial_capital <= 0:
            return 0.0

        return (
            self.total_pnl
            / self.initial_capital
        ) * 100

    @property
    def is_active(self) -> bool:
        return self.status == PortfolioStatus.ACTIVE

    @property
    def is_valid(self) -> bool:
        return (
            self.initial_capital >= 0
            and self.cash_balance >= 0
            and self.buying_power >= 0
            and self.margin_used >= 0
        )

    def add_position(
        self,
        position: Position,
    ) -> None:
        self.positions.append(position)

    def to_dict(self) -> dict:

        return {
            "portfolio_id": self.portfolio_id,
            "name": self.name,
            "portfolio_type": self.portfolio_type.value,
            "status": self.status.value,
            "base_currency": self.base_currency,
            "initial_capital": self.initial_capital,
            "cash_balance": self.cash_balance,
            "buying_power": self.buying_power,
            "margin_used": self.margin_used,
            "position_count": self.position_count,
            "market_value": self.market_value,
            "cost_basis": self.cost_basis,
            "equity": self.equity,
            "total_realized_pnl": self.total_realized_pnl,
            "total_unrealized_pnl": self.total_unrealized_pnl,
            "total_pnl": self.total_pnl,
            "return_percentage": self.return_percentage,
            "gross_exposure": self.gross_exposure,
            "net_exposure": self.net_exposure,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __str__(self) -> str:

        return (
            f"Portfolio("
            f"id={self.portfolio_id}, "
            f"name={self.name}, "
            f"positions={self.position_count})"
        )