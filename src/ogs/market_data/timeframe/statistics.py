"""
OGS Smart Money AI
------------------

Market Data - Timeframe Statistics

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from .collection import TimeframeCollection
from .domain import Timeframe


class TimeframeStatistics:
    """
    Statistics for TimeframeCollection.
    """

    def __init__(
        self,
        collection: TimeframeCollection,
    ) -> None:

        self._collection = collection

    @property
    def count(self) -> int:

        return len(self._collection)

    @property
    def intraday_count(self) -> int:

        return sum(
            timeframe.is_intraday
            for timeframe in self._collection
        )

    @property
    def higher_timeframe_count(self) -> int:

        return sum(
            timeframe.is_daily_or_higher
            for timeframe in self._collection
        )

    @property
    def shortest(self) -> Timeframe | None:

        if len(self._collection) == 0:
            return None

        return min(
            self._collection,
            key=lambda tf: tf.seconds,
        )

    @property
    def longest(self) -> Timeframe | None:

        if len(self._collection) == 0:
            return None

        return max(
            self._collection,
            key=lambda tf: tf.seconds,
        )

    @property
    def average_minutes(self) -> float:

        if len(self._collection) == 0:
            return 0.0

        return (
            sum(
                tf.minutes
                for tf in self._collection
            )
            / len(self._collection)
        )