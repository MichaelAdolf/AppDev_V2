import pandas as pd
import streamlit as st
from stockmind.application.strategy.activate_fitted_profile_use_case import ActivateFittedProfileUseCase,DeactivateFittedProfileUseCase
from stockmind.application.strategy.cross_stock_profile_validation_use_case import CrossStockProfileValidationUseCase
from stockmind.application.strategy.fitted_profile_candidate_use_case import SaveFittedProfileCandidateUseCase
from stockmind.application.strategy.fitted_profile_search_use_case import FittedProfileSearchUseCase
from stockmind.application.strategy.fitted_profile_signal_use_case import FittedProfileSignalUseCase
from stockmind.application.strategy.fitted_profile_validation_use_case import FittedProfileValidationUseCase
from stockmind.application.strategy.profile_validation_use_case import ProfileValidationUseCase
from stockmind.infrastructure.strategy.fitted_profile_repository import FittedProfileRepository
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository

def render():
 st.subheader('Entry Strategy Research');st.caption('Standardprofile bleiben unverändert. Nur VALIDATED Fitted Profiles können manuell aktiviert werden.')
 stocks=[x for x in WatchlistRepository().load_all() if x.active];labels={f'{x.company_name} ({x.symbol})':x.symbol for x in stocks}
 if not labels:st.info('Keine aktiven Watchlist-Aktien.');return
 single,cross,fitted,validation,activation=st.tabs(['Standardprofile Einzelaktie','Standardprofile Cross-Stock','Fitted Candidate Search','Fitted Candidate Validation','Fitted Activation'])
 with single:
  label=st.selectbox('Aktie',list(labels),key='entry_validation_symbol')
  if st.button('Profile für Aktie validieren',type='primary'):r=ProfileValidationUseCase().analyze(labels[label]);st.dataframe(pd.DataFrame([{'Profil':x.profile_name,'Rollen-Fit':x.profile_role_status,'Perioden':x.period_count,'Target Hit %':round(x.target_hit_rate*100,1),'Coverage %':round(x.signal_coverage_rate*100,2),'Sample':x.sample_quality} for x in r.rows]),width='stretch',hide_index=True)
 with cross:
  if st.button('Profile über Watchlist validieren',type='primary'):rows=CrossStockProfileValidationUseCase().analyze();st.dataframe(pd.DataFrame([{'Profil':x.profile_name,'Rollen-Fit':x.role_fit_status,'Vollständige Perioden':x.total_complete_periods,'Target Hit %':round(x.weighted_target_hit_rate*100,1),'Coverage %':round(x.average_signal_coverage_rate*100,2)} for x in rows]),width='stretch',hide_index=True)
 with fitted:
  label=st.selectbox('Aktie für Fitting',list(labels),key='fitted_symbol');base=st.selectbox('Ausgangsprofil',['conservative','balanced','aggressive'],index=1);limit=st.slider('Maximale Kandidaten',5,25,15)
  if st.button('Fitted Candidates suchen',type='primary'):st.session_state['fitted_rows']=FittedProfileSearchUseCase().search(labels[label],base,limit)
  rows=st.session_state.get('fitted_rows',[])
  if rows:
   st.dataframe(pd.DataFrame([{'ID':x.candidate_id,'RSI':x.rsi_oversold_threshold,'Bollinger':x.bollinger_lower_threshold,'ADX':x.adx_trend_strength_threshold,'Stochastic':x.stochastic_oversold_threshold,'Perioden':x.complete_period_count,'Target Hit %':round(x.target_hit_rate*100,1),'Coverage %':round(x.coverage_rate*100,2),'Objective':round(x.objective_score,1)} for x in rows]),width='stretch',hide_index=True);chosen=st.selectbox('Kandidat speichern',[x.candidate_id for x in rows]);candidate=next(x for x in rows if x.candidate_id==chosen)
   if st.button('Als FITTED_CANDIDATE speichern'):p=SaveFittedProfileCandidateUseCase().execute(candidate);st.success(f'{p.symbol} Fitted v{p.version} gespeichert.')
 with validation:
  label=st.selectbox('Aktie mit gespeicherten Kandidaten',list(labels),key='validation_symbol');profiles=FittedProfileRepository().load_by_symbol(labels[label]);candidates=[x for x in profiles if x.status!='ACTIVE']
  if candidates:
   names={f'{x.symbol} Fitted v{x.version} · {x.status}':x.id for x in candidates};selected=st.selectbox('Kandidat',list(names))
   if st.button('Kandidat validieren',type='primary'):
    r=FittedProfileValidationUseCase().validate(names[selected]);st.success(f'Status: {r.status}');st.dataframe(pd.DataFrame([{'Bereich':'Train','Fälle':r.train.sample_count,'Target Hit %':round(r.train.target_hit_rate*100,1)},{'Bereich':'Validation','Fälle':r.validation.sample_count,'Target Hit %':round(r.validation.target_hit_rate*100,1)},{'Bereich':f'Benchmark {r.base_profile}','Fälle':r.benchmark_validation.sample_count,'Target Hit %':round(r.benchmark_validation.target_hit_rate*100,1)}]),width='stretch',hide_index=True)
  else:st.info('Keine Kandidaten vorhanden.')
 with activation:
  label=st.selectbox('Aktie für Aktivierung',list(labels),key='activation_symbol');symbol=labels[label];repo=FittedProfileRepository();profiles=repo.load_by_symbol(symbol);active=repo.load_active(symbol);validated=[x for x in profiles if x.status=='VALIDATED']
  if active:
   signal=FittedProfileSignalUseCase().evaluate(symbol);st.success(f'Aktiv: {signal.strategy_name} · aktuelles Signal {signal.signal}');st.caption(f'Basis: {signal.base_profile} · erfüllte Bedingungen {signal.matched_conditions}/{signal.required_conditions}')
   if st.button('Aktives Fitted Profile deaktivieren'):DeactivateFittedProfileUseCase().execute(symbol);st.success('Fitted Profile deaktiviert. Standardprofile bleiben aktiv.');st.rerun()
  else:st.info('Für diese Aktie ist kein Fitted Profile aktiv.')
  if validated:
   names={f'{x.symbol} Fitted v{x.version} · VALIDATED':x.id for x in validated};chosen=st.selectbox('Validiertes Profil aktivieren',list(names))
   confirm=st.checkbox('Ich bestätige die manuelle Aktivierung dieses validierten Fitted Profiles.')
   if st.button('Fitted Profile aktivieren',disabled=not confirm):p=ActivateFittedProfileUseCase().execute(names[chosen]);st.success(f'{p.symbol} Fitted v{p.version} ist jetzt ACTIVE.');st.rerun()
  else:st.caption('Keine VALIDATED Kandidaten für die Aktivierung verfügbar.')
