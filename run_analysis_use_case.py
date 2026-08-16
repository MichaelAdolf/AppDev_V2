from stockmind.application.models.analysis_run_result import ( AnalysisRunResult )

from stockmind.application.use_cases.analyze_stock_use_case import ( AnalyzeStockUseCase )

class RunAnalysisUseCase:

    def execute(
        self,
        symbols: str,
        profile_name: str
    ) -> AnalysisRunResult:

        results = []

        analyze_use_case = (
            AnalyzeStockUseCase()
        )

        for symbol in symbols:

            try:

                result = (
                    analyze_use_case.execute(
                        symbol=symbol,
                        profile_name=profile_name
                    )
                )

                results.append(
                    result
                )

            except Exception as ex:

                print(
                    f"ERROR analysing "
                    f"{symbol}: {ex}"
                )

        results.sort(
            key=lambda item:
                item.opportunity_score,
            reverse=True
        )

        return AnalysisRunResult(
            profile_name=profile_name,
            stock_results=results
        )
