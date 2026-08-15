from stockmind.application.dashboard.use_cases.fundamental_dashboard_use_case import (
    FundamentalDashboardUseCase
)

result = (
    FundamentalDashboardUseCase()
    .load(
        "NVDA"
    )
)

print(result)
