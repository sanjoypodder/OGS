"""
Tests for Contract analyzer.
"""

from ogs.market_data.contract import (
    Contract,
    ContractAnalyzer,
    ContractCollection,
)


def test_analyze():

    collection = ContractCollection()

    collection.add(
        Contract(
            contract_id="1",
            instrument_id="1",
            contract_symbol="BTCUSDT",
            exchange="BINANCE",
            underlying="BTC",
        )
    )

    analyzer = ContractAnalyzer()

    result = analyzer.analyze(collection)

    assert isinstance(result, dict)

    assert "summary" in result
    assert "contract_analysis" in result
    assert "distribution_analysis" in result

    assert result["summary"]["count"] == 1