"""
OGS FinOS

Premium / Discount Analyzer

Determines whether price is in Premium,
Equilibrium or Discount.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

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


class PremiumDiscountAnalyzer:
    """
    Premium / Discount Analyzer.

    Builds PremiumDiscount objects from
    a completed dealing range.
    """

    def analyze(
        self,
        range_high: Decimal,
        range_low: Decimal,
        current_price: Decimal,
    ) -> PremiumDiscountCollection:
        """
        Analyze a completed dealing range.

        Parameters
        ----------
        range_high : Decimal
        range_low : Decimal
        current_price : Decimal

        Returns
        -------
        PremiumDiscountCollection
        """

        equilibrium = self._calculate_equilibrium(
            range_high,
            range_low,
        )

        zone = self._determine_zone(
            current_price,
            equilibrium,
        )

        premium_discount = PremiumDiscount(
            range_high=range_high,
            range_low=range_low,
            equilibrium=equilibrium,
            current_price=current_price,
            zone=zone,
        )

        collection = PremiumDiscountCollection()
        collection.add(premium_discount)

        return collection

    def _calculate_equilibrium(
        self,
        range_high: Decimal,
        range_low: Decimal,
    ) -> Decimal:
        """
        Calculate equilibrium (50%).
        """

        return (
            range_high + range_low
        ) / Decimal("2")

    def _determine_zone(
        self,
        current_price: Decimal,
        equilibrium: Decimal,
    ) -> PremiumDiscountZone:
        """
        Determine Premium/Discount zone.
        """

        if current_price > equilibrium:
            return PremiumDiscountZone.PREMIUM

        if current_price < equilibrium:
            return PremiumDiscountZone.DISCOUNT

        return PremiumDiscountZone.EQUILIBRIUM