from dataclasses import dataclass

@dataclass(frozen=True)
class FittedProfileCandidate:
 candidate_id:str;symbol:str;base_profile:str
 rsi_oversold_threshold:float;rsi_overbought_threshold:float
 bollinger_lower_threshold:float;adx_trend_strength_threshold:float
 stochastic_oversold_threshold:float
 complete_period_count:int;target_hit_count:int;target_hit_rate:float
 signal_count:int;coverage_rate:float;median_days_to_target:float|None
 average_drawdown_pct:float|None;objective_score:float;status:str
