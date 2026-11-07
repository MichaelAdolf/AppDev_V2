import pandas as pd
import streamlit as st
from stockmind.application.strategy.cross_stock_profile_validation_use_case import CrossStockProfileValidationUseCase
from stockmind.application.strategy.profile_validation_use_case import ProfileValidationUseCase
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository

def render():
 st.subheader('Entry Profile Validation');st.caption('Misst, wie Conservative, Balanced und Aggressive heute tatsächlich arbeiten. Noch keine Parameteroptimierung.')
 stocks=[x for x in WatchlistRepository().load_all() if x.active];labels={f'{x.company_name} ({x.symbol})':x.symbol for x in stocks}
 if not labels:st.info('Keine aktiven Watchlist-Aktien.');return
 single,cross=st.tabs(['Einzelaktie','Cross-Stock'])
 with single:
  label=st.selectbox('Aktie',list(labels),key='entry_validation_symbol')
  if st.button('Profile für Aktie validieren',type='primary'):
   r=ProfileValidationUseCase().analyze(labels[label]);st.dataframe(pd.DataFrame([{'Profil':x.profile_name,'Rollen-Fit':x.profile_role_status,'Perioden':x.period_count,'Vollständig':x.complete_period_count,'Target Hit %':round(x.target_hit_rate*100,1),'Below %':round(x.below_target_rate*100,1),'Flat %':round(x.flat_rate*100,1),'Negative %':round(x.negative_rate*100,1),'Median Tage':x.median_days_to_target,'Ø Drawdown %':round(x.average_max_drawdown_pct,2) if x.average_max_drawdown_pct is not None else None,'BUY-Tage':x.buy_signal_days,'Coverage %':round(x.signal_coverage_rate*100,2),'Sample':x.sample_quality} for x in r.rows]),width='stretch',hide_index=True)
 with cross:
  if st.button('Profile über gesamte Watchlist validieren',type='primary'):
   with st.spinner('Profile werden über alle aktiven Aktien ausgewertet...'):rows=CrossStockProfileValidationUseCase().analyze()
   st.dataframe(pd.DataFrame([{'Profil':x.profile_name,'Soll-Rolle':x.intended_role,'Rollen-Fit':x.role_fit_status,'Aktien':x.stock_count,'Aktien mit Sample':x.eligible_stock_count,'Vollständige Perioden':x.total_complete_periods,'Target Hit % gewichtet':round(x.weighted_target_hit_rate*100,1),'Ø Perioden/Aktie':round(x.average_periods_per_stock,1),'Ø Coverage %':round(x.average_signal_coverage_rate*100,2),'Ø Median Tage':round(x.average_median_days_to_target,1) if x.average_median_days_to_target is not None else None,'Ø Drawdown %':round(x.average_max_drawdown_pct,2) if x.average_max_drawdown_pct is not None else None,'Sample':x.sample_quality} for x in rows]),width='stretch',hide_index=True)
   st.info('Gewichtet bedeutet: alle vollständigen Perioden eines Profils gemeinsam. Die Optimierung der Schwellenwerte folgt erst im nächsten Sprint.')
