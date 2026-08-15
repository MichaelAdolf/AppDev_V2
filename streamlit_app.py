import streamlit as st

from components.watchlist_view import (
    render as render_watchlist
)

from components.top_movers_view import (
    render as render_top_movers
)

from components.portfolio_view import (
    render as render_portfolio
)

from components.stock_detail_view import (
    render as render_stock_detail
)

from components.stock_selector import (
    render as render_stock_selector
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

selected_symbol = (
    render_stock_selector(
        profile
    )
)

#
# Session State
#

if "selected_symbol" not in st.session_state:
    st.session_state["selected_symbol"] = None

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

if selected_symbol:

    st.divider()

    render_stock_detail(
        profile_name=profile,
        symbol=selected_symbol
    )