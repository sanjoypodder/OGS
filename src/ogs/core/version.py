"""
===========================================================

Module:
    version.py

Purpose:
    Central version information for OGS.

Author:
    Om Ganapati Solution

Project:
    OGS Smart Money AI

===========================================================
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Version:
    """Application version information."""

    major: int = 0
    minor: int = 1
    patch: int = 0
    stage: str = "alpha"
    build: int = 1

    @property
    def short(self) -> str:
        """Return semantic version."""
        return f"{self.major}.{self.minor}.{self.patch}"

    @property
    def full(self) -> str:
        """Return complete version string."""
        return f"{self.major}.{self.minor}.{self.patch}-{self.stage}.{self.build}"


VERSION = Version()
