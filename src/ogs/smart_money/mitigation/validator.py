"""
===========================================================

OGS Smart Money AI

Mitigation Block Validator

===========================================================
"""

from __future__ import annotations

from .domain import MitigationBlock


class MitigationBlockValidator:
    """
    Validates Mitigation Block objects.
    """

    @staticmethod
    def validate(
        mitigation: MitigationBlock,
    ) -> None:

        if mitigation.candle is None:
            raise ValueError(
                "Mitigation candle is required."
            )

        if mitigation.direction is None:
            raise ValueError(
                "Direction is required."
            )

        if mitigation.top < mitigation.bottom:
            raise ValueError(
                "Top price must be greater than or equal to Bottom price."
            )

        if mitigation.size < 0:
            raise ValueError(
                "Size cannot be negative."
            )