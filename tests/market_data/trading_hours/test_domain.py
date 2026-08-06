"""
Tests for TradingHours domain.
"""

from datetime import time

from ogs.market_data.trading_hours import (
    TradingHours,
    TradingHoursStatus,
    TradingHoursType,
)


def test_default():

    obj = TradingHours()

    assert obj.trading_hours_id == ""
    assert obj.exchange == ""
    assert obj.market == ""
    assert obj.session_name == ""
    assert obj.timezone == "UTC"

    assert obj.open_time == time(0, 0)
    assert obj.close_time == time(0, 0)

    assert obj.trading_days == []

    assert obj.trading_hours_type == TradingHoursType.UNKNOWN
    assert obj.status == TradingHoursStatus.UNKNOWN

    assert obj.active

    assert not obj.is_valid
    assert not obj.is_active


def test_valid():

    obj = TradingHours(
        trading_hours_id="TH001",
        exchange="NSE",
        market="Equity",
        session_name="Regular",
    )

    assert obj.is_valid


def test_active():

    obj = TradingHours(
        trading_hours_id="TH001",
        exchange="NSE",
        market="Equity",
        session_name="Regular",
        status=TradingHoursStatus.ACTIVE,
    )

    assert obj.is_active


def test_duration():

    obj = TradingHours(
        open_time=time(9, 15),
        close_time=time(15, 30),
    )

    assert obj.duration == 375


def test_to_dict():

    obj = TradingHours(
        trading_hours_id="TH001",
        exchange="NSE",
        market="Equity",
        session_name="Regular",
    )

    data = obj.to_dict()

    assert isinstance(data, dict)

    assert data["trading_hours_id"] == "TH001"
    assert data["exchange"] == "NSE"
    assert data["market"] == "Equity"


def test_string():

    obj = TradingHours(
        trading_hours_id="TH001",
        exchange="NSE",
        session_name="Regular",
    )

    assert "TradingHours" in str(obj)