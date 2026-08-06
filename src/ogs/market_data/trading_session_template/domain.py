"""
===========================================================

OGS Smart Money AI

TradingSessionTemplate Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime, time

from .enums import (
    TradingSessionTemplateStatus,
    TradingSessionTemplateType,
)


@dataclass(slots=True)
class TradingSessionTemplate:
    """
    Trading session template entity.
    """

    trading_session_template_id: str = ""

    template_name: str = ""

    exchange: str = ""

    market: str = ""

    timezone: str = ""

    open_time: time = field(
        default_factory=lambda: time(9, 15)
    )

    close_time: time = field(
        default_factory=lambda: time(15, 30)
    )

    trading_days: list[str] = field(
        default_factory=lambda: [
            "MON",
            "TUE",
            "WED",
            "THU",
            "FRI",
        ]
    )

    description: str = ""

    session_type: TradingSessionTemplateType = (
        TradingSessionTemplateType.UNKNOWN
    )

    status: TradingSessionTemplateStatus = (
        TradingSessionTemplateStatus.UNKNOWN
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
            and self.status
            == TradingSessionTemplateStatus.ACTIVE
        )

    @property
    def is_valid(self) -> bool:

        return (
            bool(
                self.trading_session_template_id.strip()
            )
            and bool(self.template_name.strip())
            and bool(self.exchange.strip())
            and bool(self.market.strip())
            and bool(self.timezone.strip())
        )

    def to_dict(self) -> dict:

        return {
            "trading_session_template_id":
                self.trading_session_template_id,
            "template_name":
                self.template_name,
            "exchange":
                self.exchange,
            "market":
                self.market,
            "timezone":
                self.timezone,
            "open_time":
                self.open_time.isoformat(),
            "close_time":
                self.close_time.isoformat(),
            "trading_days":
                self.trading_days,
            "description":
                self.description,
            "session_type":
                self.session_type.value,
            "status":
                self.status.value,
            "active":
                self.active,
        }

    def __str__(self) -> str:

        return (
            "TradingSessionTemplate("
            f"id='{self.trading_session_template_id}', "
            f"name='{self.template_name}')"
        )