import unittest
from types import SimpleNamespace
from stockmind.application.exit.exit_simulation_use_case import ExitSimulationUseCase
from stockmind.domain.exit.exit_strategy import ExitStrategy
class ExitSimulationTest(unittest.TestCase):
 def test_baseline_exits_when_target_is_reached(self):
  period=SimpleNamespace(symbol='NVDA',profile_name='balanced',start_date='2026-01-01',entry_price=100.0)
  prices=[SimpleNamespace(trading_date='2026-01-01',close_price=100.0),SimpleNamespace(trading_date='2026-01-10',close_price=105.0),SimpleNamespace(trading_date='2026-01-20',close_price=108.5)]
  result=ExitSimulationUseCase().simulate(period,prices,[],ExitStrategy('BASELINE'))
  self.assertEqual(result.exit_reason,'TARGET_REACHED');self.assertAlmostEqual(result.return_pct,8.5);self.assertEqual(result.holding_days,19)
 def test_stop_loss_can_exit_before_time_limit(self):
  period=SimpleNamespace(symbol='NVDA',profile_name='balanced',start_date='2026-01-01',entry_price=100.0)
  prices=[SimpleNamespace(trading_date='2026-01-01',close_price=100.0),SimpleNamespace(trading_date='2026-01-05',close_price=94.0)]
  result=ExitSimulationUseCase().simulate(period,prices,[],ExitStrategy('STOP',stop_loss_pct=.05))
  self.assertEqual(result.exit_reason,'STOP_LOSS');self.assertAlmostEqual(result.return_pct,-6.0)
if __name__=='__main__':unittest.main()
