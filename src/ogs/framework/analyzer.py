"""
OGS Generic Base Analyzer
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseAnalyzer(ABC):
    """
    Base class for all analyzers.

    Every analyzer in OGS should inherit from this class.
    """

    @abstractmethod
    def analyze(self, data):
        """
        Analyze data and return a result.
        """
        raise NotImplementedError

    def __call__(self, data):
        return self.analyze(data)