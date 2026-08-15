import streamlit as st

from stockmind.infrastructure.watchlists.watchlist_repository import (
    WatchlistRepository
)


def render(
    profile_name: str
):

    st.subheader(
        "🔍 Aktie auswählen"
    )

    watchlist_entries = (
        WatchlistRepository()
        .load_all()
    )

    active_entries = [
        entry
        for entry in watchlist_entries
        if entry.active
    ]

    if not active_entries:

        st.warning(
            "Keine Aktien auf der Watchlist vorhanden."
        )

        return None

    display_map = {

        f"{entry.symbol} | {entry.company_name}":
            entry.symbol

        for entry in active_entries
    }

    selected_display = st.selectbox(
        "Aktie",
        list(
            display_map.keys()
        ),
        index=0
    )

    selected_symbol = (
        display_map[
            selected_display
        ]
    )

    st.session_state[
        "selected_symbol"
    ] = selected_symbol

    return selected_symbol
