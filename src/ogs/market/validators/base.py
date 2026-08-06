"""
===========================================================

OGS Smart Money AI

Validation Base Classes

===========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Validator(ABC, Generic[T]):
    """
    Base class for all validators.
    """

    @abstractmethod
    def validate(self, item: T) -> None:
        """
        Validate an object.

        Raises:
            ValueError:
                If validation fails.
        """
        raise NotImplementedError