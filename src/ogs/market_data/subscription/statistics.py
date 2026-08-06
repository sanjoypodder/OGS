"""
OGS Smart Money AI

Subscription Statistics
"""

from __future__ import annotations

from collections import Counter

from ogs.framework import BaseStatistics

from .collection import SubscriptionCollection


class SubscriptionStatistics(BaseStatistics):
    """
    Statistics for SubscriptionCollection.
    """

    def __init__(
        self,
        subscriptions: SubscriptionCollection,
    ):
        self.subscriptions = subscriptions

    @property
    def count(self) -> int:
        return len(self.subscriptions)

    @property
    def active_count(self) -> int:
        return self.subscriptions.total_active()

    @property
    def inactive_count(self) -> int:
        return self.count - self.active_count

    @property
    def type_distribution(self) -> dict[str, int]:
        return dict(
            Counter(
                subscription.subscription_type.value
                for subscription in self.subscriptions
            )
        )

    @property
    def provider_distribution(self) -> dict[str, int]:
        return dict(
            Counter(
                subscription.provider
                for subscription in self.subscriptions
            )
        )

    def summary(self) -> dict:
        return {
            "count": self.count,
            "active": self.active_count,
            "inactive": self.inactive_count,
            "type_distribution": self.type_distribution,
            "provider_distribution": self.provider_distribution,
        }