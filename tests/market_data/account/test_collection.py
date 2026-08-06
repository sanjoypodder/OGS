"""
Tests for Account collection.
"""

from ogs.market_data.account import (
    Account,
    AccountCollection,
    AccountStatus,
    AccountType,
)


def make_account(i):

    return Account(
        account_id=f"A{i}",
        name=f"Account {i}",
        account_type=AccountType.LIVE,
        status=AccountStatus.ACTIVE,
    )


def test_collection():

    c = AccountCollection()

    assert len(c) == 0

    c.add(make_account(1))

    assert len(c) == 1


def test_find():

    c = AccountCollection()

    a = make_account(1)

    c.add(a)

    assert c.find("A1") == a
    assert c.find("UNKNOWN") is None


def test_filters():

    c = AccountCollection()

    c.add(
        Account(
            account_id="1",
            name="Live",
            account_type=AccountType.LIVE,
            status=AccountStatus.ACTIVE,
        )
    )

    c.add(
        Account(
            account_id="2",
            name="Paper",
            account_type=AccountType.PAPER,
            status=AccountStatus.INACTIVE,
        )
    )

    assert len(c.live()) == 1
    assert len(c.paper()) == 1
    assert len(c.active()) == 1
    assert len(c.inactive()) == 1


def test_totals():

    c = AccountCollection()

    c.add(
        Account(
            account_id="1",
            name="A",
        )
    )

    assert c.total_equity() == 0.0
    assert c.total_cash() == 0.0
    assert c.total_market_value() == 0.0
    assert c.total_realized_pnl() == 0.0
    assert c.total_unrealized_pnl() == 0.0
    assert c.total_pnl() == 0.0


def test_to_list():

    c = AccountCollection()

    c.add(
        Account(
            account_id="1",
            name="A",
        )
    )

    data = c.to_list()

    assert isinstance(data, list)
    assert len(data) == 1