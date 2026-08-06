"""
OGS Framework Interfaces
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import TypeVar

T = TypeVar("T")


class AnalyzerInterface(ABC):
    """
    Interface for analyzers.
    """

    @abstractmethod
    def analyze(self, data):
        """
        Analyze the supplied data.
        """
        raise NotImplementedError


class ValidatorInterface(ABC):
    """
    Interface for validators.
    """

    @abstractmethod
    def validate(self, obj) -> bool:
        """
        Validate an object.
        """
        raise NotImplementedError


class FactoryInterface(ABC):
    """
    Interface for factories.
    """

    @abstractmethod
    def create(self, *args, **kwargs):
        """
        Create an object.
        """
        raise NotImplementedError


class StatisticsInterface(ABC):
    """
    Interface for statistics providers.
    """

    @property
    @abstractmethod
    def count(self) -> int:
        raise NotImplementedError


class CollectionInterface(ABC, Generic[T]):
    """
    Interface for collections.
    """

    @abstractmethod
    def append(self, item: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def extend(self, items: Iterable[T]) -> None:
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def __iter__(self) -> Iterator[T]:
        raise NotImplementedError

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError