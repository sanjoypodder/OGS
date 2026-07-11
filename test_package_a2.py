from ogs.core.config import CONFIG
from ogs.core.logger import get_logger
from ogs.core.exceptions import EngineError

log = get_logger()

log.info("Logger initialized successfully.")

print(CONFIG.app_name)
print(CONFIG.version)

try:
    raise EngineError("Sample Engine Error")
except EngineError as ex:
    log.error(ex)
