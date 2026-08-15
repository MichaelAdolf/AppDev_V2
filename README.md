import yfinance as yf

from stockmind.domain.history.historical_setup_entry import (
    HistoricalSetupEntry
)

from stockmind.infrastructure.history.historical_setup_repository import (
    HistoricalSetupRepository
)


class HistoricalSetupReplayUseCase:

    def execute(
        self,
        symbol: str,
        profile_name: str,
        analysis_period: str,
        target_pct: float = 0.08,
        lookahead_days: int = 60
    ) -> list[HistoricalSetupEntry]:

        symbol = (
            symbol
            .upper()
            .strip()
        )

        data = (
            yf.Ticker(
                symbol
            )
            .history(
                period=self._map_period(
                    analysis_period
                )
            )
        )

        if data.empty:

            return []

        data = (
            data
            .copy()
        )

        data = self._calculate_indicators(
            data
        )

        thresholds = self._profile_thresholds(
            profile_name
        )

        entries = self._find_setups(
            symbol=symbol,
            profile_name=profile_name,
            analysis_period=analysis_period,
            data=data,
            thresholds=thresholds,
            target_pct=target_pct,
            lookahead_days=lookahead_days
        )

        repository = (
            HistoricalSetupRepository()
        )

        repository.delete_for(
            symbol=symbol,
            profile_name=profile_name,
            analysis_period=analysis_period
        )

        for entry in entries:

            repository.save(
                entry
            )

        return entries

    def _map_period(
        self,
        analysis_period: str
    ) -> str:

        mapping = {
            "1m": "1mo",
            "6m": "6mo",
            "1y": "1y",
            "3y": "3y",
            "5y": "5y"
        }

        return mapping.get(
            analysis_period,
            "1y"
        )

    def _profile_thresholds(
        self,
        profile_name: str
    ) -> dict:

        if profile_name == "conservative":

            return {
                "rsi": 30,
                "bb_position": 0.12,
                "require_macd_rising": True,
                "cooldown_days": 8
            }

        if profile_name == "aggressive":

            return {
                "rsi": 42,
                "bb_position": 0.35,
                "require_macd_rising": False,
                "cooldown_days": 4
            }

        return {
            "rsi": 35,
            "bb_position": 0.22,
            "require_macd_rising": True,
            "cooldown_days": 6
        }

    def _calculate_indicators(
        self,
        data
    ):

        data["BB_Middle"] = (
            data["Close"]
            .rolling(
                window=20
            )
            .mean()
        )

        data["BB_Std"] = (
            data["Close"]
            .rolling(
                window=20
            )
            .std()
        )

        data["BB_Upper"] = (
            data["BB_Middle"]
            + 2 * data["BB_Std"]
        )

        data["BB_Lower"] = (
            data["BB_Middle"]
            - 2 * data["BB_Std"]
        )

        data["BB_Position"] = (
            (
                data["Close"]
                - data["BB_Lower"]
            )
            / (
                data["BB_Upper"]
                - data["BB_Lower"]
            )
        )

        delta = (
            data["Close"]
            .diff()
        )

        gain = (
            delta
            .where(
                delta > 0,
                0
            )
            .rolling(
                window=14
            )
            .mean()
        )

        loss = (
            -delta
            .where(
                delta < 0,
                0
            )
            .rolling(
                window=14
            )
            .mean()
        )

        rs = (
            gain
            / loss
        )

        data["RSI"] = (
            100
            - (
                100
                / (
                    1
                    + rs
                )
            )
        )

        ema_12 = (
            data["Close"]
            .ewm(
                span=12,
                adjust=False
            )
            .mean()
        )

        ema_26 = (
            data["Close"]
            .ewm(
                span=26,
                adjust=False
            )
            .mean()
        )

        data["MACD"] = (
            ema_12
            - ema_26
        )

        data["MACD_Signal"] = (
            data["MACD"]
            .ewm(
                span=9,
                adjust=False
            )
            .mean()
        )

        data["MACD_Hist"] = (
            data["MACD"]
            - data["MACD_Signal"]
        )

        data["MACD_Hist_Rising"] = (
            data["MACD_Hist"]
            > data["MACD_Hist"]
            .shift(1)
        )

        return data

    def _find_setups(
        self,
        symbol: str,
        profile_name: str,
        analysis_period: str,
        data,
        thresholds: dict,
        target_pct: float,
        lookahead_days: int
    ) -> list[HistoricalSetupEntry]:

        entries = []

        cooldown = 0

        rows = (
            data
            .reset_index()
        )

        for index in range(
            30,
            len(rows) - lookahead_days
        ):

            if cooldown > 0:

                cooldown -= 1

                continue

            row = rows.iloc[
                index
            ]

            if self._is_invalid_row(
                row
            ):

                continue

            rsi_ok = (
                row["RSI"]
                <= thresholds["rsi"]
            )

            bb_ok = (
                row["BB_Position"]
                <= thresholds["bb_position"]
            )

            macd_ok = True

            if thresholds["require_macd_rising"]:

                macd_ok = bool(
                    row["MACD_Hist_Rising"]
                )

            setup_detected = (
                rsi_ok
                and bb_ok
                and macd_ok
            )

            if not setup_detected:

                continue

            entry = self._evaluate_setup(
                symbol=symbol,
                profile_name=profile_name,
                analysis_period=analysis_period,
                rows=rows,
                index=index,
                target_pct=target_pct,
                lookahead_days=lookahead_days
            )

            entries.append(
                entry
            )

            cooldown = thresholds[
                "cooldown_days"
            ]

        return entries

    def _is_invalid_row(
        self,
        row
    ) -> bool:

        required = [
            "Close",
            "High",
            "Low",
            "RSI",
            "BB_Position",
            "MACD_Hist_Rising"
        ]

        for column in required:

            value = row[
                column
            ]

            if value != value:

                return True

        return False

    def _evaluate_setup(
        self,
        symbol: str,
        profile_name: str,
        analysis_period: str,
        rows,
        index: int,
        target_pct: float,
        lookahead_days: int
    ) -> HistoricalSetupEntry:

        row = rows.iloc[
            index
        ]

        entry_price = float(
            row["Close"]
        )

        setup_date = (
            row["Date"]
            .date()
            .isoformat()
        )

        target_price = (
            entry_price
            * (
                1
                + target_pct
            )
        )

        future = (
            rows
            .iloc[
                index + 1:
                index + 1 + lookahead_days
            ]
        )

        success = False

        days_to_target = None

        for offset, future_row in enumerate(
            future.itertuples(),
            start=1
        ):

            if float(
                future_row.High
            ) >= target_price:

                success = True

                days_to_target = offset

                break

        max_high = float(
            future["High"]
            .max()
        )

        min_low = float(
            future["Low"]
            .min()
        )

        max_gain_pct = (
            (
                max_high
                - entry_price
            )
            / entry_price
            * 100
        )

        max_drawdown_pct = (
            (
                min_low
                - entry_price
            )
            / entry_price
            * 100
        )

        return HistoricalSetupEntry(
            symbol=symbol,
            profile_name=profile_name,
            analysis_period=analysis_period,
            setup_date=setup_date,
            entry_price=entry_price,
            target_pct=target_pct,
            success=success,
            days_to_target=days_to_target,
            max_gain_pct=max_gain_pct,
            max_drawdown_pct=max_drawdown_pct
        )
