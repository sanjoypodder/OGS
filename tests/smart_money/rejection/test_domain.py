from tests.factories.rejection_factory import (
    make_bearish_rejection,
    make_bullish_rejection,
)


def test_bullish_properties():
    rejection = make_bullish_rejection()

    assert rejection.is_bullish
    assert not rejection.is_bearish
    assert rejection.size == 8
    assert rejection.is_confirmed


def test_bearish_properties():
    rejection = make_bearish_rejection()

    assert rejection.is_bearish
    assert not rejection.is_bullish
    assert rejection.size == 9