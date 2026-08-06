"""
===========================================================

OGS Smart Money AI

Screener Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.validator import BaseValidator

from .domain import Screener
from .enums import (
    ScreenerStatus,
    ScreenerType,
)


class ScreenerValidator(
    BaseValidator[Screener],
):
    """
    Screener Validator.
    """

    def validate(
        self,
        value: Screener,
    ) -> None:

        if not value.screener_id.strip():
            raise ValueError(
                "Invalid screener id."
            )

        if not value.screener_name.strip():
            raise ValueError(
                "Invalid screener name."
            )

        if not isinstance(
            value.filters,
            list,
        ):
            raise ValueError(
                "Filters must be a list."
            )

        if not isinstance(
            value.screener_type,
            ScreenerType,
        ):
            raise ValueError(
                "Invalid screener type."
            )

        if not isinstance(
            value.status,
            ScreenerStatus,
        ):
            raise ValueError(
                "Invalid screener status."
            )

        if (
            value.sort_order
            and value.sort_order.upper()
            not in {"ASC", "DESC"}
        ):
            raise ValueError(
                "Invalid sort order."
            )