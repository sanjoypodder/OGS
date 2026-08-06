"""
===========================================================

OGS Smart Money AI

Rejection Block Validator

===========================================================
"""

from __future__ import annotations

from .domain import RejectionBlock


class RejectionBlockValidator:
    """
    Validates Rejection Block objects.
    """

    @staticmethod
    def validate(
        rejection: RejectionBlock,
    ) -> None:

        if rejection.candle is None:
            raise ValueError(
                "Rejection candle is required."
            )

        if rejection.direction is None:
            raise ValueError(
                "Direction is required."
            )

        if rejection.top < rejection.bottom:
            raise ValueError(
                "Top price must be greater than or equal to Bottom price."
            )

        if rejection.size < 0:
            raise ValueError(
                "Size cannot be negative."
            )