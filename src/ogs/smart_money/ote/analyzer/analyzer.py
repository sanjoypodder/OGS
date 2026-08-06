"""
OGS FinOS

Optimal Trade Entry Analyzer

Constructs institutional OTE objects
from a confirmed DealingRange.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from decimal import Decimal

from ogs.smart_money.dealing_range.domain import (
    DealingRange,
)
from ogs.smart_money.ote.collection import (
    OTECollection,
)
from ogs.smart_money.ote.domain import (
    OTE,
)
from ogs.smart_money.ote.enums import (
    OTEDirection,
)


class OTEAnalyzer:
    """
    Builds immutable OTE objects from a
    confirmed DealingRange.
    """

    def analyze(
        self,
        dealing_range: DealingRange,
    ) -> OTECollection:
        """
        Calculate the institutional OTE zone.
        """

        if dealing_range.is_bullish:

            level_62 = self._bullish_level(
                dealing_range.range_high,
                dealing_range.range_low,
                Decimal("0.62"),
            )

            level_705 = self._bullish_level(
                dealing_range.range_high,
                dealing_range.range_low,
                Decimal("0.705"),
            )

            level_79 = self._bullish_level(
                dealing_range.range_high,
                dealing_range.range_low,
                Decimal("0.79"),
            )

            direction = OTEDirection.BULLISH

        else:

            level_62 = self._bearish_level(
                dealing_range.range_high,
                dealing_range.range_low,
                Decimal("0.62"),
            )

            level_705 = self._bearish_level(
                dealing_range.range_high,
                dealing_range.range_low,
                Decimal("0.705"),
            )

            level_79 = self._bearish_level(
                dealing_range.range_high,
                dealing_range.range_low,
                Decimal("0.79"),
            )

            direction = OTEDirection.BEARISH

        zone_low = min(
            level_62,
            level_79,
        )

        zone_high = max(
            level_62,
            level_79,
        )

        ote = OTE(
            range_high=dealing_range.range_high,
            range_low=dealing_range.range_low,
            level_62=level_62,
            level_705=level_705,
            level_79=level_79,
            zone_low=zone_low,
            zone_high=zone_high,
            direction=direction,
        )

        collection = OTECollection()

        collection.add(ote)

        return collection

    @staticmethod
    def _bullish_level(
        high: Decimal,
        low: Decimal,
        ratio: Decimal,
    ) -> Decimal:
        """
        Bullish Fibonacci retracement.
        """
        return high - (
            (high - low) * ratio
        )

    @staticmethod
    def _bearish_level(
        high: Decimal,
        low: Decimal,
        ratio: Decimal,
    ) -> Decimal:
        """
        Bearish Fibonacci retracement.
        """
        return low + (
            (high - low) * ratio
        )