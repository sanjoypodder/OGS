"""
Tests for Account domain.
"""

from ogs.market_data.account import (
    Account,
    AccountStatus,
    AccountType,
)


def test_default_account():

    account = Account()

    assert account.account_id == ""
    assert account.name == ""
    assert account.broker == ""
    assert account.account_number == ""
    assert account.account_type == AccountType.UNKNOWN
    assert account.status == AccountStatus.UNKNOWN
    assert account.base_currency == "USD"

    assert account.initial_balance == 0.0
    assert account.cash_balance == 0.0
    assert account.buying_power == 0.0
    assert account.margin_used == 0.0
    assert account.leverage == 1.0

    assert account.portfolio_count == 0
    assert account.total_market_value == 0.0
    assert account.total_cash == 0.0
    assert account.total_equity == 0.0
    assert account.total_realized_pnl == 0.0
    assert account.total_unrealized_pnl == 0.0
    assert account.total_pnl == 0.0
    assert account.available_margin == 0.0
    assert account.return_percentage == 0.0

    assert account.is_valid


def test_to_dict():

    account = Account()

    data = account.to_dict()

    assert isinstance(data, dict)

    assert data["account_id"] == ""
    assert data["portfolio_count"] == 0


def test_str():

    account = Account()

    assert "Account" in str(account)


def test_is_active():

    account = Account(status=AccountStatus.ACTIVE)

    assert account.is_active


def test_return_percentage_zero():

    account = Account()

    assert account.return_percentage == 0.0