"""
===========================================================

OGS Smart Money AI

Market Structure Validator

===========================================================
"""

from ogs.smart_money.base import BaseValidator

from .domain import SwingPoint


class SwingPointValidator(
    BaseValidator[SwingPoint],
):
    """
    Validator for SwingPoint objects.
    """

    def validate(
        self,
        swing: SwingPoint,
    ) -> bool:
        """
        Validate a SwingPoint.

        Returns
        -------
        bool
            True if valid, otherwise False.
        """

        if swing is None:
            return False

        if not swing.symbol:
            return False

        if swing.candle is None:
            return False

        if swing.index < 0:
            return False

        if swing.price <= 0:
            return False

        if swing.type is None:
            return False

        if swing.strength is None:
            return False

        return True