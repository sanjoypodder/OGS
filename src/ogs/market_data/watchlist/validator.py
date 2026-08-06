"""
===========================================================

OGS Smart Money AI

Watchlist Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.validator import BaseValidator

from .domain import Watchlist
from .enums import (
    WatchlistStatus,
    WatchlistType,
)


class WatchlistValidator(
    BaseValidator[Watchlist],
):
    """
    Watchlist Validator.
    """

    def validate(
        self,
        value: Watchlist,
    ) -> None:

        if not value.watchlist_id.strip():
            raise ValueError(
                "Invalid watchlist id."
            )

        if not value.watchlist_name.strip():
            raise ValueError(
                "Invalid watchlist name."
            )

        if not isinstance(
            value.symbols,
            list,
        ):
            raise ValueError(
                "Symbols must be a list."
            )

        if not isinstance(
            value.watchlist_type,
            WatchlistType,
        ):
            raise ValueError(
                "Invalid watchlist type."
            )

        if not isinstance(
            value.status,
            WatchlistStatus,
        ):
            raise ValueError(
                "Invalid watchlist status."
            )