"""
OGS FinOS

Premium / Discount Collection

Stores PremiumDiscount domain objects.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from collections.abc import Iterator

from ogs.smart_money.premium_discount.domain.premium_discount import (
    PremiumDiscount,
)
from ogs.smart_money.premium_discount.enums.premium_discount_zone import (
    PremiumDiscountZone,
)


class PremiumDiscountCollection:
    """
    Collection of PremiumDiscount objects.
    """

    def __init__(self) -> None:
        self._items: list[PremiumDiscount] = []

    def add(self, premium_discount: PremiumDiscount) -> None:
        """
        Add a PremiumDiscount object.
        """
        self._items.append(premium_discount)

    def extend(self, items: list[PremiumDiscount]) -> None:
        """
        Add multiple PremiumDiscount objects.
        """
        self._items.extend(items)

    def clear(self) -> None:
        """
        Remove all items.
        """
        self._items.clear()

    def get_by_id(self, object_id: str) -> PremiumDiscount | None:
        """
        Return a PremiumDiscount by ID.
        """
        for item in self._items:
            if item.id == object_id:
                return item
        return None

    def filter_by_zone(
        self,
        zone: PremiumDiscountZone,
    ) -> "PremiumDiscountCollection":
        """
        Filter by Premium/Discount zone.
        """
        collection = PremiumDiscountCollection()

        collection.extend(
            [
                item
                for item in self._items
                if item.zone == zone
            ]
        )

        return collection

    @property
    def premium(self) -> "PremiumDiscountCollection":
        """
        Premium entries.
        """
        return self.filter_by_zone(
            PremiumDiscountZone.PREMIUM
        )

    @property
    def equilibrium(self) -> "PremiumDiscountCollection":
        """
        Equilibrium entries.
        """
        return self.filter_by_zone(
            PremiumDiscountZone.EQUILIBRIUM
        )

    @property
    def discount(self) -> "PremiumDiscountCollection":
        """
        Discount entries.
        """
        return self.filter_by_zone(
            PremiumDiscountZone.DISCOUNT
        )

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[PremiumDiscount]:
        return iter(self._items)

    def __getitem__(self, index: int) -> PremiumDiscount:
        return self._items[index]

    def __contains__(self, item: PremiumDiscount) -> bool:
        return item in self._items

    def __bool__(self) -> bool:
        return bool(self._items)