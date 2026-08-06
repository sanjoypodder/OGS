"""
Currency analyzer detection tests.
"""

from ogs.market_data.currency import (
    Currency,
    CurrencyAnalyzer,
    CurrencyCollection,
    CurrencyType,
)


def test_distribution_detection():

    collection = CurrencyCollection()

    collection.add(
        Currency(
            currency_code="USD",
            numeric_code=840,
            name="US Dollar",
            currency_type=CurrencyType.FIAT,
            is_fiat=True,
        )
    )

    collection.add(
        Currency(
            currency_code="BTC",
            numeric_code=1000,
            name="Bitcoin",
            currency_type=CurrencyType.CRYPTO,
            is_crypto=True,
        )
    )

    analyzer = CurrencyAnalyzer()

    result = analyzer.analyze(collection)

    distribution = result["distribution_analysis"]

    assert distribution["currency_type"]["FIAT"] == 1
    assert distribution["currency_type"]["CRYPTO"] == 1