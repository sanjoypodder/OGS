"""
Analyzer detection tests.
"""

from ogs.market_data.contract import (
    Contract,
    ContractAnalyzer,
    ContractCollection,
    ContractType,
)


def test_distribution():

    collection = ContractCollection()

    collection.add(
        Contract(
            contract_id="1",
            instrument_id="1",
            contract_symbol="BTCUSDT-PERP",
            exchange="BINANCE",
            underlying="BTC",
            contract_type=ContractType.PERPETUAL,
        )
    )

    analyzer = ContractAnalyzer()

    result = analyzer.analyze(collection)

    distribution = result["distribution_analysis"]

    assert distribution["contract_type"]["PERPETUAL"] == 1