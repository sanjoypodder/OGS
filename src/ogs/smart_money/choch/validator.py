"""
===========================================================

OGS Smart Money AI

CHOCH Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseValidator

from .domain import CHOCH


class CHOCHValidator(
    BaseValidator[CHOCH]
):
    """
    Validate CHOCH objects.
    """

    def validate(
        self,
        choch: CHOCH,
    ) -> None:

        if choch is None:
            raise ValueError(
                "CHOCH cannot be None."
            )

        if choch.candle is None:
            raise ValueError(
                "CHOCH candle cannot be None."
            )

        if choch.broken_bos is None:
            raise ValueError(
                "Broken BOS cannot be None."
            )