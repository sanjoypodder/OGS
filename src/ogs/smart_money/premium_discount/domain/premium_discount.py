"""
OGS FinOS

Premium / Discount Domain Model

Represents the Premium / Discount state of a completed
dealing range.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from decimal import Decimal
from typing import Any
from uuid import uuid4

from ogs.smart_money.premium_discount.enums.premium_discount_zone import (
    PremiumDiscountZone,
)


@dataclass(frozen=True, slots=True)
class PremiumDiscount:
    """
    Represents the Premium / Discount state of a dealing range.

    Premium:
        Price above equilibrium.

    Equilibrium:
        Price at the midpoint of the dealing range.

    Discount:
        Price below equilibrium.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    range_high: Decimal = Decimal("0")

    range_low: Decimal = Decimal("0")

    equilibrium: Decimal = Decimal("0")

    current_price: Decimal = Decimal("0")

    zone: PremiumDiscountZone = PremiumDiscountZone.EQUILIBRIUM

    confidence: float = 1.0

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def range_size(self) -> Decimal:
        """
        Total size of the dealing range.
        """
        return self.range_high - self.range_low

    @property
    def premium_boundary(self) -> Decimal:
        """
        Upper 50% boundary (equilibrium).
        """
        return self.equilibrium

    @property
    def discount_boundary(self) -> Decimal:
        """
        Lower 50% boundary (equilibrium).
        """
        return self.equilibrium

    @property
    def is_premium(self) -> bool:
        """
        Returns True if current price is in Premium.
        """
        return self.zone == PremiumDiscountZone.PREMIUM

    @property
    def is_discount(self) -> bool:
        """
        Returns True if current price is in Discount.
        """
        return self.zone == PremiumDiscountZone.DISCOUNT

    @property
    def is_equilibrium(self) -> bool:
        """
        Returns True if current price is at Equilibrium.
        """
        return self.zone == PremiumDiscountZone.EQUILIBRIUM

    def __str__(self) -> str:
        return (
            f"PremiumDiscount("
            f"zone={self.zone.value}, "
            f"price={self.current_price}, "
            f"range=[{self.range_low}, {self.range_high}], "
            f"equilibrium={self.equilibrium})"
        )

    def __repr__(self) -> str:
        return self.__str__()