"""
OGS Smart Money AI

Account Collection
"""

from __future__ import annotations

from ogs.framework import BaseCollection

from .domain import Account
from .enums import (
    AccountStatus,
    AccountType,
)


class AccountCollection(BaseCollection[Account]):
    """
    Collection of Account objects.
    """

    def __init__(self, items=None):
        super().__init__(items)

    @property
    def items(self) -> list[Account]:
        """
        Compatibility property.
        """
        return self._items

    def add(
        self,
        account: Account,
    ) -> None:
        self.append(account)

    def active(self) -> list[Account]:
        return [
            account
            for account in self
            if account.status == AccountStatus.ACTIVE
        ]

    def inactive(self) -> list[Account]:
        return [
            account
            for account in self
            if account.status == AccountStatus.INACTIVE
        ]

    def live(self) -> list[Account]:
        return [
            account
            for account in self
            if account.account_type == AccountType.LIVE
        ]

    def paper(self) -> list[Account]:
        return [
            account
            for account in self
            if account.account_type == AccountType.PAPER
        ]

    def backtest(self) -> list[Account]:
        return [
            account
            for account in self
            if account.account_type == AccountType.BACKTEST
        ]

    def find(
        self,
        account_id: str,
    ) -> Account | None:

        return next(
            (
                account
                for account in self
                if account.account_id == account_id
            ),
            None,
        )

    def total_equity(self) -> float:
        return sum(
            account.total_equity
            for account in self
        )

    def total_cash(self) -> float:
        return sum(
            account.total_cash
            for account in self
        )

    def total_market_value(self) -> float:
        return sum(
            account.total_market_value
            for account in self
        )

    def total_realized_pnl(self) -> float:
        return sum(
            account.total_realized_pnl
            for account in self
        )

    def total_unrealized_pnl(self) -> float:
        return sum(
            account.total_unrealized_pnl
            for account in self
        )

    def total_pnl(self) -> float:
        return sum(
            account.total_pnl
            for account in self
        )

    def to_list(self) -> list[dict]:
        return [
            account.to_dict()
            for account in self
        ]