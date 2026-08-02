from datetime import (
    datetime,
    date
)

from sqlalchemy import (
    String,
    DateTime,
    Integer,
    Float,
    Date,
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

    started_at: Mapped[datetime] = mapped_column(
        DateTime
    )


class MarketPriceModel(Base):
    __tablename__ = "market_prices"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    symbol: Mapped[str] = mapped_column(
        String,
        index=True
    )

    trading_date: Mapped[date] = mapped_column(
        Date
    )

    open_price: Mapped[float] = mapped_column(
        Float
    )

    high_price: Mapped[float] = mapped_column(
        Float
    )

    low_price: Mapped[float] = mapped_column(
        Float
    )

    close_price: Mapped[float] = mapped_column(
        Float
    )

    volume: Mapped[int] = mapped_column(
        Integer
    )
