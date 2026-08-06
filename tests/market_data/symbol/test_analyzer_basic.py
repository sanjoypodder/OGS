"""
Tests for SymbolAnalyzer basic functionality.
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


def test_analyze_returns_dictionary():

    analyzer = SymbolAnalyzer()

    result = analyzer.analyze(create_collection())

    assert isinstance(result, dict)


def test_total_count():

    analyzer = SymbolAnalyzer()

    result = analyzer.analyze(create_collection())

    assert result["count"] == 3


def test_active_count():

    analyzer = SymbolAnalyzer()

    result = analyzer.analyze(create_collection())

    assert result["active"] == 3


def test_inactive_count():

    analyzer = SymbolAnalyzer()

    result = analyzer.analyze(create_collection())

    assert result["inactive"] == 0


def test_forex_count():

    analyzer = SymbolAnalyzer()

    result = analyzer.analyze(create_collection())

    assert result["forex"] == 1


def test_crypto_count():

    analyzer = SymbolAnalyzer()

    result = analyzer.analyze(create_collection())

    assert result["crypto"] == 1


def test_stock_count():

    analyzer = SymbolAnalyzer()

    result = analyzer.analyze(create_collection())

    assert result["stocks"] == 1


def test_indices_count():

    analyzer = SymbolAnalyzer()

    result = analyzer.analyze(create_collection())

    assert result["indices"] == 0


def test_commodities_count():

    analyzer = SymbolAnalyzer()

    result = analyzer.analyze(create_collection())

    assert result["commodities"] == 0