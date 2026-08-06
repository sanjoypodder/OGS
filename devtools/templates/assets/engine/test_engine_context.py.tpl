"""
Tests for EngineContext.

Generated for {{PROJECT_NAME}}.
Module: {{MODULE_NAME}}
"""

from datetime import datetime, timezone

import pytest

from ogs.engine.base.engine_context import EngineContext


def test_context_generates_execution_id() -> None:
    """Context should automatically generate an execution identifier."""

    context = EngineContext()

    assert isinstance(context.execution_id, str)
    assert context.execution_id


def test_context_uses_timezone_aware_timestamp() -> None:
    """Generated timestamp should be timezone-aware."""

    context = EngineContext()

    assert context.created_at.tzinfo is not None
    assert context.created_at.utcoffset() is not None


def test_context_accepts_symbol_and_timeframe() -> None:
    """Context should retain normalized market information."""

    context = EngineContext(
        symbol=" XAUUSD ",
        timeframe=" 15m ",
    )

    assert context.symbol == "XAUUSD"
    assert context.timeframe == "15m"


def test_context_normalizes_blank_optional_values() -> None:
    """Whitespace-only optional values should become None."""

    context = EngineContext(
        symbol="   ",
        timeframe="   ",
    )

    assert context.symbol is None
    assert context.timeframe is None


def test_context_rejects_empty_execution_id() -> None:
    """An empty execution identifier should be rejected."""

    with pytest.raises(
        ValueError,
        match="execution_id cannot be empty",
    ):
        EngineContext(execution_id="   ")


def test_context_rejects_naive_datetime() -> None:
    """Context timestamps must be timezone-aware."""

    naive_datetime = datetime(2026, 1, 1)

    with pytest.raises(
        ValueError,
        match="created_at must be timezone-aware",
    ):
        EngineContext(created_at=naive_datetime)


def test_context_accepts_timezone_aware_datetime() -> None:
    """Explicit timezone-aware timestamps should be accepted."""

    timestamp = datetime(
        2026,
        1,
        1,
        tzinfo=timezone.utc,
    )

    context = EngineContext(created_at=timestamp)

    assert context.created_at == timestamp


def test_context_metadata_is_read_only() -> None:
    """Metadata exposed by the context should not be mutable."""

    context = EngineContext(
        metadata={
            "source": "test",
        }
    )

    assert context.metadata["source"] == "test"

    with pytest.raises(TypeError):
        context.metadata["source"] = "changed"  # type: ignore[index]


def test_context_copies_metadata() -> None:
    """External metadata mutations should not alter the context."""

    metadata = {
        "source": "original",
    }

    context = EngineContext(metadata=metadata)

    metadata["source"] = "changed"

    assert context.metadata["source"] == "original"


def test_context_is_immutable() -> None:
    """EngineContext itself should be immutable."""

    context = EngineContext(symbol="XAUUSD")

    with pytest.raises(AttributeError):
        context.symbol = "BTCUSD"  # type: ignore[misc]
