"""
OGS FinOS

Premium / Discount Statistics

Provides statistical summaries for PremiumDiscountCollection.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from decimal import Decimal

from ogs.smart_money.premium_discount.collection.premium_discount_collection import (
    PremiumDiscountCollection,
)


class PremiumDiscountStatistics:
    """
    Read-only statistics for PremiumDiscountCollection.
    """

    def __init__(
        self,
        collection: PremiumDiscountCollection,
    ) -> None:
        self._collection = collection

    @property
    def total(self) -> int:
        """
        Total Premium/Discount objects.
        """
        return len(self._collection)

    @property
    def premium(self) -> int:
        """
        Total Premium zones.
        """
        return len(self._collection.premium)

    @property
    def equilibrium(self) -> int:
        """
        Total Equilibrium zones.
        """
        return len(self._collection.equilibrium)

    @property
    def discount(self) -> int:
        """
        Total Discount zones.
        """
        return len(self._collection.discount)

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
    def average_confidence(self) -> float:
        """
        Average confidence score.
        """
        if not self._collection:
            return 0.0

        total = sum(
            item.confidence
            for item in self._collection
        )

        return total / len(self._collection)

    @property
    def premium_ratio(self) -> float:
        """
        Ratio of Premium objects.
        """
        if not self._collection:
            return 0.0

        return self.premium / self.total

    @property
    def equilibrium_ratio(self) -> float:
        """
        Ratio of Equilibrium objects.
        """
        if not self._collection:
            return 0.0

        return self.equilibrium / self.total

    @property
    def discount_ratio(self) -> float:
        """
        Ratio of Discount objects.
        """
        if not self._collection:
            return 0.0

        return self.discount / self.total

    def summary(self) -> dict[str, int | float | Decimal]:
        """
        Returns all statistics as a dictionary.
        """
        return {
            "total": self.total,
            "premium": self.premium,
            "equilibrium": self.equilibrium,
            "discount": self.discount,
            "average_range_size": self.average_range_size,
            "average_confidence": self.average_confidence,
            "premium_ratio": self.premium_ratio,
            "equilibrium_ratio": self.equilibrium_ratio,
            "discount_ratio": self.discount_ratio,
        }