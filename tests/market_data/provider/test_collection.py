"""
Tests for ProviderCollection.
"""

from ogs.market_data.provider import (
    ConnectionStatus,
    ProviderCollection,
    ProviderFactory,
    ProviderType,
)


def create_collection() -> ProviderCollection:
    return ProviderCollection(
        [
            ProviderFactory.create(
                name="FYERS",
                provider_type=ProviderType.BROKER,
                status=ConnectionStatus.CONNECTED,
                latency_ms=15,
                supports_live=True,
                supports_historical=True,
                supports_websocket=True,
            ),
            ProviderFactory.create(
                name="NSE",
                provider_type=ProviderType.EXCHANGE,
                status=ConnectionStatus.CONNECTED,
                latency_ms=5,
                supports_live=True,
                supports_historical=True,
            ),
            ProviderFactory.create(
                name="CSV",
                provider_type=ProviderType.CSV,
                status=ConnectionStatus.DISCONNECTED,
                latency_ms=100,
                supports_historical=True,
            ),
        ]
    )


def test_length() -> None:
    collection = create_collection()

    assert len(collection) == 3


def test_connected() -> None:
    collection = create_collection()

    assert len(collection.connected()) == 2


def test_disconnected() -> None:
    collection = create_collection()

    assert len(collection.disconnected()) == 1


def test_live_capable() -> None:
    collection = create_collection()

    assert len(collection.live_capable()) == 2


def test_historical_capable() -> None:
    collection = create_collection()

    assert len(collection.historical_capable()) == 3


def test_websocket_capable() -> None:
    collection = create_collection()

    assert len(collection.websocket_capable()) == 1


def test_by_type() -> None:
    collection = create_collection()

    brokers = collection.by_type(ProviderType.BROKER)

    assert len(brokers) == 1
    assert brokers[0].name == "FYERS"


def test_find() -> None:
    collection = create_collection()

    provider = collection.find("FYERS")

    assert provider is not None
    assert provider.name == "FYERS"


def test_find_returns_none() -> None:
    collection = create_collection()

    assert collection.find("ABC") is None


def test_fastest() -> None:
    collection = create_collection()

    assert collection.fastest().name == "NSE"


def test_slowest() -> None:
    collection = create_collection()

    assert collection.slowest().name == "CSV"


def test_average_latency() -> None:
    collection = create_collection()

    assert collection.average_latency() == (15 + 5 + 100) / 3


def test_names() -> None:
    collection = create_collection()

    assert collection.names() == [
        "CSV",
        "FYERS",
        "NSE",
    ]


def test_add() -> None:
    collection = create_collection()

    collection.add(
        ProviderFactory.create(name="Demo")
    )

    assert len(collection) == 4


def test_to_list() -> None:
    collection = create_collection()

    data = collection.to_list()

    assert isinstance(data, list)
    assert len(data) == 3