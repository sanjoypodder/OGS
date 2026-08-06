"""
OGS Smart Money AI

Trade Domain
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime

from .enums import (
    TradeSide,
    TradeStatus,
)


@dataclass(slots=True)
class Trade:
    """
    Represents an executed trade.
    """

    trade_id: str = ""

    provider: str = ""
    exchange: str = ""
    symbol: str = ""

    side: TradeSide = TradeSide.UNKNOWN
    status: TradeStatus = TradeStatus.UNKNOWN

    price: float = 0.0
    quantity: float = 0.0
    fees: float = 0.0

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def value(self) -> float:
        return self.price * self.quantity

    @property
    def total_cost(self) -> float:
        return self.value + self.fees

    @property
    def is_buy(self) -> bool:
        return self.side == TradeSide.BUY

    @property
    def is_sell(self) -> bool:
        return self.side == TradeSide.SELL

    @property
    def is_filled(self) -> bool:
        return self.status == TradeStatus.FILLED

    @property
    def is_valid(self) -> bool:
        return (
            self.price >= 0
            and self.quantity >= 0
            and self.fees >= 0
        )

    def to_dict(self) -> dict:
        return {
            "trade_id": self.trade_id,
            "provider": self.provider,
            "exchange": self.exchange,
            "symbol": self.symbol,
            "side": self.side.value,
            "status": self.status.value,
            "price": self.price,
            "quantity": self.quantity,
            "fees": self.fees,
            "value": self.value,
            "total_cost": self.total_cost,
            "timestamp": self.timestamp,
        }

    def __str__(self) -> str:
        return (
            f"Trade("
            f"id={self.trade_id}, "
            f"symbol={self.symbol}, "
            f"side={self.side.value}, "
            f"price={self.price}, "
            f"qty={self.quantity})"
        )