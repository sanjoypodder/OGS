"""
===========================================================

OGS Smart Money AI

Rejection Block Analyzer

===========================================================
"""

from __future__ import annotations

from decimal import Decimal

from ogs.market.candle import Candle
from ogs.smart_money.base import BaseAnalyzer

from .collection import RejectionBlockSeries
from .domain import RejectionBlock
from .enums import RejectionBlockDirection


class RejectionBlockAnalyzer(
    BaseAnalyzer[list[Candle], RejectionBlockSeries]
):
    """
    Detects ICT Rejection Blocks.

    Version 1
    ---------
    Detects wick rejection with confirmation.

    Future versions will integrate with:
        • BOS
        • CHOCH
        • Order Block
        • Liquidity
    """

    def analyze(
        self,
        candles: list[Candle],
    ) -> RejectionBlockSeries:

        series = RejectionBlockSeries()

        if len(candles) < 2:
            return series

        for i in range(1, len(candles)):

            rejection = candles[i - 1]
            confirmation = candles[i]

            upper_wick = (
                rejection.high.value
                - max(
                    rejection.open.value,
                    rejection.close.value,
                )
            )

            lower_wick = (
                min(
                    rejection.open.value,
                    rejection.close.value,
                )
                - rejection.low.value
            )

            body = abs(
                rejection.close.value
                - rejection.open.value
            )

            # Avoid division by zero
            if body == Decimal("0"):
                body = Decimal("0.01")

            # -----------------------------
            # Bullish Rejection
            # -----------------------------
            if (
                lower_wick >= body * 2
                and confirmation.close.value
                > rejection.high.value
            ):

                series.append(
                    RejectionBlock(
                        candle=rejection,
                        direction=RejectionBlockDirection.BULLISH,
                        top=rejection.high.value,
                        bottom=rejection.low.value,
                        midpoint=(
                            rejection.high.value
                            + rejection.low.value
                        ) / 2,
                        size=(
                            rejection.high.value
                            - rejection.low.value
                        ),
                        is_confirmed=True,
                    )
                )

            # -----------------------------
            # Bearish Rejection
            # -----------------------------
            elif (
                upper_wick >= body * 2
                and confirmation.close.value
                < rejection.low.value
            ):

                series.append(
                    RejectionBlock(
                        candle=rejection,
                        direction=RejectionBlockDirection.BEARISH,
                        top=rejection.high.value,
                        bottom=rejection.low.value,
                        midpoint=(
                            rejection.high.value
                            + rejection.low.value
                        ) / 2,
                        size=(
                            rejection.high.value
                            - rejection.low.value
                        ),
                        is_confirmed=True,
                    )
                )

        return series