"""
===========================================================

OGS Smart Money AI

Settlement Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime, time

from .enums import (
    SettlementCycle,
    SettlementMethod,
    SettlementStatus,
    SettlementType,
)


@dataclass(slots=True)
class Settlement:
    """
    Settlement entity.
    """

    settlement_id: str = ""

    exchange: str = ""

    market: str = ""

    instrument: str = ""

    settlement_cycle: SettlementCycle = (
        SettlementCycle.UNKNOWN
    )

    settlement_method: SettlementMethod = (
        SettlementMethod.UNKNOWN
    )

    settlement_currency: str = ""

    cutoff_time: time = field(
        default_factory=lambda: time(0, 0)
    )

    settlement_location: str = ""

    settlement_type: SettlementType = (
        SettlementType.UNKNOWN
    )

    status: SettlementStatus = (
        SettlementStatus.UNKNOWN
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
            and self.status == SettlementStatus.ACTIVE
        )

    @property
    def is_valid(self) -> bool:

        return (
            bool(self.settlement_id.strip())
            and bool(self.exchange.strip())
            and bool(self.market.strip())
            and bool(self.instrument.strip())
        )

    def to_dict(self) -> dict:

        return {
            "settlement_id": self.settlement_id,
            "exchange": self.exchange,
            "market": self.market,
            "instrument": self.instrument,
            "settlement_cycle": self.settlement_cycle.value,
            "settlement_method": self.settlement_method.value,
            "settlement_currency": self.settlement_currency,
            "cutoff_time": self.cutoff_time.isoformat(),
            "settlement_location": self.settlement_location,
            "settlement_type": self.settlement_type.value,
            "status": self.status.value,
            "active": self.active,
        }

    def __str__(self) -> str:

        return (
            f"Settlement("
            f"id='{self.settlement_id}', "
            f"instrument='{self.instrument}')"
        )