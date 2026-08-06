"""
OGS Smart Money AI
------------------

Market Data - Timeframe Factory

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from .domain import Timeframe
from .enums import TimeframeType
from .validator import TimeframeValidator


class TimeframeFactory:
    """
    Factory for creating validated Timeframe objects.
    """

    _validator = TimeframeValidator()

    @classmethod
    def create(
        cls,
        value: TimeframeType,
    ) -> Timeframe:

        timeframe = Timeframe(
            value=value,
        )

        if not cls._validator.validate(
            timeframe,
        ):
            raise ValueError(
                "Invalid Timeframe."
            )

        return timeframe

    @classmethod
    def from_string(
        cls,
        value: str,
    ) -> Timeframe:
        """
        Create Timeframe from string.
        """

        try:

            timeframe_type = TimeframeType(
                value.upper(),
            )

        except ValueError as exc:

            raise ValueError(
                f"Unsupported timeframe: {value}"
            ) from exc

        return cls.create(
            timeframe_type,
        )