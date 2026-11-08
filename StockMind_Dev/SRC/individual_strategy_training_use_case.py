from stockmind.application.strategy.fitted_profile_candidate_use_case import SaveFittedProfileCandidateUseCase
from stockmind.application.strategy.fitted_profile_validation_use_case import FittedProfileValidationUseCase
from stockmind.application.strategy.individual_strategy_optimizer import IndividualStrategyOptimizer
from stockmind.domain.strategy.individual_strategy_training_result import IndividualStrategyTrainingResult,IndividualTrainingCandidateResult

class IndividualStrategyTrainingUseCase:
    def __init__(self,database_path=None):self._database_path=database_path
    def execute(self,symbol,max_candidates=180,top_candidates=8):
        optimized=IndividualStrategyOptimizer(self._database_path).optimize(symbol,max_candidates,top_candidates)
        results=[]
        for candidate in optimized['candidates']:
            profile=SaveFittedProfileCandidateUseCase(self._database_path).execute(candidate)
            validation=FittedProfileValidationUseCase(self._database_path).validate(profile.id)
            results.append(IndividualTrainingCandidateResult(profile.id,profile.version,validation.status,candidate.objective_score,validation.validation.target_hit_rate,validation.validation.sample_count,validation.benchmark_validation.target_hit_rate,validation.stable_fold_rate,candidate.rsi_oversold_threshold,candidate.bollinger_lower_threshold,candidate.adx_trend_strength_threshold,candidate.stochastic_oversold_threshold))
        validated=[x for x in results if x.status=='VALIDATED']
        validated.sort(key=lambda x:(x.validation_target_hit_rate-x.benchmark_target_hit_rate,x.validation_sample_count,x.stable_fold_rate,x.objective_score),reverse=True)
        proposed=validated[0] if validated else None
        reasons=['BEST_ROBUST_CANDIDATE_PROPOSED'] if proposed else ['NO_ROBUST_CANDIDATE']
        return IndividualStrategyTrainingResult(symbol.upper(),'PROPOSAL_READY' if proposed else 'NO_ROBUST_CANDIDATE',optimized['searched_candidate_count'],len(validated),proposed.profile_id if proposed else None,proposed.version if proposed else None,results,reasons)
