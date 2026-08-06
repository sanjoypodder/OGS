"""
OGS FinOS

Unit Tests

Premium Discount Analyzer
"""

from decimal import Decimal

from ogs.smart_money.premium_discount.analyzer import (
    PremiumDiscountAnalyzer,
)


def test_analyzer() -> None:
    analyzer = PremiumDiscountAnalyzer()

    collection = analyzer.analyze(
        range_high=Decimal("200"),
        range_low=Decimal("100"),
        current_price=Decimal("175"),
    )

    assert len(collection) == 1

    premium_discount = collection[0]

    assert premium_discount.current_price == Decimal("175")
    assert premium_discount.equilibrium == Decimal("150")