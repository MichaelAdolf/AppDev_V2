from dataclasses import dataclass
@dataclass(frozen=True)
class FittedProfileValidationMetrics:
 sample_count:int;target_hit_count:int;target_hit_rate:float;signal_count:int;coverage_rate:float;median_days_to_target:float|None;average_drawdown_pct:float|None
@dataclass(frozen=True)
class FittedProfileWalkForwardFold:
 fold_number:int;train_start:str;train_end:str;validation_start:str;validation_end:str;train_target_hit_rate:float;validation_target_hit_rate:float;validation_sample_count:int
@dataclass(frozen=True)
class FittedProfileValidationResult:
 profile_id:str;symbol:str;version:int;base_profile:str;status:str;train:FittedProfileValidationMetrics;validation:FittedProfileValidationMetrics;benchmark_validation:FittedProfileValidationMetrics;target_hit_degradation:float;benchmark_advantage:float;walk_forward:list[FittedProfileWalkForwardFold];stable_fold_rate:float;reasons:list[str]
