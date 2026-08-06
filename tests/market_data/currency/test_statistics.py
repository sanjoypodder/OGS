"""
Tests for Currency statistics.
"""

from ogs.market_data.currency import (
    Currency,
    CurrencyCollection,
    CurrencyStatistics,
)


def make(code, numeric, name, fiat=False, crypto=False):

    return Currency(
        currency_code=code,
        numeric_code=numeric,
        name=name,
        is_fiat=fiat,
        is_crypto=crypto,
    )


def build_collection():

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

    collection.add(
        make(
            "EUR",
            978,
            "Euro",
            fiat=True,
        )
    )

    return collection


def test_counts():

    stats = CurrencyStatistics(build_collection())

    assert stats.count == 3
    assert stats.fiat_count == 2
    assert stats.crypto_count == 1


def test_distribution():

    stats = CurrencyStatistics(build_collection())

    distribution = stats.distribution()

    assert isinstance(distribution, dict)


def test_summary():

    stats = CurrencyStatistics(build_collection())

    summary = stats.summary()

    assert summary["count"] == 3
    assert summary["fiat"] == 2
    assert summary["crypto"] == 1