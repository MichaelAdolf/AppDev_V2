from stockmind.application.use_cases.analyze_stock_use_case import (
    AnalyzeStockUseCase
)


def main():

    profiles = [
        "conservative",
        "balanced",
        "aggressive"
    ]

    for profile in profiles:

        result = (
            AnalyzeStockUseCase()
            .execute(
                symbol="NVDA",
                profile_name=profile
            )
        )

        print(
            "\n================================"
        )

        print(
            profile.upper()
        )

        print(
            "================================"
        )

        print(
            f"Score: "
            f"{result.opportunity_score:.2f}"
        )

        print(
            f"Confidence: "
            f"{result.confidence:.2%}"
        )

        print(
            f"Historical: "
            f"{result.historical_success_rate:.2%}"
        )

        print(
            f"Risk: "
            f"{result.risk_level}"
        )

        print(
            f"Signal: "
            f"{result.signal.signal.value}"
        )


if __name__ == "__main__":
    main()
