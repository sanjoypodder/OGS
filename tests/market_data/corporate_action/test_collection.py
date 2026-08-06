"""
Tests for CorporateAction collection.
"""

from ogs.market_data.corporate_action import (
    CorporateAction,
    CorporateActionCollection,
    CorporateActionStatus,
    CorporateActionType,
)


def make(
    action_id,
    action_type,
    status,
):

    return CorporateAction(
        action_id=action_id,
        symbol="RELIANCE",
        exchange="NSE",
        market="Cash",
        action_type=action_type,
        status=status,
    )


def test_add():

    collection = CorporateActionCollection()

    collection.add(
        make(
            "1",
            CorporateActionType.DIVIDEND,
            CorporateActionStatus.ANNOUNCED,
        )
    )

    assert len(collection) == 1


def test_find():

    collection = CorporateActionCollection()

    obj = make(
        "ABC",
        CorporateActionType.DIVIDEND,
        CorporateActionStatus.ANNOUNCED,
    )

    collection.add(obj)

    assert collection.find("ABC") == obj

    assert collection.find("XYZ") is None


def test_filters():

    collection = CorporateActionCollection()

    collection.add(
        make(
            "1",
            CorporateActionType.DIVIDEND,
            CorporateActionStatus.EFFECTIVE,
        )
    )

    collection.add(
        make(
            "2",
            CorporateActionType.BONUS,
            CorporateActionStatus.ANNOUNCED,
        )
    )

    assert len(collection.dividends()) == 1

    assert len(collection.effective()) == 1


def test_to_list():

    collection = CorporateActionCollection()

    collection.add(
        make(
            "1",
            CorporateActionType.DIVIDEND,
            CorporateActionStatus.EFFECTIVE,
        )
    )

    assert len(collection.to_list()) == 1