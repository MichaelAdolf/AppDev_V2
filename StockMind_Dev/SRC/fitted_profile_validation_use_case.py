from datetime import date,datetime
from statistics import mean,median
from stockmind.application.strategy.models.fitted_profile_validation_result import FittedProfileValidationMetrics,FittedProfileValidationResult,FittedProfileWalkForwardFold
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository
from stockmind.infrastructure.history.indicator_chart_data_repository import IndicatorChartDataRepository
from stockmind.infrastructure.profiles.profile_repository import ProfileRepository
from stockmind.infrastructure.strategy.fitted_profile_repository import FittedProfileRepository
class FittedProfileValidationUseCase:
 MIN_TRAIN=12;MIN_VALIDATION=5
 def __init__(self,database_path=None):self._database_path=database_path
 def validate(self,profile_id):
  repo=FittedProfileRepository(self._database_path);p=repo.load(profile_id)
  if not p:raise ValueError('Fitted Profile wurde nicht gefunden.')
  prices={x.trading_date:x for x in ChartDataRepository(self._database_path).load_by_symbol(p.symbol)};indicators=IndicatorChartDataRepository(self._database_path).load_by_symbol(p.symbol);dates=sorted(prices);split=dates[int(len(dates)*.70)] if dates else ''
  fitted_params=(p.rsi_oversold_threshold,p.bollinger_lower_threshold,p.adx_trend_strength_threshold,p.stochastic_oversold_threshold);base=ProfileRepository().get_by_name(p.base_profile);base_params=(base.rsi_oversold_threshold,base.bollinger_lower_threshold,base.adx_trend_strength_threshold,base.stochastic_oversold_threshold)
  train=self._metrics(fitted_params,prices,[x for x in indicators if x.trading_date<split]);validation=self._metrics(fitted_params,prices,[x for x in indicators if x.trading_date>=split]);benchmark=self._metrics(base_params,prices,[x for x in indicators if x.trading_date>=split]);degradation=validation.target_hit_rate-train.target_hit_rate;advantage=validation.target_hit_rate-benchmark.target_hit_rate;folds=self._walk_forward(fitted_params,prices,indicators);stable=sum(x.validation_target_hit_rate>=max(0,x.train_target_hit_rate-.15) and x.validation_sample_count>=2 for x in folds);fold_rate=stable/len(folds) if folds else 0;reasons=[]
  if train.sample_count<self.MIN_TRAIN or validation.sample_count<self.MIN_VALIDATION:status='INSUFFICIENT_SAMPLE';reasons.append('MIN_SAMPLE_NOT_REACHED')
  elif validation.target_hit_rate<=0:status='FAILED';reasons.append('VALIDATION_NOT_POSITIVE')
  elif degradation<-.15:status='DEGRADED';reasons.append('TRAIN_VALIDATION_COLLAPSE')
  elif advantage<-.05:status='DEGRADED';reasons.append('WORSE_THAN_BASE_PROFILE')
  elif folds and fold_rate<.5:status='DEGRADED';reasons.append('WALK_FORWARD_UNSTABLE')
  else:status='VALIDATED';reasons.append('VALIDATION_CRITERIA_MET')
  repo.update_status(p.id,status);repo.save_validation(p.id,status,train.sample_count,validation.sample_count,train.target_hit_rate,validation.target_hit_rate,benchmark.target_hit_rate,fold_rate,reasons,datetime.now().isoformat(timespec='seconds'))
  return FittedProfileValidationResult(p.id,p.symbol,p.version,p.base_profile,status,train,validation,benchmark,degradation,advantage,folds,fold_rate,reasons)
 def _signals(self,params,prices,indicators):
  rsi,boll,adx,stoch=params;out=[]
  for x in indicators:
   q=prices.get(x.trading_date)
   if not q or None in (x.rsi_14,x.adx,x.stoch_k,q.bollinger_lower,q.bollinger_upper):continue
   width=q.bollinger_upper-q.bollinger_lower;position=(q.close_price-q.bollinger_lower)/width if width else 1
   if x.rsi_14<=rsi and position<=boll and x.adx>=adx and x.stoch_k<=stoch:out.append((x.trading_date,q.close_price))
  return out
 def _metrics(self,params,prices,indicators):
  signals=self._signals(params,prices,indicators);periods=[];latest=max(prices) if prices else ''
  for d,entry in signals:
   if periods and (date.fromisoformat(d)-date.fromisoformat(periods[-1][0])).days<=4:continue
   if not latest or (date.fromisoformat(latest)-date.fromisoformat(d)).days<60:continue
   future=[q for q in prices.values() if d<q.trading_date and (date.fromisoformat(q.trading_date)-date.fromisoformat(d)).days<=60];hit=next((q for q in future if (q.high_price if q.high_price is not None else q.close_price)>=entry*1.08),None);draw=min((((q.low_price if q.low_price is not None else q.close_price)-entry)/entry*100 for q in future),default=0);days=(date.fromisoformat(hit.trading_date)-date.fromisoformat(d)).days if hit else None;periods.append((d,bool(hit),days,draw))
  n=len(periods);hits=sum(x[1] for x in periods);days=[x[2] for x in periods if x[2] is not None];return FittedProfileValidationMetrics(n,hits,hits/n if n else 0,len(signals),len(signals)/len(indicators) if indicators else 0,median(days) if days else None,mean(x[3] for x in periods) if periods else None)
 def _walk_forward(self,params,prices,indicators):
  dates=sorted({x.trading_date for x in indicators});folds=[]
  if len(dates)<400:return folds
  for i,ratio in enumerate((.55,.65,.75),1):
   split=dates[int(len(dates)*ratio)];end_index=min(len(dates)-1,int(len(dates)*(ratio+.10)));end=dates[end_index];train_i=[x for x in indicators if x.trading_date<split];val_i=[x for x in indicators if split<=x.trading_date<=end];tr=self._metrics(params,prices,train_i);va=self._metrics(params,prices,val_i);folds.append(FittedProfileWalkForwardFold(i,dates[0],split,split,end,tr.target_hit_rate,va.target_hit_rate,va.sample_count))
  return folds
