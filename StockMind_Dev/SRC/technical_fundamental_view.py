import streamlit as st
def render(dashboard):
 st.subheader("Technisch vs. Fundamental");f=dashboard.fundamental
 if not f:st.info("Keine Fundamentaldaten verfügbar.");return
 c1,c2=st.columns(2)
 with c1:st.write("**Technische Situation**");st.metric("Signal",dashboard.signal);st.metric("Opportunity",f"{dashboard.score:.1f}");st.metric("Confidence",f"{dashboard.confidence:.1%}")
 with c2:st.write("**Fundamentale Situation**");st.metric("Fundamental Score",f"{f.fundamental_score:.0f}/100");st.metric("Bewertung",f.valuation);st.metric("Analysten-Upside",f"{f.target_upside_pct:.1f}%" if f.target_upside_pct is not None else "-")
 if f.target_upside_pct is not None:
  relation="über" if f.target_upside_pct>=8 else "unter";st.info(f"StockMind-Ziel: +8,0 % | Analysten-Upside: {f.target_upside_pct:+.1f} % | Differenz: {dashboard.analyst_target_difference_pct:+.1f} Prozentpunkte. Das Analystenziel liegt {relation} dem StockMind-Ziel.")
