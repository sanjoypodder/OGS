"""
Performance tests for CandleAnalyzer.
"""

from datetime import datetime

from ogs.market_data.candle import (
    Candle,
    CandleAnalyzer,
    CandleSeries,
)


def test_large_dataset():

    analyzer = CandleAnalyzer()

    series = CandleSeries()

    for i in range(10000):

        series.append(
            Candle(
                symbol="BTCUSD",
                timeframe="M1",
                timestamp=datetime.now(),
                open=100.0,
                high=110.0,
                low=90.0,
                close=105.0,
                volume=100.0,
            )
        )

    assert len(analyzer.bullish(series)) == 10000
    assert analyzer.average_close(series) == 105.0


def test_analysis_large_dataset():

    analyzer = CandleAnalyzer()

    series = CandleSeries()

    for _ in range(5000):

        series.append(
            Candle(
                symbol="EURUSD",
                timeframe="H1",
                timestamp=datetime.now(),
                open=100,
                high=120,
                low=90,
                close=110,
            )
        )

    result = analyzer.analyze(series)

    assert result["count"] == 5000
    assert result["bullish"] == 5000
    assert result["bearish"] == 0
    assert result["doji"] == 0