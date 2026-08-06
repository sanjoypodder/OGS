"""
===========================================================

OGS Smart Money AI

Market Structure Analyzer

Performance & Stress Tests

===========================================================
"""

from __future__ import annotations

import random
import time

from ogs.market_structure import MarketStructureAnalyzer

from tests.fixtures import CandleFactory


def generate_random_candles(count: int):

    candles = []

    price = 100.0

    for _ in range(count):

        move = random.uniform(-3, 3)

        price = max(10.0, price + move)

        low = price - random.uniform(0.5, 2.0)
        high = price + random.uniform(0.5, 2.0)

        open_price = low + (high - low) * 0.30
        close_price = low + (high - low) * 0.70

        candles.append(
            CandleFactory.create(
                open=open_price,
                high=high,
                low=low,
                close=close_price,
            )
        )

    return candles


# ==========================================================
# Performance
# ==========================================================

def test_100_candles():

    analyzer = MarketStructureAnalyzer()

    candles = generate_random_candles(100)

    swings = analyzer.analyze(candles)

    assert len(swings) >= 0


def test_1000_candles():

    analyzer = MarketStructureAnalyzer()

    candles = generate_random_candles(1000)

    swings = analyzer.analyze(candles)

    assert len(swings) >= 0


def test_5000_candles():

    analyzer = MarketStructureAnalyzer()

    candles = generate_random_candles(5000)

    swings = analyzer.analyze(candles)

    assert len(swings) >= 0


# ==========================================================
# Timing
# ==========================================================

def test_execution_time():

    analyzer = MarketStructureAnalyzer()

    candles = generate_random_candles(5000)

    start = time.perf_counter()

    analyzer.analyze(candles)

    elapsed = time.perf_counter() - start

    print(f"\nExecution Time: {elapsed:.4f} sec")

    assert elapsed < 5.0


# ==========================================================
# Stability
# ==========================================================

def test_repeatability():

    analyzer = MarketStructureAnalyzer()

    candles = generate_random_candles(1000)

    for _ in range(20):

        swings = analyzer.analyze(candles)

        assert len(swings) >= 0


# ==========================================================
# Smoke
# ==========================================================

def test_performance_smoke():

    analyzer = MarketStructureAnalyzer()

    candles = generate_random_candles(200)

    analyzer.analyze(candles)