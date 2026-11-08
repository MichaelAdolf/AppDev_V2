from datetime import datetime
from hashlib import sha1
from statistics import mean,median
from stockmind.domain.strategy.fitted_profile_candidate import FittedProfileCandidate
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository
from stockmind.infrastructure.history.indicator_chart_data_repository import IndicatorChartDataRepository
from stockmind.infrastructure.profiles.profile_repository import ProfileRepository

class FittedProfileSearchUseCase:
 def __init__(self,database_path=None):self._database_path=database_path
 def search(self,symbol,base_profile='balanced',max_candidates=25):
  base=ProfileRepository().get_by_name(base_profile);prices={x.trading_date:x for x in ChartDataRepository(self._database_path).load_by_symbol(symbol)};indicators=IndicatorChartDataRepository(self._database_path).load_by_symbol(symbol)
  universe=self._candidates(base)[:max_candidates];results=[]
  for params in universe:results.append(self._evaluate(symbol,base_profile,params,prices,indicators))
  return sorted(results,key=lambda x:(x.objective_score,x.target_hit_rate,x.complete_period_count),reverse=True)
 def _candidates(self,base):
  center=(base.rsi_oversold_threshold,base.bollinger_lower_threshold,base.adx_trend_strength_threshold,base.stochastic_oversold_threshold);values=[center]
  deltas=[('rsi',-2.5),('rsi',2.5),('boll',-.05),('boll',.05),('adx',-5),('adx',5),('stoch',-5),('stoch',5)]
  for name,d in deltas:
   r,b,a,s=center
   if name=='rsi':r+=d
   if name=='boll':b+=d
   if name=='adx':a+=d
   if name=='stoch':s+=d
   values.append((r,b,a,s))
  # combine promising directional relaxations/tightenings without exploding search space
  for dr,db,da,ds in [(-2.5,-.05,5,-5),(2.5,.05,-5,5),(-2.5,0,5,0),(2.5,0,-5,0),(0,-.05,0,-5),(0,.05,0,5)]:values.append((center[0]+dr,center[1]+db,center[2]+da,center[3]+ds))
  return list(dict.fromkeys(values))
 def _evaluate(self,symbol,base_name,p,prices,indicators):
  rsi,boll,adx,stoch=p;signals=[]
  for x in indicators:
   price=prices.get(x.trading_date)
   if not price or x.rsi_14 is None or x.adx is None or x.stoch_k is None or price.bollinger_lower is None or price.bollinger_upper is None:continue
   width=price.bollinger_upper-price.bollinger_lower;position=(price.close_price-price.bollinger_lower)/width if width else 1
   if x.rsi_14<=rsi and position<=boll and x.adx>=adx and x.stoch_k<=stoch:signals.append((x.trading_date,price.close_price))
  periods=[]
  for d,entry in signals:
   if periods and (__import__('datetime').date.fromisoformat(d)-__import__('datetime').date.fromisoformat(periods[-1][0])).days<=4:continue
   future=[q for q in prices.values() if q.trading_date>d and (__import__('datetime').date.fromisoformat(q.trading_date)-__import__('datetime').date.fromisoformat(d)).days<=60]
   complete=bool(future) and (__import__('datetime').date.fromisoformat(max(q.trading_date for q in prices.values()))-__import__('datetime').date.fromisoformat(d)).days>=60
   if not complete:continue
   hit=next((q for q in future if (q.high_price if q.high_price is not None else q.close_price)>=entry*1.08),None);draw=min((((q.low_price if q.low_price is not None else q.close_price)-entry)/entry*100 for q in future),default=0);days=(__import__('datetime').date.fromisoformat(hit.trading_date)-__import__('datetime').date.fromisoformat(d)).days if hit else None;periods.append((d,bool(hit),days,draw))
  n=len(periods);hits=sum(x[1] for x in periods);rate=hits/n if n else 0;coverage=len(signals)/len(indicators) if indicators else 0;med=median([x[2] for x in periods if x[2] is not None]) if hits else None;dd=mean(x[3] for x in periods) if periods else None
  # multi-criteria: quality dominates, but tiny samples are penalized and coverage rewarded moderately
  sample_factor=min(1,n/20);score=100*(.55*rate+.20*sample_factor+.15*min(1,coverage/.08)+.10*max(0,min(1,(dd+12)/12 if dd is not None else 0)))
  cid=sha1(f'{symbol}|{base_name}|{p}'.encode()).hexdigest()[:12]
  return FittedProfileCandidate(cid,symbol.upper(),base_name,rsi,ProfileRepository().get_by_name(base_name).rsi_overbought_threshold,boll,adx,stoch,n,hits,rate,len(signals),coverage,med,dd,score,'CANDIDATE')
