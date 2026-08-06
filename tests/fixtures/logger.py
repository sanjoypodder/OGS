from __future__ import annotations

import pytest

from ogs.core.logger import get_logger


@pytest.fixture
def logger():
    """
    Return the configured OGS logger.
    """

    return get_logger()
