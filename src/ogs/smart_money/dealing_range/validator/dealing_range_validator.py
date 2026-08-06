"""
OGS FinOS

Dealing Range Validator

Structural validation for DealingRange.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from ogs.smart_money.dealing_range.domain import (
    DealingRange,
)
from ogs.smart_money.dealing_range.enums import (
    DealingRangeDirection,
)


class DealingRangeValidator:
    """
    Validates DealingRange objects.
    """

    @staticmethod
    def validate(
        dealing_range: DealingRange,
    ) -> None:
        """
        Validate a dealing range.

        Raises:
            ValueError
        """

        if dealing_range.range_high <= 0:
            raise ValueError(
                "Range high must be positive."
            )

        if dealing_range.range_low <= 0:
            raise ValueError(
                "Range low must be positive."
            )

        if (
            dealing_range.range_high
            <= dealing_range.range_low
        ):
            raise ValueError(
                "Range high must be greater than range low."
            )

        if not (
            dealing_range.range_low
            <= dealing_range.equilibrium
            <= dealing_range.range_high
        ):
            raise ValueError(
                "Equilibrium must lie within the dealing range."
            )

        if dealing_range.range_size <= 0:
            raise ValueError(
                "Range size must be greater than zero."
            )

        if (
            dealing_range.start_index
            > dealing_range.end_index
        ):
            raise ValueError(
                "Start index cannot exceed end index."
            )

        if not isinstance(
            dealing_range.direction,
            DealingRangeDirection,
        ):
            raise ValueError(
                "Invalid dealing range direction."
            )

    @classmethod
    def is_valid(
        cls,
        dealing_range: DealingRange,
    ) -> bool:
        """
        Returns True if valid.
        """

        try:
            cls.validate(dealing_range)
            return True

        except ValueError:
            return False