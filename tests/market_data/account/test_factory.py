"""
Tests for Account factory.
"""

from ogs.market_data.account import (
    Account,
    AccountFactory,
    AccountStatus,
    AccountType,
)


def test_create():

    account = AccountFactory.create(
        account_id="ACC001",
        name="Primary",
    )

    assert isinstance(account, Account)
    assert account.account_id == "ACC001"
    assert account.name == "Primary"


def test_live():

    account = AccountFactory.live(
        account_id="LIVE001",
        name="Live",
    )

    assert account.account_type == AccountType.LIVE
    assert account.status == AccountStatus.ACTIVE


def test_paper():

    account = AccountFactory.paper(
        account_id="PAPER001",
        name="Paper",
    )

    assert account.account_type == AccountType.PAPER
    assert account.status == AccountStatus.ACTIVE


def test_backtest():

    account = AccountFactory.backtest(
        account_id="BT001",
        name="Backtest",
    )

    assert account.account_type == AccountType.BACKTEST
    assert account.status == AccountStatus.ACTIVE


def test_clone():

    account = AccountFactory.create(
        account_id="ACC001",
        name="Primary",
    )

    clone = AccountFactory.clone(account)

    assert clone == account
    assert clone is not account