"""
OGS FinOS

Unit Tests

Premium Discount Domain
"""

from decimal import Decimal

from ogs.smart_money.premium_discount.domain.premium_discount import (
    PremiumDiscount,
)
from ogs.smart_money.premium_discount.enums.premium_discount_zone import (
    PremiumDiscountZone,
)


def test_create_premium_discount() -> None:
    premium_discount = PremiumDiscount(
        range_high=Decimal("200"),
        range_low=Decimal("100"),
        equilibrium=Decimal("150"),
        current_price=Decimal("170"),
        zone=PremiumDiscountZone.PREMIUM,
    )

    assert premium_discount.range_high == Decimal("200")
    assert premium_discount.range_low == Decimal("100")
    assert premium_discount.current_price == Decimal("170")
    assert premium_discount.zone == PremiumDiscountZone.PREMIUM


def test_range_size() -> None:
    premium_discount = PremiumDiscount(
        range_high=Decimal("200"),
        range_low=Decimal("100"),
        equilibrium=Decimal("150"),
        current_price=Decimal("170"),
        zone=PremiumDiscountZone.PREMIUM,
    )

    assert premium_discount.range_size == Decimal("100")


def test_zone_properties() -> None:
    premium_discount = PremiumDiscount(
        range_high=Decimal("200"),
        range_low=Decimal("100"),
        equilibrium=Decimal("150"),
        current_price=Decimal("170"),
        zone=PremiumDiscountZone.PREMIUM,
    )

    assert premium_discount.is_premium
    assert not premium_discount.is_discount
    assert not premium_discount.is_equilibrium