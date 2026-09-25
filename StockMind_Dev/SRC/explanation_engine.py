from stockmind.domain.explainability.explanation_result import ExplanationResult


class ExplanationEngine:
    def create(
        self,
        symbol: str,
        core_setup_result,
        quality_result,
        confidence_result,
        historical_result,
        risk_result,
        opportunity_result,
        rule_results,
    ) -> ExplanationResult:
        strengths = []
        weaknesses = []
        for result in rule_results:
            if result.triggered:
                strengths.append(result.reason)
            else:
                weaknesses.append(result.rule_name)

        source = getattr(historical_result, "source", "SETUPS")
        sample_count = getattr(
            historical_result,
            "sample_count",
            getattr(historical_result, "complete_count", 0),
        )
        source_label = (
            "BUY-Perioden" if source == "BUY_PERIODS"
            else "historische Setups"
        )
        strengths.append(
            f"Target-Hit-Rate aus {source_label}: "
            f"{historical_result.success_rate:.1%} "
            f"bei {sample_count} vollständigen Fällen"
        )

        if source == "BUY_PERIODS":
            strengths.append(
                "Outcome-Verteilung: "
                f"unter Ziel {historical_result.below_target_rate:.1%}, "
                f"flat {historical_result.flat_rate:.1%}, "
                f"negativ {historical_result.negative_rate:.1%}"
            )
        similarity = getattr(historical_result, "average_similarity", None)
        if similarity is not None:
            strengths.append(
                f"Durchschnittliche Ähnlichkeit {similarity:.2f}"
            )

        active_start = getattr(historical_result, "active_period_start", None)
        if active_start:
            strengths.append(
                "Aktive BUY-Periode seit "
                f"{active_start} mit "
                f"{historical_result.active_period_buy_signal_count} BUY-Signalen"
            )

        summary = (
            f"{symbol}: {quality_result.quality} Setup, "
            f"Confidence {confidence_result.confidence:.1%}, "
            f"Risk {risk_result.level}. "
            f"Historische Evidenz: {historical_result.success_rate:.1%} "
            f"Target Hit aus {source_label}."
        )
        return ExplanationResult(
            title=f"{symbol} Analyse",
            summary=summary,
            strengths=strengths,
            weaknesses=weaknesses,
            opportunity_score=opportunity_result.score,
        )
