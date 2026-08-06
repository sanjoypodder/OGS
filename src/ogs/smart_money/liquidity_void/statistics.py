"""
Liquidity Void Statistics
"""

from .collection import LiquidityVoidSeries


class LiquidityVoidStatistics:
    """
    Statistics for Liquidity Void collections.
    """

    def __init__(self, series: LiquidityVoidSeries) -> None:
        self._series = series

    @property
    def total(self) -> int:
        return len(self._series)

    @property
    def bullish(self) -> int:
        return sum(item.is_bullish for item in self._series)

    @property
    def bearish(self) -> int:
        return sum(item.is_bearish for item in self._series)

    @property
    def filled(self) -> int:
        return sum(item.is_filled for item in self._series)

    @property
    def unfilled(self) -> int:
        return self.total - self.filled