"""
Tests for Instrument package exports.
"""

from ogs.market_data.instrument import (
    __version__,
    Instrument,
    InstrumentAnalyzer,
    InstrumentCollection,
    InstrumentFactory,
    InstrumentStatistics,
    InstrumentStatus,
    InstrumentType,
    InstrumentValidator,
)


def test_version():
    assert __version__ == "0.1.0"


def test_exports():
    assert Instrument is not None
    assert InstrumentAnalyzer is not None
    assert InstrumentCollection is not None
    assert InstrumentFactory is not None
    assert InstrumentStatistics is not None
    assert InstrumentValidator is not None
    assert InstrumentType is not None
    assert InstrumentStatus is not None