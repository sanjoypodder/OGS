"""
===========================================================

OGS Smart Money AI

Order Block Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.engine import Analysis
from ogs.market import Candle, CandleSeries

from .candidate import OrderBlockCandidate
from .candidate_builder import OrderBlockCandidateBuilder
from .collection import OrderBlockSeries


class OrderBlockAnalyzer:
    """
    Institutional Order Block analyzer.
    """

    def __init__(self):

        self._builder = OrderBlockCandidateBuilder()

    def analyze(
        self,
        candles: CandleSeries,
        analysis: Analysis,
    ) -> OrderBlockSeries:

        candidates = self._build_candidates(
            candles,
            analysis,
        )

        candidates = self._validate_candidates(
            candidates,
            analysis,
        )

        return self._build_order_blocks(
            candidates,
        )

    # --------------------------------------------------

    def _build_candidates(
        self,
        candles: CandleSeries,
        analysis: Analysis,
    ) -> list[OrderBlockCandidate]:

        candidates = []

        if len(analysis.sweeps) == 0:
            return candidates

        if len(analysis.mss) == 0:
            return candidates

        for sweep in analysis.sweeps:

            for mss in analysis.mss:

                if mss.timestamp <= sweep.timestamp:
                    continue

                origin = self._find_last_bearish_candle(
                    candles,
                    mss.timestamp,
                )

                if origin is None:
                    break

                candidate = self._builder.build(
                    origin_candle=origin,
                    mss=mss,
                    liquidity_sweep=sweep,
                )

                candidates.append(candidate)

                break

        return candidates

    # --------------------------------------------------

    def _validate_candidates(
        self,
        candidates: list[OrderBlockCandidate],
        analysis: Analysis,
    ) -> list[OrderBlockCandidate]:

        return candidates

    # --------------------------------------------------

    def _build_order_blocks(
        self,
        candidates: list[OrderBlockCandidate],
    ) -> OrderBlockSeries:

        return OrderBlockSeries([])

    # --------------------------------------------------

    def _find_last_bearish_candle(
        self,
        candles: CandleSeries,
        mss_timestamp,
    ) -> Candle | None:

        last_bearish = None

        for candle in candles:

            if candle.timestamp >= mss_timestamp:
                break

            if candle.close.value < candle.open.value:
                last_bearish = candle

        return last_bearish

    # --------------------------------------------------
    # Temporary TDD helper
    # --------------------------------------------------

    def candidate_count(
        self,
        candles: CandleSeries,
        analysis: Analysis,
    ) -> int:

        return len(
            self._build_candidates(
                candles,
                analysis,
            )
        )