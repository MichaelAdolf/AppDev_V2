from stockmind.application.use_cases.run_analysis_use_case import (
    RunAnalysisUseCase
)


def main():

    symbols = [
        "NVDA",
        "AMD",
        "AAPL",
        "MSFT",
        "GOOGL",
    ]

    result = (
        RunAnalysisUseCase()
        .execute(
            symbols=symbols,
            profile_name="balanced"
        )
    )

    print(
        "\n=== OPPORTUNITY RANKING ===\n"
    )

    rank = 1

    for stock in result.stock_results:

        print(
            f"{rank}. {stock.symbol}"
        )

        print(
            f"Opportunity Score: "
            f"{stock.opportunity_score:.2f}"
        )

        print(
            f"Confidence: "
            f"{stock.confidence:.2%}"
        )

        print(
            f"Historical Success: "
            f"{stock.historical_success_rate:.2%}"
        )

        print(
            f"Quality: "
            f"{stock.quality}"
        )

        print(
            f"Risk: "
            f"{stock.risk_level}"
        )

        print(
            f"Signal: "
            f"{stock.signal.signal.value}"
        )

        print()

        rank += 1


if __name__ == "__main__":
    main()
