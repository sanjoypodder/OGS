"""
OGS FinOS

OTE Statistics

Provides statistical summaries for OTECollection.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from decimal import Decimal

from ogs.smart_money.ote.collection import (
    OTECollection,
)
from ogs.smart_money.ote.enums import (
    OTEDirection,
)


class OTEStatistics:
    """
    Read-only statistics for OTECollection.
    """

    def __init__(
        self,
        collection: OTECollection,
    ) -> None:
        self._collection = collection

    @property
    def total(self) -> int:
        """
        Total OTEs.
        """
        return len(self._collection)

    @property
    def bullish(self) -> int:
        """
        Total bullish OTEs.
        """
        return sum(
            1
            for item in self._collection
            if item.direction == OTEDirection.BULLISH
        )

    @property
    def bearish(self) -> int:
        """
        Total bearish OTEs.
        """
        return sum(
            1
            for item in self._collection
            if item.direction == OTEDirection.BEARISH
        )

    @property
    def average_zone_size(self) -> Decimal:
        """
        Average OTE zone size.
        """
        if not self._collection:
            return Decimal("0")

        total = sum(
            item.zone_size
            for item in self._collection
        )

        return total / Decimal(len(self._collection))

    @property
    def maximum_zone_size(self) -> Decimal:
        """
        Largest OTE zone.
        """
        if not self._collection:
            return Decimal("0")

        return max(
            item.zone_size
            for item in self._collection
        )

    @property
    def minimum_zone_size(self) -> Decimal:
        """
        Smallest OTE zone.
        """
        if not self._collection:
            return Decimal("0")

        return min(
            item.zone_size
            for item in self._collection
        )

    @property
    def average_level_62(self) -> Decimal:
        """
        Average 62% level.
        """
        if not self._collection:
            return Decimal("0")

        total = sum(
            item.level_62
            for item in self._collection
        )

        return total / Decimal(len(self._collection))

    @property
    def average_level_705(self) -> Decimal:
        """
        Average 70.5% level.
        """
        if not self._collection:
            return Decimal("0")

        total = sum(
            item.level_705
            for item in self._collection
        )

        return total / Decimal(len(self._collection))

    @property
    def average_level_79(self) -> Decimal:
        """
        Average 79% level.
        """
        if not self._collection:
            return Decimal("0")

        total = sum(
            item.level_79
            for item in self._collection
        )

        return total / Decimal(len(self._collection))

    def summary(
        self,
    ) -> dict[str, int | Decimal]:
        """
        Return a summary of OTE statistics.
        """
        return {
            "total": self.total,
            "bullish": self.bullish,
            "bearish": self.bearish,
            "average_zone_size": self.average_zone_size,
            "maximum_zone_size": self.maximum_zone_size,
            "minimum_zone_size": self.minimum_zone_size,
            "average_level_62": self.average_level_62,
            "average_level_705": self.average_level_705,
            "average_level_79": self.average_level_79,
        }