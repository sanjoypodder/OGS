"""
OGS FinOS

Optimal Trade Entry (OTE)

Immutable institutional OTE representation.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime
from decimal import Decimal
from uuid import UUID
from uuid import uuid4

from ogs.smart_money.ote.enums import (
    OTEDirection,
)


@dataclass(
    frozen=True,
    slots=True,
)
class OTE:
    """
    Immutable Optimal Trade Entry (OTE).

    Represents the institutional Fibonacci
    retracement zone between 62% and 79%.
    """

    range_high: Decimal

    range_low: Decimal

    level_62: Decimal

    level_705: Decimal

    level_79: Decimal

    zone_low: Decimal

    zone_high: Decimal

    direction: OTEDirection

    id: UUID = field(
        default_factory=uuid4
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    metadata: dict = field(
        default_factory=dict
    )

    @property
    def zone_size(self) -> Decimal:
        """
        Width of the OTE zone.
        """
        return self.zone_high - self.zone_low

    @property
    def is_bullish(self) -> bool:
        return (
            self.direction
            == OTEDirection.BULLISH
        )

    @property
    def is_bearish(self) -> bool:
        return (
            self.direction
            == OTEDirection.BEARISH
        )

    def __str__(self) -> str:

        return (
            f"OTE("
            f"{self.direction.value}, "
            f"62={self.level_62}, "
            f"70.5={self.level_705}, "
            f"79={self.level_79})"
        )

    def __repr__(self) -> str:

        return (
            f"OTE("
            f"id={self.id}, "
            f"direction={self.direction.value})"
        )