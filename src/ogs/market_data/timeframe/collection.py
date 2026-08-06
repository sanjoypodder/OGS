"""
OGS Smart Money AI
------------------

Market Data - Timeframe Collection

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from collections.abc import Iterable

from ogs.smart_money.base.collection import BaseCollection

from .domain import Timeframe
from .enums import TimeframeType


class TimeframeCollection(BaseCollection[Timeframe]):
    """
    Collection of Timeframe objects.
    """

    def __init__(
        self,
        items: Iterable[Timeframe] | None = None,
    ) -> None:

        super().__init__(items)

    def append(
        self,
        timeframe: Timeframe,
    ) -> None:

        self._items.append(timeframe)

    def by_type(
        self,
        value: TimeframeType,
    ) -> list[Timeframe]:

        return [
            timeframe
            for timeframe in self._items
            if timeframe.value is value
        ]

    def intraday(
        self,
    ) -> list[Timeframe]:

        return [
            timeframe
            for timeframe in self._items
            if timeframe.is_intraday
        ]

    def higher_timeframes(
        self,
    ) -> list[Timeframe]:

        return [
            timeframe
            for timeframe in self._items
            if timeframe.is_daily_or_higher
        ]

    def shortest(self) -> Timeframe | None:

        if not self._items:
            return None

        return min(
            self._items,
            key=lambda tf: tf.seconds,
        )

    def longest(self) -> Timeframe | None:

        if not self._items:
            return None

        return max(
            self._items,
            key=lambda tf: tf.seconds,
        )