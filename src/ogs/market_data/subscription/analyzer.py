"""
OGS Smart Money AI

Subscription Analyzer
"""

from __future__ import annotations

from ogs.framework import BaseAnalyzer

from .collection import SubscriptionCollection
from .statistics import SubscriptionStatistics


class SubscriptionAnalyzer(BaseAnalyzer):
    """
    Analyzer for Subscription collections.
    """

    def __init__(
        self,
        subscriptions: SubscriptionCollection,
    ):
        self.subscriptions = subscriptions
        self.statistics = SubscriptionStatistics(
            subscriptions
        )

    def analyze(self) -> dict:
        return {
            "summary": self.summary(),
            "activity": self.activity_analysis(),
            "distribution": self.distribution_analysis(),
        }

    def summary(self) -> dict:
        return self.statistics.summary()

    def activity_analysis(self) -> dict:
        return {
            "active": self.statistics.active_count,
            "inactive": self.statistics.inactive_count,
            "total": self.statistics.count,
        }

    def distribution_analysis(self) -> dict:
        return {
            "type_distribution":
                self.statistics.type_distribution,
            "provider_distribution":
                self.statistics.provider_distribution,
        }