"""
Tests for Session package exports.
"""

from ogs.market_data.session import (
    __version__,
    Session,
    SessionAnalyzer,
    SessionCollection,
    SessionFactory,
    SessionStatistics,
    SessionStatus,
    SessionType,
    SessionValidator,
)


def test_version():

    assert __version__ == "0.1.0"


def test_exports():

    assert Session is not None
    assert SessionAnalyzer is not None
    assert SessionCollection is not None
    assert SessionFactory is not None
    assert SessionStatistics is not None
    assert SessionValidator is not None
    assert SessionType is not None
    assert SessionStatus is not None