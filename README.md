import pandas as pd

from stockmind.domain.historical_success.historical_success_result import (
    HistoricalSuccessResult
)

from stockmind.domain.profiles.trading_profile import (
    TradingProfile
)


class HistoricalSuccessEngine:

    def analyze(
        self,
        symbol: str,
        data: pd.DataFrame,
        profile: TradingProfile,
        target_pct: float = 0.08,
        lookahead_days: int = 60
    ) -> HistoricalSuccessResult:

        prepared_data = self._prepare_data(
            data
        )

        setup_count = 0

        success_count = 0

        max_index = (
            len(prepared_data)
            - lookahead_days
            - 1
        )

        for index in range(
            30,
            max_index
        ):

            row = prepared_data.iloc[
                index
            ]

            if not self._is_valid_setup_row(
                row
            ):

                continue

            if not self._is_setup(
                row=row,
                profile=profile
            ):

                continue

            setup_count += 1

            entry_price = float(
                row["Close"]
            )

            target_price = entry_price * (
                1 + target_pct
            )

            future_window = prepared_data.iloc[
                index + 1:
                index + 1 + lookahead_days
            ]

            max_future_high = float(
                future_window["High"].max()
            )

            if max_future_high >= target_price:

                success_count += 1

        failure_count = (
            setup_count
            - success_count
        )

        success_rate = 0.0

        if setup_count > 0:

            success_rate = (
                success_count
                / setup_count
            )

        return HistoricalSuccessResult(
            symbol=symbol,
            profile_name=profile.name,
            setup_count=setup_count,
            success_count=success_count,
            failure_count=failure_count,
            success_rate=success_rate,
            target_pct=target_pct,
            lookahead_days=lookahead_days,
            sample_quality=self._sample_quality(
                setup_count
            )
        )

    def _prepare_data(
        self,
        data: pd.DataFrame
    ) -> pd.DataFrame:

        prepared = data.copy()

        prepared["rsi_14"] = self._calculate_rsi(
            prepared
        )

        prepared["bollinger_position"] = (
            self._calculate_bollinger_position(
                prepared
            )
        )

        prepared["adx_14"] = self._calculate_adx(
            prepared
        )

        return prepared

    def _calculate_rsi(
        self,
        data: pd.DataFrame
    ) -> pd.Series:

        delta = data["Close"].diff()

        gain = (
            delta.where(
                delta > 0,
                0
            )
            .rolling(
                window=14
            )
            .mean()
        )

        loss = (
            -delta.where(
                delta < 0,
                0
            )
            .rolling(
                window=14
            )
            .mean()
        )

        rs = gain / loss

        rsi = 100 - (
            100 / (1 + rs)
        )

        return rsi

    def _calculate_bollinger_position(
        self,
        data: pd.DataFrame
    ) -> pd.Series:

        sma = (
            data["Close"]
            .rolling(
                window=20
            )
            .mean()
        )

        std = (
            data["Close"]
            .rolling(
                window=20
            )
            .std()
        )

        upper = sma + (
            std * 2
        )

        lower = sma - (
            std * 2
        )

        position = (
            data["Close"] - lower
        ) / (
            upper - lower
        )

        return position

    def _calculate_adx(
        self,
        data: pd.DataFrame
    ) -> pd.Series:

        high = data["High"]

        low = data["Low"]

        close = data["Close"]

        up_move = high.diff()

        down_move = (
            low.shift(1)
            - low
        )

        plus_dm = up_move.where(
            (up_move > down_move)
            & (up_move > 0),
            0.0
        )

        minus_dm = down_move.where(
            (down_move > up_move)
            & (down_move > 0),
            0.0
        )

        previous_close = close.shift(1)

        true_range = pd.concat(
            [
                high - low,
                (
                    high
                    - previous_close
                ).abs(),
                (
                    low
                    - previous_close
                ).abs(),
            ],
            axis=1
        ).max(
            axis=1
        )

        atr = true_range.rolling(
            window=14
        ).mean()

        plus_di = 100 * (
            plus_dm.rolling(
                window=14
            ).mean()
            / atr
        )

        minus_di = 100 * (
            minus_dm.rolling(
                window=14
            ).mean()
            / atr
        )

        dx = 100 * (
            (
                plus_di
                - minus_di
            ).abs()
            / (
                plus_di
                + minus_di
            )
        )

        adx = dx.rolling(
            window=14
        ).mean()

        return adx

    def _is_valid_setup_row(
        self,
        row
    ) -> bool:

        required_columns = [
            "rsi_14",
            "bollinger_position",
            "adx_14",
            "Close",
            "High",
        ]

        for column in required_columns:

            if pd.isna(
                row[column]
            ):

                return False

        return True

    def _is_setup(
        self,
        row,
        profile: TradingProfile
    ) -> bool:

        rsi_condition = (
            row["rsi_14"]
            <= profile.rsi_oversold_threshold
        )

        bollinger_condition = (
            row["bollinger_position"]
            <= profile.bollinger_lower_threshold
        )

        adx_condition = (
            row["adx_14"]
            >= profile.adx_trend_strength_threshold
        )

        return (
            rsi_condition
            and bollinger_condition
            and adx_condition
        )

    def _sample_quality(
        self,
        setup_count: int
    ) -> str:

        if setup_count >= 50:

            return "HIGH"

        if setup_count >= 20:

            return "MEDIUM"

        if setup_count > 0:

            return "LOW"

        return "NO_SAMPLE"
