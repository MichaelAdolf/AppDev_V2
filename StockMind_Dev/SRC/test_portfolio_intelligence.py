import unittest
from types import SimpleNamespace
from unittest.mock import patch
from stockmind.application.portfolio.portfolio_intelligence_use_case import PortfolioIntelligenceUseCase
class PortfolioIntelligenceTest(unittest.TestCase):
 @patch('stockmind.application.portfolio.portfolio_intelligence_use_case.LatestAnalysisRepository')
 @patch('stockmind.application.portfolio.portfolio_intelligence_use_case.ChartDataRepository')
 @patch('stockmind.application.portfolio.portfolio_intelligence_use_case.PortfolioRepository')
 @patch('stockmind.application.portfolio.portfolio_intelligence_use_case.date')
 def test_target_reached_and_deterioration_are_attention_reasons(self,date_type,repo_type,chart_type,latest_type):
  date_type.today.return_value=__import__('datetime').date(2026,11,1);date_type.fromisoformat.side_effect=__import__('datetime').date.fromisoformat
  pos=SimpleNamespace(id='p1',symbol='NVDA',company_name='Nvidia',purchase_price=100.0,quantity=10.0,purchase_fees=0.0,purchase_date='2026-10-01',entry_profile='balanced',entry_opportunity_score=82.0,entry_confidence=.85,entry_risk='MEDIUM',entry_signal='BUY')
  repo_type.return_value.load_open_positions.return_value=[pos];repo_type.return_value.load_lots_for_position.return_value=[];chart_type.return_value.load_by_symbol.return_value=[SimpleNamespace(close_price=109.0)]
  latest_type.return_value.load_all.side_effect=lambda p:[SimpleNamespace(symbol='NVDA',opportunity_score=68.0,confidence=.65,risk_level='HIGH',signal='HOLD')] if p=='balanced' else []
  item=PortfolioIntelligenceUseCase().load()[0];self.assertTrue(item.target_reached);self.assertIn('TARGET_REACHED',item.attention_reasons);self.assertIn('SCORE_DETERIORATED',item.attention_reasons);self.assertEqual(item.attention_level,'CRITICAL')
if __name__=='__main__':unittest.main()
