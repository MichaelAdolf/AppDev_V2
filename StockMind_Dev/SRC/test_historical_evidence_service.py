import unittest
from types import SimpleNamespace
from unittest.mock import patch

from stockmind.application.history.historical_evidence_service import HistoricalEvidenceService


class HistoricalEvidenceServiceTest(unittest.TestCase):
    @patch("stockmind.application.history.historical_evidence_service.BuyPeriodDashboardUseCase")
    def test_periods_have_priority(self, use_case_type):
        use_case_type.return_value.load.return_value = SimpleNamespace(
            statistics=SimpleNamespace(
                complete_period_count=25,
                incomplete_period_count=2,
                target_hit_rate=0.8,
                below_target_rate=0.08,
                flat_rate=0.04,
                negative_rate=0.08,
            ),
            active_period=None,
        )
        setup = SimpleNamespace(
            success_rate=0.5, sample_quality="HIGH", complete_count=50,
            target_hit_rate=0.5, below_target_rate=0.2,
            flat_rate=0.1, negative_rate=0.2, incomplete_count=0,
            average_similarity=0.9,
        )
        result = HistoricalEvidenceService().build("AAPL", "balanced", setup)
        self.assertEqual(result.source, "BUY_PERIODS")
        self.assertEqual(result.success_rate, 0.8)
        self.assertEqual(result.sample_quality, "MEDIUM")

    @patch("stockmind.application.history.historical_evidence_service.BuyPeriodDashboardUseCase")
    def test_setup_fallback_without_complete_periods(self, use_case_type):
        use_case_type.return_value.load.return_value = SimpleNamespace(
            statistics=SimpleNamespace(
                complete_period_count=0,
                incomplete_period_count=3,
                target_hit_rate=0.0,
                below_target_rate=0.0,
                flat_rate=0.0,
                negative_rate=0.0,
            ),
            active_period=None,
        )
        setup = SimpleNamespace(
            success_rate=0.65, sample_quality="HIGH", complete_count=80,
            target_hit_rate=0.65, below_target_rate=0.1,
            flat_rate=0.05, negative_rate=0.2, incomplete_count=1,
            average_similarity=0.88,
        )
        result = HistoricalEvidenceService().build("AAPL", "balanced", setup)
        self.assertEqual(result.source, "SETUP_FALLBACK")
        self.assertEqual(result.success_rate, 0.65)


if __name__ == "__main__":
    unittest.main()
