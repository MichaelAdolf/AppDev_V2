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
