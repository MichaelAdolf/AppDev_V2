from stockmind.domain.entities.analysis_run import (
    AnalysisRun
)

from stockmind.infrastructure.database.database import (
    SessionLocal
)

from stockmind.infrastructure.database.models import (
    AnalysisRunModel
)


class AnalysisRunRepository:

    def add(
        self,
        run: AnalysisRun
    ) -> None:

        session = SessionLocal()

        try:

            db_run = AnalysisRunModel(
                run_id=run.run_id,
                status=run.status.value,
                watchlist_name=run.watchlist_name,
                started_at=run.started_at
            )

            session.add(
                db_run
            )

            session.commit()

        finally:

            session.close()
