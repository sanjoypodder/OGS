"""
Edge case tests for SymbolAnalyzer.
"""

from ogs.market_data.symbol import (
    Currency,
    SymbolAnalyzer,
    SymbolCollection,
    SymbolFactory,
)


def test_empty_collection():

    analyzer = SymbolAnalyzer()

    collection = SymbolCollection()

    result = analyzer.analyze(collection)

    assert result["count"] == 0
    assert result["active"] == 0
    assert result["inactive"] == 0
    assert result["forex"] == 0
    assert result["crypto"] == 0
    assert result["stocks"] == 0
    assert result["indices"] == 0
    assert result["commodities"] == 0


def test_empty_find():

    analyzer = SymbolAnalyzer()

    collection = SymbolCollection()

    assert analyzer.find(collection, "EURUSD") is None


def test_empty_symbols():

    analyzer = SymbolAnalyzer()

    collection = SymbolCollection()

    assert analyzer.symbols(collection) == []


def test_empty_exchanges():

    analyzer = SymbolAnalyzer()

    collection = SymbolCollection()

    assert analyzer.exchanges(collection) == []


def test_single_symbol():

    analyzer = SymbolAnalyzer()

    collection = SymbolCollection()

    collection.append(
        SymbolFactory.forex(
            "EURUSD",
            Currency.EUR,
            Currency.USD,
        )
    )

    result = analyzer.analyze(collection)

    assert result["count"] == 1
    assert result["forex"] == 1
    assert result["crypto"] == 0


def test_duplicate_symbols():

    analyzer = SymbolAnalyzer()

    collection = SymbolCollection()

    collection.append(
        SymbolFactory.forex(
            "EURUSD",
            Currency.EUR,
            Currency.USD,
        )
    )

    collection.append(
        SymbolFactory.forex(
            "EURUSD",
            Currency.EUR,
            Currency.USD,
        )
    )

    result = analyzer.analyze(collection)

    assert result["count"] == 2
    assert len(analyzer.forex(collection)) == 2