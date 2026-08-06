"""
OGS Smart Money AI
------------------

Market Data - Candle Validator

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from ogs.smart_money.base.validator import BaseValidator

from .domain import Candle


class CandleValidator(BaseValidator):
    """
    Validator for Candle objects.
    """

    def validate(
        self,
        candle: Candle,
    ) -> bool:

        if candle is None:
            return False

        if not candle.symbol:
            return False

        if not candle.timeframe:
            return False

        if candle.timestamp is None:
            return False

        if candle.high < candle.low:
            return False

        if candle.open > candle.high:
            return False

        if candle.open < candle.low:
            return False

        if candle.close > candle.high:
            return False

        if candle.close < candle.low:
            return False

        if candle.volume < 0:
            return False

        return True