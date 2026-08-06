from ogs.smart_money.liquidity_void import LiquidityVoidDirection


def test_bullish_enum():
    assert LiquidityVoidDirection.BULLISH.value == "Bullish"


def test_bearish_enum():
    assert LiquidityVoidDirection.BEARISH.value == "Bearish"