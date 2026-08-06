"""
OGS Smart Money AI

Market Factory
"""

from __future__ import annotations

from copy import deepcopy

from .domain import Market
from .enums import MarketStatus


class MarketFactory:
    """
    Factory for Market objects.
    """

    @staticmethod
    def create(
        market_id: str,
        name: str,
        **kwargs,
    ) -> Market:

        return Market(
            market_id=market_id,
            name=name,
            **kwargs,
        )

    @staticmethod
    def open(
        market_id: str,
        name: str,
        **kwargs,
    ) -> Market:

        return Market(
            market_id=market_id,
            name=name,
            status=MarketStatus.OPEN,
            **kwargs,
        )

    @staticmethod
    def closed(
        market_id: str,
        name: str,
        **kwargs,
    ) -> Market:

        return Market(
            market_id=market_id,
            name=name,
            status=MarketStatus.CLOSED,
            **kwargs,
        )

    @staticmethod
    def clone(
        market: Market,
    ) -> Market:

        return deepcopy(market)