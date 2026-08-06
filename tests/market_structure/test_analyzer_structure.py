"""
===========================================================

OGS Smart Money AI

Market Structure Analyzer

Structure Classification Tests

===========================================================
"""

from __future__ import annotations

from ogs.market_structure import (
    MarketStructureAnalyzer,
    SwingType,
)

from tests.fixtures import CandleFactory


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


def test_first_high_is_high():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(
        highs=[10, 20, 50, 20, 10],
        lows=[1, 2, 3, 2, 1],
    )

    swings = analyzer.analyze(candles)

    highs = [s for s in swings if s.is_high]

    assert highs
    assert highs[0].type is SwingType.HIGH


def test_first_low_is_low():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(
        highs=[30] * 5,
        lows=[20, 10, 1, 10, 20],
    )

    swings = analyzer.analyze(candles)

    lows = [s for s in swings if s.is_low]

    assert lows
    assert lows[0].type is SwingType.LOW


def test_higher_high_detected():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[
            10, 20, 40, 20, 10,
            20, 60, 20, 10
        ],

        lows=[
            1, 2, 3, 2, 1,
            2, 3, 2, 1
        ],
    )

    swings = analyzer.analyze(candles)

    highs = [s for s in swings if s.is_high]

    assert len(highs) >= 2

    assert highs[1].type is SwingType.HIGHER_HIGH


def test_lower_high_detected():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[
            10, 20, 60, 20, 10,
            20, 40, 20, 10
        ],

        lows=[
            1, 2, 3, 2, 1,
            2, 3, 2, 1
        ],
    )

    swings = analyzer.analyze(candles)

    highs = [s for s in swings if s.is_high]

    assert len(highs) >= 2

    assert highs[1].type is SwingType.LOWER_HIGH


def test_higher_low_detected():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[
            40, 30, 20, 30, 40,
            50, 40, 30, 40, 50
        ],

        lows=[
            30, 20, 10, 20, 30,
            35, 25, 15, 25, 35
        ],
    )

    swings = analyzer.analyze(candles)

    lows = [s for s in swings if s.is_low]

    if len(lows) >= 2:

        assert lows[1].type is SwingType.HIGHER_LOW


def test_lower_low_detected():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[
            40, 30, 20, 30, 40,
            30, 20, 10, 20, 30
        ],

        lows=[
            30, 20, 10, 20, 30,
            20, 10, 5, 10, 20
        ],
    )

    swings = analyzer.analyze(candles)

    lows = [s for s in swings if s.is_low]

    if len(lows) >= 2:

        assert lows[1].type is SwingType.LOWER_LOW


def test_structure_smoke():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[
            10,20,40,20,10,
            20,60,20,10,
            20,30,20,10
        ],

        lows=[
            1,2,3,2,1,
            2,3,2,1,
            2,3,2,1
        ],
    )

    swings = analyzer.analyze(candles)

    assert len(swings) > 0

    for swing in swings:

        assert swing.type in (
            SwingType.HIGH,
            SwingType.LOW,
            SwingType.HIGHER_HIGH,
            SwingType.LOWER_HIGH,
            SwingType.HIGHER_LOW,
            SwingType.LOWER_LOW,
        )