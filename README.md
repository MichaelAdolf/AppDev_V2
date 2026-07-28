(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python scripts/setup_database.py
MODELS LOADED
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\setup_database.py", line 9, in <module>
    from stockmind.infrastructure.database.models import (
        AnalysisRunModel
    )
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\infrastructure\database\models.py", line 11, in <module>
    class AnalysisRunModel(Base):
    ...<17 lines>...
        )
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\sqlalchemy\orm\decl_api.py", line 849, in __init_subclass__
    _as_declarative(cls._sa_registry, cls, cls.__dict__)
    ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\sqlalchemy\orm\decl_base.py", line 245, in _as_declarative
    return _MapperConfig.setup_mapping(registry, cls, dict_, None, {})
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\sqlalchemy\orm\decl_base.py", line 326, in setup_mapping
    return _ClassScanMapperConfig(
        registry, cls_, dict_, table, mapper_kw
    )
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\sqlalchemy\orm\decl_base.py", line 579, in __init__
    self._setup_inheriting_columns(mapper_kw)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\sqlalchemy\orm\decl_base.py", line 1839, in _setup_inheriting_columns
    raise exc.InvalidRequestError(
    ...<3 lines>...
    )
sqlalchemy.exc.InvalidRequestError: Class <class 'stockmind.infrastructure.database.models.AnalysisRunModel'> does not have a __table__ or __tablename__ specified and does not inherit from an existing table-mapped class.
