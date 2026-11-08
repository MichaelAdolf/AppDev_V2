from dataclasses import dataclass
from stockmind.application.strategy.active_strategy_resolver import ActiveStrategyResolver
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository
from stockmind.infrastructure.history.indicator_chart_data_repository import IndicatorChartDataRepository

@dataclass(frozen=True)
class FittedProfileSignalResult:
    symbol:str;active:bool;profile_id:str|None;strategy_name:str|None;base_profile:str|None;validation_status:str|None;signal:str|None;matched_conditions:int;required_conditions:int;reasons:list[str]

class FittedProfileSignalUseCase:
    REQUIRED=4
    def __init__(self,database_path=None):self._database_path=database_path
    def evaluate(self,symbol):
        strategy=ActiveStrategyResolver(self._database_path).resolve(symbol)
        if strategy.strategy_type!='FITTED':return FittedProfileSignalResult(symbol.upper(),False,None,None,None,None,None,0,self.REQUIRED,[])
        profile=strategy.fitted_profile;prices=ChartDataRepository(self._database_path).load_by_symbol(symbol);indicators=IndicatorChartDataRepository(self._database_path).load_by_symbol(symbol)
        if not prices or not indicators:return FittedProfileSignalResult(symbol.upper(),True,profile.id,strategy.strategy_name,profile.base_profile,'ACTIVE','HOLD',0,self.REQUIRED,['Keine aktuellen Indikator- oder Kursdaten'])
        price=prices[-1];indicator=next((x for x in reversed(indicators) if x.trading_date==price.trading_date),indicators[-1]);width=(price.bollinger_upper-price.bollinger_lower) if price.bollinger_upper is not None and price.bollinger_lower is not None else None;position=(price.close_price-price.bollinger_lower)/width if width else None
        checks=[('RSI oversold',indicator.rsi_14 is not None and indicator.rsi_14<=profile.rsi_oversold_threshold),('Near lower Bollinger',position is not None and position<=profile.bollinger_lower_threshold),('ADX trend strength',indicator.adx is not None and indicator.adx>=profile.adx_trend_strength_threshold),('Stochastic oversold',indicator.stoch_k is not None and indicator.stoch_k<=profile.stochastic_oversold_threshold)]
        matched=sum(ok for _,ok in checks);signal='BUY' if matched==self.REQUIRED else 'HOLD';reasons=[name for name,ok in checks if ok]
        return FittedProfileSignalResult(symbol.upper(),True,profile.id,strategy.strategy_name,profile.base_profile,'ACTIVE',signal,matched,self.REQUIRED,reasons)
