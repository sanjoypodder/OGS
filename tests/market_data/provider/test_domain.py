"""
Tests for Provider domain.
"""

from ogs.market_data.provider import (
    ConnectionStatus,
    Provider,
    ProviderType,
)


def test_provider_creation() -> None:
    """
    Test Provider creation.
    """

    provider = Provider(
        name="FYERS",
        provider_type=ProviderType.BROKER,
        status=ConnectionStatus.CONNECTED,
        latency_ms=18.5,
        supports_live=True,
        supports_historical=True,
        supports_websocket=True,
        supports_order_execution=True,
        supports_level2=True,
        supports_options=True,
        supports_futures=True,
    )

    assert provider.name == "FYERS"
    assert provider.provider_type is ProviderType.BROKER
    assert provider.status is ConnectionStatus.CONNECTED
    assert provider.latency_ms == 18.5

    assert provider.supports_live
    assert provider.supports_historical
    assert provider.supports_websocket
    assert provider.supports_order_execution
    assert provider.supports_level2
    assert provider.supports_options
    assert provider.supports_futures


def test_connected_property() -> None:
    provider = Provider(
        name="Broker",
        status=ConnectionStatus.CONNECTED,
    )

    assert provider.connected
    assert provider.online
    assert not provider.offline


def test_disconnected_property() -> None:
    provider = Provider(
        name="Broker",
        status=ConnectionStatus.DISCONNECTED,
    )

    assert provider.disconnected
    assert provider.offline
    assert not provider.connected


def test_provider_valid() -> None:
    provider = Provider(
        name="Provider",
    )

    assert provider.is_valid


def test_provider_to_dict() -> None:
    provider = Provider(
        name="FYERS",
        provider_type=ProviderType.BROKER,
        status=ConnectionStatus.CONNECTED,
        latency_ms=20,
    )

    data = provider.to_dict()

    assert data["name"] == "FYERS"
    assert data["provider_type"] == "BROKER"
    assert data["status"] == "CONNECTED"
    assert data["latency_ms"] == 20


def test_str_returns_string() -> None:
    provider = Provider(
        name="Broker",
    )

    assert isinstance(str(provider), str)


def test_repr_returns_string() -> None:
    provider = Provider(
        name="Broker",
    )

    assert isinstance(repr(provider), str)