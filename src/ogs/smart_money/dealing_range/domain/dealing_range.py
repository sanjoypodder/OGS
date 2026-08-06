"""
OGS FinOS

Dealing Range Domain

Immutable representation of an institutional dealing range.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from decimal import Decimal
from typing import Any
from uuid import UUID, uuid4

from ogs.smart_money.dealing_range.enums import (
    DealingRangeDirection,
)


@dataclass(frozen=True, slots=True)
class DealingRange:
    """
    Immutable institutional dealing range.
    """

    range_high: Decimal

    range_low: Decimal

    equilibrium: Decimal

    direction: DealingRangeDirection

    start_index: int

    end_index: int

    id: UUID = field(default_factory=uuid4)

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    @property
    def range_size(self) -> Decimal:
        """
        Total dealing range.
        """
        return self.range_high - self.range_low

    @property
    def is_bullish(self) -> bool:
        """
        True if bullish dealing range.
        """
        return (
            self.direction
            == DealingRangeDirection.BULLISH
        )

    @property
    def is_bearish(self) -> bool:
        """
        True if bearish dealing range.
        """
        return (
            self.direction
            == DealingRangeDirection.BEARISH
        )

    @property
    def is_sideways(self) -> bool:
        """
        True if sideways dealing range.
        """
        return (
            self.direction
            == DealingRangeDirection.SIDEWAYS
        )

    def __str__(self) -> str:
        return (
            "DealingRange("
            f"High={self.range_high}, "
            f"Low={self.range_low}, "
            f"Direction={self.direction.value})"
        )

    def __repr__(self) -> str:
        return (
            "DealingRange("
            f"id={self.id}, "
            f"high={self.range_high}, "
            f"low={self.range_low}, "
            f"direction={self.direction.value})"
        )