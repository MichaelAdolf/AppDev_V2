from stockmind.shared.config.settings import Settings
from stockmind.shared.logging.logger import (
    configure_logging
)

import logging


settings = Settings.load()

configure_logging(
    settings.log_level
)

logger = logging.getLogger(
    "startup"
)

logger.info(
    "StockMind gestartet."
)

print(settings)
