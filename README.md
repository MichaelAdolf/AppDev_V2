from datetime import datetime

from stockmind.domain.entities.analysis_run import (
    AnalysisRun
)

from stockmind.domain.enums.run_status import (
    RunStatus
)

from stockmind.infrastructure.repositories.analysis_run_repository import (
    AnalysisRunRepository
)

repo = AnalysisRunRepository()

run = AnalysisRun(
    run_id="RUN-001",
    started_at=datetime.now(),
    status=RunStatus.RUNNING,
    watchlist_name="default"
)

repo.add(run)

print("Run gespeichert.")
