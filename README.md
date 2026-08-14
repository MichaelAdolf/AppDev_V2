from stockmind.application.dashboard.models.alert_result import (
    AlertResult
)

from stockmind.infrastructure.history.latest_analysis_repository import (
    LatestAnalysisRepository
)


class AlertsDashboardUseCase:

    def load(
        self,
        profile_name: str
    ) -> list[AlertResult]:

        results = (
            LatestAnalysisRepository()
            .load_all(
                profile_name
            )
        )

        alerts = []

        for item in results:

            if item.opportunity_score >= 85:

                alerts.append(
                    AlertResult(
                        title="Hot Opportunity",
                        message=(
                            f"{item.symbol} hat einen sehr hohen "
                            f"Opportunity Score von "
                            f"{item.opportunity_score:.1f}."
                        ),
                        severity="success"
                    )
                )

            elif item.opportunity_score >= 75:

                alerts.append(
                    AlertResult(
                        title="Interessantes Setup",
                        message=(
                            f"{item.symbol} ist beobachtenswert "
                            f"mit einem Opportunity Score von "
                            f"{item.opportunity_score:.1f}."
                        ),
                        severity="info"
                    )
                )

            if item.confidence >= 0.75:

                alerts.append(
                    AlertResult(
                        title="Hohe Confidence",
                        message=(
                            f"{item.symbol} hat eine Confidence "
                            f"von {item.confidence:.1%}."
                        ),
                        severity="success"
                    )
                )

            if item.risk_level == "HIGH":

                alerts.append(
                    AlertResult(
                        title="Erhöhtes Risiko",
                        message=(
                            f"{item.symbol} hat aktuell ein "
                            f"hohes Risikoniveau."
                        ),
                        severity="warning"
                    )
                )

            if item.signal == "BUY":

                alerts.append(
                    AlertResult(
                        title="BUY Signal",
                        message=(
                            f"{item.symbol} hat aktuell ein "
                            f"BUY Signal."
                        ),
                        severity="success"
                    )
                )

        return alerts
