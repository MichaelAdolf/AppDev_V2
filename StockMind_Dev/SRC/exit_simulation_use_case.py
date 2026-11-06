from datetime import date,timedelta
from statistics import mean,median
from stockmind.domain.exit.exit_simulation_result import ExitSimulationResult,ExitStrategySummary

class ExitSimulationUseCase:
    def simulate(self,period,prices,opportunities,strategy):
        points=[p for p in prices if p.trading_date>=period.start_date and p.trading_date<= (date.fromisoformat(period.start_date)+timedelta(days=strategy.max_holding_days)).isoformat()]
        if not points:return None
        entry=float(period.entry_price);peak=entry;min_price=entry;target=entry*(1+strategy.target_pct);target_seen=False;exit_point=points[-1];reason='TIME_LIMIT'
        opp={x.trading_date:x for x in opportunities};entry_opp=opp.get(period.start_date);entry_score=entry_opp.opportunity_score if entry_opp else None;entry_conf=entry_opp.confidence if entry_opp else None
        for point in points:
            close=float(point.close_price);peak=max(peak,close);min_price=min(min_price,close);days=(date.fromisoformat(point.trading_date)-date.fromisoformat(period.start_date)).days
            if close>=target:target_seen=True;exit_point=point;reason='TARGET_REACHED';break
            if strategy.stop_loss_pct is not None and close<=entry*(1-strategy.stop_loss_pct):exit_point=point;reason='STOP_LOSS';break
            if strategy.trailing_stop_pct is not None and peak>entry and close<=peak*(1-strategy.trailing_stop_pct):exit_point=point;reason='TRAILING_STOP';break
            current=opp.get(point.trading_date)
            if current:
                if strategy.score_drop is not None and entry_score is not None and current.opportunity_score<=entry_score-strategy.score_drop:exit_point=point;reason='SCORE_DROP';break
                if strategy.confidence_drop is not None and entry_conf is not None and current.confidence<=entry_conf-strategy.confidence_drop:exit_point=point;reason='CONFIDENCE_DROP';break
                if strategy.exit_on_sell and current.signal=='SELL':exit_point=point;reason='SIGNAL_SELL';break
                if strategy.exit_on_hold and current.signal in ('HOLD','SELL'):exit_point=point;reason='SIGNAL_HOLD';break
                if strategy.exit_on_high_risk and current.risk_level=='HIGH':exit_point=point;reason='RISK_HIGH';break
            if days>=strategy.max_holding_days:exit_point=point;reason='TIME_LIMIT';break
        exit_price=float(exit_point.close_price);holding=(date.fromisoformat(exit_point.trading_date)-date.fromisoformat(period.start_date)).days
        return ExitSimulationResult(period.symbol,period.profile_name,period.start_date,strategy.name,exit_point.trading_date,reason,entry,exit_price,(exit_price/entry-1)*100,holding,(peak/entry-1)*100,(min_price/entry-1)*100,target_seen)

    def summarize(self,strategy_name,results):
        valid=[x for x in results if x]
        if not valid:return ExitStrategySummary(strategy_name,0,0,0,0,0,0,0,0,0,0,0)
        returns=[x.return_pct for x in valid];drawdowns=[x.max_drawdown_pct for x in valid]
        return ExitStrategySummary(strategy_name,len(valid),sum(x.return_pct>0 for x in valid),sum(x.target_reached_before_exit for x in valid),sum(x.return_pct>0 for x in valid)/len(valid),sum(x.target_reached_before_exit for x in valid)/len(valid),mean(returns),median(returns),mean(x.holding_days for x in valid),mean(drawdowns),min(returns),max(returns))
