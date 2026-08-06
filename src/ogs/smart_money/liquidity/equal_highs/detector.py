"""
===========================================================

OGS Smart Money AI

Equal High Detector

===========================================================
"""

from __future__ import annotations

from decimal import Decimal

from ogs.smart_money.base import BaseDetector
from ogs.smart_money.swing import SwingSeries

from .collection import EqualHighSeries
from .constants import DEFAULT_TOLERANCE
from .domain import EqualHigh
from .enums import EqualHighType


class EqualHighDetector(
    BaseDetector[
        SwingSeries,
        EqualHighSeries,
    ]
):
    """
    Detect Equal High liquidity zones.
    """

    def detect(
        self,
        swings: SwingSeries,
    ) -> EqualHighSeries:

        if swings is None:
            return EqualHighSeries([])

        if len(swings) < 2:
            return EqualHighSeries([])

        zones: list[EqualHigh] = []

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
                    EqualHigh(
                        first_swing=first,
                        second_swing=second,
                        zone_price=zone_price,
                        tolerance=tolerance,
                        equal_high_type=EqualHighType.CONFIRMED,
                    )
                )

        return EqualHighSeries(zones)