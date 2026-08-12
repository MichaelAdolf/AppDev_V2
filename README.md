from stockmind.application.use_cases.analyze_stock_use_case import (
    AnalyzeStockUseCase
)

from stockmind.infrastructure.history.analysis_history_repository import (
    AnalysisHistoryRepository
)


def main():

    AnalyzeStockUseCase().execute(
        symbol="NVDA",
        profile_name="balanced"
    )

    AnalyzeStockUseCase().execute(
        symbol="NVDA",
        profile_name="balanced"
    )

    history = (
        AnalysisHistoryRepository()
        .load_by_symbol(
            "NVDA"
        )
    )

    print(
        "\n=== HISTORY ===\n"
    )

    for entry in history:

        print(entry)


if __name__ == "__main__":
    main()
