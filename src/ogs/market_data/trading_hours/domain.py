"""
OGS Smart Money AI

TradingHours Domain
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime, time

from .enums import (
    TradingHoursStatus,
    TradingHoursType,
)


@dataclass(slots=True)
class TradingHours:
    """
    Trading Hours entity.
    """

    trading_hours_id: str = ""

    exchange: str = ""

    market: str = ""

    session_name: str = ""

    timezone: str = "UTC"

    open_time: time = field(
        default_factory=lambda: time(0, 0)
    )

    close_time: time = field(
        default_factory=lambda: time(0, 0)
    )

    trading_days: list[str] = field(
        default_factory=list
    )

    trading_hours_type: TradingHoursType = (
        TradingHoursType.UNKNOWN
    )

    status: TradingHoursStatus = (
        TradingHoursStatus.UNKNOWN
    )

    active: bool = True

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def is_active(self) -> bool:

        return (
            self.active
            and self.status == TradingHoursStatus.ACTIVE
        )

    @property
    def is_valid(self) -> bool:

        return (
            bool(self.trading_hours_id.strip())
            and bool(self.exchange.strip())
            and bool(self.market.strip())
            and bool(self.session_name.strip())
        )

    @property
    def duration(self) -> int:
        """
        Placeholder duration in minutes.
        """
        return (
            self.close_time.hour * 60
            + self.close_time.minute
            - self.open_time.hour * 60
            - self.open_time.minute
        )

    def to_dict(self) -> dict:

        return {
            "trading_hours_id": self.trading_hours_id,
            "exchange": self.exchange,
            "market": self.market,
            "session_name": self.session_name,
            "timezone": self.timezone,
            "open_time": self.open_time.isoformat(),
            "close_time": self.close_time.isoformat(),
            "trading_days": self.trading_days,
            "trading_hours_type": self.trading_hours_type.value,
            "status": self.status.value,
            "active": self.active,
        }

    def __str__(self) -> str:

        return (
            f"TradingHours("
            f"id='{self.trading_hours_id}', "
            f"exchange='{self.exchange}', "
            f"session='{self.session_name}')"
        )