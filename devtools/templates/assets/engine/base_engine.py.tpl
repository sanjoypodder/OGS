"""
Base engine contract for {{PROJECT_NAME}}.

Project      : {{PROJECT_SHORT_NAME}}
Module       : {{MODULE_NAME}}
Organization : {{ORGANIZATION}}
Version      : {{PROJECT_VERSION}}
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from .engine_context import EngineContext
from .engine_result import EngineResult
from .exceptions import (
    EngineExecutionError,
    EngineInitializationError,
    EngineValidationError,
)


T = TypeVar("T")


class BaseEngine(ABC, Generic[T]):
    """Abstract base class for all OGS engines."""

    def __init__(self, name: str) -> None:
        """Initialize the engine."""

        normalized_name = name.strip()

        if not normalized_name:
            raise EngineInitializationError(
                "Engine name cannot be empty or whitespace."
            )

        self._name = normalized_name
        self._initialized = False

    @property
    def name(self) -> str:
        """Return the unique engine name."""

        return self._name

    @property
    def initialized(self) -> bool:
        """Return whether the engine has been initialized."""

        return self._initialized

    def initialize(self) -> None:
        """Initialize the engine."""

        if self._initialized:
            return

        try:
            self._initialize()
        except Exception as exc:
            raise EngineInitializationError(
                f"Failed to initialize engine '{self.name}'."
            ) from exc

        self._initialized = True

    def _initialize(self) -> None:
        """Perform subclass-specific initialization."""

    def execute(
        self,
        context: EngineContext,
        **kwargs: Any,
    ) -> EngineResult[T]:
        """Execute the engine using the supplied context."""

        if not isinstance(context, EngineContext):
            raise EngineValidationError(
                "context must be an EngineContext instance."
            )

        if not self._initialized:
            self.initialize()

        try:
            result = self._execute(
                context=context,
                **kwargs,
            )
        except EngineValidationError:
            raise
        except Exception as exc:
            raise EngineExecutionError(
                f"Engine '{self.name}' execution failed."
            ) from exc

        if not isinstance(result, EngineResult):
            raise EngineExecutionError(
                f"Engine '{self.name}' returned an invalid result."
            )

        return result

    @abstractmethod
    def _execute(
        self,
        context: EngineContext,
        **kwargs: Any,
    ) -> EngineResult[T]:
        """Implement engine-specific execution logic."""

        raise NotImplementedError
