"""
===========================================================

OGS Smart Money AI

Balanced Price Range Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseAnalyzer

from ogs.smart_money.fair_value_gap.collection import (
    FairValueGapSeries,
)

from ogs.smart_money.fair_value_gap.enums import (
    FairValueGapDirection,
)

from .collection import (
    BalancedPriceRangeSeries,
)

from .domain import (
    BalancedPriceRange,
)

from .enums import (
    BalancedPriceRangeDirection,
)


class BalancedPriceRangeAnalyzer(
    BaseAnalyzer[
        FairValueGapSeries,
        BalancedPriceRangeSeries,
    ]
):
    """
    Detect Balanced Price Ranges.
    """

    def analyze(
        self,
        data: FairValueGapSeries,
    ) -> BalancedPriceRangeSeries:

        series = BalancedPriceRangeSeries()

        if len(data) < 2:
            return series

        bullish = [
            gap
            for gap in data
            if gap.direction
            is FairValueGapDirection.BULLISH
        ]

        bearish = [
            gap
            for gap in data
            if gap.direction
            is FairValueGapDirection.BEARISH
        ]

        for bull in bullish:

            for bear in bearish:

                overlap_top = min(
                    bull.top,
                    bear.top,
                )

                overlap_bottom = max(
                    bull.bottom,
                    bear.bottom,
                )

                if overlap_top <= overlap_bottom:
                    continue

                midpoint = (
                    overlap_top
                    + overlap_bottom
                ) / 2

                size = (
                    overlap_top
                    - overlap_bottom
                )

                direction = (
                    BalancedPriceRangeDirection.BULLISH
                    if bull.size >= bear.size
                    else BalancedPriceRangeDirection.BEARISH
                )

                series.append(

                    BalancedPriceRange(

                        bullish_gap=bull,

                        bearish_gap=bear,

                        direction=direction,

                        top=overlap_top,

                        bottom=overlap_bottom,

                        midpoint=midpoint,

                        size=size,
                    )
                )

        return series