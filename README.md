(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python scripts/refresh_chart_data.py
>> 
Refreshing OHLC chart data for AAPL
Refreshing OHLC chart data for ALV
Refreshing OHLC chart data for ALV.DE
Refreshing OHLC chart data for AMD
Refreshing OHLC chart data for AMZN
Refreshing OHLC chart data for ASML
Refreshing OHLC chart data for AVGO
Refreshing OHLC chart data for DEFT
Refreshing OHLC chart data for DRO.AX
Refreshing OHLC chart data for GEV
Refreshing OHLC chart data for GOOGL
Refreshing OHLC chart data for MUV2
HTTP Error 404: {"quoteSummary":{"result":null,"error":{"code":"Not Found","description":"Quote not found for symbol: MUV2"}}}
$MUV2: possibly delisted; no price data found  (period=5y) (Yahoo error = "No data found, symbol may be delisted")
Refreshing OHLC chart data for NFLX
Refreshing OHLC chart data for NVDA
Refreshing OHLC chart data for SAP
OHLC chart data refresh complete.
(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python -m unittest tests.test_exit_research_validation tests.test_exit_strategy_research tests.test_portfolio_intelligence
>> 
..FF.
======================================================================
FAIL: test_baseline_exits_when_target_is_reached (tests.test_exit_strategy_research.ExitSimulationTest.test_baseline_exits_when_target_is_reached)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\tests\test_exit_strategy_research.py", line 10, in test_baseline_exits_when_target_is_reached
    self.assertEqual(result.exit_reason,'TARGET_REACHED');self.assertAlmostEqual(result.return_pct,8.5);self.assertEqual(result.holding_days,19)
                                                          ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 8.000000000000007 != 8.5 within 7 places (0.4999999999999929 difference)

======================================================================
FAIL: test_stop_loss_can_exit_before_time_limit (tests.test_exit_strategy_research.ExitSimulationTest.test_stop_loss_can_exit_before_time_limit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\tests\test_exit_strategy_research.py", line 15, in test_stop_loss_can_exit_before_time_limit
    self.assertEqual(result.exit_reason,'STOP_LOSS');self.assertAlmostEqual(result.return_pct,-6.0)
                                                     ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: -5.000000000000004 != -6.0 within 7 places (0.9999999999999956 difference)

----------------------------------------------------------------------
Ran 5 tests in 0.006s

FAILED (failures=2)
