"""
OGS Smart Money AI

Account Factory
"""

from __future__ import annotations

from copy import deepcopy

from ogs.framework import BaseFactory

from .domain import Account
from .enums import (
    AccountStatus,
    AccountType,
)
from .validator import AccountValidator


class AccountFactory(BaseFactory):
    """
    Factory for Account objects.
    """

    validator = AccountValidator()

    @classmethod
    def create(
        cls,
        **kwargs,
    ) -> Account:

        account = Account(**kwargs)

        cls.validator(account)

        return account

    @classmethod
    def live(
        cls,
        **kwargs,
    ) -> Account:

        kwargs["account_type"] = AccountType.LIVE
        kwargs.setdefault(
            "status",
            AccountStatus.ACTIVE,
        )

        return cls.create(**kwargs)

    @classmethod
    def paper(
        cls,
        **kwargs,
    ) -> Account:

        kwargs["account_type"] = AccountType.PAPER
        kwargs.setdefault(
            "status",
            AccountStatus.ACTIVE,
        )

        return cls.create(**kwargs)

    @classmethod
    def backtest(
        cls,
        **kwargs,
    ) -> Account:

        kwargs["account_type"] = AccountType.BACKTEST
        kwargs.setdefault(
            "status",
            AccountStatus.ACTIVE,
        )

        return cls.create(**kwargs)

    @classmethod
    def clone(
        cls,
        account: Account,
    ) -> Account:

        clone = deepcopy(account)

        cls.validator(clone)

        return clone