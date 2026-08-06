from tests.factories.liquidity_void_factory import (
    make_bullish_liquidity_void,
    make_bearish_liquidity_void,
)


def test_bullish_properties():
    lv = make_bullish_liquidity_void()

    assert lv.is_bullish
    assert not lv.is_bearish
    assert lv.size == 5
    assert lv.candle_count == 3


def test_bearish_properties():
    lv = make_bearish_liquidity_void()

    assert lv.is_bearish
    assert not lv.is_bullish
    assert lv.size == 5