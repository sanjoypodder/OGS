"""
OGS Smart Money AI
------------------

SMT Divergence Analyzer

Detects Smart Money Technique (SMT) Divergences between two
correlated markets.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import SMTDivergenceSeries
from .domain import SMTDivergence
from .enums import (
    SMTComparisonType,
    SMTConfidence,
    SMTDivergenceDirection,
)


class SMTDivergenceAnalyzer(
    BaseAnalyzer,
):
    """
    Analyzer for detecting SMT Divergences.
    """

    def analyze(
        self,
        first_swings,
        second_swings,
    ) -> SMTDivergenceSeries:
        """
        Analyze two synchronized swing sequences and detect SMT
        divergences.

        Parameters
        ----------
        first_swings
            Swing points of the first market.

        second_swings
            Swing points of the second market.

        Returns
        -------
        SMTDivergenceSeries
        """

        divergences = SMTDivergenceSeries()

        if len(first_swings) != len(second_swings):
            return divergences

        for first, second in zip(first_swings, second_swings):

            direction = self._detect_direction(
                first,
                second,
            )

            if direction is None:
                continue

            divergences.append(
                SMTDivergence(
                    first_symbol=first.symbol,
                    second_symbol=second.symbol,
                    first_price=first.price,
                    second_price=second.price,
                    comparison=first.comparison,
                    direction=direction,
                    timestamp=first.timestamp,
                    confidence=SMTConfidence.MEDIUM,
                )
            )

        return divergences

    @staticmethod
    def _detect_direction(
        first,
        second,
    ) -> SMTDivergenceDirection | None:
        """
        Detect SMT divergence direction between two swing points.
        """

        if (
            first.is_higher_high
            and second.is_lower_high
        ):
            return SMTDivergenceDirection.BEARISH

        if (
            first.is_lower_low
            and second.is_higher_low
        ):
            return SMTDivergenceDirection.BULLISH

        if (
            first.is_higher_low
            and second.is_lower_low
        ):
            return SMTDivergenceDirection.HIDDEN_BULLISH

        if (
            first.is_lower_high
            and second.is_higher_high
        ):
            return SMTDivergenceDirection.HIDDEN_BEARISH

        return None