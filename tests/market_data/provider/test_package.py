"""
Tests for the Provider package exports.
"""

from ogs.market_data.provider import (
    ConnectionStatus,
    Provider,
    ProviderAnalyzer,
    ProviderCollection,
    ProviderFactory,
    ProviderStatistics,
    ProviderType,
    ProviderValidator,
)


def test_package_exports() -> None:
    """
    Verify all public objects are importable.
    """

    assert Provider is not None
    assert ProviderType is not None
    assert ConnectionStatus is not None

    assert ProviderValidator is not None
    assert ProviderFactory is not None
    assert ProviderCollection is not None
    assert ProviderStatistics is not None
    assert ProviderAnalyzer is not None