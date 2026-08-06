"""
===========================================================

OGS Smart Money AI

Swing Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.validator import BaseValidator

from .domain import Swing


class SwingValidator(BaseValidator[Swing]):
    """
    Validate Swing objects.
    """

    def validate(self, swing: Swing) -> None:

        if swing.index < 0:
            raise ValueError(
                "Swing index cannot be negative."
            )

        if swing.candle is None:
            raise ValueError(
                "Swing must contain a candle."
            )