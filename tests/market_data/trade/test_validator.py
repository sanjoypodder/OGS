"""
Tests for TradeValidator.
"""

from datetime import UTC
from datetime import datetime

import pytest

from ogs.market_data.trade import (
    Trade,
    TradeSide,
    TradeStatus,
    TradeValidator,
)


validator = TradeValidator()


def test_validator_accepts_valid_trade():

    trade = Trade(
        trade_id="TRD001",
        price=100,
        quantity=10,
    )

    assert validator(trade)


def test_validator_rejects_non_trade():

    with pytest.raises(TypeError):
        validator("invalid")


def test_validator_rejects_empty_trade_id():

    with pytest.raises(ValueError):
        validator(Trade())


def test_negative_price():

    with pytest.raises(ValueError):
        validator(
            Trade(
                trade_id="TRD001",
                price=-1,
            )
        )


def test_negative_quantity():

    with pytest.raises(ValueError):
        validator(
            Trade(
                trade_id="TRD001",
                quantity=-1,
            )
        )


def test_negative_fees():

    with pytest.raises(ValueError):
        validator(
            Trade(
                trade_id="TRD001",
                fees=-1,
            )
        )


def test_invalid_side():

    trade = Trade(
        trade_id="TRD001",
    )

    trade.side = "BUY"

    with pytest.raises(ValueError):
        validator(trade)


def test_invalid_status():

    trade = Trade(
        trade_id="TRD001",
    )

    trade.status = "FILLED"

    with pytest.raises(ValueError):
        validator(trade)


def test_invalid_timestamp():

    trade = Trade(
        trade_id="TRD001",
    )

    trade.timestamp = "today"

    with pytest.raises(ValueError):
        validator(trade)


def test_callable_validator():

    trade = Trade(
        trade_id="TRD001",
        price=10,
        quantity=5,
    )

    assert validator(trade)


def test_valid_enums():

    assert isinstance(
        TradeSide.BUY,
        TradeSide,
    )

    assert isinstance(
        TradeStatus.FILLED,
        TradeStatus,
    )


def test_valid_datetime():

    assert isinstance(
        datetime.now(UTC),
        datetime,
    )