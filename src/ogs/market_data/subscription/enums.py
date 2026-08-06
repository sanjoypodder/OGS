"""
OGS Smart Money AI

Subscription Enumerations
"""

from enum import Enum


class SubscriptionType(Enum):
    """
    Type of subscription.
    """

    LIVE = "LIVE"
    HISTORICAL = "HISTORICAL"
    PAPER = "PAPER"
    SIMULATED = "SIMULATED"
    UNKNOWN = "UNKNOWN"


class SubscriptionStatus(Enum):
    """
    Current subscription status.
    """

    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"
    CANCELLED = "CANCELLED"
    EXPIRED = "EXPIRED"
    UNKNOWN = "UNKNOWN"