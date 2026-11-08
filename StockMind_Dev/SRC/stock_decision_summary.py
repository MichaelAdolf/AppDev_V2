import pandas as pd
import streamlit as st

from stockmind.application.dashboard.use_cases.profile_comparison_dashboard_use_case import (
    ProfileComparisonDashboardUseCase,
)
from stockmind.application.exit.portfolio_exit_use_case import PortfolioExitUseCase
from stockmind.application.portfolio.portfolio_intelligence_use_case import (
    PortfolioIntelligenceUseCase,
)
from stockmind.application.strategy.fitted_profile_signal_use_case import (
    FittedProfileSignalUseCase,
)


def _decision_icon(signal):
    return {
        "BUY": "🟢",
        "HOLD": "🔵",
        "SELL": "🔴",
        "WATCH": "🟡",
        "EXIT_REVIEW": "🔴",
    }.get(signal, "⚪")


def render(symbol: str):
    symbol = symbol.upper()
    st.subheader("Entscheidungsübersicht")

    comparison = ProfileComparisonDashboardUseCase().load(symbol, "5y", 3)
    rows = []
    for item in comparison.entries:
        signal = "BUY" if item.current_buy_signal is True else item.signal
        rows.append({
            "Profil": item.profile_name.title(),
            "Entscheidung": f"{_decision_icon(signal)} {signal}",
            "Score": round(item.score, 1),
            "Confidence %": round(item.confidence * 100, 1),
            "Hist. Trefferquote %": round(item.target_hit_rate * 100, 1),
            "Vollständige Perioden": item.complete_period_count,
            "Risiko": item.risk_level,
        })

    individual = FittedProfileSignalUseCase().evaluate(symbol)
    if individual.active:
        rows.append({
            "Profil": "Individual",
            "Entscheidung": f"{_decision_icon(individual.signal)} {individual.signal}",
            "Score": None,
            "Confidence %": None,
            "Hist. Trefferquote %": None,
            "Vollständige Perioden": None,
            "Risiko": None,
        })
    else:
        rows.append({
            "Profil": "Individual",
            "Entscheidung": "⚪ Nicht aktiv",
            "Score": None,
            "Confidence %": None,
            "Hist. Trefferquote %": None,
            "Vollständige Perioden": None,
            "Risiko": None,
        })

    st.dataframe(pd.DataFrame(rows), width="stretch", hide_index=True)

    if individual.active:
        st.caption(
            f"Aktive Individual-Strategie: {individual.strategy_name} · "
            f"Basis {individual.base_profile} · "
            f"Bedingungen {individual.matched_conditions}/"
            f"{individual.required_conditions}"
        )

    portfolio_item = next(
        (
            item
            for item in PortfolioIntelligenceUseCase().load()
            if item.symbol.upper() == symbol
        ),
        None,
    )
    exit_decision = next(
        (
            item
            for item in PortfolioExitUseCase().load()
            if item.symbol.upper() == symbol
        ),
        None,
    )

    st.divider()
    if portfolio_item is None:
        st.info("Diese Aktie ist aktuell nicht im Portfolio.")
        return

    st.success("Diese Aktie ist aktuell im Portfolio.")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Stück", f"{portfolio_item.quantity:g}")
    c2.metric("Ø Kaufkurs", f"{portfolio_item.weighted_purchase_price:.2f} €")
    c3.metric(
        "P/L",
        "–" if portfolio_item.unrealized_profit is None
        else f"{portfolio_item.unrealized_profit:+.2f} €",
        None if portfolio_item.unrealized_return_pct is None
        else f"{portfolio_item.unrealized_return_pct:+.1%}",
    )
    c4.metric("Tag", f"{portfolio_item.holding_days}/60")

    if exit_decision:
        message = (
            f"{_decision_icon(exit_decision.status)} "
            f"{exit_decision.status}: {exit_decision.action_text}"
        )
        if exit_decision.status == "EXIT_REVIEW":
            st.error(message)
        elif exit_decision.status == "WATCH":
            st.warning(message)
        else:
            st.info(message)
        st.caption(
            f"Exit-Strategie: {exit_decision.strategy_name} · "
            f"Validation: {exit_decision.validation_status} · "
            f"Gründe: {', '.join(exit_decision.reasons) or 'keine'}"
        )
