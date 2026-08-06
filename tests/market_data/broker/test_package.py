"""
Tests for Broker package exports.
"""

from ogs.market_data.broker import (
    __version__,
    Broker,
    BrokerAnalyzer,
    BrokerCollection,
    BrokerFactory,
    BrokerStatistics,
    BrokerStatus,
    BrokerValidator,
    MarketType,
)


def test_version():
    assert __version__ == "0.1.0"


def test_exports():
    assert Broker is not None
    assert BrokerAnalyzer is not None
    assert BrokerCollection is not None
    assert BrokerFactory is not None
    assert BrokerStatistics is not None
    assert BrokerValidator is not None
    assert BrokerStatus is not None
    assert MarketType is not None