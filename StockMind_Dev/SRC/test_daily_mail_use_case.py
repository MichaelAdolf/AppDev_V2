import unittest
from types import SimpleNamespace
from unittest.mock import patch
from stockmind.application.notifications.daily_mail_use_case import DailyMailUseCase
from stockmind.application.notifications.daily_mail_renderer import DailyMailRenderer

class DailyMailUseCaseTest(unittest.TestCase):
 @patch("stockmind.application.notifications.daily_mail_use_case.ProfileComparisonDashboardUseCase")
 @patch("stockmind.application.notifications.daily_mail_use_case.WatchlistDashboardUseCase")
 @patch("stockmind.application.notifications.daily_mail_use_case.DailyIntelligenceDashboardUseCase")
 def test_buy_section_contains_stock_if_any_profile_is_buy(self,intel,watch,comparison):
  intel.return_value.load.return_value=SimpleNamespace(latest_trading_date="2026-09-25",previous_trading_date="2026-09-24",items=[])
  watch.return_value.load.return_value=SimpleNamespace(stocks=[SimpleNamespace(symbol="NVDA",company_name="Nvidia")])
  comparison.return_value.load.return_value=SimpleNamespace(entries=[SimpleNamespace(profile_name="conservative",signal="HOLD",current_buy_signal=False,target_hit_rate=.7,complete_period_count=30),SimpleNamespace(profile_name="balanced",signal="HOLD",current_buy_signal=True,target_hit_rate=.84,complete_period_count=38),SimpleNamespace(profile_name="aggressive",signal="HOLD",current_buy_signal=False,target_hit_rate=.75,complete_period_count=60)])
  result=DailyMailUseCase().build();self.assertEqual(len(result.buy_signal_stocks),1);self.assertEqual(result.buy_signal_stocks[0].profiles[1].signal,"BUY")
  html=DailyMailRenderer().render(result);self.assertIn("84%",html);self.assertIn("38 Perioden",html)
if __name__=="__main__":unittest.main()
