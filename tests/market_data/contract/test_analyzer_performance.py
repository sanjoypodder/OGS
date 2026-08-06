"""
Performance tests.
"""

from ogs.market_data.contract import (
    Contract,
    ContractAnalyzer,
    ContractCollection,
)


def test_large_collection():

    collection = ContractCollection()

    for i in range(1000):

        collection.add(
            Contract(
                contract_id=str(i),
                instrument_id=str(i),
                contract_symbol=f"CONTRACT{i}",
                exchange="TEST",
                underlying="TEST",
            )
        )

    analyzer = ContractAnalyzer()

    result = analyzer.analyze(collection)

    assert result["summary"]["count"] == 1000