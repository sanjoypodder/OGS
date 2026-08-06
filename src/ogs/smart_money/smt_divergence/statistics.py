"""
OGS Smart Money AI
------------------

SMT Divergence Statistics

Provides statistical information about a collection
of SMT Divergence objects.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from .collection import SMTDivergenceSeries
from .domain import SMTDivergence
from .enums import (
    SMTConfidence,
    SMTDivergenceDirection,
)


class SMTDivergenceStatistics:
    """
    Statistics for SMT Divergence collections.
    """

    def __init__(
        self,
        series: SMTDivergenceSeries,
    ) -> None:
        self._series = series

    @property
    def count(self) -> int:
        return len(self._series)

    @property
    def bullish_count(self) -> int:
        return sum(
            divergence.direction == SMTDivergenceDirection.BULLISH
            for divergence in self._series
        )

    @property
    def bearish_count(self) -> int:
        return sum(
            divergence.direction == SMTDivergenceDirection.BEARISH
            for divergence in self._series
        )

    @property
    def hidden_bullish_count(self) -> int:
        return sum(
            divergence.direction == SMTDivergenceDirection.HIDDEN_BULLISH
            for divergence in self._series
        )

    @property
    def hidden_bearish_count(self) -> int:
        return sum(
            divergence.direction == SMTDivergenceDirection.HIDDEN_BEARISH
            for divergence in self._series
        )

    @property
    def high_confidence_count(self) -> int:
        return sum(
            divergence.confidence == SMTConfidence.HIGH
            for divergence in self._series
        )

    @property
    def medium_confidence_count(self) -> int:
        return sum(
            divergence.confidence == SMTConfidence.MEDIUM
            for divergence in self._series
        )

    @property
    def low_confidence_count(self) -> int:
        return sum(
            divergence.confidence == SMTConfidence.LOW
            for divergence in self._series
        )

    @property
    def latest(self) -> SMTDivergence | None:
        if len(self._series) == 0:
            return None

        return self._series.last

    @property
    def oldest(self) -> SMTDivergence | None:
        if len(self._series) == 0:
            return None

        return self._series.first