"""
OGS Smart Money AI

Instrument Domain
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from .enums import (
    InstrumentStatus,
    InstrumentType,
)


@dataclass(slots=True)
class Instrument:
    """
    Tradable financial instrument.
    """

    instrument_id: str = ""

    symbol: str = ""
    exchange: str = ""
    asset: str = ""
    market: str = ""

    name: str = ""

    instrument_type: InstrumentType = InstrumentType.UNKNOWN
    status: InstrumentStatus = InstrumentStatus.ACTIVE

    currency: str = "USD"

    tick_size: float = 0.01
    lot_size: int = 1

    isin: str = ""

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
            and self.status == InstrumentStatus.ACTIVE
        )

    @property
    def is_tradable(self) -> bool:
        return (
            self.is_active
            and self.instrument_type != InstrumentType.UNKNOWN
        )

    @property
    def is_valid(self) -> bool:
        return (
            bool(self.instrument_id.strip())
            and bool(self.symbol.strip())
            and bool(self.exchange.strip())
            and bool(self.asset.strip())
            and bool(self.name.strip())
        )

    def to_dict(self) -> dict:

        return {
            "instrument_id": self.instrument_id,
            "symbol": self.symbol,
            "exchange": self.exchange,
            "asset": self.asset,
            "market": self.market,
            "name": self.name,
            "instrument_type": self.instrument_type.value,
            "status": self.status.value,
            "currency": self.currency,
            "tick_size": self.tick_size,
            "lot_size": self.lot_size,
            "isin": self.isin,
            "active": self.active,
        }

    def __str__(self) -> str:

        return (
            f"Instrument("
            f"id='{self.instrument_id}', "
            f"symbol='{self.symbol}', "
            f"exchange='{self.exchange}')"
        )