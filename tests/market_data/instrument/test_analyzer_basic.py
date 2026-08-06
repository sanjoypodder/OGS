"""
Tests for Instrument analyzer.
"""

from ogs.market_data.instrument import (
    Instrument,
    InstrumentAnalyzer,
    InstrumentCollection,
)


def test_analyze():

    c = InstrumentCollection()

    c.add(
        Instrument(
            instrument_id="1",
            symbol="AAPL",
            exchange="NASDAQ",
            asset="AAPL",
            name="Apple",
        )
    )

    result = InstrumentAnalyzer(c).analyze()

    assert "summary" in result
    assert "instrument_analysis" in result
    assert "distribution_analysis" in result