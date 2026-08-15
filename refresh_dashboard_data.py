from stockmind.application.use_cases.run_analysis_use_case import ( RunAnalysisUseCase )

from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository

def get_symbols():
    return(
        WatchlistRepository()
        .load_active_symbols()
    )

def main():

    symbols = [
        "NVDA",
        "AMD",
        "MSFT",
        "AAPL",
        "GOOGL",
        "AMZN",
        "META",
        "PLTR",
        "TSLA"
    ]

    profiles = [
        "conservative",
        "balanced",
        "aggressive"
    ]

    for symbols in get_symbols:

        print(
            f"Refreshing {symbols}"
        )

        RunAnalysisUseCase().execute(
            symbols=symbols
        )

if __name__ == "__main__": 
    main()