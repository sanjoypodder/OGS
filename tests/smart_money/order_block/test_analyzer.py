"""
===========================================================

OGS Smart Money AI

Order Block Analyzer Tests

===========================================================
"""

from ogs.engine import Analysis
from ogs.market import CandleSeries

from ogs.smart_money.order_block import (
    OrderBlockAnalyzer,
)


def test_create():

    analyzer = OrderBlockAnalyzer()

    assert analyzer is not None


def test_empty():

    analyzer = OrderBlockAnalyzer()

    candles = CandleSeries([])

    analysis = Analysis()

    result = analyzer.analyze(
        candles,
        analysis,
    )

    assert len(result) == 0