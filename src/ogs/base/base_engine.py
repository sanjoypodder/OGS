"""
===========================================================

Module:
    base_engine.py

Purpose:
    Abstract base class for every engine in OGS.

Author:
    Om Ganapati Solution

Project:
    OGS Smart Money AI

===========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class BaseEngine(ABC):
    """
    Base class for every engine in OGS.

    All engines must inherit from this class.
    """

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        """Return engine name."""
        return self._name

    @abstractmethod
    def initialize(self) -> None:
        """
        Initialize engine resources.
        """
        raise NotImplementedError

    @abstractmethod
    def analyze(self, market_state: object) -> object:
        """
        Analyze market data.

        Parameters
        ----------
        market_state
            Current market state.

        Returns
        -------
        object
            Analysis result.
        """
        raise NotImplementedError

    @abstractmethod
    def reset(self) -> None:
        """
        Reset engine state.
        """
        raise NotImplementedError

    @abstractmethod
    def shutdown(self) -> None:
        """
        Shutdown engine.
        """
        raise NotImplementedError
