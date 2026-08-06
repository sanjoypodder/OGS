"""
OGS Smart Money AI

CorporateEvent Module
"""

__version__ = "0.1.0"

from .analyzer import CorporateEventAnalyzer
from .collection import CorporateEventCollection
from .domain import CorporateEvent
from .enums import (
    CorporateEventStatus,
    CorporateEventType,
)
from .factory import CorporateEventFactory
from .statistics import CorporateEventStatistics
from .validator import CorporateEventValidator

__all__ = [
    "__version__",
    "CorporateEvent",
    "CorporateEventType",
    "CorporateEventStatus",
    "CorporateEventValidator",
    "CorporateEventFactory",
    "CorporateEventCollection",
    "CorporateEventStatistics",
    "CorporateEventAnalyzer",
]