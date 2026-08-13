(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python scripts/test_latest_analysis.py
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\test_latest_analysis.py", line 1, in <module>
    from stockmind.application.use_cases.run_analysis_use_case import ( RunAnalysisUseCase )
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\use_cases\run_analysis_use_case.py", line 3, in <module>
    from stockmind.application.use_cases.analyze_stock_use_case import ( AnalyzeStockUseCase )
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\use_cases\analyze_stock_use_case.py", line 97, in <module>
    from stockmind.domain.history.analysis_detail_entry import AnalysisDetailEntry
ImportError: cannot import name 'AnalysisDetailEntry' from 'stockmind.domain.history.analysis_detail_entry' (D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\domain\history\analysis_detail_entry.py)
