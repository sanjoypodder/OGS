"""
===========================================================

OGS Smart Money AI

Break of Structure Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.market import CandleSeries
from ogs.smart_money.base import BaseAnalyzer
from ogs.smart_money.swing import SwingSeries, SwingType

from .collection import BOSSeries
from .domain import BOS
from .enums import BOSType


class BOSAnalyzer(
    BaseAnalyzer[
        tuple[CandleSeries, SwingSeries],
        BOSSeries,
    ]
):
    """
    Detect Break of Structure events.
    """

    def analyze(
        self,
        data: tuple[
            CandleSeries,
            SwingSeries,
        ],
    ) -> BOSSeries:

        candles, swings = data

        if candles is None or swings is None:
            return BOSSeries([])

        if len(candles) == 0:
            return BOSSeries([])

        if len(swings) == 0:
            return BOSSeries([])

        bos_events: list[BOS] = []

        for swing in swings:

            # Look only at candles after the swing
            for candle in candles[swing.index + 1:]:

                # Bullish BOS
                if (
                    swing.swing_type == SwingType.HIGH
                    and candle.close > swing.price
                ):
                    bos_events.append(
                        BOS(
                            candle=candle,
                            broken_swing=swing,
                            bos_type=BOSType.BULLISH,
                        )
                    )
                    break

                # Bearish BOS
                if (
                    swing.swing_type == SwingType.LOW
                    and candle.close < swing.price
                ):
                    bos_events.append(
                        BOS(
                            candle=candle,
                            broken_swing=swing,
                            bos_type=BOSType.BEARISH,
                        )
                    )
                    break

        return BOSSeries(bos_events)