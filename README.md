from pathlib import Path
import os

DATABASE_PATH = os.getenv(
    "STOCKMIND_DB_PATH",
    "config/stockmind/stockmind.db"
)

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
