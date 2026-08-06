"""
OGS Smart Money AI

Account Validator
"""

from __future__ import annotations

from datetime import datetime

from ogs.framework import BaseValidator
from ogs.market_data.portfolio import PortfolioCollection

from .domain import Account
from .enums import (
    AccountStatus,
    AccountType,
)


class AccountValidator(BaseValidator):
    """
    Validator for Account objects.
    """

    def validate(
        self,
        account: Account,
    ) -> bool:

        if not isinstance(account, Account):
            raise TypeError(
                "Expected Account."
            )

        if not account.account_id:
            raise ValueError(
                "Account ID cannot be empty."
            )

        if not account.name:
            raise ValueError(
                "Account name cannot be empty."
            )

        if not isinstance(
            account.account_type,
            AccountType,
        ):
            raise ValueError(
                "Invalid AccountType."
            )

        if not isinstance(
            account.status,
            AccountStatus,
        ):
            raise ValueError(
                "Invalid AccountStatus."
            )

        if not isinstance(
            account.portfolios,
            PortfolioCollection,
        ):
            raise ValueError(
                "Invalid PortfolioCollection."
            )

        if account.initial_balance < 0:
            raise ValueError(
                "Initial balance cannot be negative."
            )

        if account.cash_balance < 0:
            raise ValueError(
                "Cash balance cannot be negative."
            )

        if account.buying_power < 0:
            raise ValueError(
                "Buying power cannot be negative."
            )

        if account.margin_used < 0:
            raise ValueError(
                "Margin used cannot be negative."
            )

        if account.leverage <= 0:
            raise ValueError(
                "Leverage must be positive."
            )

        if not isinstance(
            account.created_at,
            datetime,
        ):
            raise ValueError(
                "Invalid created_at."
            )

        if not isinstance(
            account.updated_at,
            datetime,
        ):
            raise ValueError(
                "Invalid updated_at."
            )

        return True

    def __call__(
        self,
        account: Account,
    ) -> bool:

        return self.validate(account)