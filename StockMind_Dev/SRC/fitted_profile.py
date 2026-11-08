from dataclasses import dataclass

@dataclass(frozen=True)
class FittedProfile:
 id:str;symbol:str;version:int;status:str;base_profile:str
 rsi_oversold_threshold:float;rsi_overbought_threshold:float
 bollinger_lower_threshold:float;adx_trend_strength_threshold:float
 stochastic_oversold_threshold:float;created_at:str
