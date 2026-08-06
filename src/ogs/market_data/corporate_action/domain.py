"""
===========================================================

OGS Smart Money AI

Corporate Action Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, date, datetime

from .enums import (
    CorporateActionStatus,
    CorporateActionType,
)


@dataclass(slots=True)
class CorporateAction:
    """
    Corporate Action.
    """

    action_id: str = ""

    symbol: str = ""

    exchange: str = ""

    market: str = ""

    action_type: CorporateActionType = (
        CorporateActionType.UNKNOWN
    )

    status: CorporateActionStatus = (
        CorporateActionStatus.UNKNOWN
    )

    announcement_date: date | None = None

    record_date: date | None = None

    ex_date: date | None = None

    effective_date: date | None = None

    ratio: float = 1.0

    cash_amount: float = 0.0

    currency: str = "USD"

    description: str = ""

    active: bool = True

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def is_effective(self) -> bool:

        return (
            self.status
            == CorporateActionStatus.EFFECTIVE
        )

    @property
    def is_valid(self) -> bool:

        return (
            bool(self.action_id.strip())
            and bool(self.symbol.strip())
            and bool(self.exchange.strip())
            and bool(self.market.strip())
        )

    def to_dict(self) -> dict:

        return {
            "action_id": self.action_id,
            "symbol": self.symbol,
            "exchange": self.exchange,
            "market": self.market,
            "action_type": self.action_type.value,
            "status": self.status.value,
            "announcement_date": self.announcement_date,
            "record_date": self.record_date,
            "ex_date": self.ex_date,
            "effective_date": self.effective_date,
            "ratio": self.ratio,
            "cash_amount": self.cash_amount,
            "currency": self.currency,
            "description": self.description,
            "active": self.active,
        }

    def __str__(self) -> str:

        return (
            f"CorporateAction("
            f"id='{self.action_id}', "
            f"symbol='{self.symbol}')"
        )