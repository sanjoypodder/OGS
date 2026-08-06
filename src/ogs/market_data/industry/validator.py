"""
===========================================================

OGS Smart Money AI

Industry Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.validator import BaseValidator

from .domain import Industry
from .enums import (
    IndustryStatus,
    IndustryType,
)


class IndustryValidator(
    BaseValidator[Industry],
):
    """
    Industry Validator.
    """

    def validate(
        self,
        value: Industry,
    ) -> None:

        if not value.industry_code.strip():
            raise ValueError(
                "Invalid industry code."
            )

        if not value.industry_name.strip():
            raise ValueError(
                "Invalid industry name."
            )

        if not value.sector_code.strip():
            raise ValueError(
                "Invalid sector code."
            )

        if not isinstance(
            value.industry_type,
            IndustryType,
        ):
            raise ValueError(
                "Invalid industry type."
            )

        if not isinstance(
            value.status,
            IndustryStatus,
        ):
            raise ValueError(
                "Invalid industry status."
            )