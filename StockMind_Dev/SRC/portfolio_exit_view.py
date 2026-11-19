import pandas as pd
import streamlit as st
from components.decision_ui import label,render_card
from stockmind.application.exit.portfolio_exit_use_case import PortfolioExitUseCase

def render():
 decisions=PortfolioExitUseCase().load();st.subheader('Exit Entscheidungen');st.caption('EXIT REVIEW bedeutet manuelle Verkaufsprüfung. StockMind führt keine Transaktion aus.')
 if not decisions:st.info('Keine offenen Positionen vorhanden.');return
 c1,c2,c3=st.columns(3);c1.metric('🔴 EXIT REVIEW',sum(x.status=='EXIT_REVIEW' for x in decisions));c2.metric('🟡 WATCH',sum(x.status=='WATCH' for x in decisions));c3.metric('🔵 HOLD',sum(x.status=='HOLD' for x in decisions))
 for x in decisions:
  render_card(x.status,x.symbol,[('Profil',x.profile_name),('Strategie',x.strategy_name),('Validation',x.validation_status)],f"Gründe: {', '.join(x.reasons) or 'keine'} · {x.action_text}")
 st.dataframe(pd.DataFrame([{'Entscheidung':label(x.status,True),'Symbol':x.symbol,'Profil':x.profile_name,'Strategie':x.strategy_name,'Validation':x.validation_status,'Gründe':', '.join(x.reasons) or '–'} for x in decisions]),width='stretch',hide_index=True)
