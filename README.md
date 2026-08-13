from stockmind.infrastructure.history.analysis_history_repository import (
    AnalysisHistoryRepository
)

from stockmind.domain.history.opportunity_trend_engine import (
    OpportunityTrendEngine
)


def main():

    history = (
        AnalysisHistoryRepository()
        .load_by_symbol(
            "NVDA"
        )
    )

    result = (
        OpportunityTrendEngine()
        .analyze(
            history
        )
    )

    print(
        "\n=== TREND ===\n"
    )

    print(result)


if __name__ == "__main__":
    main()
