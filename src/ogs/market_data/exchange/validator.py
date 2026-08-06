"""
OGS Smart Money AI

Exchange Validator
"""

from __future__ import annotations

from datetime import datetime

from ogs.framework import BaseValidator
from ogs.market_data.broker import BrokerCollection

from .domain import Exchange
from .enums import (
    ExchangeStatus,
    TradingSession,
)


class ExchangeValidator(BaseValidator):
    """
    Validator for Exchange objects.
    """

    def validate(
        self,
        exchange: Exchange,
    ) -> bool:

        if not isinstance(exchange, Exchange):
            raise TypeError(
                "Expected Exchange."
            )

        if not exchange.exchange_id:
            raise ValueError(
                "Exchange ID cannot be empty."
            )

        if not exchange.name:
            raise ValueError(
                "Exchange name cannot be empty."
            )

        if not isinstance(
            exchange.session,
            TradingSession,
        ):
            raise ValueError(
                "Invalid TradingSession."
            )

        if not isinstance(
            exchange.status,
            ExchangeStatus,
        ):
            raise ValueError(
                "Invalid ExchangeStatus."
            )

        if not isinstance(
            exchange.brokers,
            BrokerCollection,
        ):
            raise ValueError(
                "Invalid BrokerCollection."
            )

        if not isinstance(
            exchange.created_at,
            datetime,
        ):
            raise ValueError(
                "Invalid created_at."
            )

        if not isinstance(
            exchange.updated_at,
            datetime,
        ):
            raise ValueError(
                "Invalid updated_at."
            )

        return True

    def __call__(
        self,
        exchange: Exchange,
    ) -> bool:

        return self.validate(exchange)