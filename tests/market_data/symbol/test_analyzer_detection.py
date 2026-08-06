"""
Tests for SymbolAnalyzer helper methods.
"""

from ogs.market_data.symbol import (
    Currency,
    SymbolAnalyzer,
    SymbolCollection,
    SymbolFactory,
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


def test_forex_detection():

    analyzer = SymbolAnalyzer()

    assert len(
        analyzer.forex(create_collection())
    ) == 1


def test_crypto_detection():

    analyzer = SymbolAnalyzer()

    assert len(
        analyzer.crypto(create_collection())
    ) == 1


def test_stock_detection():

    analyzer = SymbolAnalyzer()

    assert len(
        analyzer.stocks(create_collection())
    ) == 1


def test_find_symbol():

    analyzer = SymbolAnalyzer()

    symbol = analyzer.find(
        create_collection(),
        "EURUSD",
    )

    assert symbol is not None
    assert symbol.symbol == "EURUSD"


def test_find_lowercase():

    analyzer = SymbolAnalyzer()

    symbol = analyzer.find(
        create_collection(),
        "eurusd",
    )

    assert symbol.symbol == "EURUSD"


def test_find_missing():

    analyzer = SymbolAnalyzer()

    assert (
        analyzer.find(
            create_collection(),
            "INVALID",
        )
        is None
    )


def test_symbols():

    analyzer = SymbolAnalyzer()

    symbols = analyzer.symbols(
        create_collection()
    )

    assert symbols == [
        "BTCUSDT",
        "EURUSD",
        "TCS",
    ]


def test_exchanges():

    analyzer = SymbolAnalyzer()

    exchanges = analyzer.exchanges(
        create_collection()
    )

    assert "FOREX" in exchanges
    assert "BINANCE" in exchanges
    assert "NSE" in exchanges