import unittest
from types import SimpleNamespace
from unittest.mock import patch

from stockmind.application.strategy.activate_fitted_profile_use_case import ActivateFittedProfileUseCase


class FittedProfileActivationTest(unittest.TestCase):
    @patch(
        "stockmind.application.strategy.activate_fitted_profile_use_case."
        "IndividualProfileActivationOrchestrator"
    )
    def test_only_validated_candidate_can_be_activated(self, orchestrator_type):
        active = SimpleNamespace(id="p1", symbol="NVDA", status="ACTIVE")
        orchestrator_type.return_value.execute.return_value = SimpleNamespace(
            profile=active
        )

        result = ActivateFittedProfileUseCase().execute("p1")

        orchestrator_type.return_value.execute.assert_called_once_with("p1")
        self.assertEqual(result.status, "ACTIVE")

    @patch(
        "stockmind.application.strategy.activate_fitted_profile_use_case."
        "IndividualProfileActivationOrchestrator"
    )
    def test_non_validated_candidate_is_rejected(self, orchestrator_type):
        orchestrator_type.return_value.execute.side_effect = ValueError(
            "Nur ein VALIDATED Fitted Profile darf aktiviert werden."
        )

        with self.assertRaises(ValueError):
            ActivateFittedProfileUseCase().execute("p1")


if __name__ == "__main__":
    unittest.main()
