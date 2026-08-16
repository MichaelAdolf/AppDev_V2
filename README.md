from stockmind.application.models.analysis_run_result import (
    AnalysisRunResult
)

from stockmind.application.use_cases.analyze_stock_use_case import (
    AnalyzeStockUseCase
)


class RunAnalysisUseCase:

    def execute(
        self,
        symbol: str,
        profile_name: str
    ) -> AnalysisRunResult:

        analyze_use_case = (
            AnalyzeStockUseCase()
        )

        result = (
            analyze_use_case.execute(
                symbol=symbol,
                profile_name=profile_name
            )
        )

        return AnalysisRunResult(
            profile_name=profile_name,
            stock_results=[
                result
            ]
        )
