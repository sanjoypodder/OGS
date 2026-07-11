"""
OGS Smart Money AI
Application Entry Point
"""

from ogs.core.config import config
from ogs.core.logger import configure_logger, get_logger


def main() -> None:
    configure_logger()

    log = get_logger()

    log.info("Starting OGS Smart Money AI")

    print("=" * 60)
    print(config.app_name)
    print(config.company)
    print(f"Version : {config.version}")
    print(f"Codename: {config.codename}")
    print("=" * 60)

    log.success("OGS Started Successfully")


if __name__ == "__main__":
    main()
