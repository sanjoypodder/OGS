"""
OGS FinOS

Unit Tests

Premium Discount Factory
"""

from ogs.smart_money.premium_discount.analyzer import (
    PremiumDiscountAnalyzer,
)
from ogs.smart_money.premium_discount.factory import (
    PremiumDiscountFactory,
)


def test_factory() -> None:
    analyzer = PremiumDiscountFactory.create_analyzer()

    assert isinstance(
        analyzer,
        PremiumDiscountAnalyzer,
    )