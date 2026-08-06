"""
Tests for CorporateAction analyzer.
"""

from ogs.market_data.corporate_action import (
    CorporateAction,
    CorporateActionAnalyzer,
    CorporateActionCollection,
    CorporateActionStatus,
    CorporateActionType,
)


def test_analyze():

    collection = CorporateActionCollection()

    collection.add(
        CorporateAction(
            action_id="1",
            symbol="RELIANCE",
            exchange="NSE",
            market="Cash",
            action_type=CorporateActionType.DIVIDEND,
            status=CorporateActionStatus.EFFECTIVE,
        )
    )

    analyzer = CorporateActionAnalyzer()

    result = analyzer.analyze(collection)

    assert isinstance(result, dict)

    assert "summary" in result
    assert "corporate_action_analysis" in result
    assert "distribution_analysis" in result