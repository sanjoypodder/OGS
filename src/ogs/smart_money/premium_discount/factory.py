"""
OGS FinOS

Premium / Discount Factory

Creates PremiumDiscountAnalyzer instances.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from ogs.smart_money.premium_discount.analyzer import (
    PremiumDiscountAnalyzer,
)


class PremiumDiscountFactory:
    """
    Factory responsible for creating
    PremiumDiscountAnalyzer instances.
    """

    @staticmethod
    def create_analyzer() -> PremiumDiscountAnalyzer:
        """
        Create a PremiumDiscountAnalyzer.

        Returns
        -------
        PremiumDiscountAnalyzer
            Configured analyzer instance.
        """
        return PremiumDiscountAnalyzer()