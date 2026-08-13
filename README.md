from stockmind.application.use_cases.run_analysis_use_case import (
    RunAnalysisUseCase
)

from stockmind.infrastructure.history.latest_analysis_repository import (
    LatestAnalysisRepository
)


def main():

    RunAnalysisUseCase().execute(
        symbols=[
            "NVDA",
            "AMD",
            "MSFT"
        ],
        profile_name="balanced"
    )

    results = (
        LatestAnalysisRepository()
        .load_all(
            "balanced"
        )
    )

    for result in results:

        print(result)


if __name__ == "__main__":
    main()
