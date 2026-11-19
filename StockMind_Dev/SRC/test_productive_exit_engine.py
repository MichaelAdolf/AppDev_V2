import unittest
from types import SimpleNamespace
from stockmind.application.exit.productive_exit_engine import ProductiveExitEngine
from stockmind.domain.exit.exit_strategy import ExitStrategy
class ProductiveExitEngineTest(unittest.TestCase):
 def item(self,**overrides):
  data=dict(position_id='p1',symbol='NVDA',entry_profile='balanced',current_price=109.0,first_purchase_date='2026-10-01',weighted_purchase_price=100.0,holding_days=30,remaining_strategy_days=30,score_change=-2.0,confidence_change=-.02,current_signal='BUY',current_risk='MEDIUM',attention_level='NORMAL');data.update(overrides);return SimpleNamespace(**data)
 def test_target_reached_results_in_exit_review(self):
  decision=ProductiveExitEngine().evaluate(self.item(),ExitStrategy('BASELINE_8PCT_60D'),'FALLBACK_BASELINE','INSUFFICIENT_VALIDATION',[])
  self.assertEqual(decision.status,'EXIT_REVIEW');self.assertIn('TARGET_REACHED',decision.reasons)
 def test_near_end_without_trigger_is_watch(self):
  decision=ProductiveExitEngine().evaluate(self.item(current_price=103.0,holding_days=52,remaining_strategy_days=8),ExitStrategy('BASELINE_8PCT_60D'),'FALLBACK_BASELINE','INSUFFICIENT_VALIDATION',[])
  self.assertEqual(decision.status,'WATCH')
 def test_regular_position_is_hold(self):
  decision=ProductiveExitEngine().evaluate(self.item(current_price=103.0),ExitStrategy('BASELINE_8PCT_60D'),'FALLBACK_BASELINE','INSUFFICIENT_VALIDATION',[])
  self.assertEqual(decision.status,'HOLD')
if __name__=='__main__':unittest.main()
