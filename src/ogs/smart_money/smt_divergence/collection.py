"""
OGS Smart Money AI
------------------

SMT Divergence Collection

Stores multiple SMT Divergence objects.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from collections.abc import Iterable

from ogs.smart_money.base.collection import BaseCollection

from .domain import SMTDivergence


class SMTDivergenceSeries(BaseCollection[SMTDivergence]):
    """
    Collection of SMT Divergence objects.
    """

    def __init__(
        self,
        items: Iterable[SMTDivergence] | None = None,
    ) -> None:
        super().__init__(items)

    def append(
        self,
        divergence: SMTDivergence,
    ) -> None:
        """
        Append a new SMT Divergence.
        """
        self._items.append(divergence)

    def latest(
        self,
        count: int = 1,
    ) -> list[SMTDivergence]:
        """
        Return the latest SMT Divergence objects.
        """
        return self._items[-count:]