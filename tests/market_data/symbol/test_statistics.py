"""
Tests for SymbolStatistics.
"""

from ogs.market_data.symbol import (
    Currency,
    SymbolCollection,
    SymbolFactory,
    SymbolStatistics,
)


def create_collection():

    collection = SymbolCollection()

    collection.append(
        SymbolFactory.forex(
            "EURUSD",
            Currency.EUR,
            Currency.USD,
        )
    )

    collection.append(
        SymbolFactory.crypto(
            "BTCUSDT",
            Currency.BTC,
        )
    )

    collection.append(
        SymbolFactory.stock(
            "TCS",
            "Tata Consultancy Services",
        )
    )

    return collection


def test_count():

    stats = SymbolStatistics(
        create_collection()
    )

    assert stats.count == 3


def test_active_count():

    stats = SymbolStatistics(
        create_collection()
    )

    assert stats.active_count == 3


def test_inactive_count():

    stats = SymbolStatistics(
        create_collection()
    )

    assert stats.inactive_count == 0


def test_forex_count():

    stats = SymbolStatistics(
        create_collection()
    )

    assert stats.forex_count == 1


def test_crypto_count():

    stats = SymbolStatistics(
        create_collection()
    )

    assert stats.crypto_count == 1


def test_stock_count():

    stats = SymbolStatistics(
        create_collection()
    )

    assert stats.stock_count == 1


def test_symbols():

    stats = SymbolStatistics(
        create_collection()
    )

    assert stats.symbols == [
        "BTCUSDT",
        "EURUSD",
        "TCS",
    ]


def test_exchanges():

    stats = SymbolStatistics(
        create_collection()
    )

    assert "FOREX" in stats.exchanges
    assert "BINANCE" in stats.exchanges
    assert "NSE" in stats.exchanges