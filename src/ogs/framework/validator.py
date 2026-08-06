"""
OGS Generic Base Validator
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseValidator(ABC):
    """
    Base validator for OGS modules.
    """

    @abstractmethod
    def validate(self, obj) -> bool:
        """
        Validate an object.
        """
        raise NotImplementedError

    def __call__(self, obj) -> bool:
        return self.validate(obj)