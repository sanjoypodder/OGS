"""
OGS Smart Money AI

Calendar Module
"""

__version__ = "0.1.0"

from .analyzer import CalendarAnalyzer
from .collection import CalendarCollection
from .domain import Calendar
from .enums import (
    CalendarStatus,
    CalendarType,
)
from .factory import CalendarFactory
from .statistics import CalendarStatistics
from .validator import CalendarValidator

__all__ = [
    "__version__",
    "Calendar",
    "CalendarType",
    "CalendarStatus",
    "CalendarValidator",
    "CalendarFactory",
    "CalendarCollection",
    "CalendarStatistics",
    "CalendarAnalyzer",
]