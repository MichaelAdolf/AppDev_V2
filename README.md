(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python scripts/refresh_dashboard_data.py                                            
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\refresh_dashboard_data.py", line 54, in <module>
    main()
    ~~~~^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\refresh_dashboard_data.py", line 27, in main
    get_symbols()
    ~~~~~~~~~~~^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\refresh_dashboard_data.py", line 14, in get_symbols
    .load_active_symbols()
     ^^^^^^^^^^^^^^^^^^^
AttributeError: 'WatchlistRepository' object has no attribute 'load_active_symbols'
