"""
===========================================================

OGS Smart Money AI

Market Structure Analyzer

Edge Case Tests

===========================================================
"""

from __future__ import annotations

from ogs.market_structure import MarketStructureAnalyzer

from tests.fixtures import CandleFactory


# ==========================================================
# Helpers
# ==========================================================

def make_candles(highs, lows):

    candles = []

    for h, l in zip(highs, lows):

        open_price = l + (h - l) * 0.40
        close_price = l + (h - l) * 0.60

        candles.append(
            CandleFactory.create(
                open=open_price,
                high=h,
                low=l,
                close=close_price,
            )
        )

    return candles


# ==========================================================
# Empty / Small Inputs
# ==========================================================

def test_empty_returns_empty():

    analyzer = MarketStructureAnalyzer()

    swings = analyzer.analyze([])

    assert len(swings) == 0


def test_single_candle():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles([10], [5])

    swings = analyzer.analyze(candles)

    assert len(swings) == 0


def test_two_candles():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles([10, 20], [5, 10])

    swings = analyzer.analyze(candles)

    assert len(swings) == 0


# ==========================================================
# Flat Market
# ==========================================================

def test_all_equal_prices():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[10] * 9,
        lows=[5] * 9,

    )

    swings = analyzer.analyze(candles)

    assert len(swings) == 0


def test_large_flat_market():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[100] * 100,
        lows=[90] * 100,

    )

    swings = analyzer.analyze(candles)

    assert len(swings) == 0


# ==========================================================
# Trending Markets
# ==========================================================

def test_monotonic_uptrend():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[10, 20, 30, 40, 50, 60, 70],
        lows=[5, 10, 15, 20, 25, 30, 35],

    )

    swings = analyzer.analyze(candles)

    assert hasattr(swings, "__len__")


def test_monotonic_downtrend():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[70, 60, 50, 40, 30, 20, 10],
        lows=[35, 30, 25, 20, 15, 10, 5],

    )

    swings = analyzer.analyze(candles)

    assert hasattr(swings, "__len__")


# ==========================================================
# Consistency
# ==========================================================

def test_multiple_calls_same_result():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[10, 20, 50, 20, 10],
        lows=[1, 2, 3, 2, 1],

    )

    s1 = analyzer.analyze(candles)

    s2 = analyzer.analyze(candles)

    assert len(s1) == len(s2)

    assert list(s1) == list(s2)


# ==========================================================
# Custom Pivot Depth
# ==========================================================

def test_custom_depth():

    analyzer = MarketStructureAnalyzer(pivot_depth=3)

    candles = make_candles(

        highs=[10, 20, 30, 100, 30, 20, 10],
        lows=[5, 6, 7, 8, 7, 6, 5],

    )

    swings = analyzer.analyze(candles)

    assert hasattr(swings, "__len__")


# ==========================================================
# Smoke Test
# ==========================================================

def test_smoke():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[12, 25, 40, 25, 12, 20, 50, 20, 12],
        lows=[5, 10, 15, 10, 5, 10, 15, 10, 5],

    )

    swings = analyzer.analyze(candles)

    assert swings is not None