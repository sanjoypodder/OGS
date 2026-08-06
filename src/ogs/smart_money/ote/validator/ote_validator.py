"""
OGS FinOS

OTE Validator

Structural validation for OTE.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from decimal import Decimal

from ogs.smart_money.ote.domain import (
    OTE,
)
from ogs.smart_money.ote.enums import (
    OTEDirection,
)


class OTEValidator:
    """
    Structural validator for OTE objects.
    """

    @staticmethod
    def validate(
        ote: OTE,
    ) -> None:
        """
        Validate an OTE.

        Raises
        ------
        ValueError
            If the OTE is structurally invalid.
        """

        if ote.range_high <= Decimal("0"):
            raise ValueError(
                "Range high must be positive."
            )

        if ote.range_low <= Decimal("0"):
            raise ValueError(
                "Range low must be positive."
            )

        if (
            ote.range_high
            <= ote.range_low
        ):
            raise ValueError(
                "Range high must be greater than range low."
            )

        if not (
            ote.range_low
            <= ote.level_62
            <= ote.range_high
        ):
            raise ValueError(
                "62% level must lie inside the dealing range."
            )

        if not (
            ote.range_low
            <= ote.level_705
            <= ote.range_high
        ):
            raise ValueError(
                "70.5% level must lie inside the dealing range."
            )

        if not (
            ote.range_low
            <= ote.level_79
            <= ote.range_high
        ):
            raise ValueError(
                "79% level must lie inside the dealing range."
            )

        if (
            ote.zone_low
            > ote.zone_high
        ):
            raise ValueError(
                "Zone low cannot exceed zone high."
            )

        if not (
            ote.zone_low
            <= ote.level_62
            <= ote.zone_high
        ):
            raise ValueError(
                "62% level must lie inside the OTE zone."
            )

        if not (
            ote.zone_low
            <= ote.level_705
            <= ote.zone_high
        ):
            raise ValueError(
                "70.5% level must lie inside the OTE zone."
            )

        if not (
            ote.zone_low
            <= ote.level_79
            <= ote.zone_high
        ):
            raise ValueError(
                "79% level must lie inside the OTE zone."
            )

        if ote.zone_size <= Decimal("0"):
            raise ValueError(
                "OTE zone size must be positive."
            )

        if not isinstance(
            ote.direction,
            OTEDirection,
        ):
            raise ValueError(
                "Invalid OTE direction."
            )

    @classmethod
    def is_valid(
        cls,
        ote: OTE,
    ) -> bool:
        """
        Return True if the OTE is valid.
        """

        try:
            cls.validate(ote)
            return True

        except ValueError:
            return False