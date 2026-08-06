"""
===========================================================

OGS Smart Money AI

Equal Low Detector

===========================================================
"""

from __future__ import annotations

from decimal import Decimal

from ogs.smart_money.base import BaseDetector
from ogs.smart_money.swing import SwingSeries

from .collection import EqualLowSeries
from .constants import DEFAULT_TOLERANCE
from .domain import EqualLow
from .enums import EqualLowType


class EqualLowDetector(
    BaseDetector[
        SwingSeries,
        EqualLowSeries,
    ]
):
    """
    Detect Equal Low liquidity zones.
    """

    def detect(
        self,
        swings: SwingSeries,
    ) -> EqualLowSeries:

        if swings is None:
            return EqualLowSeries([])

        if len(swings) < 2:
            return EqualLowSeries([])

        zones: list[EqualLow] = []

        tolerance = Decimal(str(DEFAULT_TOLERANCE))

        for i in range(len(swings) - 1):

            first = swings[i]
            second = swings[i + 1]

            first_price = Decimal(str(first.price.value))
            second_price = Decimal(str(second.price.value))

            if abs(first_price - second_price) <= tolerance:

                zone_price = (
                    first_price + second_price
                ) / Decimal("2")

                zones.append(
                    EqualLow(
                        first_swing=first,
                        second_swing=second,
                        zone_price=zone_price,
                        tolerance=tolerance,
                        equal_low_type=EqualLowType.CONFIRMED,
                    )
                )

        return EqualLowSeries(zones)