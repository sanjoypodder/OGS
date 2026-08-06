"""
OGS Smart Money AI

Subscription Module
"""

from .analyzer import SubscriptionAnalyzer
from .collection import SubscriptionCollection
from .domain import Subscription
from .enums import (
    SubscriptionStatus,
    SubscriptionType,
)
from .factory import SubscriptionFactory
from .statistics import SubscriptionStatistics
from .validator import SubscriptionValidator

__all__ = [
    "Subscription",
    "SubscriptionType",
    "SubscriptionStatus",
    "SubscriptionValidator",
    "SubscriptionFactory",
    "SubscriptionCollection",
    "SubscriptionStatistics",
    "SubscriptionAnalyzer",
]

__version__ = "0.1.0"