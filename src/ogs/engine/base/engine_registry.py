"""
Engine registry for OGS Financial Operating System.

Project      : OGS-FOS
Module       : Base
Organization : Om Ganapati Solution
Version      : 0.0.1
"""

from __future__ import annotations

from types import MappingProxyType
from typing import Iterator, Mapping

from .base_engine import BaseEngine
from .exceptions import (
    DuplicateEngineError,
    EngineNotFoundError,
    EngineRegistrationError,
)


class EngineRegistry:
    """Registry for OGS engine instances.

    The registry provides controlled registration and lookup of engine
    instances while protecting its internal state from external mutation.
    """

    def __init__(self) -> None:
        """Initialize an empty engine registry."""

        self._engines: dict[str, BaseEngine] = {}

    def register(
        self,
        engine: BaseEngine,
        *,
        replace: bool = False,
    ) -> None:
        """Register an engine instance.

        Args:
            engine:
                Engine instance to register.

            replace:
                Replace an existing engine with the same name when True.

        Raises:
            EngineRegistrationError:
                If ``engine`` is not a BaseEngine instance.

            DuplicateEngineError:
                If an engine with the same name is already registered
                and replacement was not requested.
        """

        if not isinstance(engine, BaseEngine):
            raise EngineRegistrationError(
                "Only BaseEngine instances can be registered."
            )

        name = engine.name

        if name in self._engines and not replace:
            raise DuplicateEngineError(
                f"Engine '{name}' is already registered."
            )

        self._engines[name] = engine

    def unregister(self, name: str) -> BaseEngine:
        """Remove and return a registered engine."""

        normalized_name = self._normalize_name(name)

        try:
            return self._engines.pop(normalized_name)
        except KeyError as exc:
            raise EngineNotFoundError(
                f"Engine '{normalized_name}' is not registered."
            ) from exc

    def get(self, name: str) -> BaseEngine:
        """Return a registered engine by name."""

        normalized_name = self._normalize_name(name)

        try:
            return self._engines[normalized_name]
        except KeyError as exc:
            raise EngineNotFoundError(
                f"Engine '{normalized_name}' is not registered."
            ) from exc

    def contains(self, name: str) -> bool:
        """Return whether an engine name is registered."""

        normalized_name = self._normalize_name(name)

        return normalized_name in self._engines

    def names(self) -> tuple[str, ...]:
        """Return registered engine names."""

        return tuple(self._engines.keys())

    def engines(self) -> Mapping[str, BaseEngine]:
        """Return a read-only view of registered engines."""

        return MappingProxyType(self._engines)

    def clear(self) -> None:
        """Remove all registered engines."""

        self._engines.clear()

    def __contains__(self, name: object) -> bool:
        """Support ``name in registry``."""

        if not isinstance(name, str):
            return False

        try:
            return self.contains(name)
        except EngineRegistrationError:
            return False

    def __len__(self) -> int:
        """Return the number of registered engines."""

        return len(self._engines)

    def __iter__(self) -> Iterator[BaseEngine]:
        """Iterate over registered engine instances."""

        return iter(self._engines.values())

    @staticmethod
    def _normalize_name(name: str) -> str:
        """Validate and normalize an engine name."""

        if not isinstance(name, str):
            raise EngineRegistrationError(
                "Engine name must be a string."
            )

        normalized_name = name.strip()

        if not normalized_name:
            raise EngineRegistrationError(
                "Engine name cannot be empty or whitespace."
            )

        return normalized_name
