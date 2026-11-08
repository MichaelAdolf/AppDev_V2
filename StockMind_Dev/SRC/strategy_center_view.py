import streamlit as st

from components.entry_strategy_research_view import render as render_entry_research
from components.exit_strategy_research_view import render as render_exit_research


def render():
    st.header("Strategien")
    st.caption(
        "Strategien trainieren, validieren und verwalten. "
        "Dieser Bereich ist vom täglichen Portfolio- und Marktworkflow getrennt."
    )

    entry_tab, exit_tab = st.tabs([
        "Entry & Individual",
        "Exit Strategy",
    ])

    with entry_tab:
        render_entry_research()

    with exit_tab:
        render_exit_research()
