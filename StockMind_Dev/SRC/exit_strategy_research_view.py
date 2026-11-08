import pandas as pd
import streamlit as st
from stockmind.application.exit.cross_stock_exit_validation_use_case import CrossStockExitValidationUseCase
from stockmind.application.exit.exit_research_validation_use_case import ExitResearchValidationUseCase
from stockmind.application.exit.exit_strategy_research_use_case import ExitStrategyResearchUseCase
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository

def render():
 st.subheader('Exit Strategy Research');st.caption('Research, Out-of-Sample-Validierung und Cross-Stock-Robustheit. Keine Strategie wird dadurch produktiv aktiviert.')
 stocks=[x for x in WatchlistRepository().load_all() if x.active];labels={f'{x.company_name} ({x.symbol})':x.symbol for x in stocks}
 if not labels:st.info('Keine aktiven Watchlist-Aktien.');return
 c1,c2=st.columns(2);label=c1.selectbox('Aktie',list(labels),key='exit_research_symbol');profile=c2.selectbox('Profil',['conservative','balanced','aggressive'],index=1,key='exit_research_profile');symbol=labels[label]
 if not ChartDataRepository().has_complete_ohlc(symbol):st.warning('Für diese Aktie ist die OHLC-Historie nicht vollständig.')
 research_tab,validation_tab,cross_tab=st.tabs(['Research','Validation & Walk-Forward','Cross-Stock Validation'])
 with research_tab:
  if st.button('Exit-Strategien vergleichen',type='primary',key='run_exit_research'):
   with st.spinner('Historische Exit-Szenarien werden ausgewertet...'):r=ExitStrategyResearchUseCase().analyze(symbol,profile)
   st.metric('Vollständige BUY-Perioden',r['period_count']);st.dataframe(pd.DataFrame([{'Strategie':x.strategy_name,'Fälle':x.sample_count,'Positive Rate %':round(x.positive_rate*100,1),'Target vor Exit %':round(x.target_reached_rate*100,1),'Ø Return %':round(x.average_return_pct,2),'Median Return %':round(x.median_return_pct,2),'Ø Tage':round(x.average_holding_days,1),'Ø Drawdown %':round(x.average_max_drawdown_pct,2),'Worst %':round(x.worst_return_pct,2),'Best %':round(x.best_return_pct,2)} for x in r['summaries']]),width='stretch',hide_index=True)
 with validation_tab:
  if st.button('Out-of-Sample validieren',type='primary',key='run_exit_validation'):
   with st.spinner('Train-/Validation-Split wird ausgewertet...'):r=ExitResearchValidationUseCase().validate(symbol,profile)
   a,b,c=st.columns(3);a.metric('Gesamtperioden',r['period_count']);b.metric('Train',r['train_count']);c.metric('Validation',r['validation_count'])
   if not r['sufficient_sample']:st.warning('Stichprobe unter 12 Train- und 5 Validation-Perioden. Nur explorativ.')
   st.dataframe(pd.DataFrame([{'Strategie':x.strategy_name,'Status':x.robustness_status,'Train Fälle':x.train_sample_count,'Validation Fälle':x.validation_sample_count,'Train Ø Return %':round(x.train_average_return_pct,2),'Validation Ø Return %':round(x.validation_average_return_pct,2),'Return Δ':round(x.return_degradation_pct,2),'Train Positive %':round(x.train_positive_rate*100,1),'Validation Positive %':round(x.validation_positive_rate*100,1),'Validation Drawdown %':round(x.validation_average_drawdown_pct,2)} for x in r['rows']]),width='stretch',hide_index=True)
   st.subheader('Walk-Forward')
   if r['walk_forward']:st.dataframe(pd.DataFrame([{'Fold':x.fold_number,'Train':f'{x.train_start} bis {x.train_end}','Validation':f'{x.validation_start} bis {x.validation_end}','Gewählte Strategie':x.strategy_name,'Train Ø Return %':round(x.train_average_return_pct,2),'Validation Ø Return %':round(x.validation_average_return_pct,2),'Validation Positive %':round(x.validation_positive_rate*100,1),'Validation Fälle':x.validation_sample_count} for x in r['walk_forward']]),width='stretch',hide_index=True)
   else:st.info('Für Walk-Forward sind mindestens 17 vollständige BUY-Perioden erforderlich.')
 with cross_tab:
  st.write('Vergleicht dieselben Exitstrategien über alle aktiven Watchlist-Aktien für das gewählte Profil.')
  if st.button('Cross-Stock Validation starten',type='primary',key='run_cross_stock'):
   with st.spinner('Alle aktiven Aktien werden validiert. Das kann etwas dauern...'):r=CrossStockExitValidationUseCase().analyze(profile)
   a,b=st.columns(2);a.metric('Aktive Aktien',r['active_stock_count']);b.metric('Ausreichende Stichprobe',r['eligible_stock_count'])
   st.dataframe(pd.DataFrame([{'Strategie':x.strategy_name,'Status':x.recommendation_status,'Robustness Score':round(x.robustness_score,1),'Aktien bewertet':x.eligible_stock_count,'Stable':x.stable_stock_count,'Stable %':round(x.stable_rate*100,1),'Degraded':x.degraded_stock_count,'Failed':x.failed_stock_count,'Insufficient':x.insufficient_stock_count,'Ø Validation Return %':round(x.average_validation_return_pct,2),'Median Validation Return %':round(x.median_validation_return_pct,2),'Ø Validation Positive %':round(x.average_validation_positive_rate*100,1),'Ø Drawdown %':round(x.average_validation_drawdown_pct,2),'Worst Aktie Return %':round(x.worst_stock_validation_return_pct,2),'Ø Degradation':round(x.average_return_degradation_pct,2),'WF positive Folds %':round(x.walk_forward_positive_fold_rate*100,1)} for x in r['summaries']]),width='stretch',hide_index=True)
   selected=st.selectbox('Strategie im Aktienvergleich',[x.strategy_name for x in r['summaries']],key='cross_strategy_detail');detail=[x for x in r['stock_rows'] if x.strategy_name==selected]
   st.dataframe(pd.DataFrame([{'Aktie':f'{x.company_name} ({x.symbol})','Status':x.robustness_status,'Train Fälle':x.train_sample_count,'Validation Fälle':x.validation_sample_count,'Validation Return %':round(x.validation_average_return_pct,2),'Positive %':round(x.validation_positive_rate*100,1),'Drawdown %':round(x.validation_average_drawdown_pct,2),'Degradation':round(x.return_degradation_pct,2)} for x in detail]),width='stretch',hide_index=True)
   st.info('ROBUST_CANDIDATE erfordert mindestens 3 Aktien mit ausreichender Stichprobe, mindestens 60 % STABLE, positiven Ø Validation Return und einen Worst-Aktien-Return über -5 %. Noch keine produktive Exitfreigabe.')
