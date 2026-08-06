"""
OGS Smart Money AI

Market Validator
"""

from __future__ import annotations

from datetime import datetime

from .domain import Market
from .enums import (
    MarketStatus,
    MarketType,
)


class MarketValidator:
    """
    Validator for Market.
    """

    def __call__(
        self,
        market: Market,
    ) -> bool:

        if not isinstance(market.market_id, str) or not market.market_id.strip():
            raise ValueError("Invalid market_id.")

        if not isinstance(market.name, str) or not market.name.strip():
            raise ValueError("Invalid market name.")

        if not isinstance(market.market_type, MarketType):
            raise ValueError("Invalid market type.")

        if not isinstance(market.status, MarketStatus):
            raise ValueError("Invalid market status.")

        if not hasattr(market.exchanges, "items"):
            raise ValueError("Invalid ExchangeCollection.")

        if not isinstance(market.created_at, datetime):
            raise ValueError("Invalid created_at.")

        if not isinstance(market.updated_at, datetime):
            raise ValueError("Invalid updated_at.")

        return True