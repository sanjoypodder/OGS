"""
OGS Smart Money AI

Broker Domain
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime

from ogs.market_data.account import (
    Account,
    AccountCollection,
)

from .enums import (
    BrokerStatus,
    MarketType,
)


@dataclass(slots=True)
class Broker:
    """
    Represents a brokerage.
    """

    broker_id: str = ""

    name: str = ""

    country: str = ""

    timezone: str = "UTC"

    website: str = ""

    status: BrokerStatus = BrokerStatus.UNKNOWN

    supported_markets: list[MarketType] = field(
        default_factory=list
    )

    accounts: AccountCollection = field(
        default_factory=AccountCollection
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def account_count(self) -> int:
        return len(self.accounts)

    @property
    def active_account_count(self) -> int:
        return sum(
            account.is_active
            for account in self.accounts
        )

    @property
    def total_equity(self) -> float:
        return sum(
            account.total_equity
            for account in self.accounts
        )

    @property
    def total_cash(self) -> float:
        return sum(
            account.total_cash
            for account in self.accounts
        )

    @property
    def total_buying_power(self) -> float:
        return sum(
            account.buying_power
            for account in self.accounts
        )

    @property
    def total_margin_used(self) -> float:
        return sum(
            account.margin_used
            for account in self.accounts
        )

    @property
    def is_active(self) -> bool:
        return self.status == BrokerStatus.ACTIVE

    @property
    def is_valid(self) -> bool:
        return (
            self.broker_id != ""
            and self.name != ""
        )

    def add_account(
        self,
        account: Account,
    ) -> None:
        self.accounts.append(account)

    def to_dict(self) -> dict:

        return {
            "broker_id": self.broker_id,
            "name": self.name,
            "country": self.country,
            "timezone": self.timezone,
            "website": self.website,
            "status": self.status.value,
            "supported_markets": [
                market.value
                for market in self.supported_markets
            ],
            "account_count": self.account_count,
            "active_account_count": self.active_account_count,
            "total_equity": self.total_equity,
            "total_cash": self.total_cash,
            "total_buying_power": self.total_buying_power,
            "total_margin_used": self.total_margin_used,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __str__(self) -> str:

        return (
            f"Broker("
            f"id={self.broker_id}, "
            f"name={self.name}, "
            f"accounts={self.account_count})"
        )