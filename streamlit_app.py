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

from stockmind.application.watchlists.add_stock_use_case import (
    AddStockUseCase
)

from stockmind.application.watchlists.remove_stock_use_case import (
    RemoveStockUseCase
)

from stockmind.infrastructure.watchlists.watchlist_repository import (
    WatchlistRepository
)


st.set_page_config(
    page_title="StockMind",
    layout="wide"
)

st.title(
    "📈 StockMind"
)

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
# Watchlist Verwaltung
#

st.sidebar.divider()

st.sidebar.subheader(
    "📋 Watchlist verwalten"
)

new_symbol = st.sidebar.text_input(
    "Aktie hinzufügen",
    value=""
)

if st.sidebar.button(
    "➕ Hinzufügen"
):

    if new_symbol.strip():

        added = (
            AddStockUseCase()
            .execute(
                new_symbol
            )
        )

        if added:

            st.sidebar.success(
                f"{new_symbol.upper()} hinzugefügt."
            )

        else:

            st.sidebar.warning(
                "Aktie bereits vorhanden."
            )

        st.rerun()

watchlist_entries = (
    WatchlistRepository()
    .load_all()
)

if watchlist_entries:

    selected_remove = (
        st.sidebar.selectbox(
            "Aktie entfernen",
            options=[
                entry.symbol
                for entry in watchlist_entries
            ]
        )
    )

    if st.sidebar.button(
        "➖ Entfernen"
    ):

        RemoveStockUseCase().execute(
            selected_remove
        )

        st.sidebar.success(
            f"{selected_remove} entfernt."
        )

        st.rerun()

#
# Auswahl
#

selected_symbol = (
    render_stock_selector(
        profile
    )
)

#
# Session State
#

if "selected_symbol" not in st.session_state:

    st.session_state[
        "selected_symbol"
    ] = None

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
        profile
    )

with tab2:

    render_top_movers(
        profile
    )

with tab3:

    render_portfolio(
        profile
    )

if selected_symbol:

    render_stock_detail(
        profile_name=profile,
        symbol=selected_symbol
    )
