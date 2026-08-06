"""
Tests for ProviderFactory.
"""

from ogs.market_data.provider import (
    ConnectionStatus,
    ProviderFactory,
    ProviderType,
)


def test_create() -> None:
    provider = ProviderFactory.create(
        name="FYERS",
        provider_type=ProviderType.BROKER,
        status=ConnectionStatus.CONNECTED,
        latency_ms=20,
        supports_live=True,
        supports_historical=True,
    )

    assert provider.name == "FYERS"
    assert provider.provider_type is ProviderType.BROKER
    assert provider.status is ConnectionStatus.CONNECTED
    assert provider.latency_ms == 20
    assert provider.supports_live
    assert provider.supports_historical


def test_simulated() -> None:
    provider = ProviderFactory.simulated()

    assert provider.provider_type is ProviderType.SIMULATION
    assert provider.status is ConnectionStatus.CONNECTED
    assert provider.supports_live
    assert provider.supports_historical


def test_offline() -> None:
    provider = ProviderFactory.offline("Offline")

    assert provider.name == "Offline"
    assert provider.status is ConnectionStatus.DISCONNECTED


def test_clone() -> None:
    original = ProviderFactory.create(
        name="Broker",
        provider_type=ProviderType.BROKER,
        status=ConnectionStatus.CONNECTED,
        latency_ms=12,
        supports_live=True,
        supports_websocket=True,
    )

    cloned = ProviderFactory.clone(original)

    assert cloned == original
    assert cloned is not original


def test_clone_preserves_all_fields() -> None:
    original = ProviderFactory.create(
        name="Exchange",
        provider_type=ProviderType.EXCHANGE,
        status=ConnectionStatus.CONNECTING,
        latency_ms=5,
        supports_live=True,
        supports_historical=True,
        supports_websocket=True,
        supports_order_execution=True,
        supports_level2=True,
        supports_options=True,
        supports_futures=True,
    )

    cloned = ProviderFactory.clone(original)

    assert cloned.name == original.name
    assert cloned.provider_type == original.provider_type
    assert cloned.status == original.status
    assert cloned.latency_ms == original.latency_ms
    assert cloned.supports_live == original.supports_live
    assert (
        cloned.supports_historical
        == original.supports_historical
    )
    assert (
        cloned.supports_websocket
        == original.supports_websocket
    )
    assert (
        cloned.supports_order_execution
        == original.supports_order_execution
    )
    assert cloned.supports_level2 == original.supports_level2
    assert cloned.supports_options == original.supports_options
    assert cloned.supports_futures == original.supports_futures