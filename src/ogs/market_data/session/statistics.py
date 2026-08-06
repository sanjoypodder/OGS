"""
===========================================================

OGS Smart Money AI

Session Statistics

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.statistics import BaseStatistics

from .collection import SessionCollection
from .enums import SessionType


class SessionStatistics(
    BaseStatistics,
):

    def __init__(
        self,
        collection: SessionCollection,
    ):

        self.collection = collection

    @property
    def count(self):

        return len(self.collection)

    @property
    def active_count(self):

        return len(self.collection.active())

    @property
    def closed_count(self):

        return len(self.collection.closed())

    @property
    def regular_count(self):

        return len(self.collection.regular())

    def distribution(self):

        return {
            t.name: len(
                [
                    s
                    for s in self.collection
                    if s.session_type == t
                ]
            )
            for t in SessionType
        }

    def summary(self):

        return {
            "count": self.count,
            "active": self.active_count,
            "closed": self.closed_count,
            "regular": self.regular_count,
        }