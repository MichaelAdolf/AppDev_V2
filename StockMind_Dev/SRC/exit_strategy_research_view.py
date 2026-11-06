import pandas as pd
import streamlit as st
from stockmind.application.exit.exit_strategy_research_use_case import ExitStrategyResearchUseCase
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository

def render():
    st.subheader('Exit Strategy Research')
    st.caption('Historischer Vergleich von Exit-Kandidaten. Die Ergebnisse aktivieren keine produktive Verkaufsregel.')
    stocks=[x for x in WatchlistRepository().load_all() if x.active]
    labels={f'{x.company_name} ({x.symbol})':x.symbol for x in stocks}
    if not labels:st.info('Keine aktiven Watchlist-Aktien.');return
    c1,c2=st.columns(2);label=c1.selectbox('Aktie',list(labels),key='exit_research_symbol');profile=c2.selectbox('Profil',['conservative','balanced','aggressive'],index=1,key='exit_research_profile')
    if st.button('Exit-Strategien vergleichen',type='primary'):
        with st.spinner('Historische Exit-Szenarien werden ausgewertet...'):
            result=ExitStrategyResearchUseCase().analyze(labels[label],profile)
        st.metric('Vollständige BUY-Perioden',result['period_count'])
        if not result['summaries']:st.warning('Keine vollständigen BUY-Perioden vorhanden.');return
        st.dataframe(pd.DataFrame([{'Strategie':x.strategy_name,'Fälle':x.sample_count,'Positive Rate %':round(x.positive_rate*100,1),'Target vor Exit %':round(x.target_reached_rate*100,1),'Ø Return %':round(x.average_return_pct,2),'Median Return %':round(x.median_return_pct,2),'Ø Tage':round(x.average_holding_days,1),'Ø Drawdown %':round(x.average_max_drawdown_pct,2),'Worst %':round(x.worst_return_pct,2),'Best %':round(x.best_return_pct,2)} for x in result['summaries']]),width='stretch',hide_index=True)
        st.info('Eine höhere historische Kennzahl ist noch kein Beweis für eine robuste Regel. Kandidaten müssen anschließend out-of-sample und per Walk-Forward geprüft werden.')
