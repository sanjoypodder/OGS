"""
Tests for Settlement factory.
"""

from ogs.market_data.settlement import (
    Settlement,
    SettlementFactory,
    SettlementStatus,
    SettlementType,
)


def test_create():

    obj = SettlementFactory.create(
        settlement_id="SET001",
        exchange="NSE",
        market="Equity",
        instrument="INFY",
    )

    assert isinstance(obj, Settlement)


def test_cash():

    obj = SettlementFactory.cash(
        settlement_id="SET001",
    )

    assert obj.settlement_type == SettlementType.CASH
    assert obj.status == SettlementStatus.ACTIVE


def test_physical():

    obj = SettlementFactory.physical(
        settlement_id="SET002",
    )

    assert obj.settlement_type == SettlementType.PHYSICAL


def test_net():

    obj = SettlementFactory.net(
        settlement_id="SET003",
    )

    assert obj.settlement_type == SettlementType.NET


def test_gross():

    obj = SettlementFactory.gross(
        settlement_id="SET004",
    )

    assert obj.settlement_type == SettlementType.GROSS


def test_delivery():

    obj = SettlementFactory.delivery(
        settlement_id="SET005",
    )

    assert obj.settlement_type == SettlementType.DELIVERY


def test_custom():

    obj = SettlementFactory.custom(
        settlement_id="SET006",
    )

    assert obj.settlement_type == SettlementType.CUSTOM


def test_clone():

    obj = SettlementFactory.create(
        settlement_id="SET001",
    )

    clone = SettlementFactory.clone(obj)

    assert clone == obj
    assert clone is not obj