"""
===========================================================

OGS Smart Money AI

Equal High Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseValidator

from .domain import EqualHigh


class EqualHighValidator(
    BaseValidator[EqualHigh]
):
    """
    Validate Equal High objects.
    """

    def validate(
        self,
        zone: EqualHigh,
    ) -> None:

        if zone is None:
            raise ValueError(
                "Equal High cannot be None."
            )

        if zone.first_swing is None:
            raise ValueError(
                "First swing cannot be None."
            )

        if zone.second_swing is None:
            raise ValueError(
                "Second swing cannot be None."
            )