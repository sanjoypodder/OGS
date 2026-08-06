"""
Tests for CorporateAction factory.
"""

from ogs.market_data.corporate_action import (
    CorporateAction,
    CorporateActionFactory,
    CorporateActionStatus,
    CorporateActionType,
)


def test_create():

    obj = CorporateActionFactory.create(
        "CA001",
        "RELIANCE",
        "NSE",
        "Cash",
    )

    assert isinstance(obj, CorporateAction)


def test_dividend():

    obj = CorporateActionFactory.dividend(
        "CA001",
        "RELIANCE",
        "NSE",
        "Cash",
        25.50,
    )

    assert obj.action_type == CorporateActionType.DIVIDEND

    assert obj.status == CorporateActionStatus.ANNOUNCED

    assert obj.cash_amount == 25.50


def test_clone():

    obj = CorporateActionFactory.create(
        "CA001",
        "RELIANCE",
        "NSE",
        "Cash",
    )

    clone = CorporateActionFactory.clone(obj)

    assert clone == obj

    assert clone is not obj