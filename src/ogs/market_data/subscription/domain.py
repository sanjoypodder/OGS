"""
OGS Smart Money AI

Subscription Domain
"""

from __future__ import annotations

from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime

from .enums import (
    SubscriptionStatus,
    SubscriptionType,
)


@dataclass(slots=True)
class Subscription:
    """
    Represents a market data subscription.
    """

    name: str = ""
    subscription_type: SubscriptionType = SubscriptionType.UNKNOWN
    status: SubscriptionStatus = SubscriptionStatus.UNKNOWN

    provider: str = ""
    symbol: str = ""
    timeframe: str = ""

    active: bool = False
    auto_reconnect: bool = True

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def is_active(self) -> bool:
        return (
            self.status == SubscriptionStatus.ACTIVE
        )

    @property
    def is_valid(self) -> bool:
        return bool(self.name.strip())

    def to_dict(self) -> dict:
        data = asdict(self)
        data["subscription_type"] = (
            self.subscription_type.value
        )
        data["status"] = self.status.value
        data["created_at"] = (
            self.created_at.isoformat()
        )
        return data

    def __str__(self) -> str:
        return (
            f"Subscription("
            f"name='{self.name}', "
            f"type={self.subscription_type.value}, "
            f"status={self.status.value})"
        )