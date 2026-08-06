"""
OGS Smart Money AI

CorporateAction Module
"""

__version__ = "0.1.0"

from .analyzer import CorporateActionAnalyzer
from .collection import CorporateActionCollection
from .domain import CorporateAction
from .enums import (
    CorporateActionStatus,
    CorporateActionType,
)
from .factory import CorporateActionFactory
from .statistics import CorporateActionStatistics
from .validator import CorporateActionValidator

__all__ = [
    "__version__",
    "CorporateAction",
    "CorporateActionType",
    "CorporateActionStatus",
    "CorporateActionValidator",
    "CorporateActionFactory",
    "CorporateActionCollection",
    "CorporateActionStatistics",
    "CorporateActionAnalyzer",
]