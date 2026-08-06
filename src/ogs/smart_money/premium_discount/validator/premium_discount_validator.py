"""
OGS FinOS

Premium / Discount Validator

Validates PremiumDiscount domain objects.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from decimal import Decimal

from ogs.smart_money.premium_discount.domain.premium_discount import (
    PremiumDiscount,
)


class PremiumDiscountValidator:
    """
    Validates PremiumDiscount domain objects.

    This validator only checks structural correctness.
    It does NOT perform Premium/Discount detection.
    """

    @staticmethod
    def validate(premium_discount: PremiumDiscount) -> None:
        """
        Validate a PremiumDiscount object.

        Raises
        ------
        ValueError
            If validation fails.
        """

        if premium_discount.range_high <= Decimal("0"):
            raise ValueError("Range high must be greater than zero.")

        if premium_discount.range_low <= Decimal("0"):
            raise ValueError("Range low must be greater than zero.")

        if premium_discount.range_high <= premium_discount.range_low:
            raise ValueError(
                "Range high must be greater than range low."
            )

        if (
            premium_discount.equilibrium
            < premium_discount.range_low
        ):
            raise ValueError(
                "Equilibrium cannot be below range low."
            )

        if (
            premium_discount.equilibrium
            > premium_discount.range_high
        ):
            raise ValueError(
                "Equilibrium cannot exceed range high."
            )

        if (
            premium_discount.current_price
            < premium_discount.range_low
        ):
            raise ValueError(
                "Current price cannot be below range low."
            )

        if (
            premium_discount.current_price
            > premium_discount.range_high
        ):
            raise ValueError(
                "Current price cannot exceed range high."
            )

        if not (0.0 <= premium_discount.confidence <= 1.0):
            raise ValueError(
                "Confidence must be between 0.0 and 1.0."
            )

    @staticmethod
    def is_valid(premium_discount: PremiumDiscount) -> bool:
        """
        Returns True if the object is valid.
        """

        try:
            PremiumDiscountValidator.validate(
                premium_discount
            )
            return True

        except ValueError:
            return False