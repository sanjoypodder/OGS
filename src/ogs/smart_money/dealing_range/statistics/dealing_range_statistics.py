"""
OGS FinOS

Dealing Range Statistics

Provides statistical summaries for DealingRangeCollection.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from decimal import Decimal

from ogs.smart_money.dealing_range.collection import (
    DealingRangeCollection,
)
from ogs.smart_money.dealing_range.enums import (
    DealingRangeDirection,
)


class DealingRangeStatistics:
    """
    Read-only statistics for DealingRangeCollection.
    """

    def __init__(
        self,
        collection: DealingRangeCollection,
    ) -> None:
        self._collection = collection

    @property
    def total(self) -> int:
        """
        Total dealing ranges.
        """
        return len(self._collection)

    @property
    def bullish(self) -> int:
        """
        Total bullish ranges.
        """
        return sum(
            1
            for item in self._collection
            if item.direction == DealingRangeDirection.BULLISH
        )

    @property
    def bearish(self) -> int:
        """
        Total bearish ranges.
        """
        return sum(
            1
            for item in self._collection
            if item.direction == DealingRangeDirection.BEARISH
        )

    @property
    def sideways(self) -> int:
        """
        Total sideways ranges.
        """
        return sum(
            1
            for item in self._collection
            if item.direction == DealingRangeDirection.SIDEWAYS
        )

    @property
    def average_range_size(self) -> Decimal:
        """
        Average dealing range size.
        """
        if not self._collection:
            return Decimal("0")

        total = sum(
            item.range_size
            for item in self._collection
        )

        return total / Decimal(len(self._collection))

    @property
    def maximum_range(self) -> Decimal:
        """
        Largest dealing range.
        """
        if not self._collection:
            return Decimal("0")

        return max(
            item.range_size
            for item in self._collection
        )

    @property
    def minimum_range(self) -> Decimal:
        """
        Smallest dealing range.
        """
        if not self._collection:
            return Decimal("0")

        return min(
            item.range_size
            for item in self._collection
        )

    def summary(
        self,
    ) -> dict[str, int | Decimal]:
        """
        Returns all statistics.
        """
        return {
            "total": self.total,
            "bullish": self.bullish,
            "bearish": self.bearish,
            "sideways": self.sideways,
            "average_range_size": self.average_range_size,
            "maximum_range": self.maximum_range,
            "minimum_range": self.minimum_range,
        }