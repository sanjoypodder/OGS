"""
Currency analyzer performance tests.
"""

from ogs.market_data.currency import (
    Currency,
    CurrencyAnalyzer,
    CurrencyCollection,
    CurrencyType,
)


def test_large_collection():

    collection = CurrencyCollection()

    for i in range(1000):

        collection.add(
            Currency(
                currency_code=f"C{i}",
                numeric_code=i + 1,
                name=f"Currency {i}",
                currency_type=CurrencyType.FIAT,
                is_fiat=True,
            )
        )

    analyzer = CurrencyAnalyzer()

    result = analyzer.analyze(collection)

    assert result["summary"]["count"] == 1000

    assert (
        result["currency_analysis"]["fiat_currencies"]
        == 1000
    )

    assert (
        result["currency_analysis"]["crypto_currencies"]
        == 0
    )