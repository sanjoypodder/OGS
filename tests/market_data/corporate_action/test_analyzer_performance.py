"""
CorporateAction analyzer performance tests.
"""

from ogs.market_data.corporate_action import (
    CorporateAction,
    CorporateActionAnalyzer,
    CorporateActionCollection,
    CorporateActionStatus,
    CorporateActionType,
)


def test_large_collection():

    collection = CorporateActionCollection()

    for i in range(1000):

        collection.add(
            CorporateAction(
                action_id=str(i),
                symbol=f"SYM{i}",
                exchange="NSE",
                market="Cash",
                action_type=CorporateActionType.DIVIDEND,
                status=CorporateActionStatus.EFFECTIVE,
            )
        )

    analyzer = CorporateActionAnalyzer()

    result = analyzer.analyze(collection)

    assert result["summary"]["count"] == 1000

    assert (
        result["corporate_action_analysis"]["dividends"]
        == 1000
    )

    assert (
        result["corporate_action_analysis"]["effective_actions"]
        == 1000
    )