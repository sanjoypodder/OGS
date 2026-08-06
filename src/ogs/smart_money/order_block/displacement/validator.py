"""
===========================================================

OGS Smart Money AI

Displacement Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseValidator

from .domain import Displacement


class DisplacementValidator(
    BaseValidator[Displacement],
):
    """
    Validates a displacement object.
    """

    def validate(
        self,
        value: Displacement,
    ) -> None:
        """
        Validate displacement.
        """

        if value is None:
            raise ValueError(
                "Displacement cannot be None."
            )

        if value.candle is None:
            raise ValueError(
                "Displacement candle is required."
            )

        if value.direction is None:
            raise ValueError(
                "Displacement direction is required."
            )