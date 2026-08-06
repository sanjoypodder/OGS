"""
===========================================================

OGS Smart Money AI

Equal Low Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseValidator

from .domain import EqualLow


class EqualLowValidator(
    BaseValidator[EqualLow]
):
    """
    Validate Equal Low objects.
    """

    def validate(
        self,
        zone: EqualLow,
    ) -> None:

        if zone is None:
            raise ValueError(
                "Equal Low cannot be None."
            )

        if zone.first_swing is None:
            raise ValueError(
                "First swing cannot be None."
            )

        if zone.second_swing is None:
            raise ValueError(
                "Second swing cannot be None."
            )