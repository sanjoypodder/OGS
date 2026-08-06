"""
Tests for Currency factory.
"""

from ogs.market_data.currency import (
    Currency,
    CurrencyFactory,
    CurrencyStatus,
    CurrencyType,
)


def test_create():

    obj = CurrencyFactory.create(
        "USD",
        840,
        "US Dollar",
    )

    assert isinstance(obj, Currency)


def test_fiat():

    obj = CurrencyFactory.fiat(
        "USD",
        840,
        "US Dollar",
    )

    assert obj.currency_type == CurrencyType.FIAT
    assert obj.status == CurrencyStatus.ACTIVE
    assert obj.is_fiat


def test_crypto():

    obj = CurrencyFactory.crypto(
        "BTC",
        1000,
        "Bitcoin",
    )

    assert obj.currency_type == CurrencyType.CRYPTO
    assert obj.status == CurrencyStatus.ACTIVE
    assert obj.is_crypto


def test_clone():

    obj = CurrencyFactory.create(
        "USD",
        840,
        "US Dollar",
    )

    clone = CurrencyFactory.clone(obj)

    assert clone == obj
    assert clone is not obj