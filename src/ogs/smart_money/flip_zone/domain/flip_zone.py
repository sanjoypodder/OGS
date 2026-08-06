"""
OGS FinOS

Flip Zone Domain Model

Represents a confirmed Support ↔ Resistance role reversal.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from decimal import Decimal
from typing import Any
from uuid import uuid4

from ogs.smart_money.flip_zone.enums.flip_zone_status import FlipZoneStatus
from ogs.smart_money.flip_zone.enums.flip_zone_type import FlipZoneType


@dataclass(frozen=True, slots=True)
class FlipZone:
    """
    Represents a confirmed Flip Zone.

    A Flip Zone is formed when a previous support becomes resistance
    or a previous resistance becomes support after a confirmed
    Break of Structure (BOS).

    This is an immutable Market Intelligence Object.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    type: FlipZoneType = FlipZoneType.BULLISH

    upper_price: Decimal = Decimal("0")

    lower_price: Decimal = Decimal("0")

    flip_price: Decimal = Decimal("0")

    originating_swing_id: str = ""

    originating_bos_id: str = ""

    confidence: float = 1.0

    status: FlipZoneStatus = FlipZoneStatus.ACTIVE

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def midpoint(self) -> Decimal:
        """
        Returns the midpoint of the Flip Zone.
        """
        return (
            self.upper_price + self.lower_price
        ) / Decimal("2")

    @property
    def height(self) -> Decimal:
        """
        Returns the total height of the Flip Zone.
        """
        return self.upper_price - self.lower_price

    @property
    def is_active(self) -> bool:
        """
        Returns True if the Flip Zone is active.
        """
        return self.status == FlipZoneStatus.ACTIVE

    @property
    def is_tested(self) -> bool:
        """
        Returns True if the Flip Zone has been tested.
        """
        return self.status == FlipZoneStatus.TESTED

    @property
    def is_confirmed(self) -> bool:
        """
        Returns True if the Flip Zone has been confirmed.
        """
        return self.status == FlipZoneStatus.CONFIRMED

    @property
    def is_invalidated(self) -> bool:
        """
        Returns True if the Flip Zone has been invalidated.
        """
        return self.status == FlipZoneStatus.INVALIDATED

    def __str__(self) -> str:
        return (
            f"FlipZone("
            f"type={self.type.value}, "
            f"range=[{self.lower_price}, {self.upper_price}], "
            f"flip={self.flip_price}, "
            f"status={self.status.value})"
        )

    def __repr__(self) -> str:
        return self.__str__()