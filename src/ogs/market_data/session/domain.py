"""
===========================================================

OGS Smart Money AI

Session Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime, time

from .enums import (
    SessionStatus,
    SessionType,
)


@dataclass(slots=True)
class Session:
    """
    Trading Session.
    """

    session_id: str = ""

    name: str = ""

    exchange: str = ""

    market: str = ""

    session_type: SessionType = SessionType.UNKNOWN

    status: SessionStatus = SessionStatus.CLOSED

    start_time: time | None = None

    end_time: time | None = None

    timezone: str = "UTC"

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
            and self.status == SessionStatus.OPEN
        )

    @property
    def is_valid(self) -> bool:

        return (
            bool(self.session_id.strip())
            and bool(self.name.strip())
            and bool(self.exchange.strip())
            and bool(self.market.strip())
        )

    def to_dict(self) -> dict:

        return {
            "session_id": self.session_id,
            "name": self.name,
            "exchange": self.exchange,
            "market": self.market,
            "session_type": self.session_type.value,
            "status": self.status.value,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "timezone": self.timezone,
            "active": self.active,
        }

    def __str__(self):

        return (
            f"Session("
            f"id='{self.session_id}', "
            f"name='{self.name}')"
        )