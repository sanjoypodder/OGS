"""
OGS Smart Money AI

Exchange Domain
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime

from ogs.market_data.broker import (
    Broker,
    BrokerCollection,
)

from .enums import (
    ExchangeStatus,
    TradingSession,
)


@dataclass(slots=True)
class Exchange:
    """
    Represents a financial exchange.
    """

    exchange_id: str = ""

    name: str = ""

    mic: str = ""

    country: str = ""

    timezone: str = "UTC"

    currency: str = "USD"

    session: TradingSession = TradingSession.REGULAR

    status: ExchangeStatus = ExchangeStatus.UNKNOWN

    brokers: BrokerCollection = field(
        default_factory=BrokerCollection
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def broker_count(self) -> int:
        return len(self.brokers)

    @property
    def active_broker_count(self) -> int:
        return sum(
            broker.is_active
            for broker in self.brokers
        )

    @property
    def account_count(self) -> int:
        return sum(
            broker.account_count
            for broker in self.brokers
        )

    @property
    def total_equity(self) -> float:
        return sum(
            broker.total_equity
            for broker in self.brokers
        )

    @property
    def total_cash(self) -> float:
        return sum(
            broker.total_cash
            for broker in self.brokers
        )

    @property
    def total_buying_power(self) -> float:
        return sum(
            broker.total_buying_power
            for broker in self.brokers
        )

    @property
    def total_margin_used(self) -> float:
        return sum(
            broker.total_margin_used
            for broker in self.brokers
        )

    @property
    def is_open(self) -> bool:
        return self.status == ExchangeStatus.OPEN

    @property
    def is_valid(self) -> bool:
        return (
            self.exchange_id != ""
            and self.name != ""
        )

    def add_broker(
        self,
        broker: Broker,
    ) -> None:
        self.brokers.append(broker)

    def to_dict(self) -> dict:

        return {
            "exchange_id": self.exchange_id,
            "name": self.name,
            "mic": self.mic,
            "country": self.country,
            "timezone": self.timezone,
            "currency": self.currency,
            "session": self.session.value,
            "status": self.status.value,
            "broker_count": self.broker_count,
            "active_broker_count": self.active_broker_count,
            "account_count": self.account_count,
            "total_equity": self.total_equity,
            "total_cash": self.total_cash,
            "total_buying_power": self.total_buying_power,
            "total_margin_used": self.total_margin_used,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __str__(self) -> str:

        return (
            f"Exchange("
            f"id={self.exchange_id}, "
            f"name={self.name}, "
            f"brokers={self.broker_count})"
        )   