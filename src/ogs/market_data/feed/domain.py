"""
OGS Smart Money AI

Feed Domain
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from .enums import (
    FeedStatus,
    FeedType,
)


@dataclass(slots=True, frozen=True)
class Feed:
    """
    Represents a market data feed.
    """

    name: str

    feed_type: FeedType = FeedType.UNKNOWN

    status: FeedStatus = FeedStatus.UNKNOWN

    provider: str = ""

    symbol: str = ""

    timeframe: str = ""

    latency_ms: float = 0.0

    update_count: int = 0

    last_price: float = 0.0

    last_updated: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def connected(self) -> bool:
        return self.status == FeedStatus.CONNECTED

    @property
    def disconnected(self) -> bool:
        return self.status == FeedStatus.DISCONNECTED

    @property
    def healthy(self) -> bool:
        return (
            self.connected
            and self.latency_ms >= 0
        )

    @property
    def is_valid(self) -> bool:
        return bool(self.name.strip())

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "feed_type": self.feed_type.value,
            "status": self.status.value,
            "provider": self.provider,
            "symbol": self.symbol,
            "timeframe": self.timeframe,
            "latency_ms": self.latency_ms,
            "update_count": self.update_count,
            "last_price": self.last_price,
            "last_updated": self.last_updated.isoformat(),
        }

    def __str__(self) -> str:
        return (
            f"{self.name} "
            f"[{self.feed_type.value}] "
            f"{self.status.value}"
        )