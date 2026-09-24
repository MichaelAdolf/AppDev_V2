import plotly.graph_objects as go
import streamlit as st

from stockmind.infrastructure.history.indicator_chart_data_repository import (
    IndicatorChartDataRepository
)


def render_rsi_chart(
    symbol: str
):

    points = (
        IndicatorChartDataRepository()
        .load_by_symbol(
            symbol
        )
    )

    if not points:

        st.warning(
            "Keine RSI-Daten vorhanden."
        )

        return

    dates = [
        point.trading_date
        for point in points
    ]

    rsi_values = [
        point.rsi_14
        for point in points
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=rsi_values,
            mode="lines",
            name="RSI 14"
        )
    )

    fig.add_hline(
        y=30,
        line_dash="dash",
        line_color="green",
        annotation_text="Oversold"
    )

    fig.add_hline(
        y=70,
        line_dash="dash",
        line_color="red",
        annotation_text="Overbought"
    )

    fig.update_layout(
        title=f"{symbol} RSI",
        xaxis_title="Datum",
        yaxis_title="RSI",
        yaxis=dict(
            range=[
                0,
                100
            ]
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def render_macd_chart(
    symbol: str
):

    points = (
        IndicatorChartDataRepository()
        .load_by_symbol(
            symbol
        )
    )

    if not points:

        st.warning(
            "Keine MACD-Daten vorhanden."
        )

        return

    dates = [
        point.trading_date
        for point in points
    ]

    macd = [
        point.macd
        for point in points
    ]

    macd_signal = [
        point.macd_signal
        for point in points
    ]

    macd_histogram = [
        point.macd_histogram
        for point in points
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=dates,
            y=macd_histogram,
            name="MACD Histogram"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=macd,
            mode="lines",
            name="MACD"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=macd_signal,
            mode="lines",
            name="Signal"
        )
    )

    fig.update_layout(
        title=f"{symbol} MACD",
        xaxis_title="Datum",
        yaxis_title="MACD"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

def render_adx_chart(
        symbol: str
):
    points = (
        IndicatorChartDataRepository()
        .load_by_symbol(
            symbol
        )
    )

    if not points:

        st.warning(
            "Keine ADX-Daten vorhanden."
        )

        return

    dates = [
        point.trading_date
        for point in points
    ]

    adx = [
        point.adx
        for point in points
    ]

    plus_di = [
        point.plus_di
        for point in points
    ]

    minus_di = [
        point.minus_di
        for point in points
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=adx,
            name="ADX"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=plus_di,
            name="+DI"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=minus_di,
            name="-DI"
        )
    )

    fig.update_layout(
        title=f"{symbol} ADX",
        xaxis_title="Datum",
        yaxis_title="ADX"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

def render_stochastic_chart(
        symbol: str
):
    points = (
        IndicatorChartDataRepository()
        .load_by_symbol(
            symbol
        )
    )

    if not points:

        st.warning(
            "Keine Stochastics-Daten vorhanden."
        )

        return

    dates = [
        point.trading_date
        for point in points
    ]

    stoch_k = [
        point.stoch_k
        for point in points
    ]

    stoch_d = [
        point.stoch_d
        for point in points
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=stoch_k,
            name="%K"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=stoch_d,
            name="%D"
        )
    )

    fig.update_layout(
        title=f"{symbol} Stochastics",
        xaxis_title="Datum",
        yaxis_title="Stochastics"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
