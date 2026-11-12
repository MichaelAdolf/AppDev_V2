from stockmind.application.strategy.individual_candidate_evaluator import IndividualCandidateEvaluator
from stockmind.application.strategy.individual_parameter_space import IndividualParameterSpace
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository
from stockmind.infrastructure.history.indicator_chart_data_repository import IndicatorChartDataRepository

class IndividualStrategyOptimizer:
    def __init__(self,database_path=None):self._database_path=database_path
    def optimize(self,symbol,max_candidates=180,top_candidates=8):
        prices={x.trading_date:x for x in ChartDataRepository(self._database_path).load_by_symbol(symbol)}
        indicators=IndicatorChartDataRepository(self._database_path).load_by_symbol(symbol)
        if not prices or not indicators:raise ValueError('Keine ausreichenden Kurs- oder Indikatordaten vorhanden.')
        evaluator=IndividualCandidateEvaluator();parameters=IndividualParameterSpace().sampled(max_candidates)
        candidates=[evaluator.evaluate(symbol,p,prices,indicators) for p in parameters]
        viable=[x for x in candidates if x.complete_period_count>=5]
        ranked=sorted(viable,key=lambda x:(x.objective_score,x.target_hit_rate,x.complete_period_count,x.coverage_rate),reverse=True)
        return {'searched_candidate_count':len(candidates),'candidates':ranked[:top_candidates]}
