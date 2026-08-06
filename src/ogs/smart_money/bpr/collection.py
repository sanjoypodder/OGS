"""
===========================================================

OGS Smart Money AI

Balanced Price Range Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .domain import BalancedPriceRange


class BalancedPriceRangeSeries(
    BaseCollection[BalancedPriceRange],
):
    """
    Collection of Balanced Price Ranges.
    """

    def __init__(
        self,
    ) -> None:

        self._items: list[
            BalancedPriceRange
        ] = []

    @property
    def balanced_price_ranges(
        self,
    ) -> list[
        BalancedPriceRange
    ]:
        """
        Returns all Balanced Price Ranges.
        """
        return self._items

    def append(
        self,
        balanced_price_range: BalancedPriceRange,
    ) -> None:
        """
        Add a Balanced Price Range.
        """
        self._items.append(
            balanced_price_range
        )

    def latest(
        self,
        count: int = 1,
    ) -> list[
        BalancedPriceRange
    ]:
        """
        Returns latest Balanced Price Ranges.
        """
        return self._items[-count:]