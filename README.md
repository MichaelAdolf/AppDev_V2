from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from stockmind.shared.config.settings import Settings


settings = Settings.load()

engine = create_engine(
    settings.database_url,
    echo=False
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
