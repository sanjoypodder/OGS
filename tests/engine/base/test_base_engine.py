"""
Tests for BaseEngine.

Generated for OGS Financial Operating System.
Module: Base
"""

from typing import Any

import pytest

from ogs.engine.base.base_engine import BaseEngine
from ogs.engine.base.engine_context import EngineContext
from ogs.engine.base.engine_result import EngineResult
from ogs.engine.base.exceptions import (
    EngineExecutionError,
    EngineInitializationError,
    EngineValidationError,
)


class SuccessfulEngine(BaseEngine[str]):
    """Simple successful engine used by the test suite."""

    def __init__(self) -> None:
        super().__init__("successful")
        self.initialize_count = 0

    def _initialize(self) -> None:
        self.initialize_count += 1

    def _execute(
        self,
        context: EngineContext,
        **kwargs: Any,
    ) -> EngineResult[str]:
        return EngineResult.ok(
            data="completed",
            metadata={
                "execution_id": context.execution_id,
            },
        )


class FailingInitializationEngine(BaseEngine[str]):
    """Engine whose initialization deliberately fails."""

    def __init__(self) -> None:
        super().__init__("failing_initialization")

    def _initialize(self) -> None:
        raise RuntimeError("Initialization failure")

    def _execute(
        self,
        context: EngineContext,
        **kwargs: Any,
    ) -> EngineResult[str]:
        return EngineResult.ok("unreachable")


class FailingExecutionEngine(BaseEngine[str]):
    """Engine whose execution deliberately fails."""

    def __init__(self) -> None:
        super().__init__("failing_execution")

    def _execute(
        self,
        context: EngineContext,
        **kwargs: Any,
    ) -> EngineResult[str]:
        raise RuntimeError("Execution failure")


class InvalidResultEngine(BaseEngine[str]):
    """Engine that deliberately violates the result contract."""

    def __init__(self) -> None:
        super().__init__("invalid_result")

    def _execute(  # type: ignore[override]
        self,
        context: EngineContext,
        **kwargs: Any,
    ) -> Any:
        return "invalid result"


class ValidationEngine(BaseEngine[str]):
    """Engine that deliberately raises a validation error."""

    def __init__(self) -> None:
        super().__init__("validation")

    def _execute(
        self,
        context: EngineContext,
        **kwargs: Any,
    ) -> EngineResult[str]:
        raise EngineValidationError(
            "Invalid engine input."
        )


def test_engine_name_is_normalized() -> None:
    """Engine names should be stripped."""

    class NamedEngine(SuccessfulEngine):
        def __init__(self) -> None:
            BaseEngine.__init__(
                self,
                "  liquidity  ",
            )
            self.initialize_count = 0

    engine = NamedEngine()

    assert engine.name == "liquidity"


def test_empty_engine_name_is_rejected() -> None:
    """Whitespace-only engine names should be rejected."""

    with pytest.raises(
        EngineInitializationError,
        match="Engine name cannot be empty or whitespace",
    ):
        BaseEngine.__init__(
            SuccessfulEngine.__new__(SuccessfulEngine),
            "   ",
        )


def test_engine_starts_uninitialized() -> None:
    """New engines should initially be uninitialized."""

    engine = SuccessfulEngine()

    assert engine.initialized is False


def test_initialize_marks_engine_initialized() -> None:
    """Explicit initialization should update lifecycle state."""

    engine = SuccessfulEngine()

    engine.initialize()

    assert engine.initialized is True
    assert engine.initialize_count == 1


def test_initialize_is_idempotent() -> None:
    """Repeated initialization should execute only once."""

    engine = SuccessfulEngine()

    engine.initialize()
    engine.initialize()

    assert engine.initialized is True
    assert engine.initialize_count == 1


def test_execute_automatically_initializes_engine() -> None:
    """Execution should initialize an engine when necessary."""

    engine = SuccessfulEngine()

    result = engine.execute(
        EngineContext()
    )

    assert engine.initialized is True
    assert engine.initialize_count == 1
    assert result.success is True


def test_execute_returns_engine_result() -> None:
    """Successful execution should return EngineResult."""

    engine = SuccessfulEngine()
    context = EngineContext()

    result = engine.execute(context)

    assert isinstance(result, EngineResult)
    assert result.success is True
    assert result.data == "completed"
    assert (
        result.metadata["execution_id"]
        == context.execution_id
    )


def test_execute_rejects_invalid_context() -> None:
    """Execution requires EngineContext."""

    engine = SuccessfulEngine()

    with pytest.raises(
        EngineValidationError,
        match="context must be an EngineContext instance",
    ):
        engine.execute(  # type: ignore[arg-type]
            "invalid"
        )


def test_initialization_failure_is_wrapped() -> None:
    """Initialization failures should use framework exceptions."""

    engine = FailingInitializationEngine()

    with pytest.raises(
        EngineInitializationError,
        match="Failed to initialize engine",
    ) as exc_info:
        engine.initialize()

    assert isinstance(
        exc_info.value.__cause__,
        RuntimeError,
    )


def test_execution_failure_is_wrapped() -> None:
    """Unexpected execution errors should be wrapped."""

    engine = FailingExecutionEngine()

    with pytest.raises(
        EngineExecutionError,
        match="execution failed",
    ) as exc_info:
        engine.execute(
            EngineContext()
        )

    assert isinstance(
        exc_info.value.__cause__,
        RuntimeError,
    )


def test_validation_error_is_not_wrapped() -> None:
    """EngineValidationError should propagate unchanged."""

    engine = ValidationEngine()

    with pytest.raises(
        EngineValidationError,
        match="Invalid engine input",
    ):
        engine.execute(
            EngineContext()
        )


def test_invalid_result_is_rejected() -> None:
    """Engines must return EngineResult instances."""

    engine = InvalidResultEngine()

    with pytest.raises(
        EngineExecutionError,
        match="returned an invalid result",
    ):
        engine.execute(
            EngineContext()
        )
