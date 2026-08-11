(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python scripts/test_historical_success_engine.py     
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\test_historical_success_engine.py", line 55, in <module>
    main()
    ~~~~^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\test_historical_success_engine.py", line 25, in main
    result = engine.analyze(
        symbol=symbol,
    ...<5 lines>...
        min_quality="MEDIUM"
    )
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\domain\historical_success\historical_success_engine.py", line 161, in analyze
    SimilarityCandidate(
    ~~~~~~~~~~~~~~~~~~~^
        trading_date=row.name.date()
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<5 lines>...
        max_future_high=max_future_high
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
TypeError: SimilarityCandidate.__init__() got an unexpected keyword argument 'trading_date'
