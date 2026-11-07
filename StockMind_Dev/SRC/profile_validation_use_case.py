from statistics import mean,median
from stockmind.application.strategy.models.profile_validation_result import ProfileValidationRow,SymbolProfileValidationResult
from stockmind.infrastructure.history.buy_period_repository import BuyPeriodRepository
from stockmind.infrastructure.history.daily_buy_signal_repository import DailyBuySignalRepository
class ProfileValidationUseCase:
 PROFILES=('conservative','balanced','aggressive')
 def __init__(self,database_path=None):self._database_path=database_path
 def analyze(self,symbol,analysis_period='5y'):
  rows=[]
  for profile in self.PROFILES:rows.append(self._row(symbol,profile,analysis_period))
  by={x.profile_name:x for x in rows};c,b,a=by['conservative'],by['balanced'],by['aggressive']
  statuses={
   'conservative':'ROLE_FIT' if c.target_hit_rate>=b.target_hit_rate and c.period_count<=b.period_count else 'ROLE_MISMATCH',
   'balanced':'ROLE_FIT' if c.period_count<=b.period_count<=a.period_count else 'ROLE_MISMATCH',
   'aggressive':'ROLE_FIT' if a.period_count>=b.period_count and a.signal_coverage_rate>=b.signal_coverage_rate else 'ROLE_MISMATCH'}
  rows=[ProfileValidationRow(**{**x.__dict__,'profile_role_status':statuses[x.profile_name]}) for x in rows]
  return SymbolProfileValidationResult(symbol.upper(),analysis_period,rows)
 def _row(self,symbol,profile,period):
  periods=BuyPeriodRepository(self._database_path).load_by_symbol(symbol,profile,period);complete=[x for x in periods if x.is_complete];hits=[x for x in complete if x.outcome=='TARGET_HIT' or x.target_hit];below=[x for x in complete if x.outcome=='BELOW_TARGET'];flat=[x for x in complete if x.outcome=='FLAT'];negative=[x for x in complete if x.outcome=='NEGATIVE'];signals=DailyBuySignalRepository(self._database_path).load_by_symbol(symbol,profile,period,False);buy=[x for x in signals if x.is_buy];days=[x.days_to_target for x in hits if x.days_to_target is not None];draw=[x.max_drawdown_pct for x in complete if x.max_drawdown_pct is not None];success_draw=[x.max_drawdown_pct for x in hits if x.max_drawdown_pct is not None];failure_draw=[x.max_drawdown_pct for x in complete if not x.target_hit and x.max_drawdown_pct is not None];n=len(complete)
  quality='HIGH' if n>=50 else 'MEDIUM' if n>=20 else 'LOW' if n else 'NO_SAMPLE'
  return ProfileValidationRow(profile,len(periods),n,len(periods)-n,len(hits),len(hits)/n if n else 0,len(below)/n if n else 0,len(flat)/n if n else 0,len(negative)/n if n else 0,median(days) if days else None,mean(days) if days else None,mean(x.max_gain_pct for x in complete if x.max_gain_pct is not None) if any(x.max_gain_pct is not None for x in complete) else None,mean(draw) if draw else None,mean(success_draw) if success_draw else None,mean(failure_draw) if failure_draw else None,len(buy),len({x.trading_date for x in buy}),len(signals),len(buy)/len(signals) if signals else 0,mean(x.calendar_duration_days for x in periods) if periods else 0,mean(x.buy_signal_count for x in periods) if periods else 0,quality,'PENDING')
