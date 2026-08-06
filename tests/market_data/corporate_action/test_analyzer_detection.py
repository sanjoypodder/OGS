"""
CorporateAction analyzer distribution tests.
"""

from ogs.market_data.corporate_action import (
    CorporateAction,
    CorporateActionAnalyzer,
    CorporateActionCollection,
    CorporateActionStatus,
    CorporateActionType,
)


def test_distribution_detection():

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

    collection.add(
        CorporateAction(
            action_id="2",
            symbol="TCS",
            exchange="NSE",
            market="Cash",
            action_type=CorporateActionType.BONUS,
            status=CorporateActionStatus.ANNOUNCED,
        )
    )

    analyzer = CorporateActionAnalyzer()

    result = analyzer.analyze(collection)

    distribution = result["distribution_analysis"]

    assert distribution["action_type"]["DIVIDEND"] == 1
    assert distribution["action_type"]["BONUS"] == 1