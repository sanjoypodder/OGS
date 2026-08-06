"""
===========================================================

OGS Smart Money AI

Candle Validator

===========================================================
"""

from __future__ import annotations

from ogs.market.candle import Candle
from ogs.market.validators.base import Validator


class CandleValidator(Validator[Candle]):
    """
    Performs additional business validation on candles.
    """

    def validate(self, candle: Candle) -> None:
        """
        Validate a candle.

        The Candle dataclass already performs structural
        validation. This validator is reserved for business
        rules and future extensions.
        """

        if candle.timestamp.tzinfo is None:
            raise ValueError("Timestamp must be timezone-aware (UTC).")

        if candle.volume < 0:
            raise ValueError("Volume cannot be negative.")