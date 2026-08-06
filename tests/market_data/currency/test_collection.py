"""
Tests for Currency collection.
"""

from ogs.market_data.currency import (
    Currency,
    CurrencyCollection,
)


def make(
    code,
    numeric,
    name,
    fiat=False,
    crypto=False,
):

    return Currency(
        currency_code=code,
        numeric_code=numeric,
        name=name,
        is_fiat=fiat,
        is_crypto=crypto,
    )


def test_add():

    collection = CurrencyCollection()

    collection.add(
        make(
            "USD",
            840,
            "US Dollar",
            fiat=True,
        )
    )

    assert len(collection) == 1


def test_find():

    collection = CurrencyCollection()

    obj = make(
        "USD",
        840,
        "US Dollar",
        fiat=True,
    )

    collection.add(obj)

    assert collection.find("USD") == obj
    assert collection.find("BTC") is None


def test_filters():

    collection = CurrencyCollection()

    collection.add(
        make(
            "USD",
            840,
            "US Dollar",
            fiat=True,
        )
    )

    collection.add(
        make(
            "BTC",
            1000,
            "Bitcoin",
            crypto=True,
        )
    )

    assert len(collection.fiat()) == 1
    assert len(collection.crypto()) == 1


def test_to_list():

    collection = CurrencyCollection()

    collection.add(
        make(
            "USD",
            840,
            "US Dollar",
            fiat=True,
        )
    )

    assert len(collection.to_list()) == 1