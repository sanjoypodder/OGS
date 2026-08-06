"""
Tests for TradingHours factory.
"""

from ogs.market_data.trading_hours import (
    TradingHours,
    TradingHoursFactory,
    TradingHoursStatus,
    TradingHoursType,
)


def test_create():

    obj = TradingHoursFactory.create(
        trading_hours_id="TH001",
        exchange="NSE",
        market="Equity",
        session_name="Regular",
    )

    assert isinstance(obj, TradingHours)


def test_regular():

    obj = TradingHoursFactory.regular(
        trading_hours_id="TH001",
    )

    assert obj.trading_hours_type == TradingHoursType.REGULAR
    assert obj.status == TradingHoursStatus.ACTIVE


def test_pre_market():

    obj = TradingHoursFactory.pre_market(
        trading_hours_id="TH002",
    )

    assert obj.trading_hours_type == TradingHoursType.PRE_MARKET


def test_post_market():

    obj = TradingHoursFactory.post_market(
        trading_hours_id="TH003",
    )

    assert obj.trading_hours_type == TradingHoursType.POST_MARKET


def test_overnight():

    obj = TradingHoursFactory.overnight(
        trading_hours_id="TH004",
    )

    assert obj.trading_hours_type == TradingHoursType.OVERNIGHT


def test_extended():

    obj = TradingHoursFactory.extended(
        trading_hours_id="TH005",
    )

    assert obj.trading_hours_type == TradingHoursType.EXTENDED


def test_custom():

    obj = TradingHoursFactory.custom(
        trading_hours_id="TH006",
    )

    assert obj.trading_hours_type == TradingHoursType.CUSTOM


def test_clone():

    obj = TradingHoursFactory.create(
        trading_hours_id="TH001",
    )

    clone = TradingHoursFactory.clone(obj)

    assert clone == obj
    assert clone is not obj