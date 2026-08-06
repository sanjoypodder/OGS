"""
OGS Smart Money AI
------------------

SMT Divergence Factory

Factory for creating validated SMT Divergence objects.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from datetime import datetime

from .domain import SMTDivergence
from .enums import (
    SMTComparisonType,
    SMTConfidence,
    SMTDivergenceDirection,
)
from .validator import SMTDivergenceValidator


class SMTDivergenceFactory:
    """
    Factory for creating SMT Divergence objects.
    """

    _validator = SMTDivergenceValidator()

    @classmethod
    def create(
        cls,
        *,
        first_symbol: str,
        second_symbol: str,
        first_price: float,
        second_price: float,
        comparison: SMTComparisonType,
        direction: SMTDivergenceDirection,
        timestamp: datetime,
        confidence: SMTConfidence = SMTConfidence.MEDIUM,
    ) -> SMTDivergence:
        """
        Create a validated SMT Divergence.

        Returns
        -------
        SMTDivergence
        """

        divergence = SMTDivergence(
            first_symbol=first_symbol,
            second_symbol=second_symbol,
            first_price=first_price,
            second_price=second_price,
            comparison=comparison,
            direction=direction,
            timestamp=timestamp,
            confidence=confidence,
        )

        if not cls._validator.validate(divergence):
            raise ValueError("Invalid SMT Divergence.")

        return divergence