import streamlit as st
def render(dashboard):
 st.subheader("Decision Intelligence");st.info(dashboard.profile_consensus)
 with st.expander("Warum diese Einschätzung?",expanded=False):
  st.write("**Erfüllte Kriterien**");[st.write(f"✓ {x}") for x in dashboard.strengths]
  st.write(f"**Historische Evidenz:** {dashboard.period_target_hit_rate:.1%} aus {dashboard.complete_buy_period_count} vollständigen Perioden")
  st.write(f"**Confidence:** {dashboard.confidence:.1%} | **Risiko:** {dashboard.risk_level}")
  st.write("**Score-Komponenten**")
  for key,label in (("quality","Quality"),("confidence","Confidence"),("historical","Historische Evidenz"),("risk","Risiko")):st.write(f"{label}: {dashboard.score_components[key]:+.1f}")
 if dashboard.score_change is not None:
  st.caption(f"Vorheriger Handelstag: Score {dashboard.previous_score:.1f} → {dashboard.score:.1f} ({dashboard.score_change:+.1f}) | Signal {dashboard.previous_signal} → {dashboard.signal} | Confidence Δ {dashboard.confidence_change:+.1%} | Risiko {dashboard.previous_risk} → {dashboard.risk_level}")
