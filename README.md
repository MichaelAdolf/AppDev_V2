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

            #
            # Hot Opportunity
            #

            if item.opportunity_score >= 85:

                alerts.append(
                    AlertResult(
                        title="Hot Opportunity",

                        message=(
                            f"{item.symbol} erreicht einen "
                            f"Opportunity Score von "
                            f"{item.opportunity_score:.1f}."
                        ),

                        severity="success",

                        symbol=item.symbol,

                        profile_name=profile_name,

                        reason=(
                            "Opportunity Score mindestens 85"
                        )
                    )
                )

            #
            # Interessantes Setup
            #

            elif item.opportunity_score >= 75:

                alerts.append(
                    AlertResult(
                        title="Interessantes Setup",

                        message=(
                            f"{item.symbol} ist mit einem "
                            f"Opportunity Score von "
                            f"{item.opportunity_score:.1f} "
                            f"beobachtenswert."
                        ),

                        severity="info",

                        symbol=item.symbol,

                        profile_name=profile_name,

                        reason=(
                            "Opportunity Score mindestens 75"
                        )
                    )
                )

            #
            # Hohe Confidence
            #

            if item.confidence >= 0.75:

                alerts.append(
                    AlertResult(
                        title="Hohe Confidence",

                        message=(
                            f"{item.symbol} besitzt eine "
                            f"Confidence von "
                            f"{item.confidence:.1%}."
                        ),

                        severity="success",

                        symbol=item.symbol,

                        profile_name=profile_name,

                        reason=(
                            "Confidence mindestens 75 %"
                        )
                    )
                )

            #
            # Erhöhtes Risiko
            #

            if item.risk_level == "HIGH":

                alerts.append(
                    AlertResult(
                        title="Erhöhtes Risiko",

                        message=(
                            f"{item.symbol} besitzt aktuell "
                            f"ein hohes Risikoniveau."
                        ),

                        severity="warning",

                        symbol=item.symbol,

                        profile_name=profile_name,

                        reason="Risk Level HIGH"
                    )
                )

            #
            # BUY-Signal
            #

            if item.signal == "BUY":

                alerts.append(
                    AlertResult(
                        title="BUY-Signal",

                        message=(
                            f"{item.symbol} besitzt aktuell "
                            f"ein BUY-Signal."
                        ),

                        severity="success",

                        symbol=item.symbol,

                        profile_name=profile_name,

                        reason=(
                            "Signal Engine liefert BUY"
                        )
                    )
                )

        return alerts
