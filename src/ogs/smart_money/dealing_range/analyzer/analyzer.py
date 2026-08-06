"""
OGS FinOS

Dealing Range Analyzer

Constructs institutional dealing ranges from
confirmed swing highs and swing lows.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from decimal import Decimal

from ogs.smart_money.dealing_range.collection import (
    DealingRangeCollection,
)
from ogs.smart_money.dealing_range.domain import (
    DealingRange,
)
from ogs.smart_money.dealing_range.enums import (
    DealingRangeDirection,
)


class DealingRangeAnalyzer:
    """
    Builds immutable DealingRange objects.
    """

    def analyze(
        self,
        *,
        swing_high: Decimal,
        swing_low: Decimal,
        start_index: int,
        end_index: int,
        direction: DealingRangeDirection,
    ) -> DealingRangeCollection:
        """
        Create a dealing range from a confirmed
        swing high and swing low.
        """

        equilibrium = self._calculate_equilibrium(
            swing_high,
            swing_low,
        )

        dealing_range = DealingRange(
            range_high=swing_high,
            range_low=swing_low,
            equilibrium=equilibrium,
            direction=direction,
            start_index=start_index,
            end_index=end_index,
        )

        collection = DealingRangeCollection()

        collection.add(dealing_range)

        return collection

    @staticmethod
    def _calculate_equilibrium(
        range_high: Decimal,
        range_low: Decimal,
    ) -> Decimal:
        """
        Midpoint of the dealing range.
        """

        return (
            range_high + range_low
        ) / Decimal("2")