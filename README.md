Folgende Fehler treten auf:
(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python scripts/apply_fx1_integration_patch.py
>> 
Patched src\stockmind\application\use_cases\analyze_stock_use_case.py
Patched src\stockmind\application\strategy\individual_history_backfill_use_case.py
Indicator history block not found: scripts\refresh_indicator_chart_data.py
(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python -m unittest tests.test_eur_market_data_service tests.test_chart_data_repository_quality tests.test_exit_strategy_research tests.test_productive_exit_engine
........
----------------------------------------------------------------------
Ran 8 tests in 0.095s

OK
(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python scripts/rebuild_eur_market_data.py
>> 
Rebuilding all market history in EUR...
Refreshing EUR-normalized OHLC chart data for AAPL
Refreshing EUR-normalized OHLC chart data for ALV
Refreshing EUR-normalized OHLC chart data for ALV.DE
Refreshing EUR-normalized OHLC chart data for AMD
Refreshing EUR-normalized OHLC chart data for AMZN
Refreshing EUR-normalized OHLC chart data for ASML
Refreshing EUR-normalized OHLC chart data for AVGO
Refreshing EUR-normalized OHLC chart data for DEFT
Refreshing EUR-normalized OHLC chart data for DRO.AX
Refreshing EUR-normalized OHLC chart data for GEV
Refreshing EUR-normalized OHLC chart data for GOOGL
Refreshing EUR-normalized OHLC chart data for MUV2
HTTP Error 404: {"quoteSummary":{"result":null,"error":{"code":"Not Found","description":"Quote not found for symbol: MUV2"}}}
$MUV2: possibly delisted; no price data found  (period=5y) (Yahoo error = "No data found, symbol may be delisted")
Skipping MUV2: no valid chart data
Refreshing EUR-normalized OHLC chart data for NFLX
Refreshing EUR-normalized OHLC chart data for NVDA
Refreshing EUR-normalized OHLC chart data for SAP
EUR-normalized chart data refresh complete.
Refreshing indicator chart data for AAPL
Refreshing indicator chart data for ALV
Refreshing indicator chart data for ALV.DE
Refreshing indicator chart data for AMD
Refreshing indicator chart data for AMZN
Refreshing indicator chart data for ASML
Refreshing indicator chart data for AVGO
Refreshing indicator chart data for DEFT
Refreshing indicator chart data for DRO.AX
Refreshing indicator chart data for GEV
Refreshing indicator chart data for GOOGL
Refreshing indicator chart data for MUV2
HTTP Error 404: {"quoteSummary":{"result":null,"error":{"code":"Not Found","description":"Quote not found for symbol: MUV2"}}}
$MUV2: possibly delisted; no price data found  (period=5y) (Yahoo error = "No data found, symbol may be delisted")
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\rebuild_eur_market_data.py", line 6, in <module>
    if __name__=='__main__':main()
                            ~~~~^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\rebuild_eur_market_data.py", line 5, in main
    print('Rebuilding all market history in EUR...');refresh_chart();refresh_indicators();print('EUR market-data rebuild complete. Run the normal StockMind refresh next to rebuild dependent histories.')
                                                                     ~~~~~~~~~~~~~~~~~~^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\refresh_indicator_chart_data.py", line 241, in main
    points = build_indicator_points(
        symbol
    )
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\refresh_indicator_chart_data.py", line 139, in build_indicator_points
    ta.trend.ADXIndicator(
    ~~~~~~~~~~~~~~~~~~~~~^
        high=data["High"],
        ^^^^^^^^^^^^^^^^^^
    ...<2 lines>...
        window=14
        ^^^^^^^^^
        )
        ^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\ta\trend.py", line 716, in __init__
    self._run()
    ~~~~~~~~~^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\ta\trend.py", line 730, in _run
    self._trs = np.zeros(len(self._close) - (self._window - 1))
                ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: negative dimensions are not allowed

Wenn ich streamlit ausführe, kommt folgende Fehlermeldung:
SyntaxError: File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\use_cases\analyze_stock_use_case.py", line 4 from stockmind.application.currency.eur_market_data_service import EurMarketDataService ^ SyntaxError: invalid syntax
Traceback:

File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\streamlit_app.py", line 6, in <module>
    from components.strategy_center_view import render as render_strategy_center
File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\components\strategy_center_view.py", line 3, in <module>
    from components.entry_strategy_research_view import render as render_entry_research
File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\components\entry_strategy_research_view.py", line 3, in <module>
    from stockmind.application.strategy.activate_fitted_profile_use_case import ActivateFittedProfileUseCase,DeactivateFittedProfileUseCase
File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\strategy\activate_fitted_profile_use_case.py", line 1, in <module>
    from stockmind.application.strategy.individual_profile_activation_orchestrator import IndividualProfileActivationOrchestrator
File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\strategy\individual_profile_activation_orchestrator.py", line 4, in <module>
    from stockmind.application.strategy.run_individual_analysis_use_case import RunIndividualAnalysisUseCase
File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\strategy\run_individual_analysis_use_case.py", line 1, in <module>
    from stockmind.application.use_cases.analyze_stock_use_case import AnalyzeStockUseCase
