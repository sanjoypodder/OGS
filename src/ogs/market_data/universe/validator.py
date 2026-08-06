"""
===========================================================

OGS Smart Money AI

Universe Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.validator import BaseValidator

from .domain import Universe
from .enums import (
    UniverseStatus,
    UniverseType,
)


class UniverseValidator(
    BaseValidator[Universe],
):
    """
    Universe Validator.
    """

    def validate(
        self,
        value: Universe,
    ) -> None:

        if not value.universe_id.strip():
            raise ValueError(
                "Invalid universe id."
            )

        if not value.universe_name.strip():
            raise ValueError(
                "Invalid universe name."
            )

        if not isinstance(
            value.symbols,
            list,
        ):
            raise ValueError(
                "Symbols must be a list."
            )

        if not isinstance(
            value.universe_type,
            UniverseType,
        ):
            raise ValueError(
                "Invalid universe type."
            )

        if not isinstance(
            value.status,
            UniverseStatus,
        ):
            raise ValueError(
                "Invalid universe status."
            )