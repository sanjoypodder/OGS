"""
OGS Generic Base Statistics
"""

from __future__ import annotations

from abc import ABC


class BaseStatistics(ABC):
    """
    Base class for statistics.

    Stores the collection being analyzed and
    provides common utility properties.
    """

    def __init__(self, collection):

        self.collection = collection

    @property
    def count(self) -> int:
        return len(self.collection)

    @property
    def empty(self) -> bool:
        return len(self.collection) == 0

    @property
    def has_items(self) -> bool:
        return len(self.collection) > 0

    def __len__(self):

        return len(self.collection)

    def __repr__(self):

        return (
            f"{self.__class__.__name__}"
            f"(count={self.count})"
        )