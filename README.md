class MarketDataRepository:

    def save(
        self,
        data: list[MarketDataPoint]
    ) -> None:

        session = SessionLocal()

        try:

            for item in data:

                row = MarketPriceModel(
                    symbol=item.symbol,
                    trading_date=item.trading_date,
                    open_price=item.open_price,
                    high_price=item.high_price,
                    low_price=item.low_price,
                    close_price=item.close_price,
                    volume=item.volume
                )

                session.add(row)

            session.commit()

        finally:

            session.close()
