"""
Tests for Account validator.
"""

import pytest

from ogs.market_data.account import (
    Account,
    AccountStatus,
    AccountType,
    AccountValidator,
)


def valid_account():

    return Account(
        account_id="ACC001",
        name="Primary",
        broker="Broker",
        account_number="12345",
        account_type=AccountType.LIVE,
        status=AccountStatus.ACTIVE,
        initial_balance=10000,
        cash_balance=5000,
        buying_power=20000,
        margin_used=1000,
        leverage=10,
    )


def test_validator_success():

    validator = AccountValidator()

    assert validator(valid_account())


@pytest.mark.parametrize(
    "field,value",
    [
        ("account_id", ""),
        ("name", ""),
    ],
)
def test_required_fields(field, value):

    account = valid_account()

    setattr(account, field, value)

    validator = AccountValidator()

    with pytest.raises(ValueError):
        validator(account)


def test_negative_initial_balance():

    account = valid_account()

    account.initial_balance = -1

    with pytest.raises(ValueError):
        AccountValidator()(account)


def test_negative_cash():

    account = valid_account()

    account.cash_balance = -1

    with pytest.raises(ValueError):
        AccountValidator()(account)


def test_negative_buying_power():

    account = valid_account()

    account.buying_power = -1

    with pytest.raises(ValueError):
        AccountValidator()(account)


def test_negative_margin():

    account = valid_account()

    account.margin_used = -1

    with pytest.raises(ValueError):
        AccountValidator()(account)


def test_invalid_leverage():

    account = valid_account()

    account.leverage = 0

    with pytest.raises(ValueError):
        AccountValidator()(account)