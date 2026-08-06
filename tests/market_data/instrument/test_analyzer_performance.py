"""
Performance tests.
"""

from ogs.market_data.instrument import (
    Instrument,
    InstrumentAnalyzer,
    InstrumentCollection,
)


def test_large():

    c = InstrumentCollection()

    for i in range(1000):

        c.add(
            Instrument(
                instrument_id=str(i),
                symbol=str(i),
                exchange="TEST",
                asset=str(i),
                name=str(i),
            )
        )

    result = InstrumentAnalyzer(c).analyze()

    assert result["summary"]["count"] == 1000