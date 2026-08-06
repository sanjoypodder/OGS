"""
OGS Smart Money AI
------------------

Market Data - Timeframe Validator

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from ogs.smart_money.base.validator import BaseValidator

from .domain import Timeframe
from .enums import TimeframeType


class TimeframeValidator(BaseValidator):
    """
    Validator for Timeframe objects.
    """

    def validate(
        self,
        timeframe: Timeframe,
    ) -> bool:

        if timeframe is None:
            return False

        if not isinstance(timeframe, Timeframe):
            return False

        if not isinstance(
            timeframe.value,
            TimeframeType,
        ):
            return False

        return True