"""
Configuration
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Config:
    """Base configuration."""