(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python scripts/test_repository.py
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\test_repository.py", line 3, in <module>
    from stockmind.domain.entities.analysis_run import (AnalysisRun)
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\domain\entities\analysis_run.py", line 2, in <module>
    from datetime import datatime
ImportError: cannot import name 'datatime' from 'datetime' (C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\datetime.py). Did you mean: 'datetime'?
