from stockmind.application.exit.exit_simulation_use_case import ExitSimulationUseCase
from stockmind.domain.exit.exit_strategy import ExitStrategy
from stockmind.domain.exit.exit_validation_result import (
    ExitValidationRow,
    WalkForwardFoldResult,
)
from stockmind.infrastructure.history.buy_period_repository import BuyPeriodRepository
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository
from stockmind.infrastructure.history.historical_opportunity_repository import HistoricalOpportunityRepository


class ExitResearchValidationUseCase:
    MIN_TRAIN = 12
    MIN_VALIDATION = 5

    def __init__(self, database_path=None):
        self._database_path = database_path

    def validate(self, symbol, profile_name="balanced", train_ratio=0.70):
        periods = sorted([
            period
            for period in BuyPeriodRepository(
                self._database_path
            ).load_by_symbol(symbol, profile_name, "5y")
            if period.is_complete
        ], key=lambda item: item.start_date)
        prices = ChartDataRepository(
            self._database_path
        ).load_by_symbol(symbol)
        opportunities = HistoricalOpportunityRepository(
            self._database_path
        ).load_by_symbol(symbol, profile_name)

        split_index = int(len(periods) * train_ratio)
        train = periods[:split_index]
        validation = periods[split_index:]
        sufficient = (
            len(train) >= self.MIN_TRAIN
            and len(validation) >= self.MIN_VALIDATION
        )
        simulator = ExitSimulationUseCase()
        rows = []
        for strategy in ExitStrategy.research_candidates():
            train_summary = simulator.summarize(
                strategy.name,
                [
                    simulator.simulate(
                        period, prices, opportunities, strategy
                    )
                    for period in train
                ],
            )
            validation_summary = simulator.summarize(
                strategy.name,
                [
                    simulator.simulate(
                        period, prices, opportunities, strategy
                    )
                    for period in validation
                ],
            )
            return_degradation = (
                validation_summary.average_return_pct
                - train_summary.average_return_pct
            )
            positive_degradation = (
                validation_summary.positive_rate
                - train_summary.positive_rate
            )
            if not sufficient:
                status = "INSUFFICIENT_SAMPLE"
            elif (
                return_degradation >= -2.0
                and positive_degradation >= -0.15
                and validation_summary.average_return_pct > 0
            ):
                status = "STABLE"
            elif validation_summary.average_return_pct > 0:
                status = "DEGRADED"
            else:
                status = "FAILED_VALIDATION"
            rows.append(ExitValidationRow(
                strategy.name,
                train_summary.sample_count,
                validation_summary.sample_count,
                train_summary.average_return_pct,
                validation_summary.average_return_pct,
                train_summary.positive_rate,
                validation_summary.positive_rate,
                train_summary.average_max_drawdown_pct,
                validation_summary.average_max_drawdown_pct,
                return_degradation,
                positive_degradation,
                status,
            ))
        order = {
            "STABLE": 3,
            "DEGRADED": 2,
            "FAILED_VALIDATION": 1,
            "INSUFFICIENT_SAMPLE": 0,
        }
        return {
            "symbol": symbol.upper(),
            "profile_name": profile_name,
            "period_count": len(periods),
            "train_count": len(train),
            "validation_count": len(validation),
            "sufficient_sample": sufficient,
            "rows": sorted(
                rows,
                key=lambda row: (
                    order[row.robustness_status],
                    row.validation_average_return_pct,
                    row.validation_positive_rate,
                ),
                reverse=True,
            ),
            "walk_forward": self._walk_forward(
                periods, prices, opportunities
            ),
        }

    def _walk_forward(self, periods, prices, opportunities):
        if len(periods) < self.MIN_TRAIN + self.MIN_VALIDATION:
            return []
        simulator = ExitSimulationUseCase()
        strategies = ExitStrategy.research_candidates()
        fold_results = []
        fold_number = 1
        train_end = self.MIN_TRAIN
        while train_end + self.MIN_VALIDATION <= len(periods):
            train = periods[:train_end]
            validation = periods[
                train_end:train_end + self.MIN_VALIDATION
            ]
            ranked = []
            for strategy in strategies:
                summary = simulator.summarize(
                    strategy.name,
                    [
                        simulator.simulate(
                            period, prices, opportunities, strategy
                        )
                        for period in train
                    ],
                )
                ranked.append((summary.average_return_pct, strategy, summary))
            _, selected, train_summary = max(
                ranked,
                key=lambda item: (item[0], item[2].positive_rate),
            )
            validation_summary = simulator.summarize(
                selected.name,
                [
                    simulator.simulate(
                        period, prices, opportunities, selected
                    )
                    for period in validation
                ],
            )
            fold_results.append(WalkForwardFoldResult(
                fold_number,
                train[0].start_date,
                train[-1].start_date,
                validation[0].start_date,
                validation[-1].start_date,
                selected.name,
                train_summary.average_return_pct,
                validation_summary.average_return_pct,
                validation_summary.positive_rate,
                validation_summary.sample_count,
            ))
            train_end += self.MIN_VALIDATION
            fold_number += 1
        return fold_results
