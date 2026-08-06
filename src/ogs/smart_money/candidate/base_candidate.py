"""
===========================================================

OGS Smart Money AI

Base Candidate

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from .status import CandidateStatus


@dataclass(frozen=True, slots=True)
class BaseCandidate:
    """
    Base class for all institutional candidates.
    """

    status: CandidateStatus