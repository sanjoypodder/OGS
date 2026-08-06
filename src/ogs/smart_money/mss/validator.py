"""
===========================================================

OGS Smart Money AI

MSS Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseValidator

from .domain import MSS


class MSSValidator(
    BaseValidator[MSS]
):
    """
    Validate MSS objects.
    """

    def validate(
        self,
        mss: MSS,
    ) -> None:

        if mss is None:
            raise ValueError(
                "MSS cannot be None."
            )

        if mss.candle is None:
            raise ValueError(
                "MSS candle cannot be None."
            )

        if mss.triggering_choch is None:
            raise ValueError(
                "Triggering CHOCH cannot be None."
            )