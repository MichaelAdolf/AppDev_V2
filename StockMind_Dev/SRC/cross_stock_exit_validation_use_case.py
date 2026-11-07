from statistics import mean, median
from stockmind.application.exit.exit_research_validation_use_case import ExitResearchValidationUseCase
from stockmind.application.exit.models.cross_stock_exit_validation_result import CrossStockStrategyRow,StockStrategyValidationRow
from stockmind.domain.exit.exit_strategy import ExitStrategy
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository

class CrossStockExitValidationUseCase:
    PROFILES=('conservative','balanced','aggressive')
    def __init__(self,database_path=None):self._database_path=database_path
    def analyze(self,profile_name='balanced'):
        watch=[x for x in WatchlistRepository(self._database_path).load_all() if x.active];validator=ExitResearchValidationUseCase(self._database_path);stock_rows=[];walks={};eligible=[]
        for entry in watch:
            result=validator.validate(entry.symbol,profile_name);walks[entry.symbol]=result['walk_forward']
            if result['sufficient_sample']:eligible.append(entry.symbol)
            for row in result['rows']:
                stock_rows.append(StockStrategyValidationRow(entry.symbol,entry.company_name,profile_name,row.strategy_name,row.robustness_status,row.train_sample_count,row.validation_sample_count,row.validation_average_return_pct,row.validation_positive_rate,row.validation_average_drawdown_pct,row.return_degradation_pct))
        summaries=[]
        for strategy in ExitStrategy.research_candidates():
            rows=[x for x in stock_rows if x.strategy_name==strategy.name];valid=[x for x in rows if x.robustness_status!='INSUFFICIENT_SAMPLE'];stable=[x for x in valid if x.robustness_status=='STABLE'];degraded=[x for x in valid if x.robustness_status=='DEGRADED'];failed=[x for x in valid if x.robustness_status=='FAILED_VALIDATION'];insufficient=[x for x in rows if x.robustness_status=='INSUFFICIENT_SAMPLE']
            fold_results=[f for folds in walks.values() for f in folds if f.strategy_name==strategy.name];positive_folds=sum(f.validation_average_return_pct>0 for f in fold_results)
            avg_return=mean(x.validation_average_return_pct for x in valid) if valid else 0;med_return=median(x.validation_average_return_pct for x in valid) if valid else 0;avg_positive=mean(x.validation_positive_rate for x in valid) if valid else 0;avg_dd=mean(x.validation_average_drawdown_pct for x in valid) if valid else 0;worst=min((x.validation_average_return_pct for x in valid),default=0);avg_deg=mean(x.return_degradation_pct for x in valid) if valid else 0;stable_rate=len(stable)/len(valid) if valid else 0;fold_rate=positive_folds/len(fold_results) if fold_results else 0
            coverage=len(valid)/len(watch) if watch else 0;score=100*(.35*stable_rate+.20*max(0,min(1,(avg_return+2)/10))+.15*avg_positive+.10*max(0,min(1,(worst+8)/10))+.10*max(0,min(1,(avg_deg+4)/6))+.10*(fold_rate if fold_results else coverage))
            if len(valid)<3:status='INSUFFICIENT_CROSS_STOCK_SAMPLE'
            elif stable_rate>=.60 and avg_return>0 and worst>-5:status='ROBUST_CANDIDATE'
            elif stable_rate>=.40 and avg_return>0:status='PROMISING'
            else:status='NOT_ROBUST'
            summaries.append(CrossStockStrategyRow(profile_name,strategy.name,len(valid),len(stable),len(degraded),len(failed),len(insufficient),stable_rate,avg_return,med_return,avg_positive,avg_dd,worst,avg_deg,len(fold_results),fold_rate,score,status))
        order={'ROBUST_CANDIDATE':3,'PROMISING':2,'NOT_ROBUST':1,'INSUFFICIENT_CROSS_STOCK_SAMPLE':0}
        summaries.sort(key=lambda x:(order[x.recommendation_status],x.robustness_score,x.average_validation_return_pct),reverse=True)
        return {'profile_name':profile_name,'active_stock_count':len(watch),'eligible_stock_count':len(set(eligible)),'summaries':summaries,'stock_rows':stock_rows}
    def analyze_all_profiles(self):return {p:self.analyze(p) for p in self.PROFILES}
