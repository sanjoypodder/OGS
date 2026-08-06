"""
Tests for EngineResult.

Generated for {{PROJECT_NAME}}.
Module: {{MODULE_NAME}}
"""

from datetime import datetime

import pytest

from ogs.engine.base.engine_result import EngineResult


def test_ok_creates_successful_result() -> None:
    """ok() should create a successful result."""

    result = EngineResult.ok(data="completed")

    assert result.success is True
    assert result.data == "completed"
    assert result.error is None


def test_ok_allows_no_data() -> None:
    """Successful results may contain no payload."""

    result = EngineResult.ok()

    assert result.success is True
    assert result.data is None
    assert result.error is None


def test_fail_creates_failed_result() -> None:
    """fail() should create a failed result."""

    result = EngineResult.fail("Execution failed")

    assert result.success is False
    assert result.data is None
    assert result.error == "Execution failed"


def test_fail_normalizes_error() -> None:
    """Failure messages should be stripped."""

    result = EngineResult.fail(
        "  Market data unavailable  "
    )

    assert result.error == "Market data unavailable"


def test_fail_rejects_empty_error() -> None:
    """Failure messages cannot be empty."""

    with pytest.raises(
        ValueError,
        match="error cannot be empty or whitespace",
    ):
        EngineResult.fail("   ")


def test_fail_rejects_non_string_error() -> None:
    """Failure messages must be strings."""

    with pytest.raises(
        TypeError,
        match="error must be a string",
    ):
        EngineResult.fail(123)  # type: ignore[arg-type]


def test_success_result_rejects_error() -> None:
    """Successful results cannot contain errors."""

    with pytest.raises(
        ValueError,
        match="successful engine result cannot contain an error",
    ):
        EngineResult(
            success=True,
            data="value",
            error="unexpected error",
        )


def test_failed_result_requires_error() -> None:
    """Failed results must contain an error."""

    with pytest.raises(
        ValueError,
        match="failed engine result must contain an error",
    ):
        EngineResult(
            success=False,
        )


def test_failed_result_rejects_blank_error() -> None:
    """Whitespace-only errors should count as missing."""

    with pytest.raises(
        ValueError,
        match="failed engine result must contain an error",
    ):
        EngineResult(
            success=False,
            error="   ",
        )


def test_completed_at_is_timezone_aware() -> None:
    """Result completion timestamps should be timezone-aware."""

    result = EngineResult.ok()

    assert isinstance(result.completed_at, datetime)
    assert result.completed_at.tzinfo is not None
    assert result.completed_at.utcoffset() is not None


def test_metadata_is_read_only() -> None:
    """Result metadata should not be externally mutable."""

    result = EngineResult.ok(
        metadata={
            "engine": "liquidity",
        }
    )

    assert result.metadata["engine"] == "liquidity"

    with pytest.raises(TypeError):
        result.metadata["engine"] = "risk"  # type: ignore[index]


def test_metadata_is_defensively_copied() -> None:
    """Mutating source metadata should not change the result."""

    metadata = {
        "engine": "market_structure",
    }

    result = EngineResult.ok(
        metadata=metadata
    )

    metadata["engine"] = "changed"

    assert result.metadata["engine"] == "market_structure"


def test_result_is_immutable() -> None:
    """EngineResult should be immutable."""

    result = EngineResult.ok(
        data="original"
    )

    with pytest.raises(AttributeError):
        result.data = "changed"  # type: ignore[misc]


def test_result_supports_structured_payload() -> None:
    """EngineResult should support arbitrary typed payloads."""

    payload = {
        "symbol": "XAUUSD",
        "timeframe": "15m",
        "signal": "bullish",
    }

    result = EngineResult.ok(
        data=payload
    )

    assert result.success is True
    assert result.data == payload
