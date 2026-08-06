"""
OGS Smart Money AI

Broker Validator
"""

from __future__ import annotations

from datetime import datetime

from ogs.framework import BaseValidator
from ogs.market_data.account import AccountCollection

from .domain import Broker
from .enums import (
    BrokerStatus,
    MarketType,
)


class BrokerValidator(BaseValidator):
    """
    Validator for Broker.
    """

    def validate(
        self,
        broker: Broker,
    ) -> bool:

        if not isinstance(
            broker,
            Broker,
        ):
            raise TypeError(
                "Expected Broker."
            )

        if not broker.broker_id:
            raise ValueError(
                "Broker ID cannot be empty."
            )

        if not broker.name:
            raise ValueError(
                "Broker name cannot be empty."
            )

        if not isinstance(
            broker.status,
            BrokerStatus,
        ):
            raise ValueError(
                "Invalid BrokerStatus."
            )

        if not isinstance(
            broker.accounts,
            AccountCollection,
        ):
            raise ValueError(
                "Invalid AccountCollection."
            )

        for market in broker.supported_markets:
            if not isinstance(
                market,
                MarketType,
            ):
                raise ValueError(
                    "Invalid MarketType."
                )

        if not isinstance(
            broker.created_at,
            datetime,
        ):
            raise ValueError(
                "Invalid created_at."
            )

        if not isinstance(
            broker.updated_at,
            datetime,
        ):
            raise ValueError(
                "Invalid updated_at."
            )

        return True

    def __call__(
        self,
        broker: Broker,
    ) -> bool:

        return self.validate(
            broker
        )