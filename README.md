(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python scripts/setup_database.py
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\setup_database.py", line 9, in <module>
    from stockmind.infrastructure.database.models import (
        AnalysisRunModel
    )
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\infrastructure\database\models.py", line 9, in <module>
    class AnalysisRunModel(Base):
    ...<15 lines>...
        started_at: Mapped[DateTime]
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
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\sqlalchemy\orm\decl_base.py", line 573, in __init__
    self._extract_mappable_attributes()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\sqlalchemy\orm\decl_base.py", line 1567, in _extract_mappable_attributes
    value.declarative_scan(
    ~~~~~~~~~~~~~~~~~~~~~~^
        self,
        ^^^^^
    ...<7 lines>...
        is_dataclass,
        ^^^^^^^^^^^^^
    )
    ^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\sqlalchemy\orm\properties.py", line 722, in declarative_scan
    self._init_column_for_annotation(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        cls,
        ^^^^
    ...<4 lines>...
        originating_module,
        ^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\sqlalchemy\orm\properties.py", line 898, in _init_column_for_annotation
    raise orm_exc.MappedAnnotationError(
    ...<3 lines>...
    )
sqlalchemy.orm.exc.MappedAnnotationError: The type provided inside the 'started_at' attribute Mapped annotation is the SQLAlchemy type <class 'sqlalchemy.sql.sqltypes.DateTime'>. Expected a Python type instead
