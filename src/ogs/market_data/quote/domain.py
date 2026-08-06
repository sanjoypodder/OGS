"""
OGS Smart Money AI

Quote Domain
"""

from __future__ import annotations

from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime

from .enums import (
    QuoteStatus,
    QuoteType,
)


@dataclass(slots=True)
class Quote:
    """
    Represents a market quote.
    """

    name: str = ""

    provider: str = ""
    exchange: str = ""
    symbol: str = ""

    bid: float = 0.0
    ask: float = 0.0
    last: float = 0.0

    bid_size: int = 0
    ask_size: int = 0

    open: float = 0.0
    high: float = 0.0
    low: float = 0.0
    close: float = 0.0

    volume: int = 0

    quote_type: QuoteType = QuoteType.UNKNOWN
    status: QuoteStatus = QuoteStatus.UNKNOWN

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def spread(self) -> float:
        return self.ask - self.bid

    @property
    def mid_price(self) -> float:
        if self.bid == 0 and self.ask == 0:
            return 0.0
        return (self.bid + self.ask) / 2

    @property
    def is_live(self) -> bool:
        return self.quote_type == QuoteType.LIVE

    @property
    def is_stale(self) -> bool:
        return self.status == QuoteStatus.STALE

    @property
    def is_valid(self) -> bool:
        return (
            bool(self.name.strip())
            and self.bid >= 0
            and self.ask >= 0
            and self.last >= 0
            and self.volume >= 0
        )

    def to_dict(self) -> dict:
        data = asdict(self)
        data["quote_type"] = self.quote_type.value
        data["status"] = self.status.value
        data["timestamp"] = self.timestamp.isoformat()
        return data

    def __str__(self) -> str:
        return (
            f"Quote("
            f"name='{self.name}', "
            f"symbol='{self.symbol}', "
            f"last={self.last})"
        )