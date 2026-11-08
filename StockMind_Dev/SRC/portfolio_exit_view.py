import pandas as pd
import streamlit as st
from stockmind.application.exit.portfolio_exit_use_case import PortfolioExitUseCase

def render():
 decisions=PortfolioExitUseCase().load();st.subheader('Produktive Exit Intelligence');st.caption('Keine automatische Transaktion. EXIT_REVIEW bedeutet, den Verkauf manuell zu prüfen.')
 if not decisions:st.info('Keine offenen Positionen vorhanden.');return
 st.dataframe(pd.DataFrame([{'Symbol':x.symbol,'Profil':x.profile_name,'Status':x.status,'Strategie':x.strategy_name,'Quelle':x.strategy_source,'Validation':x.validation_status,'Gründe':', '.join(x.reasons) if x.reasons else '–','Aktion':x.action_text} for x in decisions]),width='stretch',hide_index=True)
