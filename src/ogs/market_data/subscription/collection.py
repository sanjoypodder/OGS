"""
OGS Smart Money AI

Subscription Collection
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator

from ogs.framework import BaseCollection

from .domain import Subscription
from .enums import (
    SubscriptionStatus,
    SubscriptionType,
)


class SubscriptionCollection(BaseCollection):
    """
    Collection of Subscription objects.
    """

    def __init__(
        self,
        subscriptions: Iterable[Subscription] = (),
    ) -> None:
        self._subscriptions = list(subscriptions)

    def __iter__(self) -> Iterator[Subscription]:
        return iter(self._subscriptions)

    def __len__(self) -> int:
        return len(self._subscriptions)

    def __getitem__(self, index: int) -> Subscription:
        return self._subscriptions[index]

    def add(
        self,
        subscription: Subscription,
    ) -> None:
        self._subscriptions.append(subscription)

    def active(self) -> "SubscriptionCollection":
        return SubscriptionCollection(
            subscription
            for subscription in self._subscriptions
            if subscription.status == SubscriptionStatus.ACTIVE
        )

    def inactive(self) -> "SubscriptionCollection":
        return SubscriptionCollection(
            subscription
            for subscription in self._subscriptions
            if subscription.status != SubscriptionStatus.ACTIVE
        )

    def by_type(
        self,
        subscription_type: SubscriptionType,
    ) -> "SubscriptionCollection":
        return SubscriptionCollection(
            subscription
            for subscription in self._subscriptions
            if subscription.subscription_type == subscription_type
        )

    def by_provider(
        self,
        provider: str,
    ) -> "SubscriptionCollection":
        return SubscriptionCollection(
            subscription
            for subscription in self._subscriptions
            if subscription.provider == provider
        )

    def find(
        self,
        name: str,
    ) -> Subscription | None:
        name = name.casefold()

        for subscription in self._subscriptions:
            if subscription.name.casefold() == name:
                return subscription

        return None

    def total_active(self) -> int:
        return len(self.active())

    def to_list(self) -> list[Subscription]:
        return list(self._subscriptions)