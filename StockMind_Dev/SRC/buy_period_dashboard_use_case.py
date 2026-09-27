from datetime import date
from statistics import median
from stockmind.application.dashboard.models.buy_period_dashboard_result import BuyPeriodDashboardResult, BuyPeriodStatistics, TargetTimeBucket
from stockmind.domain.history.historical_outcome import HistoricalOutcome
from stockmind.infrastructure.history.buy_period_repository import BuyPeriodRepository


class BuyPeriodDashboardUseCase:
    def load(self, symbol: str, profile_name: str="balanced", analysis_period: str="5y", max_gap_days: int=3) -> BuyPeriodDashboardResult:
        periods=BuyPeriodRepository().load_by_symbol(symbol,profile_name,analysis_period)
        complete=[p for p in periods if p.is_complete]
        incomplete=[p for p in periods if not p.is_complete]
        successful=[p for p in complete if p.outcome==HistoricalOutcome.TARGET_HIT.value]
        failed=[p for p in complete if p.outcome!=HistoricalOutcome.TARGET_HIT.value]
        count=lambda o:sum(1 for p in complete if p.outcome==o.value)
        days=[p.days_to_target for p in successful if p.days_to_target is not None]
        durations=[p.calendar_duration_days for p in complete]
        buckets=[]
        for label,lo,hi in (("0-15",0,15),("16-30",16,30),("31-45",31,45),("46-60",46,60)):
            value=sum(1 for d in days if lo<=d<=hi)
            buckets.append(TargetTimeBucket(label,value,self._rate(value,len(days))))
        stats=BuyPeriodStatistics(
            complete_period_count=len(complete), incomplete_period_count=len(incomplete),
            target_hit_count=len(successful), below_target_count=count(HistoricalOutcome.BELOW_TARGET),
            flat_count=count(HistoricalOutcome.FLAT), negative_count=count(HistoricalOutcome.NEGATIVE),
            target_hit_rate=self._rate(len(successful),len(complete)),
            below_target_rate=self._rate(count(HistoricalOutcome.BELOW_TARGET),len(complete)),
            flat_rate=self._rate(count(HistoricalOutcome.FLAT),len(complete)),
            negative_rate=self._rate(count(HistoricalOutcome.NEGATIVE),len(complete)),
            average_days_to_target=self._average(days), median_days_to_target=self._median(days),
            fastest_days_to_target=min(days) if days else None, slowest_days_to_target=max(days) if days else None,
            target_time_buckets=buckets,
            average_calendar_duration_days=self._average([p.calendar_duration_days for p in periods]),
            median_calendar_duration_days=self._median(durations), duration_q25_days=self._percentile(durations,.25),
            duration_q75_days=self._percentile(durations,.75),
            average_buy_signal_count=self._average([p.buy_signal_count for p in periods]),
            average_max_gain_pct=self._average([p.max_gain_pct for p in complete if p.max_gain_pct is not None]),
            average_max_drawdown_pct=self._average([p.max_drawdown_pct for p in complete if p.max_drawdown_pct is not None]),
            median_max_drawdown_pct=self._median([p.max_drawdown_pct for p in complete if p.max_drawdown_pct is not None]),
            successful_average_max_gain_pct=self._average([p.max_gain_pct for p in successful if p.max_gain_pct is not None]),
            successful_average_max_drawdown_pct=self._average([p.max_drawdown_pct for p in successful if p.max_drawdown_pct is not None]),
            failed_average_max_gain_pct=self._average([p.max_gain_pct for p in failed if p.max_gain_pct is not None]),
            failed_average_max_drawdown_pct=self._average([p.max_drawdown_pct for p in failed if p.max_drawdown_pct is not None]),
            sample_quality=self._sample_quality(len(complete)),
        )
        active=self._active_period(periods,max_gap_days)
        return BuyPeriodDashboardResult(symbol.upper(),profile_name,analysis_period,max_gap_days,len(periods),stats,active,self._phase(active,stats),periods)
    def _active_period(self,periods,max_gap_days):
        if not periods:return None
        latest=max(periods,key=lambda x:x.end_date)
        return latest if (date.today()-date.fromisoformat(latest.end_date)).days-1<=max_gap_days else None
    def _phase(self,active,stats):
        if not active or not stats.complete_period_count:return "KEINE VERGLEICHSDATEN"
        d=active.calendar_duration_days
        if d<stats.duration_q25_days:return "FRÜHER BEREICH"
        if d>stats.duration_q75_days:return "SPÄTER BEREICH"
        return "TYPISCHER BEREICH"
    def _rate(self,n,d):return n/d if d else 0.0
    def _average(self,v):return sum(v)/len(v) if v else 0.0
    def _median(self,v):return float(median(v)) if v else 0.0
    def _percentile(self,v,q):
        if not v:return 0.0
        values=sorted(v);pos=(len(values)-1)*q;lo=int(pos);hi=min(lo+1,len(values)-1);w=pos-lo
        return values[lo]*(1-w)+values[hi]*w
    def _sample_quality(self,n):
        return "HIGH" if n>=50 else "MEDIUM" if n>=20 else "LOW" if n else "NO_SAMPLE"
