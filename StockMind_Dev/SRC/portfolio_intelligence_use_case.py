from datetime import date
from stockmind.application.portfolio.models.portfolio_intelligence_result import PortfolioIntelligenceItem
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository
from stockmind.infrastructure.history.latest_analysis_repository import LatestAnalysisRepository
from stockmind.infrastructure.portfolio.portfolio_repository import PortfolioRepository

class PortfolioIntelligenceUseCase:
    TARGET_RETURN = 0.08
    STRATEGY_DAYS = 60
    TIME_WARNING_DAY = 46
    SCORE_DETERIORATION = 10.0
    CONFIDENCE_DETERIORATION = 0.15

    def __init__(self,database_path=None):self._database_path=database_path
    def load(self):
        repo=PortfolioRepository(self._database_path);chart=ChartDataRepository(self._database_path)
        latest={p:{x.symbol.upper():x for x in LatestAnalysisRepository(self._database_path).load_all(p)} for p in ('conservative','balanced','aggressive')}
        items=[]
        for pos in repo.load_open_positions():
            lots=repo.load_lots_for_position(pos.id);points=chart.load_by_symbol(pos.symbol);price=points[-1].close_price if points else None
            current=latest.get(pos.entry_profile,{}).get(pos.symbol.upper());invested=pos.purchase_price*pos.quantity+pos.purchase_fees;value=price*pos.quantity if price is not None else None;profit=value-invested if value is not None else None;ret=profit/invested if profit is not None and invested else None;target=pos.purchase_price*(1+self.TARGET_RETURN);distance=target/price-1 if price else None;days=(date.today()-date.fromisoformat(pos.purchase_date)).days;remaining=max(0,self.STRATEGY_DAYS-days)
            status='WINDOW_EXCEEDED' if days>=self.STRATEGY_DAYS else 'WINDOW_NEAR_END' if days>=self.TIME_WARNING_DAY else 'IN_WINDOW'
            score=current.opportunity_score if current else None;confidence=current.confidence if current else None;risk=current.risk_level if current else None;signal=current.signal if current else None
            score_change=(score-pos.entry_opportunity_score) if score is not None and pos.entry_opportunity_score is not None else None;confidence_change=(confidence-pos.entry_confidence) if confidence is not None and pos.entry_confidence is not None else None
            reasons=[]
            if ret is not None and ret>=self.TARGET_RETURN:reasons.append('TARGET_REACHED')
            if status=='WINDOW_NEAR_END':reasons.append('TIME_WINDOW_NEAR_END')
            if status=='WINDOW_EXCEEDED':reasons.append('TIME_WINDOW_EXCEEDED')
            if score_change is not None and score_change<=-self.SCORE_DETERIORATION:reasons.append('SCORE_DETERIORATED')
            if confidence_change is not None and confidence_change<=-self.CONFIDENCE_DETERIORATION:reasons.append('CONFIDENCE_DETERIORATED')
            if pos.entry_risk and risk and pos.entry_risk!='HIGH' and risk=='HIGH':reasons.append('RISK_INCREASED')
            if pos.entry_signal=='BUY' and signal and signal!='BUY':reasons.append('SIGNAL_CHANGED_FROM_BUY')
            critical={'TARGET_REACHED','TIME_WINDOW_EXCEEDED'};warning={'TIME_WINDOW_NEAR_END','SCORE_DETERIORATED','CONFIDENCE_DETERIORATED','RISK_INCREASED','SIGNAL_CHANGED_FROM_BUY'}
            level='CRITICAL' if critical.intersection(reasons) else 'ATTENTION' if warning.intersection(reasons) else 'NORMAL'
            items.append(PortfolioIntelligenceItem(pos.id,pos.symbol,pos.company_name,lots,pos.quantity,pos.purchase_price,pos.purchase_fees,invested,price,value,profit,ret,target,ret is not None and ret>=self.TARGET_RETURN,distance,pos.purchase_date,days,remaining,status,pos.entry_profile,pos.entry_opportunity_score,score,score_change,pos.entry_confidence,confidence,confidence_change,pos.entry_risk,risk,pos.entry_signal,signal,reasons,level))
        priority={'CRITICAL':2,'ATTENTION':1,'NORMAL':0};return sorted(items,key=lambda x:(priority[x.attention_level],x.unrealized_return_pct if x.unrealized_return_pct is not None else -999),reverse=True)
