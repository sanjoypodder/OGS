"""
===========================================================

OGS Smart Money AI

BOS Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseValidator

from .domain import BOS


class BOSValidator(BaseValidator[BOS]):
    """
    Validate BOS objects.
    """

    def validate(
        self,
        bos: BOS,
    ) -> None:

        if bos is None:
            raise ValueError("BOS cannot be None.")

        if bos.candle is None:
            raise ValueError("BOS candle cannot be None.")

        if bos.broken_swing is None:
            raise ValueError("Broken swing cannot be None.")