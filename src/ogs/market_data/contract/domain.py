"""
OGS Smart Money AI

Contract Domain
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from .enums import (
    ContractStatus,
    ContractType,
    ExerciseStyle,
    OptionType,
    SettlementType,
)


@dataclass(slots=True)
class Contract:
    """
    Tradable contract.
    """

    contract_id: str = ""

    instrument_id: str = ""

    contract_symbol: str = ""

    exchange: str = ""

    underlying: str = ""

    contract_type: ContractType = ContractType.UNKNOWN

    option_type: OptionType = OptionType.NONE

    settlement_type: SettlementType = SettlementType.UNKNOWN

    exercise_style: ExerciseStyle = ExerciseStyle.UNKNOWN

    status: ContractStatus = ContractStatus.ACTIVE

    expiry: datetime | None = None

    strike_price: float = 0.0

    multiplier: float = 1.0

    tick_size: float = 0.01

    lot_size: int = 1

    currency: str = "USD"

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
            and self.status == ContractStatus.ACTIVE
        )

    @property
    def is_tradable(self) -> bool:
        return (
            self.is_active
            and self.contract_type != ContractType.UNKNOWN
        )

    @property
    def is_valid(self) -> bool:
        return (
            bool(self.contract_id.strip())
            and bool(self.instrument_id.strip())
            and bool(self.contract_symbol.strip())
            and bool(self.exchange.strip())
            and bool(self.underlying.strip())
        )

    def to_dict(self) -> dict:

        return {
            "contract_id": self.contract_id,
            "instrument_id": self.instrument_id,
            "contract_symbol": self.contract_symbol,
            "exchange": self.exchange,
            "underlying": self.underlying,
            "contract_type": self.contract_type.value,
            "option_type": self.option_type.value,
            "settlement_type": self.settlement_type.value,
            "exercise_style": self.exercise_style.value,
            "status": self.status.value,
            "expiry": self.expiry,
            "strike_price": self.strike_price,
            "multiplier": self.multiplier,
            "tick_size": self.tick_size,
            "lot_size": self.lot_size,
            "currency": self.currency,
            "active": self.active,
        }

    def __str__(self) -> str:

        return (
            f"Contract("
            f"id='{self.contract_id}', "
            f"symbol='{self.contract_symbol}')"
        )