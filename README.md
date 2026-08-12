from stockmind.application.use_cases.analyze_stock_use_case import (
    AnalyzeStockUseCase
)


def main():

    result = (
        AnalyzeStockUseCase()
        .execute(
            symbol="NVDA",
            profile_name="balanced"
        )
    )

    print("\n=== ANALYSE ===\n")

    print(
        result.explanation.title
    )

    print(
        result.explanation.summary
    )

    print("\nSTÄRKEN")

    for item in result.explanation.strengths:

        print(
            f"✅ {item}"
        )

    print("\nSCHWÄCHEN")

    for item in result.explanation.weaknesses:

        print(
            f"⚠ {item}"
        )

    print(
        f"\nOpportunity Score: "
        f"{result.opportunity_score:.2f}"
    )


if __name__ == "__main__":
    main()
