from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    app_name: str
    app_version: str
    environment: str
    database_url: str
    log_level: str

    @classmethod
    def load(cls) -> "Settings":
        load_dotenv()

        database_path = os.getenv(
            "STOCKMIND_DB_PATH",
            "config/stockmind/stockmind.db"
        )

        Path(database_path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        return cls(
            app_name="StockMind",
            app_version="1.0.0",
            environment=os.getenv(
                "APP_ENV",
                "development"
            ),
            database_url=f"sqlite:///{database_path}",
            log_level=os.getenv(
                "LOG_LEVEL",
                "INFO"
            )
        )
