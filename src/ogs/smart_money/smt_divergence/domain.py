"""
OGS Smart Money AI
------------------

SMT Divergence Domain Model

Represents a Smart Money Technique (SMT) divergence detected
between two correlated markets.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from dataclasses import dataclass
from datetime import datetime

from .enums import (
    SMTComparisonType,
    SMTConfidence,
    SMTDivergenceDirection,
)


@dataclass(frozen=True, slots=True)
class SMTDivergence:
    """
    Represents a single SMT Divergence.
    """

    first_symbol: str
    second_symbol: str

    first_price: float
    second_price: float

    comparison: SMTComparisonType

    direction: SMTDivergenceDirection

    timestamp: datetime

    confidence: SMTConfidence = SMTConfidence.MEDIUM

    @property
    def is_bullish(self) -> bool:
        """Return True if bullish SMT."""
        return self.direction == SMTDivergenceDirection.BULLISH

    @property
    def is_bearish(self) -> bool:
        """Return True if bearish SMT."""
        return self.direction == SMTDivergenceDirection.BEARISH

    @property
    def is_hidden_bullish(self) -> bool:
        """Return True if hidden bullish SMT."""
        return self.direction == SMTDivergenceDirection.HIDDEN_BULLISH

    @property
    def is_hidden_bearish(self) -> bool:
        """Return True if hidden bearish SMT."""
        return self.direction == SMTDivergenceDirection.HIDDEN_BEARISH