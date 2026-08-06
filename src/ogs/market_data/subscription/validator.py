"""
OGS Smart Money AI

Subscription Validator
"""

from __future__ import annotations

from datetime import datetime

from ogs.framework import BaseValidator

from .domain import Subscription
from .enums import (
    SubscriptionStatus,
    SubscriptionType,
)


class SubscriptionValidator(BaseValidator):
    """
    Validator for Subscription objects.
    """

    def validate(
        self,
        subscription: Subscription,
    ) -> None:

        if not isinstance(
            subscription,
            Subscription,
        ):
            raise TypeError(
                "Expected Subscription instance."
            )

        if not subscription.name.strip():
            raise ValueError(
                "Subscription name cannot be empty."
            )

        if not isinstance(
            subscription.subscription_type,
            SubscriptionType,
        ):
            raise ValueError(
                "Invalid subscription type."
            )

        if not isinstance(
            subscription.status,
            SubscriptionStatus,
        ):
            raise ValueError(
                "Invalid subscription status."
            )

        if not isinstance(
            subscription.created_at,
            datetime,
        ):
            raise ValueError(
                "Invalid creation timestamp."
            )

    def __call__(
        self,
        subscription: Subscription,
    ) -> None:
        self.validate(subscription)