"""
===========================================================

OGS Smart Money AI

Application Entry Point

Author:
    Om Ganapati Solution

===========================================================
"""

from ogs.core.application import Application
from ogs.core.logger import configure_logger


def main() -> None:
    """
    OGS Entry Point.
    """

    configure_logger()

    application = Application()

    try:
        application.run()

    except KeyboardInterrupt:
        application.shutdown()

    except Exception:
        application.shutdown()

        raise

    finally:
        if application.application_state != "STOPPED":
            application.shutdown()


if __name__ == "__main__":
    main()
