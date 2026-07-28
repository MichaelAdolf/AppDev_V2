from datetime import datetime
from uuid import uuid4

from stockmind.domain.entities.analysis_run import (
    AnalysisRun
)

from stockmind.domain.enums.run_status import (
    RunStatus
)


class CreateAnalysisRunUseCase:

    def execute(
        self,
        watchlist_name: str
    ) -> AnalysisRun:

        return AnalysisRun(
            run_id=str(uuid4()),
            started_at=datetime.now(),
            status=RunStatus.PENDING,
            watchlist_name=watchlist_name
        )
