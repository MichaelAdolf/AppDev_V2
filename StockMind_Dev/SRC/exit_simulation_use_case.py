from datetime import date, timedelta
from statistics import mean, median

from stockmind.domain.exit.exit_simulation_result import (
    ExitSimulationResult,
    ExitStrategySummary,
)


class ExitSimulationUseCase:
    def simulate(self, period, prices, opportunities, strategy):
        end_date = (
            date.fromisoformat(period.start_date)
            + timedelta(days=strategy.max_holding_days)
        ).isoformat()
        points = [
            point for point in prices
            if period.start_date <= point.trading_date <= end_date
        ]
        if not points:
            return None

        entry = float(period.entry_price)
        target = entry * (1 + strategy.target_pct)
        peak = entry
        minimum = entry
        exit_point = points[-1]
        exit_price = float(exit_point.close_price)
        reason = "TIME_LIMIT"
        target_seen = False

        opportunities_by_date = {
            item.trading_date: item for item in opportunities
        }
        entry_opportunity = opportunities_by_date.get(period.start_date)
        entry_score = (
            entry_opportunity.opportunity_score
            if entry_opportunity else None
        )
        entry_confidence = (
            entry_opportunity.confidence
            if entry_opportunity else None
        )

        for point in points:
            close = float(point.close_price)
            has_high_attr = hasattr(point, "high_price")
            has_low_attr = hasattr(point, "low_price")
            high_value = getattr(point, "high_price", None)
            low_value = getattr(point, "low_price", None)
            has_ohlc = (
                has_high_attr
                and has_low_attr
                and high_value is not None
                and low_value is not None
            )
            high = float(high_value if has_ohlc else close)
            low = float(low_value if has_ohlc else close)
            peak = max(peak, high)
            minimum = min(minimum, low)
            days = (
                date.fromisoformat(point.trading_date)
                - date.fromisoformat(period.start_date)
            ).days

            # Conservative daily-bar ordering: protective exits are evaluated
            # before the profit target when both prices occur in the same bar.
            if (
                strategy.stop_loss_pct is not None
                and low <= entry * (1 - strategy.stop_loss_pct)
            ):
                exit_point = point
                exit_price = (
                    entry * (1 - strategy.stop_loss_pct)
                    if has_ohlc else close
                )
                reason = "STOP_LOSS"
                break

            trailing_level = peak * (1 - strategy.trailing_stop_pct)                 if strategy.trailing_stop_pct is not None else None
            if (
                trailing_level is not None
                and peak > entry
                and low <= trailing_level
            ):
                exit_point = point
                exit_price = trailing_level
                reason = "TRAILING_STOP"
                break

            if high >= target:
                target_seen = True
                exit_point = point
                exit_price = target if has_ohlc else close
                reason = "TARGET_REACHED"
                break

            current = opportunities_by_date.get(point.trading_date)
            if current:
                if (
                    strategy.score_drop is not None
                    and entry_score is not None
                    and current.opportunity_score
                    <= entry_score - strategy.score_drop
                ):
                    exit_point = point
                    exit_price = close
                    reason = "SCORE_DROP"
                    break
                if (
                    strategy.confidence_drop is not None
                    and entry_confidence is not None
                    and current.confidence
                    <= entry_confidence - strategy.confidence_drop
                ):
                    exit_point = point
                    exit_price = close
                    reason = "CONFIDENCE_DROP"
                    break
                if strategy.exit_on_sell and current.signal == "SELL":
                    exit_point = point
                    exit_price = close
                    reason = "SIGNAL_SELL"
                    break
                if (
                    strategy.exit_on_hold
                    and current.signal in ("HOLD", "SELL")
                ):
                    exit_point = point
                    exit_price = close
                    reason = "SIGNAL_HOLD"
                    break
                if (
                    strategy.exit_on_high_risk
                    and current.risk_level == "HIGH"
                ):
                    exit_point = point
                    exit_price = close
                    reason = "RISK_HIGH"
                    break

            if days >= strategy.max_holding_days:
                exit_point = point
                exit_price = close
                reason = "TIME_LIMIT"
                break

        holding_days = (
            date.fromisoformat(exit_point.trading_date)
            - date.fromisoformat(period.start_date)
        ).days
        return ExitSimulationResult(
            symbol=period.symbol,
            profile_name=period.profile_name,
            period_start=period.start_date,
            strategy_name=strategy.name,
            exit_date=exit_point.trading_date,
            exit_reason=reason,
            entry_price=entry,
            exit_price=exit_price,
            return_pct=(exit_price / entry - 1) * 100,
            holding_days=holding_days,
            max_gain_pct=(peak / entry - 1) * 100,
            max_drawdown_pct=(minimum / entry - 1) * 100,
            target_reached_before_exit=target_seen,
        )

    def summarize(self, strategy_name, results):
        valid = [result for result in results if result]
        if not valid:
            return ExitStrategySummary(
                strategy_name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            )
        returns = [result.return_pct for result in valid]
        drawdowns = [result.max_drawdown_pct for result in valid]
        return ExitStrategySummary(
            strategy_name=strategy_name,
            sample_count=len(valid),
            positive_count=sum(result.return_pct > 0 for result in valid),
            target_reached_count=sum(
                result.target_reached_before_exit for result in valid
            ),
            positive_rate=sum(
                result.return_pct > 0 for result in valid
            ) / len(valid),
            target_reached_rate=sum(
                result.target_reached_before_exit for result in valid
            ) / len(valid),
            average_return_pct=mean(returns),
            median_return_pct=median(returns),
            average_holding_days=mean(
                result.holding_days for result in valid
            ),
            average_max_drawdown_pct=mean(drawdowns),
            worst_return_pct=min(returns),
            best_return_pct=max(returns),
        )
