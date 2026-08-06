"""
Tests for Trade domain.
"""

from datetime import UTC
from datetime import datetime

from ogs.market_data.trade import (
    Trade,
    TradeSide,
    TradeStatus,
)


def test_default_trade():

    trade = Trade()

    assert trade.trade_id == ""
    assert trade.price == 0.0
    assert trade.quantity == 0.0
    assert trade.fees == 0.0


def test_trade_value():

    trade = Trade(
        price=100,
        quantity=5,
    )

    assert trade.value == 500


def test_total_cost():

    trade = Trade(
        price=100,
        quantity=5,
        fees=25,
    )

    assert trade.total_cost == 525


def test_is_buy():

    trade = Trade(
        side=TradeSide.BUY,
    )

    assert trade.is_buy


def test_is_sell():

    trade = Trade(
        side=TradeSide.SELL,
    )

    assert trade.is_sell


def test_is_filled():

    trade = Trade(
        status=TradeStatus.FILLED,
    )

    assert trade.is_filled


def test_valid_trade():

    trade = Trade(
        price=100,
        quantity=10,
        fees=1,
    )

    assert trade.is_valid


def test_invalid_trade():

    trade = Trade(
        price=-100,
    )

    assert not trade.is_valid


def test_to_dict():

    trade = Trade(
        trade_id="TRD001",
    )

    data = trade.to_dict()

    assert data["trade_id"] == "TRD001"


def test_timestamp():

    trade = Trade()

    assert isinstance(
        trade.timestamp,
        datetime,
    )


def test_custom_timestamp():

    ts = datetime.now(UTC)

    trade = Trade(timestamp=ts)

    assert trade.timestamp == ts


def test_string():

    trade = Trade(
        trade_id="TRD001",
    )

    assert "TRD001" in str(trade)