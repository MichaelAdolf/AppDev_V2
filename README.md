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

    print(
        "\n=== STOCK ANALYSIS RESULT ===\n"
    )

    print(result)


if __name__ == "__main__":
    main()
