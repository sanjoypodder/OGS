"""
===========================================================

OGS Smart Money AI

Breaker Block Validator

===========================================================
"""

from __future__ import annotations

from .domain import BreakerBlock


class BreakerBlockValidator:
    """
    Validates Breaker Block objects.
    """

    @staticmethod
    def validate(
        breaker: BreakerBlock,
    ) -> None:

        if breaker.candle is None:
            raise ValueError("Breaker candle is required.")

        if breaker.direction is None:
            raise ValueError("Direction is required.")

        if breaker.top < breaker.bottom:
            raise ValueError(
                "Top price must be greater than or equal to Bottom price."
            )

        if breaker.size < 0:
            raise ValueError(
                "Size cannot be negative."
            )