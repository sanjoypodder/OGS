"""
OGS FinOS

Unit Tests

Premium Discount Validator
"""

from decimal import Decimal

from ogs.smart_money.premium_discount.domain.premium_discount import (
    PremiumDiscount,
)
from ogs.smart_money.premium_discount.enums.premium_discount_zone import (
    PremiumDiscountZone,
)
from ogs.smart_money.premium_discount.validator.premium_discount_validator import (
    PremiumDiscountValidator,
)


def test_valid() -> None:
    premium_discount = PremiumDiscount(
        range_high=Decimal("200"),
        range_low=Decimal("100"),
        equilibrium=Decimal("150"),
        current_price=Decimal("170"),
        zone=PremiumDiscountZone.PREMIUM,
    )

    assert PremiumDiscountValidator.is_valid(
        premium_discount
    )


def test_invalid() -> None:
    premium_discount = PremiumDiscount(
        range_high=Decimal("100"),
        range_low=Decimal("200"),
        equilibrium=Decimal("150"),
        current_price=Decimal("170"),
        zone=PremiumDiscountZone.PREMIUM,
    )

    assert not PremiumDiscountValidator.is_valid(
        premium_discount
    )