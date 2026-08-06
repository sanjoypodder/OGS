"""
Edge case tests.
"""

from ogs.market_data.contract import (
    ContractAnalyzer,
    ContractCollection,
)


def test_empty_collection():

    collection = ContractCollection()

    analyzer = ContractAnalyzer()

    result = analyzer.analyze(collection)

    assert result["summary"]["count"] == 0
    assert result["summary"]["active"] == 0
    assert result["summary"]["expired"] == 0