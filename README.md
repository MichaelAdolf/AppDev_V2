@app.post(
    "/watchlist/{symbol}"
)
def add_stock(
    symbol: str
):

    added = (
        AddStockUseCase()
        .execute(
            symbol
        )
    )

    return {
        "symbol": symbol,
        "added": added
    }
