"""
===========================================================

OGS Smart Money AI

Market Structure Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.market import Candle
from ogs.smart_money.base import BaseAnalyzer

from .collection import SwingSeries
from .domain import SwingPoint
from .enums import (
    SwingStrength,
    SwingType,
)
from .factory import SwingPointFactory


class MarketStructureAnalyzer(
    BaseAnalyzer[
        list[Candle],
        SwingSeries,
    ],
):
    """
    Detects market structure swing points.
    """

    def __init__(
        self,
        pivot_depth: int = 2,
    ) -> None:

        self._pivot_depth = pivot_depth

    def analyze(
        self,
        candles: list[Candle],
    ) -> SwingSeries:

        swings = SwingSeries()

        if len(candles) < (self._pivot_depth * 2 + 1):
            return swings

        previous_high = None
        previous_low = None

        for i in range(
            self._pivot_depth,
            len(candles) - self._pivot_depth,
        ):

            candle = candles[i]

            # ---------------------------------------
            # Pivot High
            # ---------------------------------------

            if self._is_pivot_high(candles, i):

                if previous_high is None:

                    swing_type = SwingType.HIGH

                elif candle.high > previous_high:

                    swing_type = SwingType.HIGHER_HIGH

                else:

                    swing_type = SwingType.LOWER_HIGH

                previous_high = candle.high

                swings.append(
                    SwingPointFactory.create(
                        symbol=candle.symbol,
                        candle=candle,
                        index=i,
                        price=float(candle.high.value),
                        type=swing_type,
                        strength=SwingStrength.NORMAL,
                    )
                )

            # ---------------------------------------
            # Pivot Low
            # ---------------------------------------

            elif self._is_pivot_low(candles, i):

                if previous_low is None:

                    swing_type = SwingType.LOW

                elif candle.low > previous_low:

                    swing_type = SwingType.HIGHER_LOW

                else:

                    swing_type = SwingType.LOWER_LOW

                previous_low = candle.low

                swings.append(
                    SwingPointFactory.create(
                        symbol=candle.symbol,
                        candle=candle,
                        index=i,
                        price=float(candle.low.value),
                        type=swing_type,
                        strength=SwingStrength.NORMAL,
                    )
                )

        return swings

    # -------------------------------------------------
    # Helpers
    # -------------------------------------------------

    def _is_pivot_high(
        self,
        candles: list[Candle],
        index: int,
    ) -> bool:

        high = candles[index].high

        for i in range(
            index - self._pivot_depth,
            index + self._pivot_depth + 1,
        ):

            if i == index:
                continue

            if candles[i].high >= high:
                return False

        return True

    def _is_pivot_low(
        self,
        candles: list[Candle],
        index: int,
    ) -> bool:

        low = candles[index].low

        for i in range(
            index - self._pivot_depth,
            index + self._pivot_depth + 1,
        ):

            if i == index:
                continue

            if candles[i].low <= low:
                return False

        return True