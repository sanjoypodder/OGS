"""
Tests for CorporateAction statistics.
"""

from ogs.market_data.corporate_action import (
    CorporateAction,
    CorporateActionCollection,
    CorporateActionStatistics,
    CorporateActionStatus,
    CorporateActionType,
)


def make(idx, action_type, status):

    return CorporateAction(
        action_id=str(idx),
        symbol=f"SYM{idx}",
        exchange="NSE",
        market="Cash",
        action_type=action_type,
        status=status,
    )


def build_collection():

    collection = CorporateActionCollection()

    collection.add(
        make(
            1,
            CorporateActionType.DIVIDEND,
            CorporateActionStatus.EFFECTIVE,
        )
    )

    collection.add(
        make(
            2,
            CorporateActionType.BONUS,
            CorporateActionStatus.ANNOUNCED,
        )
    )

    collection.add(
        make(
            3,
            CorporateActionType.DIVIDEND,
            CorporateActionStatus.EFFECTIVE,
        )
    )

    return collection


def test_counts():

    stats = CorporateActionStatistics(build_collection())

    assert stats.count == 3
    assert stats.dividend_count == 2
    assert stats.effective_count == 2


def test_distribution():

    stats = CorporateActionStatistics(build_collection())

    distribution = stats.distribution()

    assert distribution["DIVIDEND"] == 2
    assert distribution["BONUS"] == 1


def test_summary():

    stats = CorporateActionStatistics(build_collection())

    summary = stats.summary()

    assert summary["count"] == 3
    assert summary["dividends"] == 2
    assert summary["effective"] == 2