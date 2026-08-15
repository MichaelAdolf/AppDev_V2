@app.delete(
    "/watchlist/{symbol}"
)
def remove_stock(
    symbol: str
):

    RemoveStockUseCase().execute(
        symbol
    )

    return {
        "removed": symbol
    }
