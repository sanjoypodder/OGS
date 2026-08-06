"""
OGS FinOS

Flip Zone Statistics

Computes statistics for Flip Zones.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from decimal import Decimal

from ogs.smart_money.flip_zone.collection.flip_zone_collection import (
    FlipZoneCollection,
)
from ogs.smart_money.flip_zone.enums.flip_zone_status import FlipZoneStatus
from ogs.smart_money.flip_zone.enums.flip_zone_type import FlipZoneType


class FlipZoneStatistics:
    """
    Computes statistics for a FlipZoneCollection.
    """

    def __init__(self, collection: FlipZoneCollection) -> None:
        self._collection = collection

    @property
    def total(self) -> int:
        return len(self._collection)

    @property
    def bullish(self) -> int:
        return len(self._collection.bullish)

    @property
    def bearish(self) -> int:
        return len(self._collection.bearish)

    @property
    def active(self) -> int:
        return len(self._collection.active)

    @property
    def confirmed(self) -> int:
        return len(self._collection.confirmed)

    @property
    def invalidated(self) -> int:
        return len(self._collection.invalidated)

    @property
    def tested(self) -> int:
        return len(
            self._collection.filter_by_status(
                FlipZoneStatus.TESTED
            )
        )

    @property
    def average_height(self) -> Decimal:
        """
        Average Flip Zone height.
        """

        if not self._collection:
            return Decimal("0")

        total = sum(
            zone.height
            for zone in self._collection
        )

        return total / Decimal(len(self._collection))

    @property
    def average_confidence(self) -> float:
        """
        Average confidence score.
        """

        if not self._collection:
            return 0.0

        return (
            sum(
                zone.confidence
                for zone in self._collection
            )
            / len(self._collection)
        )

    @property
    def bullish_ratio(self) -> float:
        """
        Bullish Flip Zone ratio.
        """

        if not self.total:
            return 0.0

        return self.bullish / self.total

    @property
    def bearish_ratio(self) -> float:
        """
        Bearish Flip Zone ratio.
        """

        if not self.total:
            return 0.0

        return self.bearish / self.total

    def summary(self) -> dict[str, int | float | Decimal]:
        """
        Returns summary statistics.
        """

        return {
            "total": self.total,
            "bullish": self.bullish,
            "bearish": self.bearish,
            "active": self.active,
            "tested": self.tested,
            "confirmed": self.confirmed,
            "invalidated": self.invalidated,
            "average_height": self.average_height,
            "average_confidence": self.average_confidence,
            "bullish_ratio": self.bullish_ratio,
            "bearish_ratio": self.bearish_ratio,
        }