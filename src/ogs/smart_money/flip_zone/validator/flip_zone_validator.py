"""
OGS FinOS

Flip Zone Validator

Validates Flip Zone domain objects.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from decimal import Decimal

from ogs.smart_money.flip_zone.domain.flip_zone import FlipZone


class FlipZoneValidator:
    """
    Validates FlipZone objects.

    The validator performs structural validation only.
    It does not detect Flip Zones.
    """

    @staticmethod
    def validate(flip_zone: FlipZone) -> None:
        """
        Validate a FlipZone object.

        Raises
        ------
        ValueError
            If the Flip Zone is invalid.
        """

        if flip_zone.upper_price <= Decimal("0"):
            raise ValueError("Upper price must be greater than zero.")

        if flip_zone.lower_price <= Decimal("0"):
            raise ValueError("Lower price must be greater than zero.")

        if flip_zone.upper_price <= flip_zone.lower_price:
            raise ValueError(
                "Upper price must be greater than lower price."
            )

        if not (
            flip_zone.lower_price
            <= flip_zone.flip_price
            <= flip_zone.upper_price
        ):
            raise ValueError(
                "Flip price must lie inside the Flip Zone."
            )

        if not 0.0 <= flip_zone.confidence <= 1.0:
            raise ValueError(
                "Confidence must be between 0.0 and 1.0."
            )

        if not flip_zone.originating_bos_id:
            raise ValueError(
                "Originating BOS ID is required."
            )

        if not flip_zone.originating_swing_id:
            raise ValueError(
                "Originating Swing ID is required."
            )

    @staticmethod
    def is_valid(flip_zone: FlipZone) -> bool:
        """
        Return True if the Flip Zone is valid.
        """
        try:
            FlipZoneValidator.validate(flip_zone)
            return True
        except ValueError:
            return False