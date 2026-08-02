from stockmind.application.data_quality.data_quality_report import (
    DataQualityReport
)

from stockmind.domain.entities.market_data import (
    MarketDataPoint
)


class MarketDataValidator:

    def validate(
        self,
        data: list[MarketDataPoint]
    ) -> DataQualityReport:

        errors = []

        warnings = []

        if not data:

            errors.append(
                "No market data available."
            )

        for point in data:

            if point.close_price <= 0:

                errors.append(
                    f"{point.symbol}: Invalid close price."
                )

            if point.volume < 0:

                errors.append(
                    f"{point.symbol}: Invalid volume."
                )

        return DataQualityReport(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
``
