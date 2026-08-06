"""
OGS FinOS

Unit Tests

Premium Discount Collection
"""

from decimal import Decimal

from ogs.smart_money.premium_discount.collection.premium_discount_collection import (
    PremiumDiscountCollection,
)
from ogs.smart_money.premium_discount.domain.premium_discount import (
    PremiumDiscount,
)
from ogs.smart_money.premium_discount.enums.premium_discount_zone import (
    PremiumDiscountZone,
)


def create_pd(zone: PremiumDiscountZone) -> PremiumDiscount:
    return PremiumDiscount(
        range_high=Decimal("200"),
        range_low=Decimal("100"),
        equilibrium=Decimal("150"),
        current_price=Decimal("170"),
        zone=zone,
    )


def test_add() -> None:
    collection = PremiumDiscountCollection()

    collection.add(create_pd(PremiumDiscountZone.PREMIUM))

    assert len(collection) == 1


def test_clear() -> None:
    collection = PremiumDiscountCollection()

    collection.add(create_pd(PremiumDiscountZone.PREMIUM))

    collection.clear()

    assert len(collection) == 0


def test_filter() -> None:
    collection = PremiumDiscountCollection()

    collection.add(create_pd(PremiumDiscountZone.PREMIUM))
    collection.add(create_pd(PremiumDiscountZone.DISCOUNT))

    assert len(collection.premium) == 1
    assert len(collection.discount) == 1