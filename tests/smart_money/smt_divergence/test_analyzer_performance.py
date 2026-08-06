"""
===========================================================

OGS Smart Money AI

SMT Divergence Analyzer Performance Tests

===========================================================
"""

from __future__ import annotations

from datetime import datetime, timedelta

from ogs.smart_money.smt_divergence import (
    SMTComparisonType,
    SMTDivergenceAnalyzer,
)


class MockSwing:

    def __init__(
        self,
        *,
        symbol="BTCUSD",
        price=100.0,
        comparison=SMTComparisonType.HIGH,
        timestamp=None,
        higher_high=False,
        lower_high=False,
        higher_low=False,
        lower_low=False,
    ):
        self.symbol = symbol
        self.price = price
        self.comparison = comparison
        self.timestamp = timestamp or datetime.now()

        self.is_higher_high = higher_high
        self.is_lower_high = lower_high
        self.is_higher_low = higher_low
        self.is_lower_low = lower_low


def make_dataset(size: int):

    first = []
    second = []

    base = datetime(2025, 1, 1)

    for i in range(size):

        first.append(
            MockSwing(
                symbol="BTCUSD",
                price=100 + i,
                timestamp=base + timedelta(minutes=i),
                higher_high=(i % 2 == 0),
                lower_low=(i % 2 == 1),
            )
        )

        second.append(
            MockSwing(
                symbol="ETHUSD",
                price=90 + i,
                timestamp=base + timedelta(minutes=i),
                lower_high=(i % 2 == 0),
                higher_low=(i % 2 == 1),
            )
        )

    return first, second


def test_100_divergences():

    analyzer = SMTDivergenceAnalyzer()

    first, second = make_dataset(100)

    result = analyzer.analyze(first, second)

    assert len(result) == 100


def test_1000_divergences():

    analyzer = SMTDivergenceAnalyzer()

    first, second = make_dataset(1000)

    result = analyzer.analyze(first, second)

    assert len(result) == 1000


def test_large_dataset_type():

    analyzer = SMTDivergenceAnalyzer()

    first, second = make_dataset(500)

    result = analyzer.analyze(first, second)

    assert result is not None
    assert len(result) == 500


def test_repeated_execution():

    analyzer = SMTDivergenceAnalyzer()

    first, second = make_dataset(200)

    for _ in range(10):
        result = analyzer.analyze(first, second)
        assert len(result) == 200


def test_empty_large_dataset():

    analyzer = SMTDivergenceAnalyzer()

    result = analyzer.analyze([], [])

    assert len(result) == 0