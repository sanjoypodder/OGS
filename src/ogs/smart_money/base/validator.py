"""
===========================================================

OGS Smart Money AI

Base Validator

===========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class BaseValidator(
    ABC,
    Generic[T],
):
    """
    Base validator.
    """

    @abstractmethod
    def validate(
        self,
        value: T,
    ) -> None:
        """
        Validate object.
        """
        raise NotImplementedError