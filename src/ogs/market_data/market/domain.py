"""
OGS Smart Money AI

Market Domain
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from ogs.market_data.exchange import (
    Exchange,
    ExchangeCollection,
)

from .enums import (
    MarketStatus,
    MarketType,
)


@dataclass(slots=True)
class Market:
    """
    Represents a financial market.
    """

    market_id: str = ""
    name: str = ""
    country: str = ""
    currency: str = "USD"
    timezone: str = "UTC"

    market_type: MarketType = MarketType.EQUITY
    status: MarketStatus = MarketStatus.UNKNOWN

    exchanges: ExchangeCollection = field(
        default_factory=ExchangeCollection
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def exchange_count(self) -> int:
        return len(self.exchanges)

    @property
    def broker_count(self) -> int:
        return self.exchanges.total_brokers()

    @property
    def account_count(self) -> int:
        return self.exchanges.total_accounts()

    @property
    def total_equity(self) -> float:
        return self.exchanges.total_equity()

    @property
    def total_cash(self) -> float:
        return self.exchanges.total_cash()

    @property
    def total_buying_power(self) -> float:
        return self.exchanges.total_buying_power()

    @property
    def total_margin_used(self) -> float:
        return self.exchanges.total_margin_used()

    @property
    def is_open(self) -> bool:
        return self.status == MarketStatus.OPEN

    @property
    def is_valid(self) -> bool:
        return (
            bool(self.market_id.strip())
            and bool(self.name.strip())
        )

    def add_exchange(
        self,
        exchange: Exchange,
    ) -> None:
        self.exchanges.add(exchange)

    def to_dict(self) -> dict:
        return {
            "market_id": self.market_id,
            "name": self.name,
            "country": self.country,
            "currency": self.currency,
            "timezone": self.timezone,
            "market_type": self.market_type.value,
            "status": self.status.value,
            "exchange_count": self.exchange_count,
            "broker_count": self.broker_count,
            "account_count": self.account_count,
            "total_equity": self.total_equity,
            "total_cash": self.total_cash,
            "total_buying_power": self.total_buying_power,
            "total_margin_used": self.total_margin_used,
        }

    def __str__(self) -> str:
        return (
            f"Market("
            f"id='{self.market_id}', "
            f"name='{self.name}', "
            f"status='{self.status.value}')"
        )