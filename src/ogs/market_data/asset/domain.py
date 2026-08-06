"""
OGS Smart Money AI

Asset Domain
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from .enums import AssetType


@dataclass(slots=True)
class Asset:
    """
    Represents a financial asset.
    """

    asset_id: str = ""
    symbol: str = ""
    name: str = ""

    asset_type: AssetType = AssetType.UNKNOWN

    currency: str = "USD"
    country: str = ""

    isin: str = ""
    cusip: str = ""

    active: bool = True

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def is_active(self) -> bool:
        return self.active

    @property
    def is_tradable(self) -> bool:
        return (
            self.active
            and self.asset_type != AssetType.UNKNOWN
        )

    @property
    def is_valid(self) -> bool:
        return (
            bool(self.asset_id.strip())
            and bool(self.symbol.strip())
            and bool(self.name.strip())
        )

    def to_dict(self) -> dict:
        return {
            "asset_id": self.asset_id,
            "symbol": self.symbol,
            "name": self.name,
            "asset_type": self.asset_type.value,
            "currency": self.currency,
            "country": self.country,
            "isin": self.isin,
            "cusip": self.cusip,
            "active": self.active,
        }

    def __str__(self) -> str:
        return (
            f"Asset("
            f"id='{self.asset_id}', "
            f"symbol='{self.symbol}', "
            f"type='{self.asset_type.value}')"
        )