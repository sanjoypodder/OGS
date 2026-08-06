"""
OGS Smart Money AI
------------------

Market Data - Timeframe Analyzer

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import TimeframeCollection
from .domain import Timeframe


class TimeframeAnalyzer(BaseAnalyzer):
    """
    Analyzer for TimeframeCollection.
    """

    def analyze(
        self,
        collection: TimeframeCollection,
    ) -> dict:
        """
        Analyze a timeframe collection.
        """

        return {
            "count": len(collection),
            "intraday": len(self.intraday(collection)),
            "higher": len(self.higher(collection)),
            "shortest": self.shortest(collection),
            "longest": self.longest(collection),
        }

    def intraday(
        self,
        collection: TimeframeCollection,
    ) -> list[Timeframe]:

        return [
            timeframe
            for timeframe in collection
            if timeframe.is_intraday
        ]

    def higher(
        self,
        collection: TimeframeCollection,
    ) -> list[Timeframe]:

        return [
            timeframe
            for timeframe in collection
            if timeframe.is_daily_or_higher
        ]

    def shortest(
        self,
        collection: TimeframeCollection,
    ) -> Timeframe | None:

        if len(collection) == 0:
            return None

        return min(
            collection,
            key=lambda tf: tf.seconds,
        )

    def longest(
        self,
        collection: TimeframeCollection,
    ) -> Timeframe | None:

        if len(collection) == 0:
            return None

        return max(
            collection,
            key=lambda tf: tf.seconds,
        )

    def average_minutes(
        self,
        collection: TimeframeCollection,
    ) -> float:

        if len(collection) == 0:
            return 0.0

        return (
            sum(
                tf.minutes
                for tf in collection
            )
            / len(collection)
        )