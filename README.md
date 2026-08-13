from stockmind.application.use_cases.run_analysis_use_case import (
    RunAnalysisUseCase
)

from stockmind.infrastructure.history.analysis_history_repository import (
    AnalysisHistoryRepository
)

from stockmind.domain.history.watchlist_trend_engine import (
    WatchlistTrendEngine
)


def main():

    symbols = [
        "NVDA",
        "AMD",
        "MSFT",
        "AAPL",
        "GOOGL"
    ]

    #
    # einige Einträge erzeugen
    #

    RunAnalysisUseCase().execute(
        symbols=symbols,
        profile_name="balanced"
    )

    movers = (
        WatchlistTrendEngine()
        .analyze(
            repository=AnalysisHistoryRepository(),
            symbols=symbols
        )
    )

    print(
        "\n=== TOP MOVERS ===\n"
    )

    rank = 1

    for mover in movers:

        print(
            f"{rank}. {mover.symbol}"
        )

        print(
            f"Latest Score: "
            f"{mover.latest_score:.2f}"
        )

        print(
            f"Change: "
            f"{mover.score_change:.2f}"
        )

        print(
            f"Trend: "
            f"{mover.trend}"
        )

        print()

        rank += 1


if __name__ == "__main__":
    main()
