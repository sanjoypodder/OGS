"""
Tests for ProviderValidator.
"""

import pytest

from ogs.market_data.provider import (
    ConnectionStatus,
    Provider,
    ProviderType,
    ProviderValidator,
)


@pytest.fixture
def validator() -> ProviderValidator:
    return ProviderValidator()


def test_validate_valid_provider(
    validator: ProviderValidator,
) -> None:
    provider = Provider(
        name="FYERS",
        provider_type=ProviderType.BROKER,
        status=ConnectionStatus.CONNECTED,
        latency_ms=15.5,
    )

    validator.validate(provider)


def test_validator_call_returns_provider(
    validator: ProviderValidator,
) -> None:
    provider = Provider(name="Demo")

    result = validator(provider)

    assert result is provider


def test_invalid_provider_type(
    validator: ProviderValidator,
) -> None:
    with pytest.raises(TypeError):
        validator.validate(object())


def test_empty_name(
    validator: ProviderValidator,
) -> None:
    provider = Provider(name="")

    with pytest.raises(ValueError):
        validator.validate(provider)


def test_negative_latency(
    validator: ProviderValidator,
) -> None:
    provider = Provider(
        name="Demo",
        latency_ms=-1,
    )

    with pytest.raises(ValueError):
        validator.validate(provider)


def test_latency_too_large(
    validator: ProviderValidator,
) -> None:
    provider = Provider(
        name="Demo",
        latency_ms=100000,
    )

    with pytest.raises(ValueError):
        validator.validate(provider)