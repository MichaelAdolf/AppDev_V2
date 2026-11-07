import pandas as pd
import streamlit as st

from stockmind.application.exit.exit_research_validation_use_case import ExitResearchValidationUseCase
from stockmind.application.exit.exit_strategy_research_use_case import ExitStrategyResearchUseCase
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository


def render():
    st.subheader("Exit Strategy Research")
    st.caption(
        "Research und Out-of-Sample-Validierung. Keine Strategie wird "
        "dadurch produktiv aktiviert."
    )
    stocks = [
        item for item in WatchlistRepository().load_all()
        if item.active
    ]
    labels = {
        f"{item.company_name} ({item.symbol})": item.symbol
        for item in stocks
    }
    if not labels:
        st.info("Keine aktiven Watchlist-Aktien.")
        return

    c1, c2 = st.columns(2)
    label = c1.selectbox("Aktie", list(labels), key="exit_research_symbol")
    profile = c2.selectbox(
        "Profil",
        ["conservative", "balanced", "aggressive"],
        index=1,
        key="exit_research_profile",
    )
    symbol = labels[label]
    repository = ChartDataRepository()
    if not repository.has_complete_ohlc(symbol):
        st.warning(
            "Für diese Aktie ist die gespeicherte OHLC-Historie noch nicht "
            "vollständig. Führe einmal den vollständigen Chart-Refresh aus, "
            "bevor Exit-Ergebnisse methodisch bewertet werden."
        )

    research_tab, validation_tab = st.tabs([
        "Research",
        "Validation & Walk-Forward",
    ])

    with research_tab:
        if st.button(
            "Exit-Strategien vergleichen",
            type="primary",
            key="run_exit_research",
        ):
            with st.spinner("Historische Exit-Szenarien werden ausgewertet..."):
                result = ExitStrategyResearchUseCase().analyze(
                    symbol, profile
                )
            st.metric("Vollständige BUY-Perioden", result["period_count"])
            st.dataframe(pd.DataFrame([{
                "Strategie": row.strategy_name,
                "Fälle": row.sample_count,
                "Positive Rate %": round(row.positive_rate * 100, 1),
                "Target vor Exit %": round(
                    row.target_reached_rate * 100, 1
                ),
                "Ø Return %": round(row.average_return_pct, 2),
                "Median Return %": round(row.median_return_pct, 2),
                "Ø Tage": round(row.average_holding_days, 1),
                "Ø Drawdown %": round(
                    row.average_max_drawdown_pct, 2
                ),
                "Worst %": round(row.worst_return_pct, 2),
                "Best %": round(row.best_return_pct, 2),
            } for row in result["summaries"]]),
                width="stretch",
                hide_index=True,
            )

    with validation_tab:
        if st.button(
            "Out-of-Sample validieren",
            type="primary",
            key="run_exit_validation",
        ):
            with st.spinner("Train-/Validation-Split wird ausgewertet..."):
                result = ExitResearchValidationUseCase().validate(
                    symbol, profile
                )
            c1, c2, c3 = st.columns(3)
            c1.metric("Gesamtperioden", result["period_count"])
            c2.metric("Train", result["train_count"])
            c3.metric("Validation", result["validation_count"])
            if not result["sufficient_sample"]:
                st.warning(
                    "Die Stichprobe unterschreitet aktuell mindestens 12 "
                    "Train- und 5 Validation-Perioden. Ergebnisse sind nur "
                    "explorativ."
                )
            st.dataframe(pd.DataFrame([{
                "Strategie": row.strategy_name,
                "Status": row.robustness_status,
                "Train Fälle": row.train_sample_count,
                "Validation Fälle": row.validation_sample_count,
                "Train Ø Return %": round(
                    row.train_average_return_pct, 2
                ),
                "Validation Ø Return %": round(
                    row.validation_average_return_pct, 2
                ),
                "Return Δ": round(row.return_degradation_pct, 2),
                "Train Positive %": round(
                    row.train_positive_rate * 100, 1
                ),
                "Validation Positive %": round(
                    row.validation_positive_rate * 100, 1
                ),
                "Positive Δ pp": round(
                    row.positive_rate_degradation * 100, 1
                ),
                "Validation Drawdown %": round(
                    row.validation_average_drawdown_pct, 2
                ),
            } for row in result["rows"]]),
                width="stretch",
                hide_index=True,
            )
            st.subheader("Walk-Forward")
            if result["walk_forward"]:
                st.dataframe(pd.DataFrame([{
                    "Fold": row.fold_number,
                    "Train": f"{row.train_start} bis {row.train_end}",
                    "Validation": (
                        f"{row.validation_start} bis "
                        f"{row.validation_end}"
                    ),
                    "Gewählte Strategie": row.strategy_name,
                    "Train Ø Return %": round(
                        row.train_average_return_pct, 2
                    ),
                    "Validation Ø Return %": round(
                        row.validation_average_return_pct, 2
                    ),
                    "Validation Positive %": round(
                        row.validation_positive_rate * 100, 1
                    ),
                    "Validation Fälle": row.validation_sample_count,
                } for row in result["walk_forward"]]),
                    width="stretch",
                    hide_index=True,
                )
            else:
                st.info(
                    "Für Walk-Forward sind mindestens 17 vollständige "
                    "BUY-Perioden erforderlich."
                )
            st.info(
                "STABLE bedeutet in diesem Sprint: Validation Return bleibt "
                "positiv, verschlechtert sich höchstens um 2 Prozentpunkte "
                "und die positive Rate höchstens um 15 Prozentpunkte. Diese "
                "Schwellen sind Research-Kriterien, noch keine Exit-Regeln."
            )
