"""
Tests for TradingSessionTemplate package exports.
"""

from ogs.market_data.trading_session_template import (
    __version__,
    TradingSessionTemplate,
    TradingSessionTemplateAnalyzer,
    TradingSessionTemplateCollection,
    TradingSessionTemplateFactory,
    TradingSessionTemplateStatistics,
    TradingSessionTemplateValidator,
    TradingSessionTemplateStatus,
    TradingSessionTemplateType,
)


def test_version():

    assert __version__ == "0.1.0"


def test_exports():

    assert TradingSessionTemplate is not None
    assert TradingSessionTemplateAnalyzer is not None
    assert TradingSessionTemplateCollection is not None
    assert TradingSessionTemplateFactory is not None
    assert TradingSessionTemplateStatistics is not None
    assert TradingSessionTemplateValidator is not None
    assert TradingSessionTemplateStatus is not None
    assert TradingSessionTemplateType is not None