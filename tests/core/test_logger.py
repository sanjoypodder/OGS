from ogs.core.logger import configure_logger, get_logger


def test_logger_creation() -> None:
    configure_logger()

    logger = get_logger()

    assert logger is not None


def test_logger_singleton() -> None:
    logger1 = get_logger()

    logger2 = get_logger()

    assert logger1 is logger2


def test_logger_info() -> None:
    logger = get_logger()

    logger.info("Logger unit test")


def test_logger_warning() -> None:
    logger = get_logger()

    logger.warning("Warning test")


def test_logger_error() -> None:
    logger = get_logger()

    logger.error("Error test")
