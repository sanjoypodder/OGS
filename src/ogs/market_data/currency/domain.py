"""
OGS Smart Money AI

Currency Domain
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from .enums import (
    CurrencyStatus,
    CurrencyType,
)


@dataclass(slots=True)
class Currency:
    """
    Represents a currency in the OGS Market Data system.
    """

    currency_code: str = ""
    numeric_code: int = 0
    name: str = ""

    currency_type: CurrencyType = CurrencyType.UNKNOWN
    status: CurrencyStatus = CurrencyStatus.UNKNOWN

    symbol: str = ""
    minor_unit: int = 0

    exchange_rate: float = 1.0

    country: str = ""

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def is_fiat(self) -> bool:
        """
        Return whether the currency is fiat.
        """

        return (
            self.currency_type
            == CurrencyType.FIAT
        )

    @property
    def is_crypto(self) -> bool:
        """
        Return whether the currency is cryptocurrency.
        """

        return (
            self.currency_type
            == CurrencyType.CRYPTO
        )

    @property
    def is_active(self) -> bool:
        """
        Return whether the currency is active.
        """

        return (
            self.status
            == CurrencyStatus.ACTIVE
        )

    @property
    def is_valid(self) -> bool:
        """
        Return whether the currency contains basic valid data.
        """

        return (
            bool(self.currency_code.strip())
            and self.numeric_code > 0
            and bool(self.name.strip())
            and self.minor_unit >= 0
            and self.exchange_rate > 0
        )

    def to_dict(self) -> dict:
        """
        Convert the currency to a dictionary.
        """

        return {
            "currency_code": self.currency_code,
            "numeric_code": self.numeric_code,
            "name": self.name,
            "currency_type": self.currency_type.value,
            "status": self.status.value,
            "symbol": self.symbol,
            "minor_unit": self.minor_unit,
            "exchange_rate": self.exchange_rate,
            "country": self.country,
        }

    def __str__(self) -> str:
        return (
            f"Currency("
            f"code='{self.currency_code}', "
            f"name='{self.name}', "
            f"type='{self.currency_type.value}', "
            f"status='{self.status.value}')"
        )