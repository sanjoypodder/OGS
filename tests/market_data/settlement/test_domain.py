"""
Tests for Settlement domain.
"""

from datetime import time

from ogs.market_data.settlement import (
    Settlement,
    SettlementStatus,
    SettlementType,
    SettlementCycle,
    SettlementMethod,
)


def test_default():

    obj = Settlement()

    assert obj.settlement_id == ""
    assert obj.exchange == ""
    assert obj.market == ""
    assert obj.instrument == ""
    assert obj.settlement_currency == ""
    assert obj.settlement_location == ""

    assert obj.cutoff_time == time(0, 0)

    assert obj.settlement_type == SettlementType.UNKNOWN
    assert obj.status == SettlementStatus.UNKNOWN
    assert obj.settlement_cycle == SettlementCycle.UNKNOWN
    assert obj.settlement_method == SettlementMethod.UNKNOWN

    assert obj.active

    assert not obj.is_valid
    assert not obj.is_active


def test_valid():

    obj = Settlement(
        settlement_id="SET001",
        exchange="NSE",
        market="Equity",
        instrument="INFY",
    )

    assert obj.is_valid


def test_active():

    obj = Settlement(
        settlement_id="SET001",
        exchange="NSE",
        market="Equity",
        instrument="INFY",
        status=SettlementStatus.ACTIVE,
    )

    assert obj.is_active


def test_to_dict():

    obj = Settlement(
        settlement_id="SET001",
        exchange="NSE",
        market="Equity",
        instrument="INFY",
    )

    data = obj.to_dict()

    assert isinstance(data, dict)

    assert data["settlement_id"] == "SET001"
    assert data["exchange"] == "NSE"
    assert data["market"] == "Equity"
    assert data["instrument"] == "INFY"


def test_string():

    obj = Settlement(
        settlement_id="SET001",
        instrument="INFY",
    )

    assert "Settlement" in str(obj)