from stockmind.application.use_cases.run_analysis_use_case import (
    RunAnalysisUseCase
)

symbols = [
    "NVDA",
    "AMD",
    "MSFT",
    "AAPL",
    "GOOGL"
]

for profile in [
    "conservative",
    "balanced",
    "aggressive"
]:

    RunAnalysisUseCase().execute(
        symbols=symbols,
        profile_name=profile
    )
