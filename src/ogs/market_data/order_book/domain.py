"""
OGS Smart Money AI

OrderBook Domain
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime

from .enums import (
    OrderBookStatus,
    OrderBookType,
)


@dataclass(slots=True)
class OrderBook:
    """
    Represents an order book snapshot.
    """

    name: str = ""

    provider: str = ""
    exchange: str = ""
    symbol: str = ""

    best_bid: float = 0.0
    best_ask: float = 0.0

    bid_levels: list[tuple[float, float]] = field(default_factory=list)
    ask_levels: list[tuple[float, float]] = field(default_factory=list)

    orderbook_type: OrderBookType = OrderBookType.UNKNOWN
    status: OrderBookStatus = OrderBookStatus.UNKNOWN

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def spread(self) -> float:
        return self.best_ask - self.best_bid

    @property
    def mid_price(self) -> float:
        if self.best_bid == 0 and self.best_ask == 0:
            return 0.0
        return (self.best_bid + self.best_ask) / 2

    @property
    def total_bid_volume(self) -> float:
        return sum(volume for _, volume in self.bid_levels)

    @property
    def total_ask_volume(self) -> float:
        return sum(volume for _, volume in self.ask_levels)

    @property
    def imbalance_ratio(self) -> float:
        total = self.total_bid_volume + self.total_ask_volume

        if total == 0:
            return 0.0

        return self.total_bid_volume / total

    @property
    def is_live(self) -> bool:
        return self.orderbook_type == OrderBookType.LIVE

    @property
    def is_valid(self) -> bool:
        return (
            self.best_bid >= 0
            and self.best_ask >= 0
            and self.best_ask >= self.best_bid
        )

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "provider": self.provider,
            "exchange": self.exchange,
            "symbol": self.symbol,
            "best_bid": self.best_bid,
            "best_ask": self.best_ask,
            "bid_levels": self.bid_levels,
            "ask_levels": self.ask_levels,
            "orderbook_type": self.orderbook_type.value,
            "status": self.status.value,
            "timestamp": self.timestamp,
        }

    def __str__(self) -> str:
        return (
            f"OrderBook("
            f"name={self.name}, "
            f"symbol={self.symbol}, "
            f"bid={self.best_bid}, "
            f"ask={self.best_ask})"
        )