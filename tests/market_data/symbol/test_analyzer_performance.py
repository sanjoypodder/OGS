"""
Performance tests for SymbolAnalyzer.
"""

from ogs.market_data.symbol import (
    Currency,
    SymbolAnalyzer,
    SymbolCollection,
    SymbolFactory,
)


def build_collection(size=1000):

    collection = SymbolCollection()

    for i in range(size):

        collection.append(

            SymbolFactory.forex(
                f"EURUSD{i}",
                Currency.EUR,
                Currency.USD,
            )

        )

    return collection


def test_large_collection():

    analyzer = SymbolAnalyzer()

    collection = build_collection(1000)

    result = analyzer.analyze(collection)

    assert result["count"] == 1000
    assert result["forex"] == 1000


def test_large_find():

    analyzer = SymbolAnalyzer()

    collection = build_collection(1000)

    symbol = analyzer.find(collection, "EURUSD999")

    assert symbol is not None
    assert symbol.symbol == "EURUSD999"


def test_large_symbols():

    analyzer = SymbolAnalyzer()

    collection = build_collection(1000)

    symbols = analyzer.symbols(collection)

    assert len(symbols) == 1000


def test_large_exchanges():

    analyzer = SymbolAnalyzer()

    collection = build_collection(1000)

    exchanges = analyzer.exchanges(collection)

    assert exchanges == ["FOREX"]


def test_multiple_analysis():

    analyzer = SymbolAnalyzer()

    collection = build_collection(500)

    for _ in range(20):

        result = analyzer.analyze(collection)

        assert result["count"] == 500