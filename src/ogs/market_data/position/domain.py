"""
OGS Smart Money AI

Position Domain
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime

from .enums import (
    PositionSide,
    PositionStatus,
)


@dataclass(slots=True)
class Position:
    """
    Represents a trading position.
    """

    position_id: str = ""

    provider: str = ""
    exchange: str = ""
    symbol: str = ""

    side: PositionSide = PositionSide.UNKNOWN
    status: PositionStatus = PositionStatus.UNKNOWN

    quantity: float = 0.0

    average_entry_price: float = 0.0
    current_price: float = 0.0

    realized_pnl: float = 0.0

    opened_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    closed_at: datetime | None = None

    @property
    def cost_basis(self) -> float:
        return self.average_entry_price * self.quantity

    @property
    def market_value(self) -> float:
        return self.current_price * self.quantity

    @property
    def unrealized_pnl(self) -> float:
        if self.side == PositionSide.SHORT:
            return (
                self.average_entry_price
                - self.current_price
            ) * self.quantity

        return (
            self.current_price
            - self.average_entry_price
        ) * self.quantity

    @property
    def total_pnl(self) -> float:
        return (
            self.realized_pnl
            + self.unrealized_pnl
        )

    @property
    def return_percentage(self) -> float:

        if self.cost_basis == 0:
            return 0.0

        return (
            self.total_pnl
            / self.cost_basis
        ) * 100

    @property
    def is_long(self) -> bool:
        return self.side == PositionSide.LONG

    @property
    def is_short(self) -> bool:
        return self.side == PositionSide.SHORT

    @property
    def is_open(self) -> bool:
        return self.status == PositionStatus.OPEN

    @property
    def is_closed(self) -> bool:
        return self.status == PositionStatus.CLOSED

    @property
    def is_valid(self) -> bool:
        return (
            self.quantity >= 0
            and self.average_entry_price >= 0
            and self.current_price >= 0
        )

    def to_dict(self) -> dict:

        return {
            "position_id": self.position_id,
            "provider": self.provider,
            "exchange": self.exchange,
            "symbol": self.symbol,
            "side": self.side.value,
            "status": self.status.value,
            "quantity": self.quantity,
            "average_entry_price": self.average_entry_price,
            "current_price": self.current_price,
            "cost_basis": self.cost_basis,
            "market_value": self.market_value,
            "realized_pnl": self.realized_pnl,
            "unrealized_pnl": self.unrealized_pnl,
            "total_pnl": self.total_pnl,
            "return_percentage": self.return_percentage,
            "opened_at": self.opened_at,
            "closed_at": self.closed_at,
        }

    def __str__(self) -> str:

        return (
            f"Position("
            f"id={self.position_id}, "
            f"symbol={self.symbol}, "
            f"side={self.side.value}, "
            f"qty={self.quantity})"
        )