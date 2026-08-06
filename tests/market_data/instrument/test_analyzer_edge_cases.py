"""
Edge cases.
"""

from ogs.market_data.instrument import (
    InstrumentAnalyzer,
    InstrumentCollection,
)


def test_empty():

    result = InstrumentAnalyzer(
        InstrumentCollection()
    ).analyze()

    assert result["summary"]["count"] == 0