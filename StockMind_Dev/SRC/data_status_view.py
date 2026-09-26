import streamlit as st
def render(status):
 with st.expander("Datenstatus"):
  labels={"market_data":"Marktdaten","opportunity_replay":"Opportunity Replay","buy_periods":"BUY-Perioden","current_analysis":"Aktuelle Analyse","fundamentals":"Fundamentaldaten"}
  for key,label in labels.items():st.write(f"**{label}:** {status.get(key) or 'keine Daten'}")
