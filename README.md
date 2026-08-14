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

    for profile in profiles:

        print(
            f"Refreshing {profile}"
        )

        RunAnalysisUseCase().execute(
            symbols=symbols,
            profile_name=profile
        )


if __name__ == "__main__":
    main()
