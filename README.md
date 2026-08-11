from stockmind.application.use_cases.run_analysis_use_case import (
    RunAnalysisUseCase
)


def main():

    symbols = [
        "NVDA",
        "AMD",
        "MSFT",
        "AAPL",
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
        "\n=== ANALYSIS RESULT ===\n"
    )

    for stock in result.stock_results:

        print(
            f"\n{stock.symbol}"
        )

        print(
            f"Quality: "
            f"{stock.quality}"
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
            f"Risk: "
            f"{stock.risk_level}"
        )

        print(
            f"Signal: "
            f"{stock.signal.signal.value}"
        )

        print(
            f"Sample Quality: "
            f"{stock.sample_quality}"
        )

        print(
            f"Average Similarity: "
            f"{stock.average_similarity}"
        )
