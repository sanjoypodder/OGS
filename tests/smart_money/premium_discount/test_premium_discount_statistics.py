"""
OGS FinOS

Unit Tests

Premium Discount Statistics
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
from ogs.smart_money.premium_discount.statistics.premium_discount_statistics import (
    PremiumDiscountStatistics,
)


def test_statistics() -> None:
    collection = PremiumDiscountCollection()

    collection.add(
        PremiumDiscount(
            range_high=Decimal("200"),
            range_low=Decimal("100"),
            equilibrium=Decimal("150"),
            current_price=Decimal("170"),
            zone=PremiumDiscountZone.PREMIUM,
        )
    )

    stats = PremiumDiscountStatistics(collection)

    assert stats.total == 1
    assert stats.premium == 1
    assert stats.average_confidence == 1.0