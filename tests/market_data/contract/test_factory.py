"""
Tests for Contract factory.
"""

from ogs.market_data.contract import (
    Contract,
    ContractFactory,
    ContractType,
    OptionType,
)


def test_create():

    obj = ContractFactory.create(
        "1",
        "INS1",
        "BTCUSDT",
        "BINANCE",
        "BTC",
    )

    assert isinstance(obj, Contract)


def test_future():

    obj = ContractFactory.future(
        "1",
        "INS1",
        "NIFTY24AUGFUT",
        "NSE",
        "NIFTY",
    )

    assert obj.contract_type == ContractType.FUTURE


def test_call():

    obj = ContractFactory.call_option(
        "1",
        "INS1",
        "NIFTY24AUG25000CE",
        "NSE",
        "NIFTY",
    )

    assert obj.option_type == OptionType.CALL


def test_put():

    obj = ContractFactory.put_option(
        "1",
        "INS1",
        "NIFTY24AUG25000PE",
        "NSE",
        "NIFTY",
    )

    assert obj.option_type == OptionType.PUT


def test_clone():

    obj = ContractFactory.create(
        "1",
        "INS1",
        "BTCUSDT",
        "BINANCE",
        "BTC",
    )

    clone = ContractFactory.clone(obj)

    assert clone == obj
    assert clone is not obj