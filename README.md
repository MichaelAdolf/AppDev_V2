from sqlalchemy import (
    String,
    DateTime
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from stockmind.infrastructure.database.base import (
    Base
)


class AnalysisRunModel(Base):
    __tablename__ = "analysis_runs"

    run_id: Mapped[str] = mapped_column(
        String,
        primary_key=True
    )

    status: Mapped[str] = mapped_column(
        String
    )

    watchlist_name: Mapped[str] = mapped_column(
        String
    )

    started_at: Mapped[DateTime]
