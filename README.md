import streamlit as st

from ui.components.watchlist_view import (
    render as render_watchlist
)

from ui.components.top_movers_view import (
    render as render_top_movers
)

from ui.components.portfolio_view import (
    render as render_portfolio
)

st.set_page_config(
    page_title="StockMind",
    layout="wide"
)

st.title("📈 StockMind")

#
# Sidebar
#

st.sidebar.header(
    "StockMind"
)

profile = st.sidebar.selectbox(
    "Profil",
    [
        "conservative",
        "balanced",
        "aggressive"
    ]
)

#
# Main Tabs
#

tab1, tab2, tab3 = st.tabs(
    [
        "🏆 Watchlist",
        "📈 Top Movers",
        "💼 Portfolio"
    ]
)

with tab1:

    render_watchlist(
        profile_name=profile
    )

with tab2:

    render_top_movers()

with tab3:

    render_portfolio()
