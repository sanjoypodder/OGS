"""
===========================================================

OGS Smart Money AI

Swing Domain Tests

===========================================================
"""

from datetime import UTC, datetime

from ogs.market import Candle, Price, Symbol, Timeframe
from ogs.smart_money.swing import Swing, SwingType


def create_candle() -> Candle:
    return Candle(
        symbol=Symbol.XAUUSD,
        timeframe=Timeframe.M5,
        timestamp=datetime(
            2026,
            1,
            1,
            12,
            0,
            tzinfo=UTC,
        ),
        open=Price(Symbol.XAUUSD, 100),
        high=Price(Symbol.XAUUSD, 110),
        low=Price(Symbol.XAUUSD, 90),
        close=Price(Symbol.XAUUSD, 105),
    )


def test_create_swing():

    swing = Swing(
        index=10,
        candle=create_candle(),
        swing_type=SwingType.HIGH,
    )

    assert swing.index == 10
    assert swing.swing_type == SwingType.HIGH


def test_timestamp():

    swing = Swing(
        index=1,
        candle=create_candle(),
        swing_type=SwingType.HIGH,
    )

    assert swing.timestamp.year == 2026


def test_high_price():

    swing = Swing(
        index=1,
        candle=create_candle(),
        swing_type=SwingType.HIGH,
    )

    assert swing.price.value == 110


def test_low_price():

    swing = Swing(
        index=1,
        candle=create_candle(),
        swing_type=SwingType.LOW,
    )

    assert swing.price.value == 90


def test_string():

    swing = Swing(
        index=1,
        candle=create_candle(),
        swing_type=SwingType.HIGH,
    )

    assert "HIGH" in str(swing)


def test_is_frozen():

    swing = Swing(
        index=1,
        candle=create_candle(),
        swing_type=SwingType.HIGH,
    )

    try:
        swing.index = 100
        modified = True
    except Exception:
        modified = False

    assert modified is False