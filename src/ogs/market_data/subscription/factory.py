"""
OGS Smart Money AI

Subscription Factory
"""

from __future__ import annotations

from copy import deepcopy

from ogs.framework import BaseFactory

from .domain import Subscription
from .enums import (
    SubscriptionStatus,
    SubscriptionType,
)
from .validator import SubscriptionValidator


class SubscriptionFactory(BaseFactory):
    """
    Factory for Subscription objects.
    """

    _validator = SubscriptionValidator()

    @classmethod
    def create(
        cls,
        **kwargs,
    ) -> Subscription:

        subscription = Subscription(
            **kwargs
        )

        cls._validator.validate(
            subscription
        )

        return subscription

    @classmethod
    def live(
        cls,
        name: str,
    ) -> Subscription:

        return cls.create(
            name=name,
            subscription_type=SubscriptionType.LIVE,
            status=SubscriptionStatus.ACTIVE,
            active=True,
        )

    @classmethod
    def historical(
        cls,
        name: str,
    ) -> Subscription:

        return cls.create(
            name=name,
            subscription_type=SubscriptionType.HISTORICAL,
            status=SubscriptionStatus.ACTIVE,
            active=True,
        )

    @classmethod
    def simulated(
        cls,
        name: str,
    ) -> Subscription:

        return cls.create(
            name=name,
            subscription_type=SubscriptionType.SIMULATED,
            status=SubscriptionStatus.ACTIVE,
            active=True,
        )

    @classmethod
    def clone(
        cls,
        subscription: Subscription,
    ) -> Subscription:

        return deepcopy(subscription)