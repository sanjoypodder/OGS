"""
===========================================================

OGS Smart Money AI

Base Validator

===========================================================
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from .result import ValidationResult


class Validator(ABC):
    """
    Base validator for all OGS validators.
    """

    @abstractmethod
    def validate(
        self,
        obj,
    ) -> ValidationResult:
        """
        Validate an object and return the validation result.
        """
        raise NotImplementedError