"""
OGS Generic Base Factory
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseFactory(ABC):
    """
    Base class for all factories.
    """

    @abstractmethod
    def create(self, *args, **kwargs):
        """
        Create and return a domain object.
        """
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        return self.create(*args, **kwargs)