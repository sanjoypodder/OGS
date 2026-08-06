"""
===========================================================

OGS Smart Money AI

Sector Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.validator import BaseValidator

from .domain import Sector
from .enums import (
    SectorStatus,
    SectorType,
)


class SectorValidator(
    BaseValidator[Sector],
):
    """
    Sector Validator.
    """

    def validate(
        self,
        value: Sector,
    ) -> None:

        if not value.sector_code.strip():
            raise ValueError(
                "Invalid sector code."
            )

        if not value.sector_name.strip():
            raise ValueError(
                "Invalid sector name."
            )

        if not isinstance(
            value.sector_type,
            SectorType,
        ):
            raise ValueError(
                "Invalid sector type."
            )

        if not isinstance(
            value.status,
            SectorStatus,
        ):
            raise ValueError(
                "Invalid sector status."
            )