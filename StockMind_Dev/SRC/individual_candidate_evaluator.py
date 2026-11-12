from datetime import date
from hashlib import sha1
from statistics import mean,median
from stockmind.domain.strategy.fitted_profile_candidate import FittedProfileCandidate

class IndividualCandidateEvaluator:
    def evaluate(self,symbol,params,prices,indicators):
        rsi,boll,adx,stoch=params;signals=[]
        for indicator in indicators:
            price=prices.get(indicator.trading_date)
            if not price or None in (indicator.rsi_14,indicator.adx,indicator.stoch_k,price.bollinger_lower,price.bollinger_upper):continue
            width=price.bollinger_upper-price.bollinger_lower
            position=(price.close_price-price.bollinger_lower)/width if width else 1
            if indicator.rsi_14<=rsi and position<=boll and indicator.adx>=adx and indicator.stoch_k<=stoch:
                signals.append((indicator.trading_date,price.close_price))
        periods=[];latest=max(prices) if prices else None
        for trading_date,entry in signals:
            if periods and (date.fromisoformat(trading_date)-date.fromisoformat(periods[-1][0])).days<=4:continue
            if not latest or (date.fromisoformat(latest)-date.fromisoformat(trading_date)).days<60:continue
            future=[point for point in prices.values() if point.trading_date>trading_date and (date.fromisoformat(point.trading_date)-date.fromisoformat(trading_date)).days<=60]
            hit=next((point for point in future if (point.high_price if point.high_price is not None else point.close_price)>=entry*1.08),None)
            drawdown=min((((point.low_price if point.low_price is not None else point.close_price)-entry)/entry*100 for point in future),default=0)
            days=(date.fromisoformat(hit.trading_date)-date.fromisoformat(trading_date)).days if hit else None
            periods.append((trading_date,bool(hit),days,drawdown))
        complete=len(periods);hits=sum(item[1] for item in periods);hit_rate=hits/complete if complete else 0;coverage=len(signals)/len(indicators) if indicators else 0
        median_days=median([item[2] for item in periods if item[2] is not None]) if hits else None
        avg_drawdown=mean(item[3] for item in periods) if periods else None
        sample_factor=min(1,complete/20);coverage_factor=min(1,coverage/.08);drawdown_factor=max(0,min(1,(avg_drawdown+12)/12 if avg_drawdown is not None else 0));speed_factor=max(0,1-(median_days or 60)/60)
        score=100*(.45*hit_rate+.20*sample_factor+.15*coverage_factor+.10*drawdown_factor+.10*speed_factor)
        candidate_id=sha1(f'{symbol}|INDIVIDUAL|{params}'.encode()).hexdigest()[:12]
        return FittedProfileCandidate(candidate_id,symbol.upper(),'balanced',rsi,70.0,boll,adx,stoch,complete,hits,hit_rate,len(signals),coverage,median_days,avg_drawdown,score,'CANDIDATE')
