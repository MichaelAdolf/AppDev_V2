import pandas as pd
import streamlit as st
from stockmind.application.strategy.cross_stock_profile_validation_use_case import CrossStockProfileValidationUseCase
from stockmind.application.strategy.fitted_profile_candidate_use_case import SaveFittedProfileCandidateUseCase
from stockmind.application.strategy.fitted_profile_search_use_case import FittedProfileSearchUseCase
from stockmind.application.strategy.profile_validation_use_case import ProfileValidationUseCase
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository

def render():
 st.subheader('Entry Strategy Research');st.caption('Standardprofile bleiben unverändert. Fitted erzeugt aktienspezifische Kandidaten, aber aktiviert sie noch nicht.')
 stocks=[x for x in WatchlistRepository().load_all() if x.active];labels={f'{x.company_name} ({x.symbol})':x.symbol for x in stocks}
 if not labels:st.info('Keine aktiven Watchlist-Aktien.');return
 single,cross,fitted=st.tabs(['Standardprofile Einzelaktie','Standardprofile Cross-Stock','Fitted Candidate Search'])
 with single:
  label=st.selectbox('Aktie',list(labels),key='entry_validation_symbol')
  if st.button('Profile für Aktie validieren',type='primary'):
   r=ProfileValidationUseCase().analyze(labels[label]);st.dataframe(pd.DataFrame([{'Profil':x.profile_name,'Rollen-Fit':x.profile_role_status,'Perioden':x.period_count,'Vollständig':x.complete_period_count,'Target Hit %':round(x.target_hit_rate*100,1),'Negative %':round(x.negative_rate*100,1),'Median Tage':x.median_days_to_target,'Ø Drawdown %':round(x.average_max_drawdown_pct,2) if x.average_max_drawdown_pct is not None else None,'Coverage %':round(x.signal_coverage_rate*100,2),'Sample':x.sample_quality} for x in r.rows]),width='stretch',hide_index=True)
 with cross:
  if st.button('Profile über Watchlist validieren',type='primary'):
   rows=CrossStockProfileValidationUseCase().analyze();st.dataframe(pd.DataFrame([{'Profil':x.profile_name,'Soll-Rolle':x.intended_role,'Rollen-Fit':x.role_fit_status,'Vollständige Perioden':x.total_complete_periods,'Target Hit %':round(x.weighted_target_hit_rate*100,1),'Ø Perioden/Aktie':round(x.average_periods_per_stock,1),'Coverage %':round(x.average_signal_coverage_rate*100,2)} for x in rows]),width='stretch',hide_index=True)
 with fitted:
  label=st.selectbox('Aktie für Fitting',list(labels),key='fitted_symbol');base=st.selectbox('Ausgangsprofil',['conservative','balanced','aggressive'],index=1);limit=st.slider('Maximale Kandidaten',5,25,15)
  if st.button('Fitted Candidates suchen',type='primary'):
   with st.spinner('Parameterkandidaten werden auf historischen Indikatoren bewertet...'):rows=FittedProfileSearchUseCase().search(labels[label],base,limit)
   st.session_state['fitted_rows']=rows
  rows=st.session_state.get('fitted_rows',[])
  if rows:
   st.dataframe(pd.DataFrame([{'ID':x.candidate_id,'RSI':x.rsi_oversold_threshold,'Bollinger':x.bollinger_lower_threshold,'ADX':x.adx_trend_strength_threshold,'Stochastic':x.stochastic_oversold_threshold,'Perioden':x.complete_period_count,'Target Hit %':round(x.target_hit_rate*100,1),'Coverage %':round(x.coverage_rate*100,2),'Median Tage':x.median_days_to_target,'Ø Drawdown %':round(x.average_drawdown_pct,2) if x.average_drawdown_pct is not None else None,'Objective':round(x.objective_score,1)} for x in rows]),width='stretch',hide_index=True)
   chosen=st.selectbox('Kandidat speichern',[x.candidate_id for x in rows]);candidate=next(x for x in rows if x.candidate_id==chosen)
   if st.button('Als FITTED_CANDIDATE speichern'):p=SaveFittedProfileCandidateUseCase().execute(candidate);st.success(f'{p.symbol} Fitted v{p.version} als CANDIDATE gespeichert.')
   st.info('Speichern aktiviert den Kandidaten nicht. Train/Validation und Walk-Forward folgen im nächsten Sprint.')
