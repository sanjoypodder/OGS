"""
Analyzer detection tests.
"""

from ogs.market_data.instrument import (
    Instrument,
    InstrumentAnalyzer,
    InstrumentCollection,
    InstrumentType,
)


def test_distribution():

    c = InstrumentCollection()

    c.add(
        Instrument(
            instrument_id="1",
            symbol="BTCUSDT",
            exchange="BINANCE",
            asset="BTC",
            name="Bitcoin",
            instrument_type=InstrumentType.CRYPTO,
        )
    )

    result = InstrumentAnalyzer(c).distribution_analysis()

    assert result["instrument_type"]["CRYPTO"] == 1