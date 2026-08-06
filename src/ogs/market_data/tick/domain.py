"""
OGS Smart Money AI

Tick Domain Model
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from .enums import ProviderType


@dataclass(slots=True, frozen=True)
class Tick:
    """
    Represents one market tick.
    """

    symbol: str

    timestamp: datetime

    bid: float

    ask: float

    last: float

    volume: float

    provider: ProviderType = ProviderType.UNKNOWN

    @property
    def spread(self) -> float:
        """
        Ask-Bid spread.
        """
        return self.ask - self.bid

    @property
    def mid_price(self) -> float:
        """
        Mid price.
        """
        return (self.bid + self.ask) / 2

    @property
    def is_buy_tick(self) -> bool:
        """
        Last traded above mid price.
        """
        return self.last >= self.mid_price

    @property
    def is_sell_tick(self) -> bool:
        """
        Last traded below mid price.
        """
        return self.last < self.mid_price

    @property
    def has_volume(self) -> bool:
        """
        Returns True if volume exists.
        """
        return self.volume > 0

    @property
    def is_valid(self) -> bool:
        """
        Performs lightweight validation.
        """
        return (
            bool(self.symbol)
            and self.bid >= 0
            and self.ask >= 0
            and self.last >= 0
            and self.volume >= 0
            and self.ask >= self.bid
        )

    def to_dict(self) -> dict:
        """
        Convert Tick to dictionary.
        """
        return {
            "symbol": self.symbol,
            "timestamp": self.timestamp,
            "bid": self.bid,
            "ask": self.ask,
            "last": self.last,
            "volume": self.volume,
            "provider": self.provider.value,
        }

    def __str__(self) -> str:
        return (
            f"{self.symbol} "
            f"Bid={self.bid} "
            f"Ask={self.ask} "
            f"Last={self.last}"
        )

    def __repr__(self) -> str:
        return (
            f"Tick("
            f"symbol='{self.symbol}', "
            f"bid={self.bid}, "
            f"ask={self.ask}, "
            f"last={self.last}, "
            f"volume={self.volume})"
        )