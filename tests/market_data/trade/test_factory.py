"""
Tests for TradeFactory.
"""

import pytest

from ogs.market_data.trade import (
    Trade,
    TradeFactory,
    TradeSide,
    TradeStatus,
)


def test_create():

    trade = TradeFactory.create(
        trade_id="TRD001",
        price=100,
        quantity=10,
    )

    assert isinstance(trade, Trade)


def test_buy_factory():

    trade = TradeFactory.buy(
        trade_id="BUY001",
        price=100,
        quantity=10,
    )

    assert trade.side == TradeSide.BUY
    assert trade.status == TradeStatus.FILLED


def test_sell_factory():

    trade = TradeFactory.sell(
        trade_id="SELL001",
        price=100,
        quantity=10,
    )

    assert trade.side == TradeSide.SELL
    assert trade.status == TradeStatus.FILLED


def test_clone():

    trade = TradeFactory.create(
        trade_id="TRD001",
        price=100,
        quantity=10,
    )

    clone = TradeFactory.clone(trade)

    assert clone == trade
    assert clone is not trade


def test_clone_independent():

    trade = TradeFactory.create(
        trade_id="TRD001",
        price=100,
        quantity=10,
    )

    clone = TradeFactory.clone(trade)

    clone.price = 500

    assert trade.price == 100


def test_factory_validation():

    with pytest.raises(ValueError):

        TradeFactory.create(
            trade_id="",
            price=100,
            quantity=10,
        )


def test_factory_negative_price():

    with pytest.raises(ValueError):

        TradeFactory.create(
            trade_id="TRD001",
            price=-100,
            quantity=10,
        )