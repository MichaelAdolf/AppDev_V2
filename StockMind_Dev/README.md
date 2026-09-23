# stockmind-platform
Modular stock analysis platform with Home Assistant, Node-RED, Jarvis and Streamlit integration.

StockMind ist eine modulare Aktienanalyse-Plattform.

Ziele:

    tägliche Marktanalyse
    Watchlist-Verwaltung
    technische Analyse
    Fundamentalanalyse
    Backtesting
    Home Assistant Integration
    Node-RED Integration
    Jarvis Integration
    Streamlit Dashboard

Architektur:

    Clean Architecture
    SOLID
    Domain Driven Design

```
stockmind-platform
├─ .dockerignore
├─ .venv
│  ├─ etc
│  │  └─ jupyter
│  │     └─ nbconfig
│  │        └─ notebook.d
│  │           └─ pydeck.json
│  ├─ Include
│  │  └─ site
│  │     └─ python3.13
│  │        └─ greenlet
│  │           └─ greenlet.h
│  ├─ Lib
│  │  └─ site-packages
│  │     ├─ ada92cb5d92a588d1b93__mypyc.cp313-win_amd64.pyd
│  │     ├─ altair
│  │     │  ├─ datasets
│  │     │  │  ├─ _cache.py
│  │     │  │  ├─ _constraints.py
│  │     │  │  ├─ _data.py
│  │     │  │  ├─ _exceptions.py
│  │     │  │  ├─ _loader.py
│  │     │  │  ├─ _metadata
│  │     │  │  │  ├─ metadata.csv.gz
│  │     │  │  │  ├─ metadata.parquet
│  │     │  │  │  └─ schemas.json.gz
│  │     │  │  ├─ _reader.py
│  │     │  │  ├─ _readimpl.py
│  │     │  │  ├─ _typing.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ expr
│  │     │  │  ├─ consts.py
│  │     │  │  ├─ core.py
│  │     │  │  ├─ funcs.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ jupyter
│  │     │  │  ├─ js
│  │     │  │  │  ├─ index.js
│  │     │  │  │  └─ README.md
│  │     │  │  ├─ jupyter_chart.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ py.typed
│  │     │  ├─ theme.py
│  │     │  ├─ typing
│  │     │  │  └─ __init__.py
│  │     │  ├─ utils
│  │     │  │  ├─ compiler.py
│  │     │  │  ├─ core.py
│  │     │  │  ├─ data.py
│  │     │  │  ├─ deprecation.py
│  │     │  │  ├─ display.py
│  │     │  │  ├─ execeval.py
│  │     │  │  ├─ html.py
│  │     │  │  ├─ mimebundle.py
│  │     │  │  ├─ plugin_registry.py
│  │     │  │  ├─ save.py
│  │     │  │  ├─ schemapi.py
│  │     │  │  ├─ selection.py
│  │     │  │  ├─ server.py
│  │     │  │  ├─ _dfi_types.py
│  │     │  │  ├─ _importers.py
│  │     │  │  ├─ _show.py
│  │     │  │  ├─ _transformed_data.py
│  │     │  │  ├─ _vegafusion_data.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ vegalite
│  │     │  │  ├─ api.py
│  │     │  │  ├─ data.py
│  │     │  │  ├─ display.py
│  │     │  │  ├─ schema.py
│  │     │  │  ├─ v6
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ compiler.py
│  │     │  │  │  ├─ data.py
│  │     │  │  │  ├─ display.py
│  │     │  │  │  ├─ schema
│  │     │  │  │  │  ├─ channels.py
│  │     │  │  │  │  ├─ core.py
│  │     │  │  │  │  ├─ mixins.py
│  │     │  │  │  │  ├─ vega-lite-schema.json
│  │     │  │  │  │  ├─ vega-themes.json
│  │     │  │  │  │  ├─ _config.py
│  │     │  │  │  │  ├─ _typing.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ theme.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _magics.py
│  │     │  └─ __init__.py
│  │     ├─ altair-6.2.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ annotated_doc
│  │     │  ├─ main.py
│  │     │  ├─ py.typed
│  │     │  └─ __init__.py
│  │     ├─ annotated_doc-0.0.5.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ annotated_types
│  │     │  ├─ py.typed
│  │     │  ├─ test_cases.py
│  │     │  └─ __init__.py
│  │     ├─ annotated_types-0.7.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ anyio
│  │     │  ├─ abc
│  │     │  │  ├─ _eventloop.py
│  │     │  │  ├─ _resources.py
│  │     │  │  ├─ _sockets.py
│  │     │  │  ├─ _streams.py
│  │     │  │  ├─ _subprocesses.py
│  │     │  │  ├─ _tasks.py
│  │     │  │  ├─ _testing.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ from_thread.py
│  │     │  ├─ functools.py
│  │     │  ├─ itertools.py
│  │     │  ├─ lowlevel.py
│  │     │  ├─ py.typed
│  │     │  ├─ pytest_plugin.py
│  │     │  ├─ streams
│  │     │  │  ├─ buffered.py
│  │     │  │  ├─ file.py
│  │     │  │  ├─ memory.py
│  │     │  │  ├─ stapled.py
│  │     │  │  ├─ text.py
│  │     │  │  ├─ tls.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ to_interpreter.py
│  │     │  ├─ to_process.py
│  │     │  ├─ to_thread.py
│  │     │  ├─ _backends
│  │     │  │  ├─ _asyncio.py
│  │     │  │  ├─ _trio.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _core
│  │     │  │  ├─ _asyncio_selector_thread.py
│  │     │  │  ├─ _contextmanagers.py
│  │     │  │  ├─ _eventloop.py
│  │     │  │  ├─ _exceptions.py
│  │     │  │  ├─ _fileio.py
│  │     │  │  ├─ _resources.py
│  │     │  │  ├─ _signals.py
│  │     │  │  ├─ _sockets.py
│  │     │  │  ├─ _streams.py
│  │     │  │  ├─ _subprocesses.py
│  │     │  │  ├─ _synchronization.py
│  │     │  │  ├─ _tasks.py
│  │     │  │  ├─ _tempfile.py
│  │     │  │  ├─ _testing.py
│  │     │  │  ├─ _typedattr.py
│  │     │  │  └─ __init__.py
│  │     │  └─ __init__.py
│  │     ├─ anyio-4.14.2.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ scm_file_list.json
│  │     │  ├─ scm_version.json
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ attr
│  │     │  ├─ converters.py
│  │     │  ├─ converters.pyi
│  │     │  ├─ exceptions.py
│  │     │  ├─ exceptions.pyi
│  │     │  ├─ filters.py
│  │     │  ├─ filters.pyi
│  │     │  ├─ py.typed
│  │     │  ├─ setters.py
│  │     │  ├─ setters.pyi
│  │     │  ├─ validators.py
│  │     │  ├─ validators.pyi
│  │     │  ├─ _cmp.py
│  │     │  ├─ _cmp.pyi
│  │     │  ├─ _compat.py
│  │     │  ├─ _config.py
│  │     │  ├─ _funcs.py
│  │     │  ├─ _make.py
│  │     │  ├─ _next_gen.py
│  │     │  ├─ _typing_compat.pyi
│  │     │  ├─ _version_info.py
│  │     │  ├─ _version_info.pyi
│  │     │  ├─ __init__.py
│  │     │  └─ __init__.pyi
│  │     ├─ attrs
│  │     │  ├─ converters.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ filters.py
│  │     │  ├─ py.typed
│  │     │  ├─ setters.py
│  │     │  ├─ validators.py
│  │     │  ├─ __init__.py
│  │     │  └─ __init__.pyi
│  │     ├─ attrs-26.1.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ beautifulsoup4-4.15.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  ├─ AUTHORS
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ blinker
│  │     │  ├─ base.py
│  │     │  ├─ py.typed
│  │     │  ├─ _utilities.py
│  │     │  └─ __init__.py
│  │     ├─ blinker-1.9.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ bs4
│  │     │  ├─ builder
│  │     │  │  ├─ _html5lib.py
│  │     │  │  ├─ _htmlparser.py
│  │     │  │  ├─ _lxml.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ css.py
│  │     │  ├─ dammit.py
│  │     │  ├─ diagnose.py
│  │     │  ├─ element.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ filter.py
│  │     │  ├─ formatter.py
│  │     │  ├─ py.typed
│  │     │  ├─ _deprecation.py
│  │     │  ├─ _typing.py
│  │     │  ├─ _warnings.py
│  │     │  └─ __init__.py
│  │     ├─ certifi
│  │     │  ├─ cacert.pem
│  │     │  ├─ core.py
│  │     │  ├─ py.typed
│  │     │  ├─ tests
│  │     │  │  ├─ test_certify.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ __init__.py
│  │     │  └─ __main__.py
│  │     ├─ certifi-2026.7.22.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ cffi
│  │     │  ├─ api.py
│  │     │  ├─ backend_ctypes.py
│  │     │  ├─ cffi_opcode.py
│  │     │  ├─ commontypes.py
│  │     │  ├─ cparser.py
│  │     │  ├─ error.py
│  │     │  ├─ ffiplatform.py
│  │     │  ├─ gen_src.py
│  │     │  ├─ lock.py
│  │     │  ├─ model.py
│  │     │  ├─ parse_c_type.h
│  │     │  ├─ pkgconfig.py
│  │     │  ├─ recompiler.py
│  │     │  ├─ setuptools_ext.py
│  │     │  ├─ vengine_cpy.py
│  │     │  ├─ vengine_gen.py
│  │     │  ├─ verifier.py
│  │     │  ├─ _cffi_errors.h
│  │     │  ├─ _cffi_gen_src.py
│  │     │  ├─ _cffi_include.h
│  │     │  ├─ _embedding.h
│  │     │  ├─ _imp_emulation.py
│  │     │  ├─ _shimmed_dist_utils.py
│  │     │  └─ __init__.py
│  │     ├─ cffi-2.1.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ charset_normalizer
│  │     │  ├─ api.py
│  │     │  ├─ cd.cp313-win_amd64.pyd
│  │     │  ├─ cd.py
│  │     │  ├─ cli
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __main__.py
│  │     │  ├─ constant.py
│  │     │  ├─ legacy.py
│  │     │  ├─ md.cp313-win_amd64.pyd
│  │     │  ├─ md.py
│  │     │  ├─ models.py
│  │     │  ├─ py.typed
│  │     │  ├─ utils.py
│  │     │  ├─ version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __main__.py
│  │     ├─ charset_normalizer-3.4.9.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ click
│  │     │  ├─ core.py
│  │     │  ├─ decorators.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ formatting.py
│  │     │  ├─ globals.py
│  │     │  ├─ parser.py
│  │     │  ├─ py.typed
│  │     │  ├─ shell_completion.py
│  │     │  ├─ termui.py
│  │     │  ├─ testing.py
│  │     │  ├─ types.py
│  │     │  ├─ utils.py
│  │     │  ├─ _compat.py
│  │     │  ├─ _termui_impl.py
│  │     │  ├─ _textwrap.py
│  │     │  ├─ _utils.py
│  │     │  ├─ _winconsole.py
│  │     │  └─ __init__.py
│  │     ├─ click-8.4.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ colorama
│  │     │  ├─ ansi.py
│  │     │  ├─ ansitowin32.py
│  │     │  ├─ initialise.py
│  │     │  ├─ tests
│  │     │  │  ├─ ansitowin32_test.py
│  │     │  │  ├─ ansi_test.py
│  │     │  │  ├─ initialise_test.py
│  │     │  │  ├─ isatty_test.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ winterm_test.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ win32.py
│  │     │  ├─ winterm.py
│  │     │  └─ __init__.py
│  │     ├─ colorama-0.4.6.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ curl_cffi
│  │     │  ├─ aio.py
│  │     │  ├─ cli
│  │     │  │  ├─ doctor.py
│  │     │  │  ├─ output.py
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ pro.py
│  │     │  │  ├─ request.py
│  │     │  │  ├─ run.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ const.py
│  │     │  ├─ curl.py
│  │     │  ├─ fingerprints.py
│  │     │  ├─ py.typed
│  │     │  ├─ requests
│  │     │  │  ├─ cache.py
│  │     │  │  ├─ cookies.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ headers.py
│  │     │  │  ├─ impersonate.py
│  │     │  │  ├─ models.py
│  │     │  │  ├─ session.py
│  │     │  │  ├─ streams.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ websockets.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ utils.py
│  │     │  ├─ _asyncio_selector.py
│  │     │  ├─ _wrapper.pyd
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __version__.py
│  │     ├─ curl_cffi-0.16.0.dist-info
│  │     │  ├─ DELVEWHEEL
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ curl_cffi.libs
│  │     │  └─ libcurl-impersonate-ec8ead0e422fe4ae62a99233a63f6007.dll
│  │     ├─ dateutil
│  │     │  ├─ easter.py
│  │     │  ├─ parser
│  │     │  │  ├─ isoparser.py
│  │     │  │  ├─ _parser.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ relativedelta.py
│  │     │  ├─ rrule.py
│  │     │  ├─ tz
│  │     │  │  ├─ tz.py
│  │     │  │  ├─ win.py
│  │     │  │  ├─ _common.py
│  │     │  │  ├─ _factories.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ tzwin.py
│  │     │  ├─ utils.py
│  │     │  ├─ zoneinfo
│  │     │  │  ├─ dateutil-zoneinfo.tar.gz
│  │     │  │  ├─ rebuild.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _common.py
│  │     │  ├─ _version.py
│  │     │  └─ __init__.py
│  │     ├─ dotenv
│  │     │  ├─ cli.py
│  │     │  ├─ ipython.py
│  │     │  ├─ main.py
│  │     │  ├─ parser.py
│  │     │  ├─ py.typed
│  │     │  ├─ variables.py
│  │     │  ├─ version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __main__.py
│  │     ├─ fastapi
│  │     │  ├─ .agents
│  │     │  │  └─ skills
│  │     │  │     └─ fastapi
│  │     │  │        ├─ references
│  │     │  │        │  ├─ dependencies.md
│  │     │  │        │  ├─ other-tools.md
│  │     │  │        │  ├─ path-operations.md
│  │     │  │        │  ├─ pydantic.md
│  │     │  │        │  ├─ responses.md
│  │     │  │        │  └─ streaming.md
│  │     │  │        └─ SKILL.md
│  │     │  ├─ applications.py
│  │     │  ├─ background.py
│  │     │  ├─ cli.py
│  │     │  ├─ concurrency.py
│  │     │  ├─ datastructures.py
│  │     │  ├─ dependencies
│  │     │  │  ├─ models.py
│  │     │  │  ├─ utils.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ encoders.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ exception_handlers.py
│  │     │  ├─ logger.py
│  │     │  ├─ middleware
│  │     │  │  ├─ asyncexitstack.py
│  │     │  │  ├─ cors.py
│  │     │  │  ├─ gzip.py
│  │     │  │  ├─ httpsredirect.py
│  │     │  │  ├─ trustedhost.py
│  │     │  │  ├─ wsgi.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ openapi
│  │     │  │  ├─ constants.py
│  │     │  │  ├─ docs.py
│  │     │  │  ├─ models.py
│  │     │  │  ├─ utils.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ params.py
│  │     │  ├─ param_functions.py
│  │     │  ├─ py.typed
│  │     │  ├─ requests.py
│  │     │  ├─ responses.py
│  │     │  ├─ routing.py
│  │     │  ├─ security
│  │     │  │  ├─ api_key.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ http.py
│  │     │  │  ├─ oauth2.py
│  │     │  │  ├─ open_id_connect_url.py
│  │     │  │  ├─ utils.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ sse.py
│  │     │  ├─ staticfiles.py
│  │     │  ├─ templating.py
│  │     │  ├─ testclient.py
│  │     │  ├─ types.py
│  │     │  ├─ utils.py
│  │     │  ├─ websockets.py
│  │     │  ├─ _compat
│  │     │  │  ├─ shared.py
│  │     │  │  ├─ v2.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ __init__.py
│  │     │  └─ __main__.py
│  │     ├─ fastapi-0.141.1.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ google
│  │     │  ├─ protobuf
│  │     │  │  ├─ any.py
│  │     │  │  ├─ any_pb2.py
│  │     │  │  ├─ api_pb2.py
│  │     │  │  ├─ compiler
│  │     │  │  │  ├─ plugin_pb2.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ descriptor.py
│  │     │  │  ├─ descriptor_database.py
│  │     │  │  ├─ descriptor_pb2.py
│  │     │  │  ├─ descriptor_pool.py
│  │     │  │  ├─ duration.py
│  │     │  │  ├─ duration_pb2.py
│  │     │  │  ├─ empty_pb2.py
│  │     │  │  ├─ field_mask_pb2.py
│  │     │  │  ├─ internal
│  │     │  │  │  ├─ api_implementation.py
│  │     │  │  │  ├─ builder.py
│  │     │  │  │  ├─ containers.py
│  │     │  │  │  ├─ decoder.py
│  │     │  │  │  ├─ encoder.py
│  │     │  │  │  ├─ enum_type_wrapper.py
│  │     │  │  │  ├─ extension_dict.py
│  │     │  │  │  ├─ field_mask.py
│  │     │  │  │  ├─ message_listener.py
│  │     │  │  │  ├─ python_edition_defaults.py
│  │     │  │  │  ├─ python_message.py
│  │     │  │  │  ├─ testing_refleaks.py
│  │     │  │  │  ├─ type_checkers.py
│  │     │  │  │  ├─ well_known_types.py
│  │     │  │  │  ├─ wire_format.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ json_format.py
│  │     │  │  ├─ message.py
│  │     │  │  ├─ message_factory.py
│  │     │  │  ├─ proto.py
│  │     │  │  ├─ proto_builder.py
│  │     │  │  ├─ proto_json.py
│  │     │  │  ├─ proto_text.py
│  │     │  │  ├─ pyext
│  │     │  │  │  ├─ cpp_message.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ reflection.py
│  │     │  │  ├─ runtime_version.py
│  │     │  │  ├─ service_reflection.py
│  │     │  │  ├─ source_context_pb2.py
│  │     │  │  ├─ struct_pb2.py
│  │     │  │  ├─ symbol_database.py
│  │     │  │  ├─ testdata
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ text_encoding.py
│  │     │  │  ├─ text_format.py
│  │     │  │  ├─ timestamp.py
│  │     │  │  ├─ timestamp_pb2.py
│  │     │  │  ├─ type_pb2.py
│  │     │  │  ├─ unknown_fields.py
│  │     │  │  ├─ util
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ wrappers_pb2.py
│  │     │  │  └─ __init__.py
│  │     │  └─ _upb
│  │     │     └─ _message.pyd
│  │     ├─ greenlet
│  │     │  ├─ CObjects.cpp
│  │     │  ├─ greenlet.cpp
│  │     │  ├─ greenlet.h
│  │     │  ├─ greenlet_allocator.hpp
│  │     │  ├─ greenlet_compiler_compat.hpp
│  │     │  ├─ greenlet_cpython_compat.hpp
│  │     │  ├─ greenlet_exceptions.hpp
│  │     │  ├─ greenlet_internal.hpp
│  │     │  ├─ greenlet_msvc_compat.hpp
│  │     │  ├─ greenlet_refs.hpp
│  │     │  ├─ greenlet_slp_switch.hpp
│  │     │  ├─ greenlet_thread_support.hpp
│  │     │  ├─ platform
│  │     │  │  ├─ setup_switch_x64_masm.cmd
│  │     │  │  ├─ switch_aarch64_gcc.h
│  │     │  │  ├─ switch_alpha_unix.h
│  │     │  │  ├─ switch_amd64_unix.h
│  │     │  │  ├─ switch_arm32_gcc.h
│  │     │  │  ├─ switch_arm32_ios.h
│  │     │  │  ├─ switch_arm64_masm.asm
│  │     │  │  ├─ switch_arm64_masm.obj
│  │     │  │  ├─ switch_arm64_msvc.h
│  │     │  │  ├─ switch_csky_gcc.h
│  │     │  │  ├─ switch_loongarch64_linux.h
│  │     │  │  ├─ switch_m68k_gcc.h
│  │     │  │  ├─ switch_mips_unix.h
│  │     │  │  ├─ switch_ppc64_aix.h
│  │     │  │  ├─ switch_ppc64_linux.h
│  │     │  │  ├─ switch_ppc_aix.h
│  │     │  │  ├─ switch_ppc_linux.h
│  │     │  │  ├─ switch_ppc_macosx.h
│  │     │  │  ├─ switch_ppc_unix.h
│  │     │  │  ├─ switch_riscv_unix.h
│  │     │  │  ├─ switch_s390_unix.h
│  │     │  │  ├─ switch_sh_gcc.h
│  │     │  │  ├─ switch_sparc_sun_gcc.h
│  │     │  │  ├─ switch_x32_unix.h
│  │     │  │  ├─ switch_x64_masm.asm
│  │     │  │  ├─ switch_x64_masm.obj
│  │     │  │  ├─ switch_x64_msvc.h
│  │     │  │  ├─ switch_x86_msvc.h
│  │     │  │  ├─ switch_x86_unix.h
│  │     │  │  └─ __init__.py
│  │     │  ├─ PyGreenlet.cpp
│  │     │  ├─ PyGreenlet.hpp
│  │     │  ├─ PyGreenletUnswitchable.cpp
│  │     │  ├─ PyModule.cpp
│  │     │  ├─ slp_platformselect.h
│  │     │  ├─ TBrokenGreenlet.cpp
│  │     │  ├─ tests
│  │     │  │  ├─ fail_clearing_run_switches.py
│  │     │  │  ├─ fail_cpp_exception.py
│  │     │  │  ├─ fail_initialstub_already_started.py
│  │     │  │  ├─ fail_slp_switch.py
│  │     │  │  ├─ fail_switch_three_greenlets.py
│  │     │  │  ├─ fail_switch_three_greenlets2.py
│  │     │  │  ├─ fail_switch_two_greenlets.py
│  │     │  │  ├─ leakcheck.py
│  │     │  │  ├─ test_contextvars.py
│  │     │  │  ├─ test_cpp.py
│  │     │  │  ├─ test_extension_interface.py
│  │     │  │  ├─ test_gc.py
│  │     │  │  ├─ test_generator.py
│  │     │  │  ├─ test_generator_nested.py
│  │     │  │  ├─ test_greenlet.py
│  │     │  │  ├─ test_greenlet_trash.py
│  │     │  │  ├─ test_interpreter_shutdown.py
│  │     │  │  ├─ test_leaks.py
│  │     │  │  ├─ test_stack_saved.py
│  │     │  │  ├─ test_throw.py
│  │     │  │  ├─ test_tracing.py
│  │     │  │  ├─ test_version.py
│  │     │  │  ├─ test_weakref.py
│  │     │  │  ├─ _test_extension.c
│  │     │  │  ├─ _test_extension.cp313-win_amd64.pyd
│  │     │  │  ├─ _test_extension_cpp.cp313-win_amd64.pyd
│  │     │  │  ├─ _test_extension_cpp.cpp
│  │     │  │  └─ __init__.py
│  │     │  ├─ TExceptionState.cpp
│  │     │  ├─ TGreenlet.cpp
│  │     │  ├─ TGreenlet.hpp
│  │     │  ├─ TGreenletGlobals.cpp
│  │     │  ├─ TMainGreenlet.cpp
│  │     │  ├─ TPythonState.cpp
│  │     │  ├─ TStackState.cpp
│  │     │  ├─ TThreadState.hpp
│  │     │  ├─ TThreadStateCreator.hpp
│  │     │  ├─ TThreadStateDestroy.cpp
│  │     │  ├─ TUserGreenlet.cpp
│  │     │  ├─ _greenlet.cp313-win_amd64.pyd
│  │     │  └─ __init__.py
│  │     ├─ greenlet-3.5.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  ├─ LICENSE
│  │     │  │  └─ LICENSE.PSF
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ h11
│  │     │  ├─ py.typed
│  │     │  ├─ _abnf.py
│  │     │  ├─ _connection.py
│  │     │  ├─ _events.py
│  │     │  ├─ _headers.py
│  │     │  ├─ _readers.py
│  │     │  ├─ _receivebuffer.py
│  │     │  ├─ _state.py
│  │     │  ├─ _util.py
│  │     │  ├─ _version.py
│  │     │  ├─ _writers.py
│  │     │  └─ __init__.py
│  │     ├─ h11-0.16.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ httptools
│  │     │  ├─ parser
│  │     │  │  ├─ cparser.pxd
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ parser.cp313-win_amd64.pyd
│  │     │  │  ├─ parser.pyi
│  │     │  │  ├─ parser.pyx
│  │     │  │  ├─ protocol.py
│  │     │  │  ├─ python.pxd
│  │     │  │  ├─ url_cparser.pxd
│  │     │  │  ├─ url_parser.cp313-win_amd64.pyd
│  │     │  │  ├─ url_parser.pyi
│  │     │  │  ├─ url_parser.pyx
│  │     │  │  └─ __init__.py
│  │     │  ├─ py.typed
│  │     │  ├─ _version.py
│  │     │  └─ __init__.py
│  │     ├─ httptools-0.8.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  ├─ LICENSE
│  │     │  │  └─ vendor
│  │     │  │     ├─ http-parser
│  │     │  │     │  └─ LICENSE-MIT
│  │     │  │     └─ llhttp
│  │     │  │        └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ idna
│  │     │  ├─ cli.py
│  │     │  ├─ codec.py
│  │     │  ├─ compat.py
│  │     │  ├─ core.py
│  │     │  ├─ idnadata.py
│  │     │  ├─ intranges.py
│  │     │  ├─ package_data.py
│  │     │  ├─ py.typed
│  │     │  ├─ uts46data.py
│  │     │  ├─ __init__.py
│  │     │  └─ __main__.py
│  │     ├─ idna-3.18.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.md
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ itsdangerous
│  │     │  ├─ encoding.py
│  │     │  ├─ exc.py
│  │     │  ├─ py.typed
│  │     │  ├─ serializer.py
│  │     │  ├─ signer.py
│  │     │  ├─ timed.py
│  │     │  ├─ url_safe.py
│  │     │  ├─ _json.py
│  │     │  └─ __init__.py
│  │     ├─ itsdangerous-2.2.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ jinja2
│  │     │  ├─ async_utils.py
│  │     │  ├─ bccache.py
│  │     │  ├─ compiler.py
│  │     │  ├─ constants.py
│  │     │  ├─ debug.py
│  │     │  ├─ defaults.py
│  │     │  ├─ environment.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ ext.py
│  │     │  ├─ filters.py
│  │     │  ├─ idtracking.py
│  │     │  ├─ lexer.py
│  │     │  ├─ loaders.py
│  │     │  ├─ meta.py
│  │     │  ├─ nativetypes.py
│  │     │  ├─ nodes.py
│  │     │  ├─ optimizer.py
│  │     │  ├─ parser.py
│  │     │  ├─ py.typed
│  │     │  ├─ runtime.py
│  │     │  ├─ sandbox.py
│  │     │  ├─ tests.py
│  │     │  ├─ utils.py
│  │     │  ├─ visitor.py
│  │     │  ├─ _identifier.py
│  │     │  └─ __init__.py
│  │     ├─ jinja2-3.1.6.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ jsonschema
│  │     │  ├─ benchmarks
│  │     │  │  ├─ const_vs_enum.py
│  │     │  │  ├─ contains.py
│  │     │  │  ├─ import_benchmark.py
│  │     │  │  ├─ issue232
│  │     │  │  │  └─ issue.json
│  │     │  │  ├─ issue232.py
│  │     │  │  ├─ json_schema_test_suite.py
│  │     │  │  ├─ nested_schemas.py
│  │     │  │  ├─ subcomponents.py
│  │     │  │  ├─ unused_registry.py
│  │     │  │  ├─ useless_applicator_schemas.py
│  │     │  │  ├─ useless_keywords.py
│  │     │  │  ├─ validator_creation.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ cli.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ protocols.py
│  │     │  ├─ tests
│  │     │  │  ├─ fuzz_validate.py
│  │     │  │  ├─ test_cli.py
│  │     │  │  ├─ test_deprecations.py
│  │     │  │  ├─ test_exceptions.py
│  │     │  │  ├─ test_format.py
│  │     │  │  ├─ test_jsonschema_test_suite.py
│  │     │  │  ├─ test_types.py
│  │     │  │  ├─ test_utils.py
│  │     │  │  ├─ test_validators.py
│  │     │  │  ├─ typing
│  │     │  │  │  ├─ test_all_concrete_validators_match_protocol.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ _suite.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ validators.py
│  │     │  ├─ _format.py
│  │     │  ├─ _keywords.py
│  │     │  ├─ _legacy_keywords.py
│  │     │  ├─ _types.py
│  │     │  ├─ _typing.py
│  │     │  ├─ _utils.py
│  │     │  ├─ __init__.py
│  │     │  └─ __main__.py
│  │     ├─ jsonschema-4.26.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ COPYING
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ jsonschema_specifications
│  │     │  ├─ schemas
│  │     │  │  ├─ draft201909
│  │     │  │  │  ├─ metaschema.json
│  │     │  │  │  └─ vocabularies
│  │     │  │  │     ├─ applicator
│  │     │  │  │     ├─ content
│  │     │  │  │     ├─ core
│  │     │  │  │     ├─ format
│  │     │  │  │     ├─ meta-data
│  │     │  │  │     └─ validation
│  │     │  │  ├─ draft202012
│  │     │  │  │  ├─ metaschema.json
│  │     │  │  │  └─ vocabularies
│  │     │  │  │     ├─ applicator
│  │     │  │  │     ├─ content
│  │     │  │  │     ├─ core
│  │     │  │  │     ├─ format-annotation
│  │     │  │  │     ├─ format-assertion
│  │     │  │  │     ├─ meta-data
│  │     │  │  │     ├─ unevaluated
│  │     │  │  │     └─ validation
│  │     │  │  ├─ draft3
│  │     │  │  │  └─ metaschema.json
│  │     │  │  ├─ draft4
│  │     │  │  │  └─ metaschema.json
│  │     │  │  ├─ draft6
│  │     │  │  │  └─ metaschema.json
│  │     │  │  └─ draft7
│  │     │  │     └─ metaschema.json
│  │     │  ├─ tests
│  │     │  │  ├─ test_jsonschema_specifications.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _core.py
│  │     │  └─ __init__.py
│  │     ├─ jsonschema_specifications-2025.9.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ COPYING
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ markupsafe
│  │     │  ├─ py.typed
│  │     │  ├─ _native.py
│  │     │  ├─ _speedups.c
│  │     │  ├─ _speedups.cp313-win_amd64.pyd
│  │     │  ├─ _speedups.pyi
│  │     │  └─ __init__.py
│  │     ├─ markupsafe-3.0.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ multipart
│  │     │  ├─ decoders.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ multipart.py
│  │     │  └─ __init__.py
│  │     ├─ multitasking
│  │     │  └─ __init__.py
│  │     ├─ multitasking-0.0.13.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ narwhals
│  │     │  ├─ compliant.py
│  │     │  ├─ dataframe.py
│  │     │  ├─ dependencies.py
│  │     │  ├─ dtypes.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ expr.py
│  │     │  ├─ expr_cat.py
│  │     │  ├─ expr_dt.py
│  │     │  ├─ expr_list.py
│  │     │  ├─ expr_name.py
│  │     │  ├─ expr_str.py
│  │     │  ├─ expr_struct.py
│  │     │  ├─ functions.py
│  │     │  ├─ group_by.py
│  │     │  ├─ plugins.py
│  │     │  ├─ py.typed
│  │     │  ├─ schema.py
│  │     │  ├─ selectors.py
│  │     │  ├─ series.py
│  │     │  ├─ series_cat.py
│  │     │  ├─ series_dt.py
│  │     │  ├─ series_list.py
│  │     │  ├─ series_str.py
│  │     │  ├─ series_struct.py
│  │     │  ├─ sql.py
│  │     │  ├─ stable
│  │     │  │  ├─ v1
│  │     │  │  │  ├─ dependencies.py
│  │     │  │  │  ├─ dtypes.py
│  │     │  │  │  ├─ selectors.py
│  │     │  │  │  ├─ typing.py
│  │     │  │  │  ├─ _dtypes.py
│  │     │  │  │  ├─ _namespace.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ v2
│  │     │  │  │  ├─ dependencies.py
│  │     │  │  │  ├─ dtypes.py
│  │     │  │  │  ├─ selectors.py
│  │     │  │  │  ├─ typing.py
│  │     │  │  │  ├─ _namespace.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ testing
│  │     │  │  ├─ asserts
│  │     │  │  │  ├─ frame.py
│  │     │  │  │  ├─ series.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ this.py
│  │     │  ├─ translate.py
│  │     │  ├─ typing.py
│  │     │  ├─ utils.py
│  │     │  ├─ _arrow
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ expr.py
│  │     │  │  ├─ group_by.py
│  │     │  │  ├─ namespace.py
│  │     │  │  ├─ selectors.py
│  │     │  │  ├─ series.py
│  │     │  │  ├─ series_cat.py
│  │     │  │  ├─ series_dt.py
│  │     │  │  ├─ series_list.py
│  │     │  │  ├─ series_str.py
│  │     │  │  ├─ series_struct.py
│  │     │  │  ├─ typing.py
│  │     │  │  ├─ utils.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _compliant
│  │     │  │  ├─ any_namespace.py
│  │     │  │  ├─ column.py
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ expr.py
│  │     │  │  ├─ group_by.py
│  │     │  │  ├─ namespace.py
│  │     │  │  ├─ selectors.py
│  │     │  │  ├─ series.py
│  │     │  │  ├─ typing.py
│  │     │  │  ├─ window.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _constants.py
│  │     │  ├─ _dask
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ expr.py
│  │     │  │  ├─ expr_dt.py
│  │     │  │  ├─ expr_str.py
│  │     │  │  ├─ group_by.py
│  │     │  │  ├─ namespace.py
│  │     │  │  ├─ selectors.py
│  │     │  │  ├─ utils.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _duckdb
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ expr.py
│  │     │  │  ├─ expr_dt.py
│  │     │  │  ├─ expr_list.py
│  │     │  │  ├─ expr_str.py
│  │     │  │  ├─ expr_struct.py
│  │     │  │  ├─ group_by.py
│  │     │  │  ├─ namespace.py
│  │     │  │  ├─ selectors.py
│  │     │  │  ├─ series.py
│  │     │  │  ├─ typing.py
│  │     │  │  ├─ utils.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _duration.py
│  │     │  ├─ _enum.py
│  │     │  ├─ _exceptions.py
│  │     │  ├─ _expression_parsing.py
│  │     │  ├─ _ibis
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ expr.py
│  │     │  │  ├─ expr_dt.py
│  │     │  │  ├─ expr_list.py
│  │     │  │  ├─ expr_str.py
│  │     │  │  ├─ expr_struct.py
│  │     │  │  ├─ group_by.py
│  │     │  │  ├─ namespace.py
│  │     │  │  ├─ selectors.py
│  │     │  │  ├─ series.py
│  │     │  │  ├─ utils.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _interchange
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ series.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _namespace.py
│  │     │  ├─ _native.py
│  │     │  ├─ _pandas_like
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ expr.py
│  │     │  │  ├─ group_by.py
│  │     │  │  ├─ namespace.py
│  │     │  │  ├─ selectors.py
│  │     │  │  ├─ series.py
│  │     │  │  ├─ series_cat.py
│  │     │  │  ├─ series_dt.py
│  │     │  │  ├─ series_list.py
│  │     │  │  ├─ series_str.py
│  │     │  │  ├─ series_struct.py
│  │     │  │  ├─ typing.py
│  │     │  │  ├─ utils.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _polars
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ expr.py
│  │     │  │  ├─ group_by.py
│  │     │  │  ├─ namespace.py
│  │     │  │  ├─ series.py
│  │     │  │  ├─ typing.py
│  │     │  │  ├─ utils.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _spark_like
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ expr.py
│  │     │  │  ├─ expr_dt.py
│  │     │  │  ├─ expr_list.py
│  │     │  │  ├─ expr_str.py
│  │     │  │  ├─ expr_struct.py
│  │     │  │  ├─ group_by.py
│  │     │  │  ├─ namespace.py
│  │     │  │  ├─ selectors.py
│  │     │  │  ├─ utils.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _sql
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ expr.py
│  │     │  │  ├─ expr_dt.py
│  │     │  │  ├─ expr_str.py
│  │     │  │  ├─ group_by.py
│  │     │  │  ├─ namespace.py
│  │     │  │  ├─ typing.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _translate.py
│  │     │  ├─ _typing.py
│  │     │  ├─ _typing_compat.py
│  │     │  ├─ _utils.py
│  │     │  └─ __init__.py
│  │     ├─ narwhals-2.24.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.md
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ numpy
│  │     │  ├─ char
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ conftest.py
│  │     │  ├─ core
│  │     │  │  ├─ arrayprint.py
│  │     │  │  ├─ arrayprint.pyi
│  │     │  │  ├─ defchararray.py
│  │     │  │  ├─ defchararray.pyi
│  │     │  │  ├─ einsumfunc.py
│  │     │  │  ├─ einsumfunc.pyi
│  │     │  │  ├─ fromnumeric.py
│  │     │  │  ├─ fromnumeric.pyi
│  │     │  │  ├─ function_base.py
│  │     │  │  ├─ function_base.pyi
│  │     │  │  ├─ getlimits.py
│  │     │  │  ├─ getlimits.pyi
│  │     │  │  ├─ multiarray.py
│  │     │  │  ├─ multiarray.pyi
│  │     │  │  ├─ numeric.py
│  │     │  │  ├─ numeric.pyi
│  │     │  │  ├─ numerictypes.py
│  │     │  │  ├─ numerictypes.pyi
│  │     │  │  ├─ overrides.py
│  │     │  │  ├─ overrides.pyi
│  │     │  │  ├─ records.py
│  │     │  │  ├─ records.pyi
│  │     │  │  ├─ shape_base.py
│  │     │  │  ├─ shape_base.pyi
│  │     │  │  ├─ umath.py
│  │     │  │  ├─ umath.pyi
│  │     │  │  ├─ _dtype.py
│  │     │  │  ├─ _dtype.pyi
│  │     │  │  ├─ _dtype_ctypes.py
│  │     │  │  ├─ _dtype_ctypes.pyi
│  │     │  │  ├─ _internal.py
│  │     │  │  ├─ _internal.pyi
│  │     │  │  ├─ _multiarray_umath.py
│  │     │  │  ├─ _utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ ctypeslib
│  │     │  │  ├─ _ctypeslib.py
│  │     │  │  ├─ _ctypeslib.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ doc
│  │     │  │  └─ ufuncs.py
│  │     │  ├─ dtypes.py
│  │     │  ├─ dtypes.pyi
│  │     │  ├─ exceptions.py
│  │     │  ├─ exceptions.pyi
│  │     │  ├─ f2py
│  │     │  │  ├─ auxfuncs.py
│  │     │  │  ├─ auxfuncs.pyi
│  │     │  │  ├─ capi_maps.py
│  │     │  │  ├─ capi_maps.pyi
│  │     │  │  ├─ cb_rules.py
│  │     │  │  ├─ cb_rules.pyi
│  │     │  │  ├─ cfuncs.py
│  │     │  │  ├─ cfuncs.pyi
│  │     │  │  ├─ common_rules.py
│  │     │  │  ├─ common_rules.pyi
│  │     │  │  ├─ crackfortran.py
│  │     │  │  ├─ crackfortran.pyi
│  │     │  │  ├─ diagnose.py
│  │     │  │  ├─ diagnose.pyi
│  │     │  │  ├─ f2py2e.py
│  │     │  │  ├─ f2py2e.pyi
│  │     │  │  ├─ f90mod_rules.py
│  │     │  │  ├─ f90mod_rules.pyi
│  │     │  │  ├─ func2subr.py
│  │     │  │  ├─ func2subr.pyi
│  │     │  │  ├─ rules.py
│  │     │  │  ├─ rules.pyi
│  │     │  │  ├─ setup.cfg
│  │     │  │  ├─ src
│  │     │  │  │  ├─ fortranobject.c
│  │     │  │  │  └─ fortranobject.h
│  │     │  │  ├─ symbolic.py
│  │     │  │  ├─ symbolic.pyi
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ src
│  │     │  │  │  │  ├─ abstract_interface
│  │     │  │  │  │  │  ├─ foo.f90
│  │     │  │  │  │  │  └─ gh18403_mod.f90
│  │     │  │  │  │  ├─ array_from_pyobj
│  │     │  │  │  │  │  └─ wrapmodule.c
│  │     │  │  │  │  ├─ assumed_shape
│  │     │  │  │  │  │  ├─ .f2py_f2cmap
│  │     │  │  │  │  │  ├─ foo_free.f90
│  │     │  │  │  │  │  ├─ foo_mod.f90
│  │     │  │  │  │  │  ├─ foo_use.f90
│  │     │  │  │  │  │  └─ precision.f90
│  │     │  │  │  │  ├─ block_docstring
│  │     │  │  │  │  │  └─ foo.f
│  │     │  │  │  │  ├─ callback
│  │     │  │  │  │  │  ├─ foo.f
│  │     │  │  │  │  │  ├─ gh17797.f90
│  │     │  │  │  │  │  ├─ gh18335.f90
│  │     │  │  │  │  │  ├─ gh25211.f
│  │     │  │  │  │  │  ├─ gh25211.pyf
│  │     │  │  │  │  │  └─ gh26681.f90
│  │     │  │  │  │  ├─ cli
│  │     │  │  │  │  │  ├─ gh_22819.pyf
│  │     │  │  │  │  │  ├─ hi77.f
│  │     │  │  │  │  │  └─ hiworld.f90
│  │     │  │  │  │  ├─ common
│  │     │  │  │  │  │  ├─ block.f
│  │     │  │  │  │  │  └─ gh19161.f90
│  │     │  │  │  │  ├─ crackfortran
│  │     │  │  │  │  │  ├─ accesstype.f90
│  │     │  │  │  │  │  ├─ common_with_division.f
│  │     │  │  │  │  │  ├─ data_common.f
│  │     │  │  │  │  │  ├─ data_multiplier.f
│  │     │  │  │  │  │  ├─ data_stmts.f90
│  │     │  │  │  │  │  ├─ data_with_comments.f
│  │     │  │  │  │  │  ├─ foo_deps.f90
│  │     │  │  │  │  │  ├─ gh15035.f
│  │     │  │  │  │  │  ├─ gh17859.f
│  │     │  │  │  │  │  ├─ gh22648.pyf
│  │     │  │  │  │  │  ├─ gh23533.f
│  │     │  │  │  │  │  ├─ gh23598.f90
│  │     │  │  │  │  │  ├─ gh23598Warn.f90
│  │     │  │  │  │  │  ├─ gh23879.f90
│  │     │  │  │  │  │  ├─ gh27697.f90
│  │     │  │  │  │  │  ├─ gh2848.f90
│  │     │  │  │  │  │  ├─ operators.f90
│  │     │  │  │  │  │  ├─ privatemod.f90
│  │     │  │  │  │  │  ├─ publicmod.f90
│  │     │  │  │  │  │  ├─ pubprivmod.f90
│  │     │  │  │  │  │  └─ unicode_comment.f90
│  │     │  │  │  │  ├─ f2cmap
│  │     │  │  │  │  │  ├─ .f2py_f2cmap
│  │     │  │  │  │  │  └─ isoFortranEnvMap.f90
│  │     │  │  │  │  ├─ inplace
│  │     │  │  │  │  │  └─ foo.f
│  │     │  │  │  │  ├─ isocintrin
│  │     │  │  │  │  │  └─ isoCtests.f90
│  │     │  │  │  │  ├─ kind
│  │     │  │  │  │  │  └─ foo.f90
│  │     │  │  │  │  ├─ mixed
│  │     │  │  │  │  │  ├─ foo.f
│  │     │  │  │  │  │  ├─ foo_fixed.f90
│  │     │  │  │  │  │  └─ foo_free.f90
│  │     │  │  │  │  ├─ modules
│  │     │  │  │  │  │  ├─ gh25337
│  │     │  │  │  │  │  │  ├─ data.f90
│  │     │  │  │  │  │  │  └─ use_data.f90
│  │     │  │  │  │  │  ├─ gh26920
│  │     │  │  │  │  │  │  ├─ two_mods_with_no_public_entities.f90
│  │     │  │  │  │  │  │  └─ two_mods_with_one_public_routine.f90
│  │     │  │  │  │  │  ├─ module_data_docstring.f90
│  │     │  │  │  │  │  └─ use_modules.f90
│  │     │  │  │  │  ├─ negative_bounds
│  │     │  │  │  │  │  └─ issue_20853.f90
│  │     │  │  │  │  ├─ parameter
│  │     │  │  │  │  │  ├─ constant_array.f90
│  │     │  │  │  │  │  ├─ constant_both.f90
│  │     │  │  │  │  │  ├─ constant_compound.f90
│  │     │  │  │  │  │  ├─ constant_integer.f90
│  │     │  │  │  │  │  ├─ constant_non_compound.f90
│  │     │  │  │  │  │  └─ constant_real.f90
│  │     │  │  │  │  ├─ quoted_character
│  │     │  │  │  │  │  └─ foo.f
│  │     │  │  │  │  ├─ regression
│  │     │  │  │  │  │  ├─ AB.inc
│  │     │  │  │  │  │  ├─ assignOnlyModule.f90
│  │     │  │  │  │  │  ├─ complex_struct_compat.f90
│  │     │  │  │  │  │  ├─ complex_struct_compat.pyf
│  │     │  │  │  │  │  ├─ datonly.f90
│  │     │  │  │  │  │  ├─ f77comments.f
│  │     │  │  │  │  │  ├─ f77fixedform.f95
│  │     │  │  │  │  │  ├─ f90continuation.f90
│  │     │  │  │  │  │  ├─ incfile.f90
│  │     │  │  │  │  │  ├─ inout.f90
│  │     │  │  │  │  │  ├─ lower_f2py_fortran.f90
│  │     │  │  │  │  │  └─ mod_derived_types.f90
│  │     │  │  │  │  ├─ return_character
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ return_complex
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ return_integer
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ return_logical
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ return_real
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ routines
│  │     │  │  │  │  │  ├─ funcfortranname.f
│  │     │  │  │  │  │  ├─ funcfortranname.pyf
│  │     │  │  │  │  │  ├─ subrout.f
│  │     │  │  │  │  │  └─ subrout.pyf
│  │     │  │  │  │  ├─ size
│  │     │  │  │  │  │  └─ foo.f90
│  │     │  │  │  │  ├─ string
│  │     │  │  │  │  │  ├─ char.f90
│  │     │  │  │  │  │  ├─ fixed_string.f90
│  │     │  │  │  │  │  ├─ gh24008.f
│  │     │  │  │  │  │  ├─ gh24662.f90
│  │     │  │  │  │  │  ├─ gh25286.f90
│  │     │  │  │  │  │  ├─ gh25286.pyf
│  │     │  │  │  │  │  ├─ gh25286_bc.pyf
│  │     │  │  │  │  │  ├─ scalar_string.f90
│  │     │  │  │  │  │  └─ string.f
│  │     │  │  │  │  └─ value_attrspec
│  │     │  │  │  │     └─ gh21665.f90
│  │     │  │  │  ├─ test_abstract_interface.py
│  │     │  │  │  ├─ test_array_from_pyobj.py
│  │     │  │  │  ├─ test_assumed_shape.py
│  │     │  │  │  ├─ test_block_docstring.py
│  │     │  │  │  ├─ test_callback.py
│  │     │  │  │  ├─ test_capi_maps.py
│  │     │  │  │  ├─ test_character.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_crackfortran.py
│  │     │  │  │  ├─ test_data.py
│  │     │  │  │  ├─ test_docs.py
│  │     │  │  │  ├─ test_f2cmap.py
│  │     │  │  │  ├─ test_f2py2e.py
│  │     │  │  │  ├─ test_inplace.py
│  │     │  │  │  ├─ test_isoc.py
│  │     │  │  │  ├─ test_kind.py
│  │     │  │  │  ├─ test_mixed.py
│  │     │  │  │  ├─ test_modules.py
│  │     │  │  │  ├─ test_parameter.py
│  │     │  │  │  ├─ test_pyf_src.py
│  │     │  │  │  ├─ test_quoted_character.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_return_character.py
│  │     │  │  │  ├─ test_return_complex.py
│  │     │  │  │  ├─ test_return_integer.py
│  │     │  │  │  ├─ test_return_logical.py
│  │     │  │  │  ├─ test_return_real.py
│  │     │  │  │  ├─ test_routines.py
│  │     │  │  │  ├─ test_semicolon_split.py
│  │     │  │  │  ├─ test_size.py
│  │     │  │  │  ├─ test_string.py
│  │     │  │  │  ├─ test_symbolic.py
│  │     │  │  │  ├─ test_value_attrspec.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ use_rules.py
│  │     │  │  ├─ use_rules.pyi
│  │     │  │  ├─ _backends
│  │     │  │  │  ├─ meson.build.template
│  │     │  │  │  ├─ _backend.py
│  │     │  │  │  ├─ _backend.pyi
│  │     │  │  │  ├─ _meson.py
│  │     │  │  │  ├─ _meson.pyi
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  ├─ _isocbind.py
│  │     │  │  ├─ _isocbind.pyi
│  │     │  │  ├─ _src_pyf.py
│  │     │  │  ├─ _src_pyf.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ __main__.py
│  │     │  │  ├─ __version__.py
│  │     │  │  └─ __version__.pyi
│  │     │  ├─ fft
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_helper.py
│  │     │  │  │  ├─ test_pocketfft.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ _helper.py
│  │     │  │  ├─ _helper.pyi
│  │     │  │  ├─ _pocketfft.py
│  │     │  │  ├─ _pocketfft.pyi
│  │     │  │  ├─ _pocketfft_umath.cp313-win_amd64.lib
│  │     │  │  ├─ _pocketfft_umath.cp313-win_amd64.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ lib
│  │     │  │  ├─ array_utils.py
│  │     │  │  ├─ array_utils.pyi
│  │     │  │  ├─ format.py
│  │     │  │  ├─ format.pyi
│  │     │  │  ├─ introspect.py
│  │     │  │  ├─ introspect.pyi
│  │     │  │  ├─ mixins.py
│  │     │  │  ├─ mixins.pyi
│  │     │  │  ├─ npyio.py
│  │     │  │  ├─ npyio.pyi
│  │     │  │  ├─ recfunctions.py
│  │     │  │  ├─ recfunctions.pyi
│  │     │  │  ├─ scimath.py
│  │     │  │  ├─ scimath.pyi
│  │     │  │  ├─ stride_tricks.py
│  │     │  │  ├─ stride_tricks.pyi
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ py2-np0-objarr.npy
│  │     │  │  │  │  ├─ py2-objarr.npy
│  │     │  │  │  │  ├─ py2-objarr.npz
│  │     │  │  │  │  ├─ py3-objarr.npy
│  │     │  │  │  │  ├─ py3-objarr.npz
│  │     │  │  │  │  ├─ python3.npy
│  │     │  │  │  │  └─ win64python2.npy
│  │     │  │  │  ├─ test_arraypad.py
│  │     │  │  │  ├─ test_arraysetops.py
│  │     │  │  │  ├─ test_arrayterator.py
│  │     │  │  │  ├─ test_array_utils.py
│  │     │  │  │  ├─ test_format.py
│  │     │  │  │  ├─ test_function_base.py
│  │     │  │  │  ├─ test_histograms.py
│  │     │  │  │  ├─ test_index_tricks.py
│  │     │  │  │  ├─ test_io.py
│  │     │  │  │  ├─ test_loadtxt.py
│  │     │  │  │  ├─ test_mixins.py
│  │     │  │  │  ├─ test_nanfunctions.py
│  │     │  │  │  ├─ test_packbits.py
│  │     │  │  │  ├─ test_polynomial.py
│  │     │  │  │  ├─ test_recfunctions.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_shape_base.py
│  │     │  │  │  ├─ test_stride_tricks.py
│  │     │  │  │  ├─ test_twodim_base.py
│  │     │  │  │  ├─ test_type_check.py
│  │     │  │  │  ├─ test_ufunclike.py
│  │     │  │  │  ├─ test_utils.py
│  │     │  │  │  ├─ test__datasource.py
│  │     │  │  │  ├─ test__iotools.py
│  │     │  │  │  ├─ test__version.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ user_array.py
│  │     │  │  ├─ user_array.pyi
│  │     │  │  ├─ _arraypad_impl.py
│  │     │  │  ├─ _arraypad_impl.pyi
│  │     │  │  ├─ _arraysetops_impl.py
│  │     │  │  ├─ _arraysetops_impl.pyi
│  │     │  │  ├─ _arrayterator_impl.py
│  │     │  │  ├─ _arrayterator_impl.pyi
│  │     │  │  ├─ _array_utils_impl.py
│  │     │  │  ├─ _array_utils_impl.pyi
│  │     │  │  ├─ _datasource.py
│  │     │  │  ├─ _datasource.pyi
│  │     │  │  ├─ _format_impl.py
│  │     │  │  ├─ _format_impl.pyi
│  │     │  │  ├─ _function_base_impl.py
│  │     │  │  ├─ _function_base_impl.pyi
│  │     │  │  ├─ _histograms_impl.py
│  │     │  │  ├─ _histograms_impl.pyi
│  │     │  │  ├─ _index_tricks_impl.py
│  │     │  │  ├─ _index_tricks_impl.pyi
│  │     │  │  ├─ _iotools.py
│  │     │  │  ├─ _iotools.pyi
│  │     │  │  ├─ _nanfunctions_impl.py
│  │     │  │  ├─ _nanfunctions_impl.pyi
│  │     │  │  ├─ _npyio_impl.py
│  │     │  │  ├─ _npyio_impl.pyi
│  │     │  │  ├─ _polynomial_impl.py
│  │     │  │  ├─ _polynomial_impl.pyi
│  │     │  │  ├─ _scimath_impl.py
│  │     │  │  ├─ _scimath_impl.pyi
│  │     │  │  ├─ _shape_base_impl.py
│  │     │  │  ├─ _shape_base_impl.pyi
│  │     │  │  ├─ _stride_tricks_impl.py
│  │     │  │  ├─ _stride_tricks_impl.pyi
│  │     │  │  ├─ _twodim_base_impl.py
│  │     │  │  ├─ _twodim_base_impl.pyi
│  │     │  │  ├─ _type_check_impl.py
│  │     │  │  ├─ _type_check_impl.pyi
│  │     │  │  ├─ _ufunclike_impl.py
│  │     │  │  ├─ _ufunclike_impl.pyi
│  │     │  │  ├─ _user_array_impl.py
│  │     │  │  ├─ _user_array_impl.pyi
│  │     │  │  ├─ _utils_impl.py
│  │     │  │  ├─ _utils_impl.pyi
│  │     │  │  ├─ _version.py
│  │     │  │  ├─ _version.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ linalg
│  │     │  │  ├─ lapack_lite.cp313-win_amd64.lib
│  │     │  │  ├─ lapack_lite.cp313-win_amd64.pyd
│  │     │  │  ├─ lapack_lite.pyi
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_deprecations.py
│  │     │  │  │  ├─ test_linalg.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ _linalg.py
│  │     │  │  ├─ _linalg.pyi
│  │     │  │  ├─ _umath_linalg.cp313-win_amd64.lib
│  │     │  │  ├─ _umath_linalg.cp313-win_amd64.pyd
│  │     │  │  ├─ _umath_linalg.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ ma
│  │     │  │  ├─ API_CHANGES.txt
│  │     │  │  ├─ core.py
│  │     │  │  ├─ core.pyi
│  │     │  │  ├─ extras.py
│  │     │  │  ├─ extras.pyi
│  │     │  │  ├─ LICENSE
│  │     │  │  ├─ mrecords.py
│  │     │  │  ├─ mrecords.pyi
│  │     │  │  ├─ README.rst
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_arrayobject.py
│  │     │  │  │  ├─ test_core.py
│  │     │  │  │  ├─ test_deprecations.py
│  │     │  │  │  ├─ test_extras.py
│  │     │  │  │  ├─ test_mrecords.py
│  │     │  │  │  ├─ test_old_ma.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_subclassing.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ testutils.py
│  │     │  │  ├─ testutils.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ matlib.py
│  │     │  ├─ matlib.pyi
│  │     │  ├─ matrixlib
│  │     │  │  ├─ defmatrix.py
│  │     │  │  ├─ defmatrix.pyi
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_defmatrix.py
│  │     │  │  │  ├─ test_interaction.py
│  │     │  │  │  ├─ test_masked_matrix.py
│  │     │  │  │  ├─ test_matrix_linalg.py
│  │     │  │  │  ├─ test_multiarray.py
│  │     │  │  │  ├─ test_numeric.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ polynomial
│  │     │  │  ├─ chebyshev.py
│  │     │  │  ├─ chebyshev.pyi
│  │     │  │  ├─ hermite.py
│  │     │  │  ├─ hermite.pyi
│  │     │  │  ├─ hermite_e.py
│  │     │  │  ├─ hermite_e.pyi
│  │     │  │  ├─ laguerre.py
│  │     │  │  ├─ laguerre.pyi
│  │     │  │  ├─ legendre.py
│  │     │  │  ├─ legendre.pyi
│  │     │  │  ├─ polynomial.py
│  │     │  │  ├─ polynomial.pyi
│  │     │  │  ├─ polyutils.py
│  │     │  │  ├─ polyutils.pyi
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_chebyshev.py
│  │     │  │  │  ├─ test_classes.py
│  │     │  │  │  ├─ test_hermite.py
│  │     │  │  │  ├─ test_hermite_e.py
│  │     │  │  │  ├─ test_laguerre.py
│  │     │  │  │  ├─ test_legendre.py
│  │     │  │  │  ├─ test_polynomial.py
│  │     │  │  │  ├─ test_polyutils.py
│  │     │  │  │  ├─ test_printing.py
│  │     │  │  │  ├─ test_symbol.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ _polybase.py
│  │     │  │  ├─ _polybase.pyi
│  │     │  │  ├─ _polytypes.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ py.typed
│  │     │  ├─ random
│  │     │  │  ├─ bit_generator.cp313-win_amd64.lib
│  │     │  │  ├─ bit_generator.cp313-win_amd64.pyd
│  │     │  │  ├─ bit_generator.pxd
│  │     │  │  ├─ bit_generator.pyi
│  │     │  │  ├─ c_distributions.pxd
│  │     │  │  ├─ lib
│  │     │  │  │  └─ npyrandom.lib
│  │     │  │  ├─ LICENSE.md
│  │     │  │  ├─ mtrand.cp313-win_amd64.lib
│  │     │  │  ├─ mtrand.cp313-win_amd64.pyd
│  │     │  │  ├─ mtrand.pyi
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ generator_pcg64_np121.pkl.gz
│  │     │  │  │  │  ├─ generator_pcg64_np126.pkl.gz
│  │     │  │  │  │  ├─ mt19937-testset-1.csv
│  │     │  │  │  │  ├─ mt19937-testset-2.csv
│  │     │  │  │  │  ├─ pcg64-testset-1.csv
│  │     │  │  │  │  ├─ pcg64-testset-2.csv
│  │     │  │  │  │  ├─ pcg64dxsm-testset-1.csv
│  │     │  │  │  │  ├─ pcg64dxsm-testset-2.csv
│  │     │  │  │  │  ├─ philox-testset-1.csv
│  │     │  │  │  │  ├─ philox-testset-2.csv
│  │     │  │  │  │  ├─ sfc64-testset-1.csv
│  │     │  │  │  │  ├─ sfc64-testset-2.csv
│  │     │  │  │  │  ├─ sfc64_np126.pkl.gz
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ test_direct.py
│  │     │  │  │  ├─ test_extending.py
│  │     │  │  │  ├─ test_generator_mt19937.py
│  │     │  │  │  ├─ test_generator_mt19937_regressions.py
│  │     │  │  │  ├─ test_random.py
│  │     │  │  │  ├─ test_randomstate.py
│  │     │  │  │  ├─ test_randomstate_regression.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_seed_sequence.py
│  │     │  │  │  ├─ test_smoke.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ _bounded_integers.cp313-win_amd64.lib
│  │     │  │  ├─ _bounded_integers.cp313-win_amd64.pyd
│  │     │  │  ├─ _bounded_integers.pxd
│  │     │  │  ├─ _bounded_integers.pyi
│  │     │  │  ├─ _common.cp313-win_amd64.lib
│  │     │  │  ├─ _common.cp313-win_amd64.pyd
│  │     │  │  ├─ _common.pxd
│  │     │  │  ├─ _common.pyi
│  │     │  │  ├─ _examples
│  │     │  │  │  ├─ cffi
│  │     │  │  │  │  ├─ extending.py
│  │     │  │  │  │  └─ parse.py
│  │     │  │  │  ├─ cython
│  │     │  │  │  │  ├─ extending.pyx
│  │     │  │  │  │  ├─ extending_distributions.pyx
│  │     │  │  │  │  └─ meson.build
│  │     │  │  │  └─ numba
│  │     │  │  │     ├─ extending.py
│  │     │  │  │     └─ extending_distributions.py
│  │     │  │  ├─ _generator.cp313-win_amd64.lib
│  │     │  │  ├─ _generator.cp313-win_amd64.pyd
│  │     │  │  ├─ _generator.pyi
│  │     │  │  ├─ _mt19937.cp313-win_amd64.lib
│  │     │  │  ├─ _mt19937.cp313-win_amd64.pyd
│  │     │  │  ├─ _mt19937.pyi
│  │     │  │  ├─ _pcg64.cp313-win_amd64.lib
│  │     │  │  ├─ _pcg64.cp313-win_amd64.pyd
│  │     │  │  ├─ _pcg64.pyi
│  │     │  │  ├─ _philox.cp313-win_amd64.lib
│  │     │  │  ├─ _philox.cp313-win_amd64.pyd
│  │     │  │  ├─ _philox.pyi
│  │     │  │  ├─ _pickle.py
│  │     │  │  ├─ _pickle.pyi
│  │     │  │  ├─ _sfc64.cp313-win_amd64.lib
│  │     │  │  ├─ _sfc64.cp313-win_amd64.pyd
│  │     │  │  ├─ _sfc64.pyi
│  │     │  │  ├─ __init__.pxd
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ rec
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ strings
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ testing
│  │     │  │  ├─ overrides.py
│  │     │  │  ├─ overrides.pyi
│  │     │  │  ├─ print_coercion_tables.py
│  │     │  │  ├─ print_coercion_tables.pyi
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_utils.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ _private
│  │     │  │  │  ├─ extbuild.py
│  │     │  │  │  ├─ extbuild.pyi
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ utils.pyi
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ tests
│  │     │  │  ├─ test_configtool.py
│  │     │  │  ├─ test_ctypeslib.py
│  │     │  │  ├─ test_lazyloading.py
│  │     │  │  ├─ test_matlib.py
│  │     │  │  ├─ test_numpy_config.py
│  │     │  │  ├─ test_numpy_version.py
│  │     │  │  ├─ test_public_api.py
│  │     │  │  ├─ test_reloading.py
│  │     │  │  ├─ test_scripts.py
│  │     │  │  ├─ test_warnings.py
│  │     │  │  ├─ test__all__.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ typing
│  │     │  │  ├─ mypy_plugin.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ fail
│  │     │  │  │  │  │  ├─ arithmetic.pyi
│  │     │  │  │  │  │  ├─ arrayprint.pyi
│  │     │  │  │  │  │  ├─ arrayterator.pyi
│  │     │  │  │  │  │  ├─ array_constructors.pyi
│  │     │  │  │  │  │  ├─ array_like.pyi
│  │     │  │  │  │  │  ├─ array_pad.pyi
│  │     │  │  │  │  │  ├─ bitwise_ops.pyi
│  │     │  │  │  │  │  ├─ char.pyi
│  │     │  │  │  │  │  ├─ chararray.pyi
│  │     │  │  │  │  │  ├─ comparisons.pyi
│  │     │  │  │  │  │  ├─ constants.pyi
│  │     │  │  │  │  │  ├─ datasource.pyi
│  │     │  │  │  │  │  ├─ dtype.pyi
│  │     │  │  │  │  │  ├─ einsumfunc.pyi
│  │     │  │  │  │  │  ├─ flatiter.pyi
│  │     │  │  │  │  │  ├─ fromnumeric.pyi
│  │     │  │  │  │  │  ├─ histograms.pyi
│  │     │  │  │  │  │  ├─ index_tricks.pyi
│  │     │  │  │  │  │  ├─ lib_function_base.pyi
│  │     │  │  │  │  │  ├─ lib_polynomial.pyi
│  │     │  │  │  │  │  ├─ lib_utils.pyi
│  │     │  │  │  │  │  ├─ lib_version.pyi
│  │     │  │  │  │  │  ├─ linalg.pyi
│  │     │  │  │  │  │  ├─ ma.pyi
│  │     │  │  │  │  │  ├─ memmap.pyi
│  │     │  │  │  │  │  ├─ modules.pyi
│  │     │  │  │  │  │  ├─ multiarray.pyi
│  │     │  │  │  │  │  ├─ ndarray.pyi
│  │     │  │  │  │  │  ├─ ndarray_misc.pyi
│  │     │  │  │  │  │  ├─ nditer.pyi
│  │     │  │  │  │  │  ├─ nested_sequence.pyi
│  │     │  │  │  │  │  ├─ npyio.pyi
│  │     │  │  │  │  │  ├─ numerictypes.pyi
│  │     │  │  │  │  │  ├─ random.pyi
│  │     │  │  │  │  │  ├─ rec.pyi
│  │     │  │  │  │  │  ├─ scalars.pyi
│  │     │  │  │  │  │  ├─ shape.pyi
│  │     │  │  │  │  │  ├─ shape_base.pyi
│  │     │  │  │  │  │  ├─ stride_tricks.pyi
│  │     │  │  │  │  │  ├─ strings.pyi
│  │     │  │  │  │  │  ├─ testing.pyi
│  │     │  │  │  │  │  ├─ twodim_base.pyi
│  │     │  │  │  │  │  ├─ type_check.pyi
│  │     │  │  │  │  │  ├─ ufunclike.pyi
│  │     │  │  │  │  │  ├─ ufuncs.pyi
│  │     │  │  │  │  │  ├─ ufunc_config.pyi
│  │     │  │  │  │  │  └─ warnings_and_errors.pyi
│  │     │  │  │  │  ├─ misc
│  │     │  │  │  │  │  └─ extended_precision.pyi
│  │     │  │  │  │  ├─ mypy.ini
│  │     │  │  │  │  ├─ pass
│  │     │  │  │  │  │  ├─ arithmetic.py
│  │     │  │  │  │  │  ├─ arrayprint.py
│  │     │  │  │  │  │  ├─ arrayterator.py
│  │     │  │  │  │  │  ├─ array_constructors.py
│  │     │  │  │  │  │  ├─ array_like.py
│  │     │  │  │  │  │  ├─ bitwise_ops.py
│  │     │  │  │  │  │  ├─ comparisons.py
│  │     │  │  │  │  │  ├─ dtype.py
│  │     │  │  │  │  │  ├─ einsumfunc.py
│  │     │  │  │  │  │  ├─ flatiter.py
│  │     │  │  │  │  │  ├─ fromnumeric.py
│  │     │  │  │  │  │  ├─ index_tricks.py
│  │     │  │  │  │  │  ├─ lib_user_array.py
│  │     │  │  │  │  │  ├─ lib_utils.py
│  │     │  │  │  │  │  ├─ lib_version.py
│  │     │  │  │  │  │  ├─ literal.py
│  │     │  │  │  │  │  ├─ ma.py
│  │     │  │  │  │  │  ├─ mod.py
│  │     │  │  │  │  │  ├─ modules.py
│  │     │  │  │  │  │  ├─ multiarray.py
│  │     │  │  │  │  │  ├─ ndarray_conversion.py
│  │     │  │  │  │  │  ├─ ndarray_misc.py
│  │     │  │  │  │  │  ├─ ndarray_shape_manipulation.py
│  │     │  │  │  │  │  ├─ nditer.py
│  │     │  │  │  │  │  ├─ numeric.py
│  │     │  │  │  │  │  ├─ numerictypes.py
│  │     │  │  │  │  │  ├─ random.py
│  │     │  │  │  │  │  ├─ recfunctions.py
│  │     │  │  │  │  │  ├─ scalars.py
│  │     │  │  │  │  │  ├─ shape.py
│  │     │  │  │  │  │  ├─ simple.py
│  │     │  │  │  │  │  ├─ ufunclike.py
│  │     │  │  │  │  │  ├─ ufuncs.py
│  │     │  │  │  │  │  ├─ ufunc_config.py
│  │     │  │  │  │  │  └─ warnings_and_errors.py
│  │     │  │  │  │  └─ reveal
│  │     │  │  │  │     ├─ arithmetic.pyi
│  │     │  │  │  │     ├─ arraypad.pyi
│  │     │  │  │  │     ├─ arrayprint.pyi
│  │     │  │  │  │     ├─ arraysetops.pyi
│  │     │  │  │  │     ├─ arrayterator.pyi
│  │     │  │  │  │     ├─ array_api_info.pyi
│  │     │  │  │  │     ├─ array_constructors.pyi
│  │     │  │  │  │     ├─ bitwise_ops.pyi
│  │     │  │  │  │     ├─ char.pyi
│  │     │  │  │  │     ├─ chararray.pyi
│  │     │  │  │  │     ├─ comparisons.pyi
│  │     │  │  │  │     ├─ constants.pyi
│  │     │  │  │  │     ├─ ctypeslib.pyi
│  │     │  │  │  │     ├─ datasource.pyi
│  │     │  │  │  │     ├─ dtype.pyi
│  │     │  │  │  │     ├─ einsumfunc.pyi
│  │     │  │  │  │     ├─ emath.pyi
│  │     │  │  │  │     ├─ fft.pyi
│  │     │  │  │  │     ├─ flatiter.pyi
│  │     │  │  │  │     ├─ fromnumeric.pyi
│  │     │  │  │  │     ├─ getlimits.pyi
│  │     │  │  │  │     ├─ histograms.pyi
│  │     │  │  │  │     ├─ index_tricks.pyi
│  │     │  │  │  │     ├─ lib_function_base.pyi
│  │     │  │  │  │     ├─ lib_polynomial.pyi
│  │     │  │  │  │     ├─ lib_utils.pyi
│  │     │  │  │  │     ├─ lib_version.pyi
│  │     │  │  │  │     ├─ linalg.pyi
│  │     │  │  │  │     ├─ ma.pyi
│  │     │  │  │  │     ├─ matrix.pyi
│  │     │  │  │  │     ├─ memmap.pyi
│  │     │  │  │  │     ├─ mod.pyi
│  │     │  │  │  │     ├─ modules.pyi
│  │     │  │  │  │     ├─ multiarray.pyi
│  │     │  │  │  │     ├─ nbit_base_example.pyi
│  │     │  │  │  │     ├─ ndarray_assignability.pyi
│  │     │  │  │  │     ├─ ndarray_conversion.pyi
│  │     │  │  │  │     ├─ ndarray_misc.pyi
│  │     │  │  │  │     ├─ ndarray_shape_manipulation.pyi
│  │     │  │  │  │     ├─ nditer.pyi
│  │     │  │  │  │     ├─ nested_sequence.pyi
│  │     │  │  │  │     ├─ npyio.pyi
│  │     │  │  │  │     ├─ numeric.pyi
│  │     │  │  │  │     ├─ numerictypes.pyi
│  │     │  │  │  │     ├─ polynomial_polybase.pyi
│  │     │  │  │  │     ├─ polynomial_polyutils.pyi
│  │     │  │  │  │     ├─ polynomial_series.pyi
│  │     │  │  │  │     ├─ random.pyi
│  │     │  │  │  │     ├─ rec.pyi
│  │     │  │  │  │     ├─ scalars.pyi
│  │     │  │  │  │     ├─ shape.pyi
│  │     │  │  │  │     ├─ shape_base.pyi
│  │     │  │  │  │     ├─ stride_tricks.pyi
│  │     │  │  │  │     ├─ strings.pyi
│  │     │  │  │  │     ├─ testing.pyi
│  │     │  │  │  │     ├─ twodim_base.pyi
│  │     │  │  │  │     ├─ type_check.pyi
│  │     │  │  │  │     ├─ ufunclike.pyi
│  │     │  │  │  │     ├─ ufuncs.pyi
│  │     │  │  │  │     ├─ ufunc_config.pyi
│  │     │  │  │  │     └─ warnings_and_errors.pyi
│  │     │  │  │  ├─ test_isfile.py
│  │     │  │  │  ├─ test_runtime.py
│  │     │  │  │  ├─ test_typing.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ version.py
│  │     │  ├─ version.pyi
│  │     │  ├─ _array_api_info.py
│  │     │  ├─ _array_api_info.pyi
│  │     │  ├─ _configtool.py
│  │     │  ├─ _configtool.pyi
│  │     │  ├─ _core
│  │     │  │  ├─ arrayprint.py
│  │     │  │  ├─ arrayprint.pyi
│  │     │  │  ├─ cversions.py
│  │     │  │  ├─ defchararray.py
│  │     │  │  ├─ defchararray.pyi
│  │     │  │  ├─ einsumfunc.py
│  │     │  │  ├─ einsumfunc.pyi
│  │     │  │  ├─ fromnumeric.py
│  │     │  │  ├─ fromnumeric.pyi
│  │     │  │  ├─ function_base.py
│  │     │  │  ├─ function_base.pyi
│  │     │  │  ├─ getlimits.py
│  │     │  │  ├─ getlimits.pyi
│  │     │  │  ├─ include
│  │     │  │  │  └─ numpy
│  │     │  │  │     ├─ arrayobject.h
│  │     │  │  │     ├─ arrayscalars.h
│  │     │  │  │     ├─ dtype_api.h
│  │     │  │  │     ├─ halffloat.h
│  │     │  │  │     ├─ ndarrayobject.h
│  │     │  │  │     ├─ ndarraytypes.h
│  │     │  │  │     ├─ npy_2_compat.h
│  │     │  │  │     ├─ npy_2_complexcompat.h
│  │     │  │  │     ├─ npy_3kcompat.h
│  │     │  │  │     ├─ npy_common.h
│  │     │  │  │     ├─ npy_cpu.h
│  │     │  │  │     ├─ npy_endian.h
│  │     │  │  │     ├─ npy_math.h
│  │     │  │  │     ├─ npy_no_deprecated_api.h
│  │     │  │  │     ├─ npy_os.h
│  │     │  │  │     ├─ numpyconfig.h
│  │     │  │  │     ├─ random
│  │     │  │  │     │  ├─ bitgen.h
│  │     │  │  │     │  ├─ distributions.h
│  │     │  │  │     │  ├─ libdivide.h
│  │     │  │  │     │  └─ LICENSE.txt
│  │     │  │  │     ├─ ufuncobject.h
│  │     │  │  │     ├─ utils.h
│  │     │  │  │     ├─ _neighborhood_iterator_imp.h
│  │     │  │  │     ├─ _numpyconfig.h
│  │     │  │  │     ├─ _public_dtype_api_table.h
│  │     │  │  │     ├─ __multiarray_api.c
│  │     │  │  │     ├─ __multiarray_api.h
│  │     │  │  │     ├─ __ufunc_api.c
│  │     │  │  │     └─ __ufunc_api.h
│  │     │  │  ├─ lib
│  │     │  │  │  ├─ npymath.lib
│  │     │  │  │  └─ pkgconfig
│  │     │  │  │     └─ numpy.pc
│  │     │  │  ├─ memmap.py
│  │     │  │  ├─ memmap.pyi
│  │     │  │  ├─ multiarray.py
│  │     │  │  ├─ multiarray.pyi
│  │     │  │  ├─ numeric.py
│  │     │  │  ├─ numeric.pyi
│  │     │  │  ├─ numerictypes.py
│  │     │  │  ├─ numerictypes.pyi
│  │     │  │  ├─ overrides.py
│  │     │  │  ├─ overrides.pyi
│  │     │  │  ├─ printoptions.py
│  │     │  │  ├─ printoptions.pyi
│  │     │  │  ├─ records.py
│  │     │  │  ├─ records.pyi
│  │     │  │  ├─ shape_base.py
│  │     │  │  ├─ shape_base.pyi
│  │     │  │  ├─ strings.py
│  │     │  │  ├─ strings.pyi
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ astype_copy.pkl
│  │     │  │  │  │  ├─ generate_umath_validation_data.cpp
│  │     │  │  │  │  ├─ recarray_from_file.fits
│  │     │  │  │  │  ├─ umath-validation-set-arccos.csv
│  │     │  │  │  │  ├─ umath-validation-set-arccosh.csv
│  │     │  │  │  │  ├─ umath-validation-set-arcsin.csv
│  │     │  │  │  │  ├─ umath-validation-set-arcsinh.csv
│  │     │  │  │  │  ├─ umath-validation-set-arctan.csv
│  │     │  │  │  │  ├─ umath-validation-set-arctanh.csv
│  │     │  │  │  │  ├─ umath-validation-set-cbrt.csv
│  │     │  │  │  │  ├─ umath-validation-set-cos.csv
│  │     │  │  │  │  ├─ umath-validation-set-cosh.csv
│  │     │  │  │  │  ├─ umath-validation-set-exp.csv
│  │     │  │  │  │  ├─ umath-validation-set-exp2.csv
│  │     │  │  │  │  ├─ umath-validation-set-expm1.csv
│  │     │  │  │  │  ├─ umath-validation-set-log.csv
│  │     │  │  │  │  ├─ umath-validation-set-log10.csv
│  │     │  │  │  │  ├─ umath-validation-set-log1p.csv
│  │     │  │  │  │  ├─ umath-validation-set-log2.csv
│  │     │  │  │  │  ├─ umath-validation-set-README.txt
│  │     │  │  │  │  ├─ umath-validation-set-sin.csv
│  │     │  │  │  │  ├─ umath-validation-set-sinh.csv
│  │     │  │  │  │  ├─ umath-validation-set-tan.csv
│  │     │  │  │  │  └─ umath-validation-set-tanh.csv
│  │     │  │  │  ├─ examples
│  │     │  │  │  │  ├─ cython
│  │     │  │  │  │  │  ├─ checks.pyx
│  │     │  │  │  │  │  ├─ meson.build
│  │     │  │  │  │  │  └─ setup.py
│  │     │  │  │  │  └─ limited_api
│  │     │  │  │  │     ├─ limited_api1.c
│  │     │  │  │  │     ├─ limited_api2.pyx
│  │     │  │  │  │     ├─ limited_api_latest.c
│  │     │  │  │  │     ├─ limited_api_opaque.c
│  │     │  │  │  │     ├─ meson.build
│  │     │  │  │  │     └─ setup.py
│  │     │  │  │  ├─ test_abc.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_argparse.py
│  │     │  │  │  ├─ test_arraymethod.py
│  │     │  │  │  ├─ test_arrayobject.py
│  │     │  │  │  ├─ test_arrayprint.py
│  │     │  │  │  ├─ test_array_api_info.py
│  │     │  │  │  ├─ test_array_coercion.py
│  │     │  │  │  ├─ test_array_interface.py
│  │     │  │  │  ├─ test_casting_floatingpoint_errors.py
│  │     │  │  │  ├─ test_casting_unittests.py
│  │     │  │  │  ├─ test_conversion_utils.py
│  │     │  │  │  ├─ test_cpu_dispatcher.py
│  │     │  │  │  ├─ test_cpu_features.py
│  │     │  │  │  ├─ test_custom_dtypes.py
│  │     │  │  │  ├─ test_cython.py
│  │     │  │  │  ├─ test_datetime.py
│  │     │  │  │  ├─ test_defchararray.py
│  │     │  │  │  ├─ test_deprecations.py
│  │     │  │  │  ├─ test_dlpack.py
│  │     │  │  │  ├─ test_dtype.py
│  │     │  │  │  ├─ test_einsum.py
│  │     │  │  │  ├─ test_errstate.py
│  │     │  │  │  ├─ test_extint128.py
│  │     │  │  │  ├─ test_finfo.py
│  │     │  │  │  ├─ test_function_base.py
│  │     │  │  │  ├─ test_getlimits.py
│  │     │  │  │  ├─ test_half.py
│  │     │  │  │  ├─ test_hashtable.py
│  │     │  │  │  ├─ test_indexerrors.py
│  │     │  │  │  ├─ test_indexing.py
│  │     │  │  │  ├─ test_item_selection.py
│  │     │  │  │  ├─ test_limited_api.py
│  │     │  │  │  ├─ test_longdouble.py
│  │     │  │  │  ├─ test_memmap.py
│  │     │  │  │  ├─ test_mem_overlap.py
│  │     │  │  │  ├─ test_mem_policy.py
│  │     │  │  │  ├─ test_multiarray.py
│  │     │  │  │  ├─ test_multiprocessing.py
│  │     │  │  │  ├─ test_multithreading.py
│  │     │  │  │  ├─ test_nditer.py
│  │     │  │  │  ├─ test_nep50_promotions.py
│  │     │  │  │  ├─ test_numeric.py
│  │     │  │  │  ├─ test_numerictypes.py
│  │     │  │  │  ├─ test_overrides.py
│  │     │  │  │  ├─ test_print.py
│  │     │  │  │  ├─ test_protocols.py
│  │     │  │  │  ├─ test_records.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_scalarbuffer.py
│  │     │  │  │  ├─ test_scalarinherit.py
│  │     │  │  │  ├─ test_scalarmath.py
│  │     │  │  │  ├─ test_scalarprint.py
│  │     │  │  │  ├─ test_scalar_ctors.py
│  │     │  │  │  ├─ test_scalar_methods.py
│  │     │  │  │  ├─ test_shape_base.py
│  │     │  │  │  ├─ test_simd.py
│  │     │  │  │  ├─ test_simd_module.py
│  │     │  │  │  ├─ test_stringdtype.py
│  │     │  │  │  ├─ test_strings.py
│  │     │  │  │  ├─ test_ufunc.py
│  │     │  │  │  ├─ test_umath.py
│  │     │  │  │  ├─ test_umath_accuracy.py
│  │     │  │  │  ├─ test_umath_complex.py
│  │     │  │  │  ├─ test_unicode.py
│  │     │  │  │  ├─ test__exceptions.py
│  │     │  │  │  ├─ _locales.py
│  │     │  │  │  └─ _natype.py
│  │     │  │  ├─ umath.py
│  │     │  │  ├─ umath.pyi
│  │     │  │  ├─ _add_newdocs.py
│  │     │  │  ├─ _add_newdocs.pyi
│  │     │  │  ├─ _add_newdocs_scalars.py
│  │     │  │  ├─ _add_newdocs_scalars.pyi
│  │     │  │  ├─ _asarray.py
│  │     │  │  ├─ _asarray.pyi
│  │     │  │  ├─ _dtype.py
│  │     │  │  ├─ _dtype.pyi
│  │     │  │  ├─ _dtype_ctypes.py
│  │     │  │  ├─ _dtype_ctypes.pyi
│  │     │  │  ├─ _exceptions.py
│  │     │  │  ├─ _exceptions.pyi
│  │     │  │  ├─ _internal.py
│  │     │  │  ├─ _internal.pyi
│  │     │  │  ├─ _methods.py
│  │     │  │  ├─ _methods.pyi
│  │     │  │  ├─ _multiarray_tests.cp313-win_amd64.lib
│  │     │  │  ├─ _multiarray_tests.cp313-win_amd64.pyd
│  │     │  │  ├─ _multiarray_umath.cp313-win_amd64.lib
│  │     │  │  ├─ _multiarray_umath.cp313-win_amd64.pyd
│  │     │  │  ├─ _operand_flag_tests.cp313-win_amd64.lib
│  │     │  │  ├─ _operand_flag_tests.cp313-win_amd64.pyd
│  │     │  │  ├─ _rational_tests.cp313-win_amd64.lib
│  │     │  │  ├─ _rational_tests.cp313-win_amd64.pyd
│  │     │  │  ├─ _simd.cp313-win_amd64.lib
│  │     │  │  ├─ _simd.cp313-win_amd64.pyd
│  │     │  │  ├─ _simd.pyi
│  │     │  │  ├─ _string_helpers.py
│  │     │  │  ├─ _string_helpers.pyi
│  │     │  │  ├─ _struct_ufunc_tests.cp313-win_amd64.lib
│  │     │  │  ├─ _struct_ufunc_tests.cp313-win_amd64.pyd
│  │     │  │  ├─ _type_aliases.py
│  │     │  │  ├─ _type_aliases.pyi
│  │     │  │  ├─ _ufunc_config.py
│  │     │  │  ├─ _ufunc_config.pyi
│  │     │  │  ├─ _umath_tests.cp313-win_amd64.lib
│  │     │  │  ├─ _umath_tests.cp313-win_amd64.pyd
│  │     │  │  ├─ _umath_tests.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ _distributor_init.py
│  │     │  ├─ _distributor_init.pyi
│  │     │  ├─ _expired_attrs_2_0.py
│  │     │  ├─ _expired_attrs_2_0.pyi
│  │     │  ├─ _globals.py
│  │     │  ├─ _globals.pyi
│  │     │  ├─ _pyinstaller
│  │     │  │  ├─ hook-numpy.py
│  │     │  │  ├─ hook-numpy.pyi
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ pyinstaller-smoke.py
│  │     │  │  │  ├─ test_pyinstaller.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ _pytesttester.py
│  │     │  ├─ _pytesttester.pyi
│  │     │  ├─ _typing
│  │     │  │  ├─ _add_docstring.py
│  │     │  │  ├─ _array_like.py
│  │     │  │  ├─ _char_codes.py
│  │     │  │  ├─ _dtype_like.py
│  │     │  │  ├─ _extended_precision.py
│  │     │  │  ├─ _nbit.py
│  │     │  │  ├─ _nbit_base.py
│  │     │  │  ├─ _nbit_base.pyi
│  │     │  │  ├─ _nested_sequence.py
│  │     │  │  ├─ _scalars.py
│  │     │  │  ├─ _shape.py
│  │     │  │  ├─ _ufunc.py
│  │     │  │  ├─ _ufunc.pyi
│  │     │  │  └─ __init__.py
│  │     │  ├─ _utils
│  │     │  │  ├─ _conversions.py
│  │     │  │  ├─ _conversions.pyi
│  │     │  │  ├─ _inspect.py
│  │     │  │  ├─ _inspect.pyi
│  │     │  │  ├─ _pep440.py
│  │     │  │  ├─ _pep440.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ __config__.py
│  │     │  ├─ __config__.pyi
│  │     │  ├─ __init__.cython-30.pxd
│  │     │  ├─ __init__.pxd
│  │     │  ├─ __init__.py
│  │     │  └─ __init__.pyi
│  │     ├─ numpy-2.5.1.dist-info
│  │     │  ├─ DELVEWHEEL
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  ├─ LICENSE.txt
│  │     │  │  └─ numpy
│  │     │  │     ├─ fft
│  │     │  │     │  └─ pocketfft
│  │     │  │     │     └─ LICENSE.md
│  │     │  │     ├─ linalg
│  │     │  │     │  └─ lapack_lite
│  │     │  │     │     └─ LICENSE.txt
│  │     │  │     ├─ ma
│  │     │  │     │  └─ LICENSE
│  │     │  │     ├─ random
│  │     │  │     │  ├─ LICENSE.md
│  │     │  │     │  └─ src
│  │     │  │     │     ├─ distributions
│  │     │  │     │     │  └─ LICENSE.md
│  │     │  │     │     ├─ mt19937
│  │     │  │     │     │  └─ LICENSE.md
│  │     │  │     │     ├─ pcg64
│  │     │  │     │     │  └─ LICENSE.md
│  │     │  │     │     ├─ philox
│  │     │  │     │     │  └─ LICENSE.md
│  │     │  │     │     ├─ sfc64
│  │     │  │     │     │  └─ LICENSE.md
│  │     │  │     │     └─ splitmix64
│  │     │  │     │        └─ LICENSE.md
│  │     │  │     └─ _core
│  │     │  │        ├─ include
│  │     │  │        │  └─ numpy
│  │     │  │        │     └─ libdivide
│  │     │  │        │        └─ LICENSE.txt
│  │     │  │        └─ src
│  │     │  │           ├─ common
│  │     │  │           │  └─ pythoncapi-compat
│  │     │  │           │     └─ COPYING
│  │     │  │           ├─ highway
│  │     │  │           │  └─ LICENSE
│  │     │  │           ├─ multiarray
│  │     │  │           │  └─ dragon4_LICENSE.txt
│  │     │  │           ├─ npysort
│  │     │  │           │  └─ x86-simd-sort
│  │     │  │           │     └─ LICENSE.md
│  │     │  │           └─ umath
│  │     │  │              └─ svml
│  │     │  │                 └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ numpy.libs
│  │     │  ├─ libscipy_openblas64_-b788215d9d47792bcba3a2e2a7114320.dll
│  │     │  └─ msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll
│  │     ├─ packaging
│  │     │  ├─ dependency_groups.py
│  │     │  ├─ direct_url.py
│  │     │  ├─ errors.py
│  │     │  ├─ licenses
│  │     │  │  ├─ _spdx.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ markers.py
│  │     │  ├─ metadata.py
│  │     │  ├─ py.typed
│  │     │  ├─ pylock.py
│  │     │  ├─ ranges.py
│  │     │  ├─ requirements.py
│  │     │  ├─ specifiers.py
│  │     │  ├─ tags.py
│  │     │  ├─ utils.py
│  │     │  ├─ version.py
│  │     │  ├─ _elffile.py
│  │     │  ├─ _manylinux.py
│  │     │  ├─ _musllinux.py
│  │     │  ├─ _parser.py
│  │     │  ├─ _ranges.py
│  │     │  ├─ _structures.py
│  │     │  ├─ _tokenizer.py
│  │     │  └─ __init__.py
│  │     ├─ packaging-26.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  ├─ LICENSE
│  │     │  │  ├─ LICENSE.APACHE
│  │     │  │  └─ LICENSE.BSD
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pandas
│  │     │  ├─ api
│  │     │  │  ├─ executors
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ extensions
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ indexers
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ interchange
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ internals.py
│  │     │  │  ├─ types
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ typing
│  │     │  │  │  ├─ aliases.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ arrays
│  │     │  │  └─ __init__.py
│  │     │  ├─ compat
│  │     │  │  ├─ numpy
│  │     │  │  │  ├─ function.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ pickle_compat.py
│  │     │  │  ├─ pyarrow.py
│  │     │  │  ├─ _constants.py
│  │     │  │  ├─ _optional.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ conftest.py
│  │     │  ├─ core
│  │     │  │  ├─ accessor.py
│  │     │  │  ├─ algorithms.py
│  │     │  │  ├─ api.py
│  │     │  │  ├─ apply.py
│  │     │  │  ├─ arraylike.py
│  │     │  │  ├─ arrays
│  │     │  │  │  ├─ arrow
│  │     │  │  │  │  ├─ accessors.py
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  ├─ extension_types.py
│  │     │  │  │  │  ├─ _arrow_utils.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ boolean.py
│  │     │  │  │  ├─ categorical.py
│  │     │  │  │  ├─ datetimelike.py
│  │     │  │  │  ├─ datetimes.py
│  │     │  │  │  ├─ floating.py
│  │     │  │  │  ├─ integer.py
│  │     │  │  │  ├─ interval.py
│  │     │  │  │  ├─ masked.py
│  │     │  │  │  ├─ numeric.py
│  │     │  │  │  ├─ numpy_.py
│  │     │  │  │  ├─ period.py
│  │     │  │  │  ├─ sparse
│  │     │  │  │  │  ├─ accessor.py
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  ├─ scipy_sparse.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ string_.py
│  │     │  │  │  ├─ string_arrow.py
│  │     │  │  │  ├─ timedeltas.py
│  │     │  │  │  ├─ _arrow_string_mixins.py
│  │     │  │  │  ├─ _mixins.py
│  │     │  │  │  ├─ _ranges.py
│  │     │  │  │  ├─ _utils.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ array_algos
│  │     │  │  │  ├─ datetimelike_accumulations.py
│  │     │  │  │  ├─ masked_accumulations.py
│  │     │  │  │  ├─ masked_reductions.py
│  │     │  │  │  ├─ putmask.py
│  │     │  │  │  ├─ quantile.py
│  │     │  │  │  ├─ replace.py
│  │     │  │  │  ├─ take.py
│  │     │  │  │  ├─ transforms.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ col.py
│  │     │  │  ├─ common.py
│  │     │  │  ├─ computation
│  │     │  │  │  ├─ align.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ engines.py
│  │     │  │  │  ├─ eval.py
│  │     │  │  │  ├─ expr.py
│  │     │  │  │  ├─ expressions.py
│  │     │  │  │  ├─ ops.py
│  │     │  │  │  ├─ parsing.py
│  │     │  │  │  ├─ pytables.py
│  │     │  │  │  ├─ scope.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ config_init.py
│  │     │  │  ├─ construction.py
│  │     │  │  ├─ dtypes
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ astype.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ cast.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ concat.py
│  │     │  │  │  ├─ dtypes.py
│  │     │  │  │  ├─ generic.py
│  │     │  │  │  ├─ inference.py
│  │     │  │  │  ├─ missing.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ flags.py
│  │     │  │  ├─ frame.py
│  │     │  │  ├─ generic.py
│  │     │  │  ├─ groupby
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ categorical.py
│  │     │  │  │  ├─ generic.py
│  │     │  │  │  ├─ groupby.py
│  │     │  │  │  ├─ grouper.py
│  │     │  │  │  ├─ indexing.py
│  │     │  │  │  ├─ numba_.py
│  │     │  │  │  ├─ ops.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ indexers
│  │     │  │  │  ├─ objects.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ indexes
│  │     │  │  │  ├─ accessors.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ category.py
│  │     │  │  │  ├─ datetimelike.py
│  │     │  │  │  ├─ datetimes.py
│  │     │  │  │  ├─ extension.py
│  │     │  │  │  ├─ frozen.py
│  │     │  │  │  ├─ interval.py
│  │     │  │  │  ├─ multi.py
│  │     │  │  │  ├─ period.py
│  │     │  │  │  ├─ range.py
│  │     │  │  │  ├─ timedeltas.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ indexing.py
│  │     │  │  ├─ interchange
│  │     │  │  │  ├─ buffer.py
│  │     │  │  │  ├─ column.py
│  │     │  │  │  ├─ dataframe.py
│  │     │  │  │  ├─ dataframe_protocol.py
│  │     │  │  │  ├─ from_dataframe.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ internals
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ blocks.py
│  │     │  │  │  ├─ concat.py
│  │     │  │  │  ├─ construction.py
│  │     │  │  │  ├─ managers.py
│  │     │  │  │  ├─ ops.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ methods
│  │     │  │  │  ├─ describe.py
│  │     │  │  │  ├─ selectn.py
│  │     │  │  │  ├─ to_dict.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ missing.py
│  │     │  │  ├─ nanops.py
│  │     │  │  ├─ ops
│  │     │  │  │  ├─ array_ops.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ dispatch.py
│  │     │  │  │  ├─ docstrings.py
│  │     │  │  │  ├─ invalid.py
│  │     │  │  │  ├─ mask_ops.py
│  │     │  │  │  ├─ missing.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ resample.py
│  │     │  │  ├─ reshape
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ concat.py
│  │     │  │  │  ├─ encoding.py
│  │     │  │  │  ├─ melt.py
│  │     │  │  │  ├─ merge.py
│  │     │  │  │  ├─ pivot.py
│  │     │  │  │  ├─ reshape.py
│  │     │  │  │  ├─ tile.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ roperator.py
│  │     │  │  ├─ sample.py
│  │     │  │  ├─ series.py
│  │     │  │  ├─ shared_docs.py
│  │     │  │  ├─ sorting.py
│  │     │  │  ├─ sparse
│  │     │  │  │  ├─ api.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ strings
│  │     │  │  │  ├─ accessor.py
│  │     │  │  │  ├─ object_array.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ tools
│  │     │  │  │  ├─ datetimes.py
│  │     │  │  │  ├─ numeric.py
│  │     │  │  │  ├─ timedeltas.py
│  │     │  │  │  ├─ times.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ util
│  │     │  │  │  ├─ hashing.py
│  │     │  │  │  ├─ numba_.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ window
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ doc.py
│  │     │  │  │  ├─ ewm.py
│  │     │  │  │  ├─ expanding.py
│  │     │  │  │  ├─ numba_.py
│  │     │  │  │  ├─ online.py
│  │     │  │  │  ├─ rolling.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ _numba
│  │     │  │  │  ├─ executor.py
│  │     │  │  │  ├─ extensions.py
│  │     │  │  │  ├─ kernels
│  │     │  │  │  │  ├─ mean_.py
│  │     │  │  │  │  ├─ min_max_.py
│  │     │  │  │  │  ├─ shared.py
│  │     │  │  │  │  ├─ sum_.py
│  │     │  │  │  │  ├─ var_.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ errors
│  │     │  │  ├─ cow.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ io
│  │     │  │  ├─ api.py
│  │     │  │  ├─ clipboard
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ clipboards.py
│  │     │  │  ├─ common.py
│  │     │  │  ├─ excel
│  │     │  │  │  ├─ _base.py
│  │     │  │  │  ├─ _calamine.py
│  │     │  │  │  ├─ _odfreader.py
│  │     │  │  │  ├─ _odswriter.py
│  │     │  │  │  ├─ _openpyxl.py
│  │     │  │  │  ├─ _pyxlsb.py
│  │     │  │  │  ├─ _util.py
│  │     │  │  │  ├─ _xlrd.py
│  │     │  │  │  ├─ _xlsxwriter.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ feather_format.py
│  │     │  │  ├─ formats
│  │     │  │  │  ├─ console.py
│  │     │  │  │  ├─ css.py
│  │     │  │  │  ├─ csvs.py
│  │     │  │  │  ├─ excel.py
│  │     │  │  │  ├─ format.py
│  │     │  │  │  ├─ html.py
│  │     │  │  │  ├─ info.py
│  │     │  │  │  ├─ printing.py
│  │     │  │  │  ├─ string.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  ├─ style_render.py
│  │     │  │  │  ├─ templates
│  │     │  │  │  │  ├─ html.tpl
│  │     │  │  │  │  ├─ html_style.tpl
│  │     │  │  │  │  ├─ html_table.tpl
│  │     │  │  │  │  ├─ latex.tpl
│  │     │  │  │  │  ├─ latex_longtable.tpl
│  │     │  │  │  │  ├─ latex_table.tpl
│  │     │  │  │  │  ├─ string.tpl
│  │     │  │  │  │  └─ typst.tpl
│  │     │  │  │  ├─ xml.py
│  │     │  │  │  ├─ _color_data.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ html.py
│  │     │  │  ├─ iceberg.py
│  │     │  │  ├─ json
│  │     │  │  │  ├─ _json.py
│  │     │  │  │  ├─ _normalize.py
│  │     │  │  │  ├─ _table_schema.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ orc.py
│  │     │  │  ├─ parquet.py
│  │     │  │  ├─ parsers
│  │     │  │  │  ├─ arrow_parser_wrapper.py
│  │     │  │  │  ├─ base_parser.py
│  │     │  │  │  ├─ c_parser_wrapper.py
│  │     │  │  │  ├─ python_parser.py
│  │     │  │  │  ├─ readers.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ pickle.py
│  │     │  │  ├─ pytables.py
│  │     │  │  ├─ sas
│  │     │  │  │  ├─ sas7bdat.py
│  │     │  │  │  ├─ sasreader.py
│  │     │  │  │  ├─ sas_constants.py
│  │     │  │  │  ├─ sas_xport.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ spss.py
│  │     │  │  ├─ sql.py
│  │     │  │  ├─ stata.py
│  │     │  │  ├─ xml.py
│  │     │  │  ├─ _util.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ plotting
│  │     │  │  ├─ _core.py
│  │     │  │  ├─ _matplotlib
│  │     │  │  │  ├─ boxplot.py
│  │     │  │  │  ├─ converter.py
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ groupby.py
│  │     │  │  │  ├─ hist.py
│  │     │  │  │  ├─ misc.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  ├─ timeseries.py
│  │     │  │  │  ├─ tools.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ _misc.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ pyproject.toml
│  │     │  ├─ testing.py
│  │     │  ├─ tests
│  │     │  │  ├─ api
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_types.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ apply
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_frame_apply.py
│  │     │  │  │  ├─ test_frame_apply_relabeling.py
│  │     │  │  │  ├─ test_frame_transform.py
│  │     │  │  │  ├─ test_invalid_arg.py
│  │     │  │  │  ├─ test_numba.py
│  │     │  │  │  ├─ test_series_apply.py
│  │     │  │  │  ├─ test_series_apply_relabeling.py
│  │     │  │  │  ├─ test_series_transform.py
│  │     │  │  │  ├─ test_str.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ arithmetic
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_array_ops.py
│  │     │  │  │  ├─ test_bool.py
│  │     │  │  │  ├─ test_categorical.py
│  │     │  │  │  ├─ test_datetime64.py
│  │     │  │  │  ├─ test_interval.py
│  │     │  │  │  ├─ test_numeric.py
│  │     │  │  │  ├─ test_object.py
│  │     │  │  │  ├─ test_period.py
│  │     │  │  │  ├─ test_string.py
│  │     │  │  │  ├─ test_timedelta64.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ arrays
│  │     │  │  │  ├─ boolean
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_comparison.py
│  │     │  │  │  │  ├─ test_construction.py
│  │     │  │  │  │  ├─ test_function.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_logical.py
│  │     │  │  │  │  ├─ test_ops.py
│  │     │  │  │  │  ├─ test_reduction.py
│  │     │  │  │  │  ├─ test_repr.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ categorical
│  │     │  │  │  │  ├─ test_algos.py
│  │     │  │  │  │  ├─ test_analytics.py
│  │     │  │  │  │  ├─ test_api.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_dtypes.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_map.py
│  │     │  │  │  │  ├─ test_missing.py
│  │     │  │  │  │  ├─ test_operators.py
│  │     │  │  │  │  ├─ test_replace.py
│  │     │  │  │  │  ├─ test_repr.py
│  │     │  │  │  │  ├─ test_sorting.py
│  │     │  │  │  │  ├─ test_subclass.py
│  │     │  │  │  │  ├─ test_take.py
│  │     │  │  │  │  ├─ test_warnings.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ datetimes
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_cumulative.py
│  │     │  │  │  │  ├─ test_reductions.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ floating
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_comparison.py
│  │     │  │  │  │  ├─ test_concat.py
│  │     │  │  │  │  ├─ test_construction.py
│  │     │  │  │  │  ├─ test_contains.py
│  │     │  │  │  │  ├─ test_function.py
│  │     │  │  │  │  ├─ test_repr.py
│  │     │  │  │  │  ├─ test_to_numpy.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ integer
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_comparison.py
│  │     │  │  │  │  ├─ test_concat.py
│  │     │  │  │  │  ├─ test_construction.py
│  │     │  │  │  │  ├─ test_dtypes.py
│  │     │  │  │  │  ├─ test_function.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_reduction.py
│  │     │  │  │  │  ├─ test_repr.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ interval
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_interval.py
│  │     │  │  │  │  ├─ test_interval_pyarrow.py
│  │     │  │  │  │  ├─ test_overlaps.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ masked
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_arrow_compat.py
│  │     │  │  │  │  ├─ test_function.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ masked_shared.py
│  │     │  │  │  ├─ numpy_
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_numpy.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ period
│  │     │  │  │  │  ├─ test_arrow_compat.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_reductions.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ sparse
│  │     │  │  │  │  ├─ test_accessor.py
│  │     │  │  │  │  ├─ test_arithmetics.py
│  │     │  │  │  │  ├─ test_array.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_combine_concat.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_dtype.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_libsparse.py
│  │     │  │  │  │  ├─ test_reductions.py
│  │     │  │  │  │  ├─ test_unary.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ string_
│  │     │  │  │  │  ├─ test_concat.py
│  │     │  │  │  │  ├─ test_string.py
│  │     │  │  │  │  ├─ test_string_arrow.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ test_array.py
│  │     │  │  │  ├─ test_datetimelike.py
│  │     │  │  │  ├─ test_datetimes.py
│  │     │  │  │  ├─ test_ndarray_backed.py
│  │     │  │  │  ├─ test_period.py
│  │     │  │  │  ├─ test_timedeltas.py
│  │     │  │  │  ├─ timedeltas
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_cumulative.py
│  │     │  │  │  │  ├─ test_reductions.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ base
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ test_constructors.py
│  │     │  │  │  ├─ test_conversion.py
│  │     │  │  │  ├─ test_fillna.py
│  │     │  │  │  ├─ test_misc.py
│  │     │  │  │  ├─ test_transpose.py
│  │     │  │  │  ├─ test_unique.py
│  │     │  │  │  ├─ test_value_counts.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ computation
│  │     │  │  │  ├─ test_compat.py
│  │     │  │  │  ├─ test_eval.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ config
│  │     │  │  │  ├─ test_config.py
│  │     │  │  │  ├─ test_localization.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ construction
│  │     │  │  │  ├─ test_extract_array.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ copy_view
│  │     │  │  │  ├─ index
│  │     │  │  │  │  ├─ test_datetimeindex.py
│  │     │  │  │  │  ├─ test_index.py
│  │     │  │  │  │  ├─ test_intervalindex.py
│  │     │  │  │  │  ├─ test_periodindex.py
│  │     │  │  │  │  ├─ test_timedeltaindex.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ test_array.py
│  │     │  │  │  ├─ test_astype.py
│  │     │  │  │  ├─ test_chained_assignment_deprecation.py
│  │     │  │  │  ├─ test_clip.py
│  │     │  │  │  ├─ test_constructors.py
│  │     │  │  │  ├─ test_copy_deprecation.py
│  │     │  │  │  ├─ test_core_functionalities.py
│  │     │  │  │  ├─ test_functions.py
│  │     │  │  │  ├─ test_indexing.py
│  │     │  │  │  ├─ test_internals.py
│  │     │  │  │  ├─ test_interp_fillna.py
│  │     │  │  │  ├─ test_methods.py
│  │     │  │  │  ├─ test_replace.py
│  │     │  │  │  ├─ test_setitem.py
│  │     │  │  │  ├─ test_util.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ dtypes
│  │     │  │  │  ├─ cast
│  │     │  │  │  │  ├─ test_box_unbox.py
│  │     │  │  │  │  ├─ test_can_hold_element.py
│  │     │  │  │  │  ├─ test_construct_from_scalar.py
│  │     │  │  │  │  ├─ test_construct_ndarray.py
│  │     │  │  │  │  ├─ test_construct_object_arr.py
│  │     │  │  │  │  ├─ test_dict_compat.py
│  │     │  │  │  │  ├─ test_downcast.py
│  │     │  │  │  │  ├─ test_find_common_type.py
│  │     │  │  │  │  ├─ test_infer_datetimelike.py
│  │     │  │  │  │  ├─ test_infer_dtype.py
│  │     │  │  │  │  ├─ test_promote.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_concat.py
│  │     │  │  │  ├─ test_dtypes.py
│  │     │  │  │  ├─ test_generic.py
│  │     │  │  │  ├─ test_inference.py
│  │     │  │  │  ├─ test_missing.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ extension
│  │     │  │  │  ├─ array_with_attr
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  ├─ test_array_with_attr.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ base
│  │     │  │  │  │  ├─ accumulate.py
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ casting.py
│  │     │  │  │  │  ├─ constructors.py
│  │     │  │  │  │  ├─ dim2.py
│  │     │  │  │  │  ├─ dtype.py
│  │     │  │  │  │  ├─ getitem.py
│  │     │  │  │  │  ├─ groupby.py
│  │     │  │  │  │  ├─ index.py
│  │     │  │  │  │  ├─ interface.py
│  │     │  │  │  │  ├─ io.py
│  │     │  │  │  │  ├─ methods.py
│  │     │  │  │  │  ├─ missing.py
│  │     │  │  │  │  ├─ ops.py
│  │     │  │  │  │  ├─ printing.py
│  │     │  │  │  │  ├─ reduce.py
│  │     │  │  │  │  ├─ reshaping.py
│  │     │  │  │  │  ├─ setitem.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ date
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ decimal
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  ├─ test_decimal.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ json
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  ├─ test_json.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ list
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  ├─ test_list.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ test_arrow.py
│  │     │  │  │  ├─ test_categorical.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_datetime.py
│  │     │  │  │  ├─ test_extension.py
│  │     │  │  │  ├─ test_interval.py
│  │     │  │  │  ├─ test_masked.py
│  │     │  │  │  ├─ test_numpy.py
│  │     │  │  │  ├─ test_period.py
│  │     │  │  │  ├─ test_sparse.py
│  │     │  │  │  ├─ test_string.py
│  │     │  │  │  ├─ uuid
│  │     │  │  │  │  ├─ test_uuid.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ frame
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ constructors
│  │     │  │  │  │  ├─ test_from_dict.py
│  │     │  │  │  │  ├─ test_from_records.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ indexing
│  │     │  │  │  │  ├─ test_coercion.py
│  │     │  │  │  │  ├─ test_delitem.py
│  │     │  │  │  │  ├─ test_get.py
│  │     │  │  │  │  ├─ test_getitem.py
│  │     │  │  │  │  ├─ test_get_value.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_insert.py
│  │     │  │  │  │  ├─ test_mask.py
│  │     │  │  │  │  ├─ test_setitem.py
│  │     │  │  │  │  ├─ test_set_value.py
│  │     │  │  │  │  ├─ test_take.py
│  │     │  │  │  │  ├─ test_where.py
│  │     │  │  │  │  ├─ test_xs.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ methods
│  │     │  │  │  │  ├─ test_add_prefix_suffix.py
│  │     │  │  │  │  ├─ test_align.py
│  │     │  │  │  │  ├─ test_asfreq.py
│  │     │  │  │  │  ├─ test_asof.py
│  │     │  │  │  │  ├─ test_assign.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_at_time.py
│  │     │  │  │  │  ├─ test_between_time.py
│  │     │  │  │  │  ├─ test_clip.py
│  │     │  │  │  │  ├─ test_combine.py
│  │     │  │  │  │  ├─ test_combine_first.py
│  │     │  │  │  │  ├─ test_compare.py
│  │     │  │  │  │  ├─ test_convert_dtypes.py
│  │     │  │  │  │  ├─ test_copy.py
│  │     │  │  │  │  ├─ test_count.py
│  │     │  │  │  │  ├─ test_cov_corr.py
│  │     │  │  │  │  ├─ test_describe.py
│  │     │  │  │  │  ├─ test_diff.py
│  │     │  │  │  │  ├─ test_dot.py
│  │     │  │  │  │  ├─ test_drop.py
│  │     │  │  │  │  ├─ test_droplevel.py
│  │     │  │  │  │  ├─ test_dropna.py
│  │     │  │  │  │  ├─ test_drop_duplicates.py
│  │     │  │  │  │  ├─ test_dtypes.py
│  │     │  │  │  │  ├─ test_duplicated.py
│  │     │  │  │  │  ├─ test_equals.py
│  │     │  │  │  │  ├─ test_explode.py
│  │     │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  ├─ test_filter.py
│  │     │  │  │  │  ├─ test_first_valid_index.py
│  │     │  │  │  │  ├─ test_get_numeric_data.py
│  │     │  │  │  │  ├─ test_head_tail.py
│  │     │  │  │  │  ├─ test_infer_objects.py
│  │     │  │  │  │  ├─ test_info.py
│  │     │  │  │  │  ├─ test_interpolate.py
│  │     │  │  │  │  ├─ test_isetitem.py
│  │     │  │  │  │  ├─ test_isin.py
│  │     │  │  │  │  ├─ test_is_homogeneous_dtype.py
│  │     │  │  │  │  ├─ test_iterrows.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_map.py
│  │     │  │  │  │  ├─ test_matmul.py
│  │     │  │  │  │  ├─ test_nlargest.py
│  │     │  │  │  │  ├─ test_pct_change.py
│  │     │  │  │  │  ├─ test_pipe.py
│  │     │  │  │  │  ├─ test_pop.py
│  │     │  │  │  │  ├─ test_quantile.py
│  │     │  │  │  │  ├─ test_rank.py
│  │     │  │  │  │  ├─ test_reindex.py
│  │     │  │  │  │  ├─ test_reindex_like.py
│  │     │  │  │  │  ├─ test_rename.py
│  │     │  │  │  │  ├─ test_rename_axis.py
│  │     │  │  │  │  ├─ test_reorder_levels.py
│  │     │  │  │  │  ├─ test_replace.py
│  │     │  │  │  │  ├─ test_reset_index.py
│  │     │  │  │  │  ├─ test_round.py
│  │     │  │  │  │  ├─ test_sample.py
│  │     │  │  │  │  ├─ test_select_dtypes.py
│  │     │  │  │  │  ├─ test_set_axis.py
│  │     │  │  │  │  ├─ test_set_index.py
│  │     │  │  │  │  ├─ test_shift.py
│  │     │  │  │  │  ├─ test_size.py
│  │     │  │  │  │  ├─ test_sort_index.py
│  │     │  │  │  │  ├─ test_sort_values.py
│  │     │  │  │  │  ├─ test_swaplevel.py
│  │     │  │  │  │  ├─ test_to_csv.py
│  │     │  │  │  │  ├─ test_to_dict.py
│  │     │  │  │  │  ├─ test_to_dict_of_blocks.py
│  │     │  │  │  │  ├─ test_to_numpy.py
│  │     │  │  │  │  ├─ test_to_period.py
│  │     │  │  │  │  ├─ test_to_records.py
│  │     │  │  │  │  ├─ test_to_timestamp.py
│  │     │  │  │  │  ├─ test_transpose.py
│  │     │  │  │  │  ├─ test_truncate.py
│  │     │  │  │  │  ├─ test_tz_convert.py
│  │     │  │  │  │  ├─ test_tz_localize.py
│  │     │  │  │  │  ├─ test_update.py
│  │     │  │  │  │  ├─ test_values.py
│  │     │  │  │  │  ├─ test_value_counts.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ test_alter_axes.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  ├─ test_arrow_interface.py
│  │     │  │  │  ├─ test_block_internals.py
│  │     │  │  │  ├─ test_constructors.py
│  │     │  │  │  ├─ test_cumulative.py
│  │     │  │  │  ├─ test_iteration.py
│  │     │  │  │  ├─ test_logical_ops.py
│  │     │  │  │  ├─ test_nonunique_indexes.py
│  │     │  │  │  ├─ test_npfuncs.py
│  │     │  │  │  ├─ test_query_eval.py
│  │     │  │  │  ├─ test_reductions.py
│  │     │  │  │  ├─ test_repr.py
│  │     │  │  │  ├─ test_stack_unstack.py
│  │     │  │  │  ├─ test_subclass.py
│  │     │  │  │  ├─ test_ufunc.py
│  │     │  │  │  ├─ test_unary.py
│  │     │  │  │  ├─ test_validate.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ generic
│  │     │  │  │  ├─ test_duplicate_labels.py
│  │     │  │  │  ├─ test_finalize.py
│  │     │  │  │  ├─ test_frame.py
│  │     │  │  │  ├─ test_generic.py
│  │     │  │  │  ├─ test_label_or_level_utils.py
│  │     │  │  │  ├─ test_series.py
│  │     │  │  │  ├─ test_to_xarray.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ groupby
│  │     │  │  │  ├─ aggregate
│  │     │  │  │  │  ├─ test_aggregate.py
│  │     │  │  │  │  ├─ test_cython.py
│  │     │  │  │  │  ├─ test_numba.py
│  │     │  │  │  │  ├─ test_other.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ methods
│  │     │  │  │  │  ├─ test_describe.py
│  │     │  │  │  │  ├─ test_groupby_shift_diff.py
│  │     │  │  │  │  ├─ test_is_monotonic.py
│  │     │  │  │  │  ├─ test_kurt.py
│  │     │  │  │  │  ├─ test_nlargest_nsmallest.py
│  │     │  │  │  │  ├─ test_nth.py
│  │     │  │  │  │  ├─ test_quantile.py
│  │     │  │  │  │  ├─ test_rank.py
│  │     │  │  │  │  ├─ test_sample.py
│  │     │  │  │  │  ├─ test_size.py
│  │     │  │  │  │  ├─ test_skew.py
│  │     │  │  │  │  ├─ test_value_counts.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ test_all_methods.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_apply.py
│  │     │  │  │  ├─ test_bin_groupby.py
│  │     │  │  │  ├─ test_categorical.py
│  │     │  │  │  ├─ test_counting.py
│  │     │  │  │  ├─ test_cumulative.py
│  │     │  │  │  ├─ test_filters.py
│  │     │  │  │  ├─ test_groupby.py
│  │     │  │  │  ├─ test_groupby_dropna.py
│  │     │  │  │  ├─ test_groupby_subclass.py
│  │     │  │  │  ├─ test_grouping.py
│  │     │  │  │  ├─ test_indexing.py
│  │     │  │  │  ├─ test_index_as_string.py
│  │     │  │  │  ├─ test_libgroupby.py
│  │     │  │  │  ├─ test_missing.py
│  │     │  │  │  ├─ test_numba.py
│  │     │  │  │  ├─ test_numeric_only.py
│  │     │  │  │  ├─ test_pipe.py
│  │     │  │  │  ├─ test_raises.py
│  │     │  │  │  ├─ test_reductions.py
│  │     │  │  │  ├─ test_timegrouper.py
│  │     │  │  │  ├─ transform
│  │     │  │  │  │  ├─ test_numba.py
│  │     │  │  │  │  ├─ test_transform.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ indexes
│  │     │  │  │  ├─ base_class
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  ├─ test_reshape.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  ├─ test_where.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ categorical
│  │     │  │  │  │  ├─ test_append.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_category.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_equals.py
│  │     │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_map.py
│  │     │  │  │  │  ├─ test_reindex.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ datetimelike_
│  │     │  │  │  │  ├─ test_drop_duplicates.py
│  │     │  │  │  │  ├─ test_equals.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_is_monotonic.py
│  │     │  │  │  │  ├─ test_nat.py
│  │     │  │  │  │  ├─ test_sort_values.py
│  │     │  │  │  │  ├─ test_value_counts.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ datetimes
│  │     │  │  │  │  ├─ methods
│  │     │  │  │  │  │  ├─ test_asof.py
│  │     │  │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  │  ├─ test_delete.py
│  │     │  │  │  │  │  ├─ test_factorize.py
│  │     │  │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  │  ├─ test_insert.py
│  │     │  │  │  │  │  ├─ test_isocalendar.py
│  │     │  │  │  │  │  ├─ test_map.py
│  │     │  │  │  │  │  ├─ test_normalize.py
│  │     │  │  │  │  │  ├─ test_repeat.py
│  │     │  │  │  │  │  ├─ test_resolution.py
│  │     │  │  │  │  │  ├─ test_round.py
│  │     │  │  │  │  │  ├─ test_shift.py
│  │     │  │  │  │  │  ├─ test_snap.py
│  │     │  │  │  │  │  ├─ test_to_frame.py
│  │     │  │  │  │  │  ├─ test_to_julian_date.py
│  │     │  │  │  │  │  ├─ test_to_period.py
│  │     │  │  │  │  │  ├─ test_to_pydatetime.py
│  │     │  │  │  │  │  ├─ test_to_series.py
│  │     │  │  │  │  │  ├─ test_tz_convert.py
│  │     │  │  │  │  │  ├─ test_tz_localize.py
│  │     │  │  │  │  │  ├─ test_unique.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_datetime.py
│  │     │  │  │  │  ├─ test_date_range.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_freq_attr.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_iter.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_npfuncs.py
│  │     │  │  │  │  ├─ test_ops.py
│  │     │  │  │  │  ├─ test_partial_slicing.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  ├─ test_reindex.py
│  │     │  │  │  │  ├─ test_scalar_compat.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  ├─ test_timezones.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ interval
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_equals.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_interval.py
│  │     │  │  │  │  ├─ test_interval_range.py
│  │     │  │  │  │  ├─ test_interval_tree.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ multi
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_analytics.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_compat.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_conversion.py
│  │     │  │  │  │  ├─ test_copy.py
│  │     │  │  │  │  ├─ test_drop.py
│  │     │  │  │  │  ├─ test_duplicates.py
│  │     │  │  │  │  ├─ test_equivalence.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_get_level_values.py
│  │     │  │  │  │  ├─ test_get_set.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_integrity.py
│  │     │  │  │  │  ├─ test_isin.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_lexsort.py
│  │     │  │  │  │  ├─ test_missing.py
│  │     │  │  │  │  ├─ test_monotonic.py
│  │     │  │  │  │  ├─ test_names.py
│  │     │  │  │  │  ├─ test_partial_indexing.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  ├─ test_reindex.py
│  │     │  │  │  │  ├─ test_reshape.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  ├─ test_sorting.py
│  │     │  │  │  │  ├─ test_take.py
│  │     │  │  │  │  ├─ test_util.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ numeric
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_numeric.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ object
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ period
│  │     │  │  │  │  ├─ methods
│  │     │  │  │  │  │  ├─ test_asfreq.py
│  │     │  │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  │  ├─ test_factorize.py
│  │     │  │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  │  ├─ test_insert.py
│  │     │  │  │  │  │  ├─ test_is_full.py
│  │     │  │  │  │  │  ├─ test_repeat.py
│  │     │  │  │  │  │  ├─ test_shift.py
│  │     │  │  │  │  │  ├─ test_to_timestamp.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_freq_attr.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_monotonic.py
│  │     │  │  │  │  ├─ test_partial_slicing.py
│  │     │  │  │  │  ├─ test_period.py
│  │     │  │  │  │  ├─ test_period_range.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  ├─ test_resolution.py
│  │     │  │  │  │  ├─ test_scalar_compat.py
│  │     │  │  │  │  ├─ test_searchsorted.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  ├─ test_tools.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ ranges
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_range.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ string
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ test_any_index.py
│  │     │  │  │  ├─ test_base.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_datetimelike.py
│  │     │  │  │  ├─ test_engines.py
│  │     │  │  │  ├─ test_frozen.py
│  │     │  │  │  ├─ test_indexing.py
│  │     │  │  │  ├─ test_index_new.py
│  │     │  │  │  ├─ test_numpy_compat.py
│  │     │  │  │  ├─ test_old_base.py
│  │     │  │  │  ├─ test_setops.py
│  │     │  │  │  ├─ test_subclass.py
│  │     │  │  │  ├─ timedeltas
│  │     │  │  │  │  ├─ methods
│  │     │  │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  │  ├─ test_factorize.py
│  │     │  │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  │  ├─ test_insert.py
│  │     │  │  │  │  │  ├─ test_repeat.py
│  │     │  │  │  │  │  ├─ test_shift.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_delete.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_freq_attr.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_ops.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  ├─ test_scalar_compat.py
│  │     │  │  │  │  ├─ test_searchsorted.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  ├─ test_timedelta.py
│  │     │  │  │  │  ├─ test_timedelta_range.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ indexing
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ interval
│  │     │  │  │  │  ├─ test_interval.py
│  │     │  │  │  │  ├─ test_interval_new.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ multiindex
│  │     │  │  │  │  ├─ test_chaining_and_caching.py
│  │     │  │  │  │  ├─ test_datetime.py
│  │     │  │  │  │  ├─ test_getitem.py
│  │     │  │  │  │  ├─ test_iloc.py
│  │     │  │  │  │  ├─ test_indexing_slow.py
│  │     │  │  │  │  ├─ test_loc.py
│  │     │  │  │  │  ├─ test_multiindex.py
│  │     │  │  │  │  ├─ test_partial.py
│  │     │  │  │  │  ├─ test_setitem.py
│  │     │  │  │  │  ├─ test_slice.py
│  │     │  │  │  │  ├─ test_sorted.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ test_at.py
│  │     │  │  │  ├─ test_categorical.py
│  │     │  │  │  ├─ test_chaining_and_caching.py
│  │     │  │  │  ├─ test_check_indexer.py
│  │     │  │  │  ├─ test_coercion.py
│  │     │  │  │  ├─ test_datetime.py
│  │     │  │  │  ├─ test_floats.py
│  │     │  │  │  ├─ test_iat.py
│  │     │  │  │  ├─ test_iloc.py
│  │     │  │  │  ├─ test_indexers.py
│  │     │  │  │  ├─ test_indexing.py
│  │     │  │  │  ├─ test_loc.py
│  │     │  │  │  ├─ test_na_indexing.py
│  │     │  │  │  ├─ test_partial.py
│  │     │  │  │  ├─ test_scalar.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ interchange
│  │     │  │  │  ├─ test_impl.py
│  │     │  │  │  ├─ test_spec_conformance.py
│  │     │  │  │  ├─ test_utils.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ internals
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_internals.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ io
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ excel
│  │     │  │  │  │  ├─ test_odf.py
│  │     │  │  │  │  ├─ test_odswriter.py
│  │     │  │  │  │  ├─ test_openpyxl.py
│  │     │  │  │  │  ├─ test_readers.py
│  │     │  │  │  │  ├─ test_style.py
│  │     │  │  │  │  ├─ test_writers.py
│  │     │  │  │  │  ├─ test_xlrd.py
│  │     │  │  │  │  ├─ test_xlsxwriter.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ formats
│  │     │  │  │  │  ├─ style
│  │     │  │  │  │  │  ├─ test_bar.py
│  │     │  │  │  │  │  ├─ test_exceptions.py
│  │     │  │  │  │  │  ├─ test_format.py
│  │     │  │  │  │  │  ├─ test_highlight.py
│  │     │  │  │  │  │  ├─ test_html.py
│  │     │  │  │  │  │  ├─ test_matplotlib.py
│  │     │  │  │  │  │  ├─ test_non_unique.py
│  │     │  │  │  │  │  ├─ test_style.py
│  │     │  │  │  │  │  ├─ test_tooltip.py
│  │     │  │  │  │  │  ├─ test_to_latex.py
│  │     │  │  │  │  │  ├─ test_to_string.py
│  │     │  │  │  │  │  ├─ test_to_typst.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ test_console.py
│  │     │  │  │  │  ├─ test_css.py
│  │     │  │  │  │  ├─ test_eng_formatting.py
│  │     │  │  │  │  ├─ test_format.py
│  │     │  │  │  │  ├─ test_ipython_compat.py
│  │     │  │  │  │  ├─ test_printing.py
│  │     │  │  │  │  ├─ test_to_csv.py
│  │     │  │  │  │  ├─ test_to_excel.py
│  │     │  │  │  │  ├─ test_to_html.py
│  │     │  │  │  │  ├─ test_to_latex.py
│  │     │  │  │  │  ├─ test_to_markdown.py
│  │     │  │  │  │  ├─ test_to_string.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ generate_legacy_storage_files.py
│  │     │  │  │  ├─ json
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_compression.py
│  │     │  │  │  │  ├─ test_deprecated_kwargs.py
│  │     │  │  │  │  ├─ test_json_table_schema.py
│  │     │  │  │  │  ├─ test_json_table_schema_ext_dtype.py
│  │     │  │  │  │  ├─ test_normalize.py
│  │     │  │  │  │  ├─ test_pandas.py
│  │     │  │  │  │  ├─ test_readlines.py
│  │     │  │  │  │  ├─ test_ujson.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ parser
│  │     │  │  │  │  ├─ common
│  │     │  │  │  │  │  ├─ test_chunksize.py
│  │     │  │  │  │  │  ├─ test_common_basic.py
│  │     │  │  │  │  │  ├─ test_data_list.py
│  │     │  │  │  │  │  ├─ test_decimal.py
│  │     │  │  │  │  │  ├─ test_file_buffer_url.py
│  │     │  │  │  │  │  ├─ test_float.py
│  │     │  │  │  │  │  ├─ test_index.py
│  │     │  │  │  │  │  ├─ test_inf.py
│  │     │  │  │  │  │  ├─ test_ints.py
│  │     │  │  │  │  │  ├─ test_iterator.py
│  │     │  │  │  │  │  ├─ test_read_errors.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ dtypes
│  │     │  │  │  │  │  ├─ test_categorical.py
│  │     │  │  │  │  │  ├─ test_dtypes_basic.py
│  │     │  │  │  │  │  ├─ test_empty.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ test_comment.py
│  │     │  │  │  │  ├─ test_compression.py
│  │     │  │  │  │  ├─ test_concatenate_chunks.py
│  │     │  │  │  │  ├─ test_converters.py
│  │     │  │  │  │  ├─ test_c_parser_only.py
│  │     │  │  │  │  ├─ test_dialect.py
│  │     │  │  │  │  ├─ test_encoding.py
│  │     │  │  │  │  ├─ test_header.py
│  │     │  │  │  │  ├─ test_index_col.py
│  │     │  │  │  │  ├─ test_mangle_dupes.py
│  │     │  │  │  │  ├─ test_multi_thread.py
│  │     │  │  │  │  ├─ test_na_values.py
│  │     │  │  │  │  ├─ test_network.py
│  │     │  │  │  │  ├─ test_parse_dates.py
│  │     │  │  │  │  ├─ test_python_parser_only.py
│  │     │  │  │  │  ├─ test_quoting.py
│  │     │  │  │  │  ├─ test_read_fwf.py
│  │     │  │  │  │  ├─ test_skiprows.py
│  │     │  │  │  │  ├─ test_textreader.py
│  │     │  │  │  │  ├─ test_unsupported.py
│  │     │  │  │  │  ├─ test_upcast.py
│  │     │  │  │  │  ├─ usecols
│  │     │  │  │  │  │  ├─ test_parse_dates.py
│  │     │  │  │  │  │  ├─ test_strings.py
│  │     │  │  │  │  │  ├─ test_usecols_basic.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ pytables
│  │     │  │  │  │  ├─ common.py
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_append.py
│  │     │  │  │  │  ├─ test_categorical.py
│  │     │  │  │  │  ├─ test_compat.py
│  │     │  │  │  │  ├─ test_complex.py
│  │     │  │  │  │  ├─ test_errors.py
│  │     │  │  │  │  ├─ test_file_handling.py
│  │     │  │  │  │  ├─ test_keys.py
│  │     │  │  │  │  ├─ test_put.py
│  │     │  │  │  │  ├─ test_pytables_missing.py
│  │     │  │  │  │  ├─ test_read.py
│  │     │  │  │  │  ├─ test_retain_attributes.py
│  │     │  │  │  │  ├─ test_round_trip.py
│  │     │  │  │  │  ├─ test_select.py
│  │     │  │  │  │  ├─ test_store.py
│  │     │  │  │  │  ├─ test_subclass.py
│  │     │  │  │  │  ├─ test_timezones.py
│  │     │  │  │  │  ├─ test_time_series.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ sas
│  │     │  │  │  │  ├─ test_byteswap.py
│  │     │  │  │  │  ├─ test_sas.py
│  │     │  │  │  │  ├─ test_sas7bdat.py
│  │     │  │  │  │  ├─ test_xport.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ test_clipboard.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_compression.py
│  │     │  │  │  ├─ test_feather.py
│  │     │  │  │  ├─ test_fsspec.py
│  │     │  │  │  ├─ test_gcs.py
│  │     │  │  │  ├─ test_html.py
│  │     │  │  │  ├─ test_http_headers.py
│  │     │  │  │  ├─ test_iceberg.py
│  │     │  │  │  ├─ test_orc.py
│  │     │  │  │  ├─ test_parquet.py
│  │     │  │  │  ├─ test_pickle.py
│  │     │  │  │  ├─ test_s3.py
│  │     │  │  │  ├─ test_spss.py
│  │     │  │  │  ├─ test_sql.py
│  │     │  │  │  ├─ test_stata.py
│  │     │  │  │  ├─ test_util.py
│  │     │  │  │  ├─ xml
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_to_xml.py
│  │     │  │  │  │  ├─ test_xml.py
│  │     │  │  │  │  ├─ test_xml_dtypes.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ libs
│  │     │  │  │  ├─ test_hashtable.py
│  │     │  │  │  ├─ test_join.py
│  │     │  │  │  ├─ test_lib.py
│  │     │  │  │  ├─ test_libalgos.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ plotting
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ frame
│  │     │  │  │  │  ├─ test_frame.py
│  │     │  │  │  │  ├─ test_frame_color.py
│  │     │  │  │  │  ├─ test_frame_groupby.py
│  │     │  │  │  │  ├─ test_frame_legend.py
│  │     │  │  │  │  ├─ test_frame_subplots.py
│  │     │  │  │  │  ├─ test_hist_box_by.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ test_backend.py
│  │     │  │  │  ├─ test_boxplot_method.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_converter.py
│  │     │  │  │  ├─ test_datetimelike.py
│  │     │  │  │  ├─ test_groupby.py
│  │     │  │  │  ├─ test_hist_method.py
│  │     │  │  │  ├─ test_misc.py
│  │     │  │  │  ├─ test_series.py
│  │     │  │  │  ├─ test_style.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ reductions
│  │     │  │  │  ├─ test_reductions.py
│  │     │  │  │  ├─ test_stat_reductions.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ resample
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_base.py
│  │     │  │  │  ├─ test_datetime_index.py
│  │     │  │  │  ├─ test_period_index.py
│  │     │  │  │  ├─ test_resampler_grouper.py
│  │     │  │  │  ├─ test_resample_api.py
│  │     │  │  │  ├─ test_timedelta.py
│  │     │  │  │  ├─ test_time_grouper.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ reshape
│  │     │  │  │  ├─ concat
│  │     │  │  │  │  ├─ test_append.py
│  │     │  │  │  │  ├─ test_append_common.py
│  │     │  │  │  │  ├─ test_categorical.py
│  │     │  │  │  │  ├─ test_concat.py
│  │     │  │  │  │  ├─ test_dataframe.py
│  │     │  │  │  │  ├─ test_datetimes.py
│  │     │  │  │  │  ├─ test_empty.py
│  │     │  │  │  │  ├─ test_index.py
│  │     │  │  │  │  ├─ test_invalid.py
│  │     │  │  │  │  ├─ test_series.py
│  │     │  │  │  │  ├─ test_sort.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ merge
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_merge.py
│  │     │  │  │  │  ├─ test_merge_antijoin.py
│  │     │  │  │  │  ├─ test_merge_asof.py
│  │     │  │  │  │  ├─ test_merge_cross.py
│  │     │  │  │  │  ├─ test_merge_index_as_string.py
│  │     │  │  │  │  ├─ test_merge_ordered.py
│  │     │  │  │  │  ├─ test_multi.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ test_crosstab.py
│  │     │  │  │  ├─ test_cut.py
│  │     │  │  │  ├─ test_from_dummies.py
│  │     │  │  │  ├─ test_get_dummies.py
│  │     │  │  │  ├─ test_melt.py
│  │     │  │  │  ├─ test_pivot.py
│  │     │  │  │  ├─ test_pivot_multilevel.py
│  │     │  │  │  ├─ test_qcut.py
│  │     │  │  │  ├─ test_union_categoricals.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ scalar
│  │     │  │  │  ├─ interval
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_contains.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_interval.py
│  │     │  │  │  │  ├─ test_overlaps.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ period
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_asfreq.py
│  │     │  │  │  │  ├─ test_period.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ test_nat.py
│  │     │  │  │  ├─ test_na_scalar.py
│  │     │  │  │  ├─ timedelta
│  │     │  │  │  │  ├─ methods
│  │     │  │  │  │  │  ├─ test_as_unit.py
│  │     │  │  │  │  │  ├─ test_round.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_timedelta.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ timestamp
│  │     │  │  │  │  ├─ methods
│  │     │  │  │  │  │  ├─ test_as_unit.py
│  │     │  │  │  │  │  ├─ test_normalize.py
│  │     │  │  │  │  │  ├─ test_replace.py
│  │     │  │  │  │  │  ├─ test_round.py
│  │     │  │  │  │  │  ├─ test_timestamp_method.py
│  │     │  │  │  │  │  ├─ test_to_julian_date.py
│  │     │  │  │  │  │  ├─ test_to_pydatetime.py
│  │     │  │  │  │  │  ├─ test_tz_convert.py
│  │     │  │  │  │  │  ├─ test_tz_localize.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_comparisons.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_timestamp.py
│  │     │  │  │  │  ├─ test_timezones.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ series
│  │     │  │  │  ├─ accessors
│  │     │  │  │  │  ├─ test_cat_accessor.py
│  │     │  │  │  │  ├─ test_dt_accessor.py
│  │     │  │  │  │  ├─ test_list_accessor.py
│  │     │  │  │  │  ├─ test_sparse_accessor.py
│  │     │  │  │  │  ├─ test_struct_accessor.py
│  │     │  │  │  │  ├─ test_str_accessor.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ indexing
│  │     │  │  │  │  ├─ test_datetime.py
│  │     │  │  │  │  ├─ test_delitem.py
│  │     │  │  │  │  ├─ test_get.py
│  │     │  │  │  │  ├─ test_getitem.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_mask.py
│  │     │  │  │  │  ├─ test_setitem.py
│  │     │  │  │  │  ├─ test_set_value.py
│  │     │  │  │  │  ├─ test_take.py
│  │     │  │  │  │  ├─ test_where.py
│  │     │  │  │  │  ├─ test_xs.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ methods
│  │     │  │  │  │  ├─ test_add_prefix_suffix.py
│  │     │  │  │  │  ├─ test_align.py
│  │     │  │  │  │  ├─ test_argsort.py
│  │     │  │  │  │  ├─ test_asof.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_autocorr.py
│  │     │  │  │  │  ├─ test_between.py
│  │     │  │  │  │  ├─ test_case_when.py
│  │     │  │  │  │  ├─ test_clip.py
│  │     │  │  │  │  ├─ test_combine.py
│  │     │  │  │  │  ├─ test_combine_first.py
│  │     │  │  │  │  ├─ test_compare.py
│  │     │  │  │  │  ├─ test_convert_dtypes.py
│  │     │  │  │  │  ├─ test_copy.py
│  │     │  │  │  │  ├─ test_count.py
│  │     │  │  │  │  ├─ test_cov_corr.py
│  │     │  │  │  │  ├─ test_describe.py
│  │     │  │  │  │  ├─ test_diff.py
│  │     │  │  │  │  ├─ test_drop.py
│  │     │  │  │  │  ├─ test_dropna.py
│  │     │  │  │  │  ├─ test_drop_duplicates.py
│  │     │  │  │  │  ├─ test_dtypes.py
│  │     │  │  │  │  ├─ test_duplicated.py
│  │     │  │  │  │  ├─ test_equals.py
│  │     │  │  │  │  ├─ test_explode.py
│  │     │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  ├─ test_get_numeric_data.py
│  │     │  │  │  │  ├─ test_head_tail.py
│  │     │  │  │  │  ├─ test_infer_objects.py
│  │     │  │  │  │  ├─ test_info.py
│  │     │  │  │  │  ├─ test_interpolate.py
│  │     │  │  │  │  ├─ test_isin.py
│  │     │  │  │  │  ├─ test_isna.py
│  │     │  │  │  │  ├─ test_is_monotonic.py
│  │     │  │  │  │  ├─ test_is_unique.py
│  │     │  │  │  │  ├─ test_item.py
│  │     │  │  │  │  ├─ test_map.py
│  │     │  │  │  │  ├─ test_matmul.py
│  │     │  │  │  │  ├─ test_nlargest.py
│  │     │  │  │  │  ├─ test_nunique.py
│  │     │  │  │  │  ├─ test_pct_change.py
│  │     │  │  │  │  ├─ test_pop.py
│  │     │  │  │  │  ├─ test_quantile.py
│  │     │  │  │  │  ├─ test_rank.py
│  │     │  │  │  │  ├─ test_reindex.py
│  │     │  │  │  │  ├─ test_reindex_like.py
│  │     │  │  │  │  ├─ test_rename.py
│  │     │  │  │  │  ├─ test_rename_axis.py
│  │     │  │  │  │  ├─ test_repeat.py
│  │     │  │  │  │  ├─ test_replace.py
│  │     │  │  │  │  ├─ test_reset_index.py
│  │     │  │  │  │  ├─ test_round.py
│  │     │  │  │  │  ├─ test_searchsorted.py
│  │     │  │  │  │  ├─ test_set_name.py
│  │     │  │  │  │  ├─ test_size.py
│  │     │  │  │  │  ├─ test_sort_index.py
│  │     │  │  │  │  ├─ test_sort_values.py
│  │     │  │  │  │  ├─ test_tolist.py
│  │     │  │  │  │  ├─ test_to_csv.py
│  │     │  │  │  │  ├─ test_to_dict.py
│  │     │  │  │  │  ├─ test_to_frame.py
│  │     │  │  │  │  ├─ test_to_numpy.py
│  │     │  │  │  │  ├─ test_truncate.py
│  │     │  │  │  │  ├─ test_tz_localize.py
│  │     │  │  │  │  ├─ test_unique.py
│  │     │  │  │  │  ├─ test_unstack.py
│  │     │  │  │  │  ├─ test_update.py
│  │     │  │  │  │  ├─ test_values.py
│  │     │  │  │  │  ├─ test_value_counts.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  ├─ test_arrow_interface.py
│  │     │  │  │  ├─ test_constructors.py
│  │     │  │  │  ├─ test_cumulative.py
│  │     │  │  │  ├─ test_formats.py
│  │     │  │  │  ├─ test_iteration.py
│  │     │  │  │  ├─ test_logical_ops.py
│  │     │  │  │  ├─ test_missing.py
│  │     │  │  │  ├─ test_npfuncs.py
│  │     │  │  │  ├─ test_reductions.py
│  │     │  │  │  ├─ test_subclass.py
│  │     │  │  │  ├─ test_ufunc.py
│  │     │  │  │  ├─ test_unary.py
│  │     │  │  │  ├─ test_validate.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ strings
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_case_justify.py
│  │     │  │  │  ├─ test_cat.py
│  │     │  │  │  ├─ test_extract.py
│  │     │  │  │  ├─ test_find_replace.py
│  │     │  │  │  ├─ test_get_dummies.py
│  │     │  │  │  ├─ test_split_partition.py
│  │     │  │  │  ├─ test_strings.py
│  │     │  │  │  ├─ test_string_array.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ test_aggregation.py
│  │     │  │  ├─ test_algos.py
│  │     │  │  ├─ test_col.py
│  │     │  │  ├─ test_common.py
│  │     │  │  ├─ test_downstream.py
│  │     │  │  ├─ test_errors.py
│  │     │  │  ├─ test_expressions.py
│  │     │  │  ├─ test_flags.py
│  │     │  │  ├─ test_multilevel.py
│  │     │  │  ├─ test_nanops.py
│  │     │  │  ├─ test_optional_dependency.py
│  │     │  │  ├─ test_register_accessor.py
│  │     │  │  ├─ test_sorting.py
│  │     │  │  ├─ test_take.py
│  │     │  │  ├─ tools
│  │     │  │  │  ├─ test_to_datetime.py
│  │     │  │  │  ├─ test_to_numeric.py
│  │     │  │  │  ├─ test_to_time.py
│  │     │  │  │  ├─ test_to_timedelta.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ tseries
│  │     │  │  │  ├─ frequencies
│  │     │  │  │  │  ├─ test_frequencies.py
│  │     │  │  │  │  ├─ test_freq_code.py
│  │     │  │  │  │  ├─ test_inference.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ holiday
│  │     │  │  │  │  ├─ test_calendar.py
│  │     │  │  │  │  ├─ test_federal.py
│  │     │  │  │  │  ├─ test_holiday.py
│  │     │  │  │  │  ├─ test_observance.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ offsets
│  │     │  │  │  │  ├─ common.py
│  │     │  │  │  │  ├─ test_business_day.py
│  │     │  │  │  │  ├─ test_business_halfyear.py
│  │     │  │  │  │  ├─ test_business_hour.py
│  │     │  │  │  │  ├─ test_business_month.py
│  │     │  │  │  │  ├─ test_business_quarter.py
│  │     │  │  │  │  ├─ test_business_year.py
│  │     │  │  │  │  ├─ test_common.py
│  │     │  │  │  │  ├─ test_custom_business_day.py
│  │     │  │  │  │  ├─ test_custom_business_hour.py
│  │     │  │  │  │  ├─ test_custom_business_month.py
│  │     │  │  │  │  ├─ test_dst.py
│  │     │  │  │  │  ├─ test_easter.py
│  │     │  │  │  │  ├─ test_fiscal.py
│  │     │  │  │  │  ├─ test_halfyear.py
│  │     │  │  │  │  ├─ test_index.py
│  │     │  │  │  │  ├─ test_month.py
│  │     │  │  │  │  ├─ test_offsets.py
│  │     │  │  │  │  ├─ test_offsets_properties.py
│  │     │  │  │  │  ├─ test_quarter.py
│  │     │  │  │  │  ├─ test_ticks.py
│  │     │  │  │  │  ├─ test_week.py
│  │     │  │  │  │  ├─ test_year.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ tslibs
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_array_to_datetime.py
│  │     │  │  │  ├─ test_ccalendar.py
│  │     │  │  │  ├─ test_conversion.py
│  │     │  │  │  ├─ test_fields.py
│  │     │  │  │  ├─ test_libfrequencies.py
│  │     │  │  │  ├─ test_liboffsets.py
│  │     │  │  │  ├─ test_npy_units.py
│  │     │  │  │  ├─ test_np_datetime.py
│  │     │  │  │  ├─ test_parse_iso8601.py
│  │     │  │  │  ├─ test_parsing.py
│  │     │  │  │  ├─ test_period.py
│  │     │  │  │  ├─ test_resolution.py
│  │     │  │  │  ├─ test_strptime.py
│  │     │  │  │  ├─ test_timedeltas.py
│  │     │  │  │  ├─ test_timezones.py
│  │     │  │  │  ├─ test_to_offset.py
│  │     │  │  │  ├─ test_tzconversion.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ util
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_assert_almost_equal.py
│  │     │  │  │  ├─ test_assert_attr_equal.py
│  │     │  │  │  ├─ test_assert_categorical_equal.py
│  │     │  │  │  ├─ test_assert_extension_array_equal.py
│  │     │  │  │  ├─ test_assert_frame_equal.py
│  │     │  │  │  ├─ test_assert_index_equal.py
│  │     │  │  │  ├─ test_assert_interval_array_equal.py
│  │     │  │  │  ├─ test_assert_numpy_array_equal.py
│  │     │  │  │  ├─ test_assert_produces_warning.py
│  │     │  │  │  ├─ test_assert_series_equal.py
│  │     │  │  │  ├─ test_deprecate.py
│  │     │  │  │  ├─ test_deprecate_kwarg.py
│  │     │  │  │  ├─ test_deprecate_nonkeyword_arguments.py
│  │     │  │  │  ├─ test_doc.py
│  │     │  │  │  ├─ test_hashing.py
│  │     │  │  │  ├─ test_numba.py
│  │     │  │  │  ├─ test_rewrite_warning.py
│  │     │  │  │  ├─ test_shares_memory.py
│  │     │  │  │  ├─ test_show_versions.py
│  │     │  │  │  ├─ test_util.py
│  │     │  │  │  ├─ test_validate_args.py
│  │     │  │  │  ├─ test_validate_args_and_kwargs.py
│  │     │  │  │  ├─ test_validate_inclusive.py
│  │     │  │  │  ├─ test_validate_kwargs.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ window
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ moments
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_moments_consistency_ewm.py
│  │     │  │  │  │  ├─ test_moments_consistency_expanding.py
│  │     │  │  │  │  ├─ test_moments_consistency_rolling.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_apply.py
│  │     │  │  │  ├─ test_base_indexer.py
│  │     │  │  │  ├─ test_cython_aggregations.py
│  │     │  │  │  ├─ test_dtypes.py
│  │     │  │  │  ├─ test_ewm.py
│  │     │  │  │  ├─ test_expanding.py
│  │     │  │  │  ├─ test_groupby.py
│  │     │  │  │  ├─ test_numba.py
│  │     │  │  │  ├─ test_online.py
│  │     │  │  │  ├─ test_pairwise.py
│  │     │  │  │  ├─ test_rolling.py
│  │     │  │  │  ├─ test_rolling_functions.py
│  │     │  │  │  ├─ test_rolling_quantile.py
│  │     │  │  │  ├─ test_rolling_skew_kurt.py
│  │     │  │  │  ├─ test_timeseries_window.py
│  │     │  │  │  ├─ test_win_type.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ tseries
│  │     │  │  ├─ api.py
│  │     │  │  ├─ frequencies.py
│  │     │  │  ├─ holiday.py
│  │     │  │  ├─ offsets.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ util
│  │     │  │  ├─ version
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ _decorators.py
│  │     │  │  ├─ _doctools.py
│  │     │  │  ├─ _exceptions.py
│  │     │  │  ├─ _print_versions.py
│  │     │  │  ├─ _tester.py
│  │     │  │  ├─ _test_decorators.py
│  │     │  │  ├─ _validators.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _config
│  │     │  │  ├─ config.py
│  │     │  │  ├─ dates.py
│  │     │  │  ├─ display.py
│  │     │  │  ├─ localization.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _libs
│  │     │  │  ├─ algos.cp313-win_amd64.lib
│  │     │  │  ├─ algos.cp313-win_amd64.pyd
│  │     │  │  ├─ algos.pyi
│  │     │  │  ├─ arrays.cp313-win_amd64.lib
│  │     │  │  ├─ arrays.cp313-win_amd64.pyd
│  │     │  │  ├─ arrays.pyi
│  │     │  │  ├─ byteswap.cp313-win_amd64.lib
│  │     │  │  ├─ byteswap.cp313-win_amd64.pyd
│  │     │  │  ├─ byteswap.pyi
│  │     │  │  ├─ groupby.cp313-win_amd64.lib
│  │     │  │  ├─ groupby.cp313-win_amd64.pyd
│  │     │  │  ├─ groupby.pyi
│  │     │  │  ├─ hashing.cp313-win_amd64.lib
│  │     │  │  ├─ hashing.cp313-win_amd64.pyd
│  │     │  │  ├─ hashing.pyi
│  │     │  │  ├─ hashtable.cp313-win_amd64.lib
│  │     │  │  ├─ hashtable.cp313-win_amd64.pyd
│  │     │  │  ├─ hashtable.pyi
│  │     │  │  ├─ index.cp313-win_amd64.lib
│  │     │  │  ├─ index.cp313-win_amd64.pyd
│  │     │  │  ├─ index.pyi
│  │     │  │  ├─ indexing.cp313-win_amd64.lib
│  │     │  │  ├─ indexing.cp313-win_amd64.pyd
│  │     │  │  ├─ indexing.pyi
│  │     │  │  ├─ internals.cp313-win_amd64.lib
│  │     │  │  ├─ internals.cp313-win_amd64.pyd
│  │     │  │  ├─ internals.pyi
│  │     │  │  ├─ interval.cp313-win_amd64.lib
│  │     │  │  ├─ interval.cp313-win_amd64.pyd
│  │     │  │  ├─ interval.pyi
│  │     │  │  ├─ join.cp313-win_amd64.lib
│  │     │  │  ├─ join.cp313-win_amd64.pyd
│  │     │  │  ├─ join.pyi
│  │     │  │  ├─ json.cp313-win_amd64.lib
│  │     │  │  ├─ json.cp313-win_amd64.pyd
│  │     │  │  ├─ json.pyi
│  │     │  │  ├─ lib.cp313-win_amd64.lib
│  │     │  │  ├─ lib.cp313-win_amd64.pyd
│  │     │  │  ├─ lib.pyi
│  │     │  │  ├─ missing.cp313-win_amd64.lib
│  │     │  │  ├─ missing.cp313-win_amd64.pyd
│  │     │  │  ├─ missing.pyi
│  │     │  │  ├─ ops.cp313-win_amd64.lib
│  │     │  │  ├─ ops.cp313-win_amd64.pyd
│  │     │  │  ├─ ops.pyi
│  │     │  │  ├─ ops_dispatch.cp313-win_amd64.lib
│  │     │  │  ├─ ops_dispatch.cp313-win_amd64.pyd
│  │     │  │  ├─ ops_dispatch.pyi
│  │     │  │  ├─ pandas_datetime.cp313-win_amd64.lib
│  │     │  │  ├─ pandas_datetime.cp313-win_amd64.pyd
│  │     │  │  ├─ pandas_parser.cp313-win_amd64.lib
│  │     │  │  ├─ pandas_parser.cp313-win_amd64.pyd
│  │     │  │  ├─ parsers.cp313-win_amd64.lib
│  │     │  │  ├─ parsers.cp313-win_amd64.pyd
│  │     │  │  ├─ parsers.pyi
│  │     │  │  ├─ properties.cp313-win_amd64.lib
│  │     │  │  ├─ properties.cp313-win_amd64.pyd
│  │     │  │  ├─ properties.pyi
│  │     │  │  ├─ reshape.cp313-win_amd64.lib
│  │     │  │  ├─ reshape.cp313-win_amd64.pyd
│  │     │  │  ├─ reshape.pyi
│  │     │  │  ├─ sas.cp313-win_amd64.lib
│  │     │  │  ├─ sas.cp313-win_amd64.pyd
│  │     │  │  ├─ sas.pyi
│  │     │  │  ├─ sparse.cp313-win_amd64.lib
│  │     │  │  ├─ sparse.cp313-win_amd64.pyd
│  │     │  │  ├─ sparse.pyi
│  │     │  │  ├─ testing.cp313-win_amd64.lib
│  │     │  │  ├─ testing.cp313-win_amd64.pyd
│  │     │  │  ├─ testing.pyi
│  │     │  │  ├─ tslib.cp313-win_amd64.lib
│  │     │  │  ├─ tslib.cp313-win_amd64.pyd
│  │     │  │  ├─ tslib.pyi
│  │     │  │  ├─ tslibs
│  │     │  │  │  ├─ base.cp313-win_amd64.lib
│  │     │  │  │  ├─ base.cp313-win_amd64.pyd
│  │     │  │  │  ├─ ccalendar.cp313-win_amd64.lib
│  │     │  │  │  ├─ ccalendar.cp313-win_amd64.pyd
│  │     │  │  │  ├─ ccalendar.pyi
│  │     │  │  │  ├─ conversion.cp313-win_amd64.lib
│  │     │  │  │  ├─ conversion.cp313-win_amd64.pyd
│  │     │  │  │  ├─ conversion.pyi
│  │     │  │  │  ├─ dtypes.cp313-win_amd64.lib
│  │     │  │  │  ├─ dtypes.cp313-win_amd64.pyd
│  │     │  │  │  ├─ dtypes.pyi
│  │     │  │  │  ├─ fields.cp313-win_amd64.lib
│  │     │  │  │  ├─ fields.cp313-win_amd64.pyd
│  │     │  │  │  ├─ fields.pyi
│  │     │  │  │  ├─ nattype.cp313-win_amd64.lib
│  │     │  │  │  ├─ nattype.cp313-win_amd64.pyd
│  │     │  │  │  ├─ nattype.pyi
│  │     │  │  │  ├─ np_datetime.cp313-win_amd64.lib
│  │     │  │  │  ├─ np_datetime.cp313-win_amd64.pyd
│  │     │  │  │  ├─ np_datetime.pyi
│  │     │  │  │  ├─ offsets.cp313-win_amd64.lib
│  │     │  │  │  ├─ offsets.cp313-win_amd64.pyd
│  │     │  │  │  ├─ offsets.pyi
│  │     │  │  │  ├─ parsing.cp313-win_amd64.lib
│  │     │  │  │  ├─ parsing.cp313-win_amd64.pyd
│  │     │  │  │  ├─ parsing.pyi
│  │     │  │  │  ├─ period.cp313-win_amd64.lib
│  │     │  │  │  ├─ period.cp313-win_amd64.pyd
│  │     │  │  │  ├─ period.pyi
│  │     │  │  │  ├─ strptime.cp313-win_amd64.lib
│  │     │  │  │  ├─ strptime.cp313-win_amd64.pyd
│  │     │  │  │  ├─ strptime.pyi
│  │     │  │  │  ├─ timedeltas.cp313-win_amd64.lib
│  │     │  │  │  ├─ timedeltas.cp313-win_amd64.pyd
│  │     │  │  │  ├─ timedeltas.pyi
│  │     │  │  │  ├─ timestamps.cp313-win_amd64.lib
│  │     │  │  │  ├─ timestamps.cp313-win_amd64.pyd
│  │     │  │  │  ├─ timestamps.pyi
│  │     │  │  │  ├─ timezones.cp313-win_amd64.lib
│  │     │  │  │  ├─ timezones.cp313-win_amd64.pyd
│  │     │  │  │  ├─ timezones.pyi
│  │     │  │  │  ├─ tzconversion.cp313-win_amd64.lib
│  │     │  │  │  ├─ tzconversion.cp313-win_amd64.pyd
│  │     │  │  │  ├─ tzconversion.pyi
│  │     │  │  │  ├─ vectorized.cp313-win_amd64.lib
│  │     │  │  │  ├─ vectorized.cp313-win_amd64.pyd
│  │     │  │  │  ├─ vectorized.pyi
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ window
│  │     │  │  │  ├─ aggregations.cp313-win_amd64.lib
│  │     │  │  │  ├─ aggregations.cp313-win_amd64.pyd
│  │     │  │  │  ├─ aggregations.pyi
│  │     │  │  │  ├─ indexers.cp313-win_amd64.lib
│  │     │  │  │  ├─ indexers.cp313-win_amd64.pyd
│  │     │  │  │  ├─ indexers.pyi
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ writers.cp313-win_amd64.lib
│  │     │  │  ├─ writers.cp313-win_amd64.pyd
│  │     │  │  ├─ writers.pyi
│  │     │  │  ├─ _cyutility.cp313-win_amd64.lib
│  │     │  │  ├─ _cyutility.cp313-win_amd64.pyd
│  │     │  │  └─ __init__.py
│  │     │  ├─ _testing
│  │     │  │  ├─ asserters.py
│  │     │  │  ├─ compat.py
│  │     │  │  ├─ contexts.py
│  │     │  │  ├─ _hypothesis.py
│  │     │  │  ├─ _io.py
│  │     │  │  ├─ _warnings.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _typing.py
│  │     │  ├─ _version.py
│  │     │  ├─ _version_meson.py
│  │     │  └─ __init__.py
│  │     ├─ pandas-3.0.3.dist-info
│  │     │  ├─ DELVEWHEEL
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pandas.libs
│  │     │  └─ msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll
│  │     ├─ peewee-4.3.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ peewee-stubs
│  │     │  └─ __init__.pyi
│  │     ├─ peewee.py
│  │     ├─ PIL
│  │     │  ├─ AvifImagePlugin.py
│  │     │  ├─ BdfFontFile.py
│  │     │  ├─ BlpImagePlugin.py
│  │     │  ├─ BmpImagePlugin.py
│  │     │  ├─ BufrStubImagePlugin.py
│  │     │  ├─ ContainerIO.py
│  │     │  ├─ CurImagePlugin.py
│  │     │  ├─ DcxImagePlugin.py
│  │     │  ├─ DdsImagePlugin.py
│  │     │  ├─ EpsImagePlugin.py
│  │     │  ├─ ExifTags.py
│  │     │  ├─ features.py
│  │     │  ├─ FitsImagePlugin.py
│  │     │  ├─ FliImagePlugin.py
│  │     │  ├─ FontFile.py
│  │     │  ├─ FpxImagePlugin.py
│  │     │  ├─ FtexImagePlugin.py
│  │     │  ├─ GbrImagePlugin.py
│  │     │  ├─ GdImageFile.py
│  │     │  ├─ GifImagePlugin.py
│  │     │  ├─ GimpGradientFile.py
│  │     │  ├─ GimpPaletteFile.py
│  │     │  ├─ GribStubImagePlugin.py
│  │     │  ├─ Hdf5StubImagePlugin.py
│  │     │  ├─ IcnsImagePlugin.py
│  │     │  ├─ IcoImagePlugin.py
│  │     │  ├─ Image.py
│  │     │  ├─ ImageChops.py
│  │     │  ├─ ImageCms.py
│  │     │  ├─ ImageColor.py
│  │     │  ├─ ImageDraw.py
│  │     │  ├─ ImageDraw2.py
│  │     │  ├─ ImageEnhance.py
│  │     │  ├─ ImageFile.py
│  │     │  ├─ ImageFilter.py
│  │     │  ├─ ImageFont.py
│  │     │  ├─ ImageGrab.py
│  │     │  ├─ ImageMath.py
│  │     │  ├─ ImageMode.py
│  │     │  ├─ ImageMorph.py
│  │     │  ├─ ImageOps.py
│  │     │  ├─ ImagePalette.py
│  │     │  ├─ ImagePath.py
│  │     │  ├─ ImageQt.py
│  │     │  ├─ ImageSequence.py
│  │     │  ├─ ImageShow.py
│  │     │  ├─ ImageStat.py
│  │     │  ├─ ImageText.py
│  │     │  ├─ ImageTk.py
│  │     │  ├─ ImageTransform.py
│  │     │  ├─ ImageWin.py
│  │     │  ├─ ImImagePlugin.py
│  │     │  ├─ ImtImagePlugin.py
│  │     │  ├─ IptcImagePlugin.py
│  │     │  ├─ Jpeg2KImagePlugin.py
│  │     │  ├─ JpegImagePlugin.py
│  │     │  ├─ JpegPresets.py
│  │     │  ├─ McIdasImagePlugin.py
│  │     │  ├─ MicImagePlugin.py
│  │     │  ├─ MpegImagePlugin.py
│  │     │  ├─ MpoImagePlugin.py
│  │     │  ├─ MspImagePlugin.py
│  │     │  ├─ PaletteFile.py
│  │     │  ├─ PalmImagePlugin.py
│  │     │  ├─ PcdImagePlugin.py
│  │     │  ├─ PcfFontFile.py
│  │     │  ├─ PcxImagePlugin.py
│  │     │  ├─ PdfImagePlugin.py
│  │     │  ├─ PdfParser.py
│  │     │  ├─ PixarImagePlugin.py
│  │     │  ├─ PngImagePlugin.py
│  │     │  ├─ PpmImagePlugin.py
│  │     │  ├─ PsdImagePlugin.py
│  │     │  ├─ PSDraw.py
│  │     │  ├─ py.typed
│  │     │  ├─ QoiImagePlugin.py
│  │     │  ├─ report.py
│  │     │  ├─ SgiImagePlugin.py
│  │     │  ├─ SpiderImagePlugin.py
│  │     │  ├─ SunImagePlugin.py
│  │     │  ├─ TarIO.py
│  │     │  ├─ TgaImagePlugin.py
│  │     │  ├─ TiffImagePlugin.py
│  │     │  ├─ TiffTags.py
│  │     │  ├─ WalImageFile.py
│  │     │  ├─ WebPImagePlugin.py
│  │     │  ├─ WmfImagePlugin.py
│  │     │  ├─ XbmImagePlugin.py
│  │     │  ├─ XpmImagePlugin.py
│  │     │  ├─ XVThumbImagePlugin.py
│  │     │  ├─ _avif.cp313-win_amd64.pyd
│  │     │  ├─ _avif.pyi
│  │     │  ├─ _binary.py
│  │     │  ├─ _deprecate.py
│  │     │  ├─ _imaging.cp313-win_amd64.pyd
│  │     │  ├─ _imaging.pyi
│  │     │  ├─ _imagingcms.cp313-win_amd64.pyd
│  │     │  ├─ _imagingcms.pyi
│  │     │  ├─ _imagingft.cp313-win_amd64.pyd
│  │     │  ├─ _imagingft.pyi
│  │     │  ├─ _imagingmath.cp313-win_amd64.pyd
│  │     │  ├─ _imagingmath.pyi
│  │     │  ├─ _imagingmorph.cp313-win_amd64.pyd
│  │     │  ├─ _imagingmorph.pyi
│  │     │  ├─ _imagingtk.cp313-win_amd64.pyd
│  │     │  ├─ _imagingtk.pyi
│  │     │  ├─ _tkinter_finder.py
│  │     │  ├─ _typing.py
│  │     │  ├─ _util.py
│  │     │  ├─ _version.py
│  │     │  ├─ _webp.cp313-win_amd64.pyd
│  │     │  ├─ _webp.pyi
│  │     │  ├─ __init__.py
│  │     │  └─ __main__.py
│  │     ├─ pillow-12.3.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ sboms
│  │     │  │  └─ pillow-12.3.0.cdx.json
│  │     │  ├─ top_level.txt
│  │     │  ├─ WHEEL
│  │     │  └─ zip-safe
│  │     ├─ pip
│  │     │  ├─ py.typed
│  │     │  ├─ _internal
│  │     │  │  ├─ build_env.py
│  │     │  │  ├─ cache.py
│  │     │  │  ├─ cli
│  │     │  │  │  ├─ autocompletion.py
│  │     │  │  │  ├─ base_command.py
│  │     │  │  │  ├─ cmdoptions.py
│  │     │  │  │  ├─ command_context.py
│  │     │  │  │  ├─ index_command.py
│  │     │  │  │  ├─ main.py
│  │     │  │  │  ├─ main_parser.py
│  │     │  │  │  ├─ parser.py
│  │     │  │  │  ├─ progress_bars.py
│  │     │  │  │  ├─ req_command.py
│  │     │  │  │  ├─ spinners.py
│  │     │  │  │  ├─ status_codes.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ commands
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ completion.py
│  │     │  │  │  ├─ configuration.py
│  │     │  │  │  ├─ debug.py
│  │     │  │  │  ├─ download.py
│  │     │  │  │  ├─ freeze.py
│  │     │  │  │  ├─ hash.py
│  │     │  │  │  ├─ help.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ inspect.py
│  │     │  │  │  ├─ install.py
│  │     │  │  │  ├─ list.py
│  │     │  │  │  ├─ lock.py
│  │     │  │  │  ├─ search.py
│  │     │  │  │  ├─ show.py
│  │     │  │  │  ├─ uninstall.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ configuration.py
│  │     │  │  ├─ distributions
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ installed.py
│  │     │  │  │  ├─ sdist.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ index
│  │     │  │  │  ├─ collector.py
│  │     │  │  │  ├─ package_finder.py
│  │     │  │  │  ├─ sources.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ locations
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ _distutils.py
│  │     │  │  │  ├─ _sysconfig.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ main.py
│  │     │  │  ├─ metadata
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ importlib
│  │     │  │  │  │  ├─ _compat.py
│  │     │  │  │  │  ├─ _dists.py
│  │     │  │  │  │  ├─ _envs.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ pkg_resources.py
│  │     │  │  │  ├─ _json.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ models
│  │     │  │  │  ├─ candidate.py
│  │     │  │  │  ├─ direct_url.py
│  │     │  │  │  ├─ format_control.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ installation_report.py
│  │     │  │  │  ├─ link.py
│  │     │  │  │  ├─ release_control.py
│  │     │  │  │  ├─ scheme.py
│  │     │  │  │  ├─ search_scope.py
│  │     │  │  │  ├─ selection_prefs.py
│  │     │  │  │  ├─ target_python.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ network
│  │     │  │  │  ├─ auth.py
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ download.py
│  │     │  │  │  ├─ lazy_wheel.py
│  │     │  │  │  ├─ session.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ xmlrpc.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ operations
│  │     │  │  │  ├─ build
│  │     │  │  │  │  ├─ build_tracker.py
│  │     │  │  │  │  ├─ metadata.py
│  │     │  │  │  │  ├─ metadata_editable.py
│  │     │  │  │  │  ├─ wheel.py
│  │     │  │  │  │  ├─ wheel_editable.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ freeze.py
│  │     │  │  │  ├─ install
│  │     │  │  │  │  ├─ wheel.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ prepare.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ pyproject.py
│  │     │  │  ├─ req
│  │     │  │  │  ├─ constructors.py
│  │     │  │  │  ├─ pep723.py
│  │     │  │  │  ├─ req_dependency_group.py
│  │     │  │  │  ├─ req_file.py
│  │     │  │  │  ├─ req_install.py
│  │     │  │  │  ├─ req_set.py
│  │     │  │  │  ├─ req_uninstall.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ resolution
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ legacy
│  │     │  │  │  │  ├─ resolver.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ resolvelib
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ candidates.py
│  │     │  │  │  │  ├─ factory.py
│  │     │  │  │  │  ├─ found_candidates.py
│  │     │  │  │  │  ├─ provider.py
│  │     │  │  │  │  ├─ reporter.py
│  │     │  │  │  │  ├─ requirements.py
│  │     │  │  │  │  ├─ resolver.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ self_outdated_check.py
│  │     │  │  ├─ utils
│  │     │  │  │  ├─ appdirs.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ compatibility_tags.py
│  │     │  │  │  ├─ datetime.py
│  │     │  │  │  ├─ deprecation.py
│  │     │  │  │  ├─ direct_url_helpers.py
│  │     │  │  │  ├─ egg_link.py
│  │     │  │  │  ├─ entrypoints.py
│  │     │  │  │  ├─ filesystem.py
│  │     │  │  │  ├─ filetypes.py
│  │     │  │  │  ├─ glibc.py
│  │     │  │  │  ├─ hashes.py
│  │     │  │  │  ├─ logging.py
│  │     │  │  │  ├─ misc.py
│  │     │  │  │  ├─ packaging.py
│  │     │  │  │  ├─ pylock.py
│  │     │  │  │  ├─ retry.py
│  │     │  │  │  ├─ subprocess.py
│  │     │  │  │  ├─ temp_dir.py
│  │     │  │  │  ├─ unpacking.py
│  │     │  │  │  ├─ urls.py
│  │     │  │  │  ├─ virtualenv.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ _jaraco_text.py
│  │     │  │  │  ├─ _log.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ vcs
│  │     │  │  │  ├─ bazaar.py
│  │     │  │  │  ├─ git.py
│  │     │  │  │  ├─ mercurial.py
│  │     │  │  │  ├─ subversion.py
│  │     │  │  │  ├─ versioncontrol.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ wheel_builder.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _vendor
│  │     │  │  ├─ cachecontrol
│  │     │  │  │  ├─ adapter.py
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ caches
│  │     │  │  │  │  ├─ file_cache.py
│  │     │  │  │  │  ├─ redis_cache.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ controller.py
│  │     │  │  │  ├─ filewrapper.py
│  │     │  │  │  ├─ heuristics.py
│  │     │  │  │  ├─ LICENSE.txt
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ serialize.py
│  │     │  │  │  ├─ wrapper.py
│  │     │  │  │  ├─ _cmd.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ certifi
│  │     │  │  │  ├─ cacert.pem
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ LICENSE
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __main__.py
│  │     │  │  ├─ distlib
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ LICENSE.txt
│  │     │  │  │  ├─ resources.py
│  │     │  │  │  ├─ scripts.py
│  │     │  │  │  ├─ t32.exe
│  │     │  │  │  ├─ t64-arm.exe
│  │     │  │  │  ├─ t64.exe
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ w32.exe
│  │     │  │  │  ├─ w64-arm.exe
│  │     │  │  │  ├─ w64.exe
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ distro
│  │     │  │  │  ├─ distro.py
│  │     │  │  │  ├─ LICENSE
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __main__.py
│  │     │  │  ├─ idna
│  │     │  │  │  ├─ codec.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ idnadata.py
│  │     │  │  │  ├─ intranges.py
│  │     │  │  │  ├─ LICENSE.md
│  │     │  │  │  ├─ package_data.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ uts46data.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ msgpack
│  │     │  │  │  ├─ COPYING
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ ext.py
│  │     │  │  │  ├─ fallback.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ packaging
│  │     │  │  │  ├─ dependency_groups.py
│  │     │  │  │  ├─ direct_url.py
│  │     │  │  │  ├─ errors.py
│  │     │  │  │  ├─ LICENSE
│  │     │  │  │  ├─ LICENSE.APACHE
│  │     │  │  │  ├─ LICENSE.BSD
│  │     │  │  │  ├─ licenses
│  │     │  │  │  │  ├─ _spdx.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ metadata.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ pylock.py
│  │     │  │  │  ├─ requirements.py
│  │     │  │  │  ├─ specifiers.py
│  │     │  │  │  ├─ tags.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ _elffile.py
│  │     │  │  │  ├─ _manylinux.py
│  │     │  │  │  ├─ _musllinux.py
│  │     │  │  │  ├─ _parser.py
│  │     │  │  │  ├─ _structures.py
│  │     │  │  │  ├─ _tokenizer.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ pkg_resources
│  │     │  │  │  ├─ LICENSE
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ platformdirs
│  │     │  │  │  ├─ android.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ LICENSE
│  │     │  │  │  ├─ macos.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ unix.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ windows.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __main__.py
│  │     │  │  ├─ pygments
│  │     │  │  │  ├─ console.py
│  │     │  │  │  ├─ filter.py
│  │     │  │  │  ├─ filters
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ formatter.py
│  │     │  │  │  ├─ formatters
│  │     │  │  │  │  ├─ _mapping.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ lexer.py
│  │     │  │  │  ├─ lexers
│  │     │  │  │  │  ├─ python.py
│  │     │  │  │  │  ├─ _mapping.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ LICENSE
│  │     │  │  │  ├─ modeline.py
│  │     │  │  │  ├─ plugin.py
│  │     │  │  │  ├─ regexopt.py
│  │     │  │  │  ├─ scanner.py
│  │     │  │  │  ├─ sphinxext.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  ├─ styles
│  │     │  │  │  │  ├─ _mapping.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ token.py
│  │     │  │  │  ├─ unistring.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __main__.py
│  │     │  │  ├─ pyproject_hooks
│  │     │  │  │  ├─ LICENSE
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ _impl.py
│  │     │  │  │  ├─ _in_process
│  │     │  │  │  │  ├─ _in_process.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ README.rst
│  │     │  │  ├─ requests
│  │     │  │  │  ├─ adapters.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ auth.py
│  │     │  │  │  ├─ certs.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ cookies.py
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ help.py
│  │     │  │  │  ├─ hooks.py
│  │     │  │  │  ├─ LICENSE
│  │     │  │  │  ├─ models.py
│  │     │  │  │  ├─ packages.py
│  │     │  │  │  ├─ sessions.py
│  │     │  │  │  ├─ status_codes.py
│  │     │  │  │  ├─ structures.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ _internal_utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __version__.py
│  │     │  │  ├─ resolvelib
│  │     │  │  │  ├─ LICENSE
│  │     │  │  │  ├─ providers.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ reporters.py
│  │     │  │  │  ├─ resolvers
│  │     │  │  │  │  ├─ abstract.py
│  │     │  │  │  │  ├─ criterion.py
│  │     │  │  │  │  ├─ exceptions.py
│  │     │  │  │  │  ├─ resolution.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ structs.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ rich
│  │     │  │  │  ├─ abc.py
│  │     │  │  │  ├─ align.py
│  │     │  │  │  ├─ ansi.py
│  │     │  │  │  ├─ bar.py
│  │     │  │  │  ├─ box.py
│  │     │  │  │  ├─ cells.py
│  │     │  │  │  ├─ color.py
│  │     │  │  │  ├─ color_triplet.py
│  │     │  │  │  ├─ columns.py
│  │     │  │  │  ├─ console.py
│  │     │  │  │  ├─ constrain.py
│  │     │  │  │  ├─ containers.py
│  │     │  │  │  ├─ control.py
│  │     │  │  │  ├─ default_styles.py
│  │     │  │  │  ├─ diagnose.py
│  │     │  │  │  ├─ emoji.py
│  │     │  │  │  ├─ errors.py
│  │     │  │  │  ├─ filesize.py
│  │     │  │  │  ├─ file_proxy.py
│  │     │  │  │  ├─ highlighter.py
│  │     │  │  │  ├─ json.py
│  │     │  │  │  ├─ jupyter.py
│  │     │  │  │  ├─ layout.py
│  │     │  │  │  ├─ LICENSE
│  │     │  │  │  ├─ live.py
│  │     │  │  │  ├─ live_render.py
│  │     │  │  │  ├─ logging.py
│  │     │  │  │  ├─ markup.py
│  │     │  │  │  ├─ measure.py
│  │     │  │  │  ├─ padding.py
│  │     │  │  │  ├─ pager.py
│  │     │  │  │  ├─ palette.py
│  │     │  │  │  ├─ panel.py
│  │     │  │  │  ├─ pretty.py
│  │     │  │  │  ├─ progress.py
│  │     │  │  │  ├─ progress_bar.py
│  │     │  │  │  ├─ prompt.py
│  │     │  │  │  ├─ protocol.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ region.py
│  │     │  │  │  ├─ repr.py
│  │     │  │  │  ├─ rule.py
│  │     │  │  │  ├─ scope.py
│  │     │  │  │  ├─ screen.py
│  │     │  │  │  ├─ segment.py
│  │     │  │  │  ├─ spinner.py
│  │     │  │  │  ├─ status.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  ├─ styled.py
│  │     │  │  │  ├─ syntax.py
│  │     │  │  │  ├─ table.py
│  │     │  │  │  ├─ terminal_theme.py
│  │     │  │  │  ├─ text.py
│  │     │  │  │  ├─ theme.py
│  │     │  │  │  ├─ themes.py
│  │     │  │  │  ├─ traceback.py
│  │     │  │  │  ├─ tree.py
│  │     │  │  │  ├─ _cell_widths.py
│  │     │  │  │  ├─ _emoji_codes.py
│  │     │  │  │  ├─ _emoji_replace.py
│  │     │  │  │  ├─ _export_format.py
│  │     │  │  │  ├─ _extension.py
│  │     │  │  │  ├─ _fileno.py
│  │     │  │  │  ├─ _inspect.py
│  │     │  │  │  ├─ _log_render.py
│  │     │  │  │  ├─ _loop.py
│  │     │  │  │  ├─ _null_file.py
│  │     │  │  │  ├─ _palettes.py
│  │     │  │  │  ├─ _pick.py
│  │     │  │  │  ├─ _ratio.py
│  │     │  │  │  ├─ _spinners.py
│  │     │  │  │  ├─ _stack.py
│  │     │  │  │  ├─ _timer.py
│  │     │  │  │  ├─ _win32_console.py
│  │     │  │  │  ├─ _windows.py
│  │     │  │  │  ├─ _windows_renderer.py
│  │     │  │  │  ├─ _wrap.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __main__.py
│  │     │  │  ├─ tomli
│  │     │  │  │  ├─ LICENSE
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ _parser.py
│  │     │  │  │  ├─ _re.py
│  │     │  │  │  ├─ _types.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ tomli_w
│  │     │  │  │  ├─ LICENSE
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ _writer.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ truststore
│  │     │  │  │  ├─ LICENSE
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ _api.py
│  │     │  │  │  ├─ _macos.py
│  │     │  │  │  ├─ _openssl.py
│  │     │  │  │  ├─ _ssl_constants.py
│  │     │  │  │  ├─ _windows.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ urllib3
│  │     │  │  │  ├─ connection.py
│  │     │  │  │  ├─ connectionpool.py
│  │     │  │  │  ├─ contrib
│  │     │  │  │  │  ├─ emscripten
│  │     │  │  │  │  │  ├─ connection.py
│  │     │  │  │  │  │  ├─ emscripten_fetch_worker.js
│  │     │  │  │  │  │  ├─ fetch.py
│  │     │  │  │  │  │  ├─ request.py
│  │     │  │  │  │  │  ├─ response.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ pyopenssl.py
│  │     │  │  │  │  ├─ socks.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ fields.py
│  │     │  │  │  ├─ filepost.py
│  │     │  │  │  ├─ http2
│  │     │  │  │  │  ├─ connection.py
│  │     │  │  │  │  ├─ probe.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ LICENSE.txt
│  │     │  │  │  ├─ poolmanager.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ response.py
│  │     │  │  │  ├─ util
│  │     │  │  │  │  ├─ connection.py
│  │     │  │  │  │  ├─ proxy.py
│  │     │  │  │  │  ├─ request.py
│  │     │  │  │  │  ├─ response.py
│  │     │  │  │  │  ├─ retry.py
│  │     │  │  │  │  ├─ ssltransport.py
│  │     │  │  │  │  ├─ ssl_.py
│  │     │  │  │  │  ├─ ssl_match_hostname.py
│  │     │  │  │  │  ├─ timeout.py
│  │     │  │  │  │  ├─ url.py
│  │     │  │  │  │  ├─ util.py
│  │     │  │  │  │  ├─ wait.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _base_connection.py
│  │     │  │  │  ├─ _collections.py
│  │     │  │  │  ├─ _request_methods.py
│  │     │  │  │  ├─ _version.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ vendor.txt
│  │     │  │  └─ __init__.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pip-runner__.py
│  │     ├─ pip-26.1.2.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  ├─ AUTHORS.txt
│  │     │  │  ├─ LICENSE.txt
│  │     │  │  └─ src
│  │     │  │     └─ pip
│  │     │  │        └─ _vendor
│  │     │  │           ├─ cachecontrol
│  │     │  │           │  └─ LICENSE.txt
│  │     │  │           ├─ certifi
│  │     │  │           │  └─ LICENSE
│  │     │  │           ├─ distlib
│  │     │  │           │  └─ LICENSE.txt
│  │     │  │           ├─ distro
│  │     │  │           │  └─ LICENSE
│  │     │  │           ├─ idna
│  │     │  │           │  └─ LICENSE.md
│  │     │  │           ├─ msgpack
│  │     │  │           │  └─ COPYING
│  │     │  │           ├─ packaging
│  │     │  │           │  ├─ LICENSE
│  │     │  │           │  ├─ LICENSE.APACHE
│  │     │  │           │  └─ LICENSE.BSD
│  │     │  │           ├─ pkg_resources
│  │     │  │           │  └─ LICENSE
│  │     │  │           ├─ platformdirs
│  │     │  │           │  └─ LICENSE
│  │     │  │           ├─ pygments
│  │     │  │           │  └─ LICENSE
│  │     │  │           ├─ pyproject_hooks
│  │     │  │           │  └─ LICENSE
│  │     │  │           ├─ requests
│  │     │  │           │  └─ LICENSE
│  │     │  │           ├─ resolvelib
│  │     │  │           │  └─ LICENSE
│  │     │  │           ├─ rich
│  │     │  │           │  └─ LICENSE
│  │     │  │           ├─ tomli
│  │     │  │           │  └─ LICENSE
│  │     │  │           ├─ tomli_w
│  │     │  │           │  └─ LICENSE
│  │     │  │           ├─ truststore
│  │     │  │           │  └─ LICENSE
│  │     │  │           └─ urllib3
│  │     │  │              └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ platformdirs
│  │     │  ├─ android.py
│  │     │  ├─ api.py
│  │     │  ├─ macos.py
│  │     │  ├─ py.typed
│  │     │  ├─ unix.py
│  │     │  ├─ version.py
│  │     │  ├─ windows.py
│  │     │  ├─ _xdg.py
│  │     │  ├─ __init__.py
│  │     │  └─ __main__.py
│  │     ├─ platformdirs-4.11.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ playhouse
│  │     │  ├─ apsw_ext.py
│  │     │  ├─ cockroachdb.py
│  │     │  ├─ cysqlite_ext.py
│  │     │  ├─ dataset.py
│  │     │  ├─ db_url.py
│  │     │  ├─ fields.py
│  │     │  ├─ flask_utils.py
│  │     │  ├─ fts_parser.py
│  │     │  ├─ hybrid.py
│  │     │  ├─ kv.py
│  │     │  ├─ migrate.py
│  │     │  ├─ mysql_ext.py
│  │     │  ├─ pool.py
│  │     │  ├─ postgres_ext.py
│  │     │  ├─ pwasyncio.py
│  │     │  ├─ pydantic_utils.py
│  │     │  ├─ README.md
│  │     │  ├─ reflection.py
│  │     │  ├─ shortcuts.py
│  │     │  ├─ signals.py
│  │     │  ├─ sqlcipher_ext.py
│  │     │  ├─ sqliteq.py
│  │     │  ├─ sqlite_changelog.py
│  │     │  ├─ sqlite_ext.py
│  │     │  ├─ sqlite_udf.py
│  │     │  ├─ test_utils.py
│  │     │  └─ __init__.py
│  │     ├─ plotly
│  │     │  ├─ animation.py
│  │     │  ├─ api
│  │     │  │  └─ __init__.py
│  │     │  ├─ basedatatypes.py
│  │     │  ├─ basewidget.py
│  │     │  ├─ callbacks.py
│  │     │  ├─ colors
│  │     │  │  └─ __init__.py
│  │     │  ├─ data
│  │     │  │  └─ __init__.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ express
│  │     │  │  ├─ colors
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ data
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ imshow_utils.py
│  │     │  │  ├─ trendline_functions
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ _chart_types.py
│  │     │  │  ├─ _core.py
│  │     │  │  ├─ _doc.py
│  │     │  │  ├─ _imshow.py
│  │     │  │  ├─ _special_inputs.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ figure_factory
│  │     │  │  ├─ README.md
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ _2d_density.py
│  │     │  │  ├─ _annotated_heatmap.py
│  │     │  │  ├─ _bullet.py
│  │     │  │  ├─ _candlestick.py
│  │     │  │  ├─ _county_choropleth.py
│  │     │  │  ├─ _dendrogram.py
│  │     │  │  ├─ _distplot.py
│  │     │  │  ├─ _facet_grid.py
│  │     │  │  ├─ _gantt.py
│  │     │  │  ├─ _hexbin_map.py
│  │     │  │  ├─ _ohlc.py
│  │     │  │  ├─ _quiver.py
│  │     │  │  ├─ _scatterplot.py
│  │     │  │  ├─ _streamline.py
│  │     │  │  ├─ _table.py
│  │     │  │  ├─ _ternary_contour.py
│  │     │  │  ├─ _trisurf.py
│  │     │  │  ├─ _violin.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ files.py
│  │     │  ├─ graph_objects
│  │     │  │  └─ __init__.py
│  │     │  ├─ graph_objs
│  │     │  │  ├─ bar
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  ├─ _pattern.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _error_x.py
│  │     │  │  │  ├─ _error_y.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _insidetextfont.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _outsidetextfont.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ barpolar
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  ├─ _pattern.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ box
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ candlestick
│  │     │  │  │  ├─ decreasing
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ increasing
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _decreasing.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _increasing.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ carpet
│  │     │  │  │  ├─ aaxis
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ baxis
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _aaxis.py
│  │     │  │  │  ├─ _baxis.py
│  │     │  │  │  ├─ _font.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ choropleth
│  │     │  │  │  ├─ colorbar
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _colorbar.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ choroplethmap
│  │     │  │  │  ├─ colorbar
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _colorbar.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ choroplethmapbox
│  │     │  │  │  ├─ colorbar
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _colorbar.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ cone
│  │     │  │  │  ├─ colorbar
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _colorbar.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _lighting.py
│  │     │  │  │  ├─ _lightposition.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ contour
│  │     │  │  │  ├─ colorbar
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ contours
│  │     │  │  │  │  ├─ _labelfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _colorbar.py
│  │     │  │  │  ├─ _contours.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ contourcarpet
│  │     │  │  │  ├─ colorbar
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ contours
│  │     │  │  │  │  ├─ _labelfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _colorbar.py
│  │     │  │  │  ├─ _contours.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ densitymap
│  │     │  │  │  ├─ colorbar
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _colorbar.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ densitymapbox
│  │     │  │  │  ├─ colorbar
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _colorbar.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ funnel
│  │     │  │  │  ├─ connector
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _connector.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _insidetextfont.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _outsidetextfont.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ funnelarea
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  ├─ _pattern.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ title
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _domain.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _insidetextfont.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _title.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ graph_objs.py
│  │     │  │  ├─ heatmap
│  │     │  │  │  ├─ colorbar
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _colorbar.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ histogram
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  ├─ _pattern.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _cumulative.py
│  │     │  │  │  ├─ _error_x.py
│  │     │  │  │  ├─ _error_y.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _insidetextfont.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _outsidetextfont.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  ├─ _xbins.py
│  │     │  │  │  ├─ _ybins.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ histogram2d
│  │     │  │  │  ├─ colorbar
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _colorbar.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _xbins.py
│  │     │  │  │  ├─ _ybins.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ histogram2dcontour
│  │     │  │  │  ├─ colorbar
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ contours
│  │     │  │  │  │  ├─ _labelfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _colorbar.py
│  │     │  │  │  ├─ _contours.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _xbins.py
│  │     │  │  │  ├─ _ybins.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ icicle
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  ├─ _pattern.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ pathbar
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _domain.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _insidetextfont.py
│  │     │  │  │  ├─ _leaf.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _outsidetextfont.py
│  │     │  │  │  ├─ _pathbar.py
│  │     │  │  │  ├─ _root.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _tiling.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ image
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ indicator
│  │     │  │  │  ├─ delta
│  │     │  │  │  │  ├─ _decreasing.py
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  ├─ _increasing.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ gauge
│  │     │  │  │  │  ├─ axis
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ bar
│  │     │  │  │  │  │  ├─ _line.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ step
│  │     │  │  │  │  │  ├─ _line.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ threshold
│  │     │  │  │  │  │  ├─ _line.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _axis.py
│  │     │  │  │  │  ├─ _bar.py
│  │     │  │  │  │  ├─ _step.py
│  │     │  │  │  │  ├─ _threshold.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ number
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ title
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _delta.py
│  │     │  │  │  ├─ _domain.py
│  │     │  │  │  ├─ _gauge.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _number.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _title.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ isosurface
│  │     │  │  │  ├─ caps
│  │     │  │  │  │  ├─ _x.py
│  │     │  │  │  │  ├─ _y.py
│  │     │  │  │  │  ├─ _z.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ colorbar
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ slices
│  │     │  │  │  │  ├─ _x.py
│  │     │  │  │  │  ├─ _y.py
│  │     │  │  │  │  ├─ _z.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _caps.py
│  │     │  │  │  ├─ _colorbar.py
│  │     │  │  │  ├─ _contour.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _lighting.py
│  │     │  │  │  ├─ _lightposition.py
│  │     │  │  │  ├─ _slices.py
│  │     │  │  │  ├─ _spaceframe.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _surface.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ layout
│  │     │  │  │  ├─ annotation
│  │     │  │  │  │  ├─ hoverlabel
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ coloraxis
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ geo
│  │     │  │  │  │  ├─ projection
│  │     │  │  │  │  │  ├─ _rotation.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _center.py
│  │     │  │  │  │  ├─ _domain.py
│  │     │  │  │  │  ├─ _lataxis.py
│  │     │  │  │  │  ├─ _lonaxis.py
│  │     │  │  │  │  ├─ _projection.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ grid
│  │     │  │  │  │  ├─ _domain.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  ├─ _grouptitlefont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legend
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  ├─ _grouptitlefont.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ map
│  │     │  │  │  │  ├─ layer
│  │     │  │  │  │  │  ├─ symbol
│  │     │  │  │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _circle.py
│  │     │  │  │  │  │  ├─ _fill.py
│  │     │  │  │  │  │  ├─ _line.py
│  │     │  │  │  │  │  ├─ _symbol.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _bounds.py
│  │     │  │  │  │  ├─ _center.py
│  │     │  │  │  │  ├─ _domain.py
│  │     │  │  │  │  ├─ _layer.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ mapbox
│  │     │  │  │  │  ├─ layer
│  │     │  │  │  │  │  ├─ symbol
│  │     │  │  │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _circle.py
│  │     │  │  │  │  │  ├─ _fill.py
│  │     │  │  │  │  │  ├─ _line.py
│  │     │  │  │  │  │  ├─ _symbol.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _bounds.py
│  │     │  │  │  │  ├─ _center.py
│  │     │  │  │  │  ├─ _domain.py
│  │     │  │  │  │  ├─ _layer.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ newselection
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ newshape
│  │     │  │  │  │  ├─ label
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _label.py
│  │     │  │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ polar
│  │     │  │  │  │  ├─ angularaxis
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ radialaxis
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _autorangeoptions.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _angularaxis.py
│  │     │  │  │  │  ├─ _domain.py
│  │     │  │  │  │  ├─ _radialaxis.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ scene
│  │     │  │  │  │  ├─ annotation
│  │     │  │  │  │  │  ├─ hoverlabel
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ camera
│  │     │  │  │  │  │  ├─ _center.py
│  │     │  │  │  │  │  ├─ _eye.py
│  │     │  │  │  │  │  ├─ _projection.py
│  │     │  │  │  │  │  ├─ _up.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ xaxis
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _autorangeoptions.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ yaxis
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _autorangeoptions.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ zaxis
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _autorangeoptions.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _annotation.py
│  │     │  │  │  │  ├─ _aspectratio.py
│  │     │  │  │  │  ├─ _camera.py
│  │     │  │  │  │  ├─ _domain.py
│  │     │  │  │  │  ├─ _xaxis.py
│  │     │  │  │  │  ├─ _yaxis.py
│  │     │  │  │  │  ├─ _zaxis.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selection
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ shape
│  │     │  │  │  │  ├─ label
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _label.py
│  │     │  │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ slider
│  │     │  │  │  │  ├─ currentvalue
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _currentvalue.py
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  ├─ _pad.py
│  │     │  │  │  │  ├─ _step.py
│  │     │  │  │  │  ├─ _transition.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ smith
│  │     │  │  │  │  ├─ imaginaryaxis
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ realaxis
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _domain.py
│  │     │  │  │  │  ├─ _imaginaryaxis.py
│  │     │  │  │  │  ├─ _realaxis.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ template
│  │     │  │  │  │  ├─ data
│  │     │  │  │  │  │  ├─ _bar.py
│  │     │  │  │  │  │  ├─ _barpolar.py
│  │     │  │  │  │  │  ├─ _box.py
│  │     │  │  │  │  │  ├─ _candlestick.py
│  │     │  │  │  │  │  ├─ _carpet.py
│  │     │  │  │  │  │  ├─ _choropleth.py
│  │     │  │  │  │  │  ├─ _choroplethmap.py
│  │     │  │  │  │  │  ├─ _choroplethmapbox.py
│  │     │  │  │  │  │  ├─ _cone.py
│  │     │  │  │  │  │  ├─ _contour.py
│  │     │  │  │  │  │  ├─ _contourcarpet.py
│  │     │  │  │  │  │  ├─ _densitymap.py
│  │     │  │  │  │  │  ├─ _densitymapbox.py
│  │     │  │  │  │  │  ├─ _funnel.py
│  │     │  │  │  │  │  ├─ _funnelarea.py
│  │     │  │  │  │  │  ├─ _heatmap.py
│  │     │  │  │  │  │  ├─ _histogram.py
│  │     │  │  │  │  │  ├─ _histogram2d.py
│  │     │  │  │  │  │  ├─ _histogram2dcontour.py
│  │     │  │  │  │  │  ├─ _icicle.py
│  │     │  │  │  │  │  ├─ _image.py
│  │     │  │  │  │  │  ├─ _indicator.py
│  │     │  │  │  │  │  ├─ _isosurface.py
│  │     │  │  │  │  │  ├─ _mesh3d.py
│  │     │  │  │  │  │  ├─ _ohlc.py
│  │     │  │  │  │  │  ├─ _parcats.py
│  │     │  │  │  │  │  ├─ _parcoords.py
│  │     │  │  │  │  │  ├─ _pie.py
│  │     │  │  │  │  │  ├─ _sankey.py
│  │     │  │  │  │  │  ├─ _scatter.py
│  │     │  │  │  │  │  ├─ _scatter3d.py
│  │     │  │  │  │  │  ├─ _scattercarpet.py
│  │     │  │  │  │  │  ├─ _scattergeo.py
│  │     │  │  │  │  │  ├─ _scattergl.py
│  │     │  │  │  │  │  ├─ _scattermap.py
│  │     │  │  │  │  │  ├─ _scattermapbox.py
│  │     │  │  │  │  │  ├─ _scatterpolar.py
│  │     │  │  │  │  │  ├─ _scatterpolargl.py
│  │     │  │  │  │  │  ├─ _scattersmith.py
│  │     │  │  │  │  │  ├─ _scatterternary.py
│  │     │  │  │  │  │  ├─ _splom.py
│  │     │  │  │  │  │  ├─ _streamtube.py
│  │     │  │  │  │  │  ├─ _sunburst.py
│  │     │  │  │  │  │  ├─ _surface.py
│  │     │  │  │  │  │  ├─ _table.py
│  │     │  │  │  │  │  ├─ _treemap.py
│  │     │  │  │  │  │  ├─ _violin.py
│  │     │  │  │  │  │  ├─ _volume.py
│  │     │  │  │  │  │  ├─ _waterfall.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _data.py
│  │     │  │  │  │  ├─ _layout.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ ternary
│  │     │  │  │  │  ├─ aaxis
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ baxis
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ caxis
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _aaxis.py
│  │     │  │  │  │  ├─ _baxis.py
│  │     │  │  │  │  ├─ _caxis.py
│  │     │  │  │  │  ├─ _domain.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ title
│  │     │  │  │  │  ├─ subtitle
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  ├─ _pad.py
│  │     │  │  │  │  ├─ _subtitle.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ updatemenu
│  │     │  │  │  │  ├─ _button.py
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  ├─ _pad.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ xaxis
│  │     │  │  │  │  ├─ rangeselector
│  │     │  │  │  │  │  ├─ _button.py
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ rangeslider
│  │     │  │  │  │  │  ├─ _yaxis.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _autorangeoptions.py
│  │     │  │  │  │  ├─ _minor.py
│  │     │  │  │  │  ├─ _rangebreak.py
│  │     │  │  │  │  ├─ _rangeselector.py
│  │     │  │  │  │  ├─ _rangeslider.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  ├─ _unifiedhovertitle.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ yaxis
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _autorangeoptions.py
│  │     │  │  │  │  ├─ _minor.py
│  │     │  │  │  │  ├─ _rangebreak.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  ├─ _unifiedhovertitle.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _activeselection.py
│  │     │  │  │  ├─ _activeshape.py
│  │     │  │  │  ├─ _annotation.py
│  │     │  │  │  ├─ _coloraxis.py
│  │     │  │  │  ├─ _colorscale.py
│  │     │  │  │  ├─ _font.py
│  │     │  │  │  ├─ _geo.py
│  │     │  │  │  ├─ _grid.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _image.py
│  │     │  │  │  ├─ _legend.py
│  │     │  │  │  ├─ _map.py
│  │     │  │  │  ├─ _mapbox.py
│  │     │  │  │  ├─ _margin.py
│  │     │  │  │  ├─ _modebar.py
│  │     │  │  │  ├─ _newselection.py
│  │     │  │  │  ├─ _newshape.py
│  │     │  │  │  ├─ _polar.py
│  │     │  │  │  ├─ _scene.py
│  │     │  │  │  ├─ _selection.py
│  │     │  │  │  ├─ _shape.py
│  │     │  │  │  ├─ _slider.py
│  │     │  │  │  ├─ _smith.py
│  │     │  │  │  ├─ _template.py
│  │     │  │  │  ├─ _ternary.py
│  │     │  │  │  ├─ _title.py
│  │     │  │  │  ├─ _transition.py
│  │     │  │  │  ├─ _uniformtext.py
│  │     │  │  │  ├─ _updatemenu.py
│  │     │  │  │  ├─ _xaxis.py
│  │     │  │  │  ├─ _yaxis.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ mesh3d
│  │     │  │  │  ├─ colorbar
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _colorbar.py
│  │     │  │  │  ├─ _contour.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _lighting.py
│  │     │  │  │  ├─ _lightposition.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ ohlc
│  │     │  │  │  ├─ decreasing
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ increasing
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _decreasing.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _increasing.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ parcats
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ line
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _dimension.py
│  │     │  │  │  ├─ _domain.py
│  │     │  │  │  ├─ _labelfont.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _tickfont.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ parcoords
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ line
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _dimension.py
│  │     │  │  │  ├─ _domain.py
│  │     │  │  │  ├─ _labelfont.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _rangefont.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _tickfont.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ pie
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  ├─ _pattern.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ title
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _domain.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _insidetextfont.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _outsidetextfont.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _title.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ sankey
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ link
│  │     │  │  │  │  ├─ hoverlabel
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorscale.py
│  │     │  │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ node
│  │     │  │  │  │  ├─ hoverlabel
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _domain.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _link.py
│  │     │  │  │  ├─ _node.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ scatter
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _gradient.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _error_x.py
│  │     │  │  │  ├─ _error_y.py
│  │     │  │  │  ├─ _fillgradient.py
│  │     │  │  │  ├─ _fillpattern.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ scatter3d
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ line
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ projection
│  │     │  │  │  │  ├─ _x.py
│  │     │  │  │  │  ├─ _y.py
│  │     │  │  │  │  ├─ _z.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _error_x.py
│  │     │  │  │  ├─ _error_y.py
│  │     │  │  │  ├─ _error_z.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _projection.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ scattercarpet
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _gradient.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ scattergeo
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _gradient.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ scattergl
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _error_x.py
│  │     │  │  │  ├─ _error_y.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ scattermap
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _cluster.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ scattermapbox
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _cluster.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ scatterpolar
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _gradient.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ scatterpolargl
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ scattersmith
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _gradient.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ scatterternary
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _gradient.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ splom
│  │     │  │  │  ├─ dimension
│  │     │  │  │  │  ├─ _axis.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _diagonal.py
│  │     │  │  │  ├─ _dimension.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ streamtube
│  │     │  │  │  ├─ colorbar
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _colorbar.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _lighting.py
│  │     │  │  │  ├─ _lightposition.py
│  │     │  │  │  ├─ _starts.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ sunburst
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  ├─ _pattern.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _domain.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _insidetextfont.py
│  │     │  │  │  ├─ _leaf.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _outsidetextfont.py
│  │     │  │  │  ├─ _root.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ surface
│  │     │  │  │  ├─ colorbar
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ contours
│  │     │  │  │  │  ├─ x
│  │     │  │  │  │  │  ├─ _project.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ y
│  │     │  │  │  │  │  ├─ _project.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ z
│  │     │  │  │  │  │  ├─ _project.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _x.py
│  │     │  │  │  │  ├─ _y.py
│  │     │  │  │  │  ├─ _z.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _colorbar.py
│  │     │  │  │  ├─ _contours.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _lighting.py
│  │     │  │  │  ├─ _lightposition.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ table
│  │     │  │  │  ├─ cells
│  │     │  │  │  │  ├─ _fill.py
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ header
│  │     │  │  │  │  ├─ _fill.py
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _cells.py
│  │     │  │  │  ├─ _domain.py
│  │     │  │  │  ├─ _header.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ treemap
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ colorbar
│  │     │  │  │  │  │  ├─ title
│  │     │  │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  ├─ _title.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  ├─ _pad.py
│  │     │  │  │  │  ├─ _pattern.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ pathbar
│  │     │  │  │  │  ├─ _textfont.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _domain.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _insidetextfont.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _outsidetextfont.py
│  │     │  │  │  ├─ _pathbar.py
│  │     │  │  │  ├─ _root.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _tiling.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ violin
│  │     │  │  │  ├─ box
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ marker
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ selected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ unselected
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _box.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _meanline.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _unselected.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ volume
│  │     │  │  │  ├─ caps
│  │     │  │  │  │  ├─ _x.py
│  │     │  │  │  │  ├─ _y.py
│  │     │  │  │  │  ├─ _z.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ colorbar
│  │     │  │  │  │  ├─ title
│  │     │  │  │  │  │  ├─ _font.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  ├─ _title.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ slices
│  │     │  │  │  │  ├─ _x.py
│  │     │  │  │  │  ├─ _y.py
│  │     │  │  │  │  ├─ _z.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _caps.py
│  │     │  │  │  ├─ _colorbar.py
│  │     │  │  │  ├─ _contour.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _lighting.py
│  │     │  │  │  ├─ _lightposition.py
│  │     │  │  │  ├─ _slices.py
│  │     │  │  │  ├─ _spaceframe.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _surface.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ waterfall
│  │     │  │  │  ├─ connector
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ decreasing
│  │     │  │  │  │  ├─ marker
│  │     │  │  │  │  │  ├─ _line.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ hoverlabel
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ increasing
│  │     │  │  │  │  ├─ marker
│  │     │  │  │  │  │  ├─ _line.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ legendgrouptitle
│  │     │  │  │  │  ├─ _font.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ totals
│  │     │  │  │  │  ├─ marker
│  │     │  │  │  │  │  ├─ _line.py
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ _connector.py
│  │     │  │  │  ├─ _decreasing.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _increasing.py
│  │     │  │  │  ├─ _insidetextfont.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _outsidetextfont.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  ├─ _totals.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ _bar.py
│  │     │  │  ├─ _barpolar.py
│  │     │  │  ├─ _box.py
│  │     │  │  ├─ _candlestick.py
│  │     │  │  ├─ _carpet.py
│  │     │  │  ├─ _choropleth.py
│  │     │  │  ├─ _choroplethmap.py
│  │     │  │  ├─ _choroplethmapbox.py
│  │     │  │  ├─ _cone.py
│  │     │  │  ├─ _contour.py
│  │     │  │  ├─ _contourcarpet.py
│  │     │  │  ├─ _densitymap.py
│  │     │  │  ├─ _densitymapbox.py
│  │     │  │  ├─ _deprecations.py
│  │     │  │  ├─ _figure.py
│  │     │  │  ├─ _figurewidget.py
│  │     │  │  ├─ _frame.py
│  │     │  │  ├─ _funnel.py
│  │     │  │  ├─ _funnelarea.py
│  │     │  │  ├─ _heatmap.py
│  │     │  │  ├─ _histogram.py
│  │     │  │  ├─ _histogram2d.py
│  │     │  │  ├─ _histogram2dcontour.py
│  │     │  │  ├─ _icicle.py
│  │     │  │  ├─ _image.py
│  │     │  │  ├─ _indicator.py
│  │     │  │  ├─ _isosurface.py
│  │     │  │  ├─ _layout.py
│  │     │  │  ├─ _mesh3d.py
│  │     │  │  ├─ _ohlc.py
│  │     │  │  ├─ _parcats.py
│  │     │  │  ├─ _parcoords.py
│  │     │  │  ├─ _pie.py
│  │     │  │  ├─ _sankey.py
│  │     │  │  ├─ _scatter.py
│  │     │  │  ├─ _scatter3d.py
│  │     │  │  ├─ _scattercarpet.py
│  │     │  │  ├─ _scattergeo.py
│  │     │  │  ├─ _scattergl.py
│  │     │  │  ├─ _scattermap.py
│  │     │  │  ├─ _scattermapbox.py
│  │     │  │  ├─ _scatterpolar.py
│  │     │  │  ├─ _scatterpolargl.py
│  │     │  │  ├─ _scattersmith.py
│  │     │  │  ├─ _scatterternary.py
│  │     │  │  ├─ _splom.py
│  │     │  │  ├─ _streamtube.py
│  │     │  │  ├─ _sunburst.py
│  │     │  │  ├─ _surface.py
│  │     │  │  ├─ _table.py
│  │     │  │  ├─ _treemap.py
│  │     │  │  ├─ _violin.py
│  │     │  │  ├─ _volume.py
│  │     │  │  ├─ _waterfall.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ io
│  │     │  │  ├─ base_renderers.py
│  │     │  │  ├─ json.py
│  │     │  │  ├─ kaleido.py
│  │     │  │  ├─ orca.py
│  │     │  │  ├─ _base_renderers.py
│  │     │  │  ├─ _defaults.py
│  │     │  │  ├─ _html.py
│  │     │  │  ├─ _json.py
│  │     │  │  ├─ _kaleido.py
│  │     │  │  ├─ _orca.py
│  │     │  │  ├─ _renderers.py
│  │     │  │  ├─ _sg_scraper.py
│  │     │  │  ├─ _templates.py
│  │     │  │  ├─ _utils.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ labextension
│  │     │  │  ├─ package.json
│  │     │  │  └─ static
│  │     │  │     ├─ 1.3ad216e94ff8bdcd7b73.js
│  │     │  │     ├─ 1.3ad216e94ff8bdcd7b73.js.LICENSE.txt
│  │     │  │     ├─ remoteEntry.58c394332ed33325ffe5.js
│  │     │  │     ├─ style.js
│  │     │  │     └─ third-party-licenses.json
│  │     │  ├─ matplotlylib
│  │     │  │  ├─ mplexporter
│  │     │  │  │  ├─ exporter.py
│  │     │  │  │  ├─ renderers
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ fake_renderer.py
│  │     │  │  │  │  ├─ vega_renderer.py
│  │     │  │  │  │  ├─ vincent_renderer.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ tests
│  │     │  │  │  │  ├─ test_basic.py
│  │     │  │  │  │  ├─ test_utils.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ tools.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ mpltools.py
│  │     │  │  ├─ renderer.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_renderer.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ missing_anywidget.py
│  │     │  ├─ offline
│  │     │  │  ├─ offline.py
│  │     │  │  ├─ _plotlyjs_version.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ optional_imports.py
│  │     │  ├─ package_data
│  │     │  │  ├─ datasets
│  │     │  │  │  ├─ carshare.csv.gz
│  │     │  │  │  ├─ election.csv.gz
│  │     │  │  │  ├─ election.geojson.gz
│  │     │  │  │  ├─ experiment.csv.gz
│  │     │  │  │  ├─ gapminder.csv.gz
│  │     │  │  │  ├─ iris.csv.gz
│  │     │  │  │  ├─ medals.csv.gz
│  │     │  │  │  ├─ stocks.csv.gz
│  │     │  │  │  ├─ tips.csv.gz
│  │     │  │  │  └─ wind.csv.gz
│  │     │  │  ├─ plotly.min.js
│  │     │  │  ├─ templates
│  │     │  │  │  ├─ ggplot2.json
│  │     │  │  │  ├─ gridon.json
│  │     │  │  │  ├─ plotly.json
│  │     │  │  │  ├─ plotly_dark.json
│  │     │  │  │  ├─ plotly_white.json
│  │     │  │  │  ├─ presentation.json
│  │     │  │  │  ├─ seaborn.json
│  │     │  │  │  ├─ simple_white.json
│  │     │  │  │  ├─ xgridoff.json
│  │     │  │  │  └─ ygridoff.json
│  │     │  │  └─ widgetbundle.js
│  │     │  ├─ serializers.py
│  │     │  ├─ shapeannotation.py
│  │     │  ├─ subplots.py
│  │     │  ├─ tools.py
│  │     │  ├─ utils.py
│  │     │  ├─ validators
│  │     │  │  └─ _validators.json
│  │     │  ├─ validator_cache.py
│  │     │  ├─ _subplots.py
│  │     │  └─ __init__.py
│  │     ├─ plotly-6.9.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ protobuf-7.35.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pwiz.py
│  │     ├─ pyarrow
│  │     │  ├─ acero.py
│  │     │  ├─ array.pxi
│  │     │  ├─ arrow.dll
│  │     │  ├─ arrow.lib
│  │     │  ├─ arrow_acero.dll
│  │     │  ├─ arrow_acero.lib
│  │     │  ├─ arrow_compute.dll
│  │     │  ├─ arrow_compute.lib
│  │     │  ├─ arrow_dataset.dll
│  │     │  ├─ arrow_dataset.lib
│  │     │  ├─ arrow_flight.dll
│  │     │  ├─ arrow_flight.lib
│  │     │  ├─ arrow_python.dll
│  │     │  ├─ arrow_python.lib
│  │     │  ├─ arrow_python_flight.dll
│  │     │  ├─ arrow_python_flight.lib
│  │     │  ├─ arrow_python_parquet_encryption.dll
│  │     │  ├─ arrow_python_parquet_encryption.lib
│  │     │  ├─ arrow_substrait.dll
│  │     │  ├─ arrow_substrait.lib
│  │     │  ├─ benchmark.pxi
│  │     │  ├─ benchmark.py
│  │     │  ├─ builder.pxi
│  │     │  ├─ cffi.py
│  │     │  ├─ compat.pxi
│  │     │  ├─ compute.py
│  │     │  ├─ config.pxi
│  │     │  ├─ conftest.py
│  │     │  ├─ csv.py
│  │     │  ├─ cuda.py
│  │     │  ├─ dataset.py
│  │     │  ├─ device.pxi
│  │     │  ├─ error.pxi
│  │     │  ├─ feather.py
│  │     │  ├─ flight.py
│  │     │  ├─ fs.py
│  │     │  ├─ gandiva.pyx
│  │     │  ├─ include
│  │     │  │  ├─ arrow
│  │     │  │  │  ├─ acero
│  │     │  │  │  │  ├─ accumulation_queue.h
│  │     │  │  │  │  ├─ aggregate_node.h
│  │     │  │  │  │  ├─ api.h
│  │     │  │  │  │  ├─ asof_join_node.h
│  │     │  │  │  │  ├─ backpressure_handler.h
│  │     │  │  │  │  ├─ benchmark_util.h
│  │     │  │  │  │  ├─ bloom_filter.h
│  │     │  │  │  │  ├─ exec_plan.h
│  │     │  │  │  │  ├─ hash_join.h
│  │     │  │  │  │  ├─ hash_join_dict.h
│  │     │  │  │  │  ├─ hash_join_node.h
│  │     │  │  │  │  ├─ map_node.h
│  │     │  │  │  │  ├─ options.h
│  │     │  │  │  │  ├─ order_by_impl.h
│  │     │  │  │  │  ├─ partition_util.h
│  │     │  │  │  │  ├─ query_context.h
│  │     │  │  │  │  ├─ schema_util.h
│  │     │  │  │  │  ├─ task_util.h
│  │     │  │  │  │  ├─ test_nodes.h
│  │     │  │  │  │  ├─ time_series_util.h
│  │     │  │  │  │  ├─ tpch_node.h
│  │     │  │  │  │  ├─ type_fwd.h
│  │     │  │  │  │  ├─ util.h
│  │     │  │  │  │  └─ visibility.h
│  │     │  │  │  ├─ adapters
│  │     │  │  │  │  ├─ orc
│  │     │  │  │  │  │  ├─ adapter.h
│  │     │  │  │  │  │  └─ options.h
│  │     │  │  │  │  └─ tensorflow
│  │     │  │  │  │     └─ convert.h
│  │     │  │  │  ├─ api.h
│  │     │  │  │  ├─ array
│  │     │  │  │  │  ├─ array_base.h
│  │     │  │  │  │  ├─ array_binary.h
│  │     │  │  │  │  ├─ array_decimal.h
│  │     │  │  │  │  ├─ array_dict.h
│  │     │  │  │  │  ├─ array_nested.h
│  │     │  │  │  │  ├─ array_primitive.h
│  │     │  │  │  │  ├─ array_run_end.h
│  │     │  │  │  │  ├─ builder_adaptive.h
│  │     │  │  │  │  ├─ builder_base.h
│  │     │  │  │  │  ├─ builder_binary.h
│  │     │  │  │  │  ├─ builder_decimal.h
│  │     │  │  │  │  ├─ builder_dict.h
│  │     │  │  │  │  ├─ builder_nested.h
│  │     │  │  │  │  ├─ builder_primitive.h
│  │     │  │  │  │  ├─ builder_run_end.h
│  │     │  │  │  │  ├─ builder_time.h
│  │     │  │  │  │  ├─ builder_union.h
│  │     │  │  │  │  ├─ concatenate.h
│  │     │  │  │  │  ├─ data.h
│  │     │  │  │  │  ├─ diff.h
│  │     │  │  │  │  ├─ statistics.h
│  │     │  │  │  │  ├─ util.h
│  │     │  │  │  │  └─ validate.h
│  │     │  │  │  ├─ array.h
│  │     │  │  │  ├─ buffer.h
│  │     │  │  │  ├─ buffer_builder.h
│  │     │  │  │  ├─ builder.h
│  │     │  │  │  ├─ c
│  │     │  │  │  │  ├─ abi.h
│  │     │  │  │  │  ├─ bridge.h
│  │     │  │  │  │  ├─ dlpack.h
│  │     │  │  │  │  ├─ dlpack_abi.h
│  │     │  │  │  │  └─ helpers.h
│  │     │  │  │  ├─ chunked_array.h
│  │     │  │  │  ├─ chunk_resolver.h
│  │     │  │  │  ├─ compare.h
│  │     │  │  │  ├─ compute
│  │     │  │  │  │  ├─ api.h
│  │     │  │  │  │  ├─ api_aggregate.h
│  │     │  │  │  │  ├─ api_scalar.h
│  │     │  │  │  │  ├─ api_vector.h
│  │     │  │  │  │  ├─ cast.h
│  │     │  │  │  │  ├─ exec.h
│  │     │  │  │  │  ├─ expression.h
│  │     │  │  │  │  ├─ function.h
│  │     │  │  │  │  ├─ function_options.h
│  │     │  │  │  │  ├─ initialize.h
│  │     │  │  │  │  ├─ kernel.h
│  │     │  │  │  │  ├─ ordering.h
│  │     │  │  │  │  ├─ registry.h
│  │     │  │  │  │  ├─ row
│  │     │  │  │  │  │  └─ grouper.h
│  │     │  │  │  │  ├─ type_fwd.h
│  │     │  │  │  │  ├─ util.h
│  │     │  │  │  │  └─ visibility.h
│  │     │  │  │  ├─ config.h
│  │     │  │  │  ├─ csv
│  │     │  │  │  │  ├─ api.h
│  │     │  │  │  │  ├─ chunker.h
│  │     │  │  │  │  ├─ column_builder.h
│  │     │  │  │  │  ├─ column_decoder.h
│  │     │  │  │  │  ├─ converter.h
│  │     │  │  │  │  ├─ invalid_row.h
│  │     │  │  │  │  ├─ options.h
│  │     │  │  │  │  ├─ parser.h
│  │     │  │  │  │  ├─ reader.h
│  │     │  │  │  │  ├─ test_common.h
│  │     │  │  │  │  ├─ type_fwd.h
│  │     │  │  │  │  └─ writer.h
│  │     │  │  │  ├─ dataset
│  │     │  │  │  │  ├─ api.h
│  │     │  │  │  │  ├─ dataset.h
│  │     │  │  │  │  ├─ dataset_writer.h
│  │     │  │  │  │  ├─ discovery.h
│  │     │  │  │  │  ├─ file_base.h
│  │     │  │  │  │  ├─ file_csv.h
│  │     │  │  │  │  ├─ file_ipc.h
│  │     │  │  │  │  ├─ file_json.h
│  │     │  │  │  │  ├─ file_orc.h
│  │     │  │  │  │  ├─ file_parquet.h
│  │     │  │  │  │  ├─ parquet_encryption_config.h
│  │     │  │  │  │  ├─ partition.h
│  │     │  │  │  │  ├─ plan.h
│  │     │  │  │  │  ├─ projector.h
│  │     │  │  │  │  ├─ scanner.h
│  │     │  │  │  │  ├─ type_fwd.h
│  │     │  │  │  │  └─ visibility.h
│  │     │  │  │  ├─ datum.h
│  │     │  │  │  ├─ device.h
│  │     │  │  │  ├─ device_allocation_type_set.h
│  │     │  │  │  ├─ engine
│  │     │  │  │  │  ├─ api.h
│  │     │  │  │  │  └─ substrait
│  │     │  │  │  │     ├─ api.h
│  │     │  │  │  │     ├─ extension_set.h
│  │     │  │  │  │     ├─ extension_types.h
│  │     │  │  │  │     ├─ options.h
│  │     │  │  │  │     ├─ relation.h
│  │     │  │  │  │     ├─ serde.h
│  │     │  │  │  │     ├─ test_plan_builder.h
│  │     │  │  │  │     ├─ test_util.h
│  │     │  │  │  │     ├─ type_fwd.h
│  │     │  │  │  │     ├─ util.h
│  │     │  │  │  │     └─ visibility.h
│  │     │  │  │  ├─ extension
│  │     │  │  │  │  ├─ bool8.h
│  │     │  │  │  │  ├─ fixed_shape_tensor.h
│  │     │  │  │  │  ├─ json.h
│  │     │  │  │  │  ├─ opaque.h
│  │     │  │  │  │  ├─ parquet_variant.h
│  │     │  │  │  │  ├─ uuid.h
│  │     │  │  │  │  └─ variable_shape_tensor.h
│  │     │  │  │  ├─ extension_type.h
│  │     │  │  │  ├─ filesystem
│  │     │  │  │  │  ├─ api.h
│  │     │  │  │  │  ├─ azurefs.h
│  │     │  │  │  │  ├─ filesystem.h
│  │     │  │  │  │  ├─ filesystem_library.h
│  │     │  │  │  │  ├─ gcsfs.h
│  │     │  │  │  │  ├─ hdfs.h
│  │     │  │  │  │  ├─ localfs.h
│  │     │  │  │  │  ├─ mockfs.h
│  │     │  │  │  │  ├─ path_util.h
│  │     │  │  │  │  ├─ s3fs.h
│  │     │  │  │  │  ├─ s3_test_util.h
│  │     │  │  │  │  ├─ test_util.h
│  │     │  │  │  │  └─ type_fwd.h
│  │     │  │  │  ├─ flight
│  │     │  │  │  │  ├─ api.h
│  │     │  │  │  │  ├─ client.h
│  │     │  │  │  │  ├─ client_auth.h
│  │     │  │  │  │  ├─ client_cookie_middleware.h
│  │     │  │  │  │  ├─ client_middleware.h
│  │     │  │  │  │  ├─ client_tracing_middleware.h
│  │     │  │  │  │  ├─ middleware.h
│  │     │  │  │  │  ├─ otel_logging.h
│  │     │  │  │  │  ├─ platform.h
│  │     │  │  │  │  ├─ server.h
│  │     │  │  │  │  ├─ server_auth.h
│  │     │  │  │  │  ├─ server_middleware.h
│  │     │  │  │  │  ├─ server_tracing_middleware.h
│  │     │  │  │  │  ├─ test_auth_handlers.h
│  │     │  │  │  │  ├─ test_definitions.h
│  │     │  │  │  │  ├─ test_flight_server.h
│  │     │  │  │  │  ├─ test_util.h
│  │     │  │  │  │  ├─ transport.h
│  │     │  │  │  │  ├─ transport_server.h
│  │     │  │  │  │  ├─ types.h
│  │     │  │  │  │  ├─ types_async.h
│  │     │  │  │  │  ├─ type_fwd.h
│  │     │  │  │  │  └─ visibility.h
│  │     │  │  │  ├─ io
│  │     │  │  │  │  ├─ api.h
│  │     │  │  │  │  ├─ buffered.h
│  │     │  │  │  │  ├─ caching.h
│  │     │  │  │  │  ├─ compressed.h
│  │     │  │  │  │  ├─ concurrency.h
│  │     │  │  │  │  ├─ file.h
│  │     │  │  │  │  ├─ hdfs.h
│  │     │  │  │  │  ├─ interfaces.h
│  │     │  │  │  │  ├─ memory.h
│  │     │  │  │  │  ├─ mman.h
│  │     │  │  │  │  ├─ slow.h
│  │     │  │  │  │  ├─ stdio.h
│  │     │  │  │  │  ├─ test_common.h
│  │     │  │  │  │  ├─ transform.h
│  │     │  │  │  │  └─ type_fwd.h
│  │     │  │  │  ├─ ipc
│  │     │  │  │  │  ├─ api.h
│  │     │  │  │  │  ├─ dictionary.h
│  │     │  │  │  │  ├─ feather.h
│  │     │  │  │  │  ├─ message.h
│  │     │  │  │  │  ├─ options.h
│  │     │  │  │  │  ├─ reader.h
│  │     │  │  │  │  ├─ test_common.h
│  │     │  │  │  │  ├─ type_fwd.h
│  │     │  │  │  │  ├─ util.h
│  │     │  │  │  │  └─ writer.h
│  │     │  │  │  ├─ json
│  │     │  │  │  │  ├─ api.h
│  │     │  │  │  │  ├─ chunked_builder.h
│  │     │  │  │  │  ├─ chunker.h
│  │     │  │  │  │  ├─ converter.h
│  │     │  │  │  │  ├─ from_string.h
│  │     │  │  │  │  ├─ object_parser.h
│  │     │  │  │  │  ├─ object_writer.h
│  │     │  │  │  │  ├─ options.h
│  │     │  │  │  │  ├─ parser.h
│  │     │  │  │  │  ├─ rapidjson_defs.h
│  │     │  │  │  │  ├─ reader.h
│  │     │  │  │  │  ├─ test_common.h
│  │     │  │  │  │  └─ type_fwd.h
│  │     │  │  │  ├─ memory_pool.h
│  │     │  │  │  ├─ memory_pool_test.h
│  │     │  │  │  ├─ pretty_print.h
│  │     │  │  │  ├─ python
│  │     │  │  │  │  ├─ api.h
│  │     │  │  │  │  ├─ arrow_to_pandas.h
│  │     │  │  │  │  ├─ async.h
│  │     │  │  │  │  ├─ benchmark.h
│  │     │  │  │  │  ├─ common.h
│  │     │  │  │  │  ├─ config.h
│  │     │  │  │  │  ├─ csv.h
│  │     │  │  │  │  ├─ datetime.h
│  │     │  │  │  │  ├─ decimal.h
│  │     │  │  │  │  ├─ extension_type.h
│  │     │  │  │  │  ├─ filesystem.h
│  │     │  │  │  │  ├─ flight.h
│  │     │  │  │  │  ├─ gdb.h
│  │     │  │  │  │  ├─ helpers.h
│  │     │  │  │  │  ├─ inference.h
│  │     │  │  │  │  ├─ io.h
│  │     │  │  │  │  ├─ ipc.h
│  │     │  │  │  │  ├─ iterators.h
│  │     │  │  │  │  ├─ lib.h
│  │     │  │  │  │  ├─ lib_api.h
│  │     │  │  │  │  ├─ numpy_convert.h
│  │     │  │  │  │  ├─ numpy_init.h
│  │     │  │  │  │  ├─ numpy_interop.h
│  │     │  │  │  │  ├─ numpy_to_arrow.h
│  │     │  │  │  │  ├─ parquet_encryption.h
│  │     │  │  │  │  ├─ platform.h
│  │     │  │  │  │  ├─ pyarrow.h
│  │     │  │  │  │  ├─ pyarrow_api.h
│  │     │  │  │  │  ├─ pyarrow_lib.h
│  │     │  │  │  │  ├─ python_test.h
│  │     │  │  │  │  ├─ python_to_arrow.h
│  │     │  │  │  │  ├─ type_traits.h
│  │     │  │  │  │  ├─ udf.h
│  │     │  │  │  │  ├─ util.h
│  │     │  │  │  │  ├─ vendored
│  │     │  │  │  │  │  └─ pythoncapi_compat.h
│  │     │  │  │  │  └─ visibility.h
│  │     │  │  │  ├─ record_batch.h
│  │     │  │  │  ├─ result.h
│  │     │  │  │  ├─ scalar.h
│  │     │  │  │  ├─ sparse_tensor.h
│  │     │  │  │  ├─ status.h
│  │     │  │  │  ├─ stl.h
│  │     │  │  │  ├─ stl_allocator.h
│  │     │  │  │  ├─ stl_iterator.h
│  │     │  │  │  ├─ table.h
│  │     │  │  │  ├─ table_builder.h
│  │     │  │  │  ├─ telemetry
│  │     │  │  │  │  └─ logging.h
│  │     │  │  │  ├─ tensor
│  │     │  │  │  │  └─ converter.h
│  │     │  │  │  ├─ tensor.h
│  │     │  │  │  ├─ testing
│  │     │  │  │  │  ├─ async_test_util.h
│  │     │  │  │  │  ├─ builder.h
│  │     │  │  │  │  ├─ executor_util.h
│  │     │  │  │  │  ├─ extension_type.h
│  │     │  │  │  │  ├─ fixed_width_test_util.h
│  │     │  │  │  │  ├─ future_util.h
│  │     │  │  │  │  ├─ generator.h
│  │     │  │  │  │  ├─ gtest_compat.h
│  │     │  │  │  │  ├─ gtest_util.h
│  │     │  │  │  │  ├─ matchers.h
│  │     │  │  │  │  ├─ math.h
│  │     │  │  │  │  ├─ process.h
│  │     │  │  │  │  ├─ random.h
│  │     │  │  │  │  ├─ uniform_real.h
│  │     │  │  │  │  ├─ util.h
│  │     │  │  │  │  └─ visibility.h
│  │     │  │  │  ├─ type.h
│  │     │  │  │  ├─ type_fwd.h
│  │     │  │  │  ├─ type_traits.h
│  │     │  │  │  ├─ util
│  │     │  │  │  │  ├─ algorithm.h
│  │     │  │  │  │  ├─ aligned_storage.h
│  │     │  │  │  │  ├─ align_util.h
│  │     │  │  │  │  ├─ async_generator.h
│  │     │  │  │  │  ├─ async_generator_fwd.h
│  │     │  │  │  │  ├─ async_util.h
│  │     │  │  │  │  ├─ base64.h
│  │     │  │  │  │  ├─ basic_decimal.h
│  │     │  │  │  │  ├─ benchmark_util.h
│  │     │  │  │  │  ├─ binary_view_util.h
│  │     │  │  │  │  ├─ bitmap.h
│  │     │  │  │  │  ├─ bitmap_builders.h
│  │     │  │  │  │  ├─ bitmap_generate.h
│  │     │  │  │  │  ├─ bitmap_ops.h
│  │     │  │  │  │  ├─ bitmap_reader.h
│  │     │  │  │  │  ├─ bitmap_visit.h
│  │     │  │  │  │  ├─ bitmap_writer.h
│  │     │  │  │  │  ├─ bit_block_counter.h
│  │     │  │  │  │  ├─ bit_run_reader.h
│  │     │  │  │  │  ├─ bit_util.h
│  │     │  │  │  │  ├─ byte_size.h
│  │     │  │  │  │  ├─ cancel.h
│  │     │  │  │  │  ├─ checked_cast.h
│  │     │  │  │  │  ├─ compare.h
│  │     │  │  │  │  ├─ compression.h
│  │     │  │  │  │  ├─ concurrent_map.h
│  │     │  │  │  │  ├─ config.h
│  │     │  │  │  │  ├─ converter.h
│  │     │  │  │  │  ├─ cpu_info.h
│  │     │  │  │  │  ├─ crc32.h
│  │     │  │  │  │  ├─ debug.h
│  │     │  │  │  │  ├─ decimal.h
│  │     │  │  │  │  ├─ delimiting.h
│  │     │  │  │  │  ├─ endian.h
│  │     │  │  │  │  ├─ float16.h
│  │     │  │  │  │  ├─ formatting.h
│  │     │  │  │  │  ├─ functional.h
│  │     │  │  │  │  ├─ future.h
│  │     │  │  │  │  ├─ hashing.h
│  │     │  │  │  │  ├─ hash_util.h
│  │     │  │  │  │  ├─ int_util.h
│  │     │  │  │  │  ├─ int_util_overflow.h
│  │     │  │  │  │  ├─ io_util.h
│  │     │  │  │  │  ├─ iterator.h
│  │     │  │  │  │  ├─ key_value_metadata.h
│  │     │  │  │  │  ├─ launder.h
│  │     │  │  │  │  ├─ list_util.h
│  │     │  │  │  │  ├─ logger.h
│  │     │  │  │  │  ├─ logging.h
│  │     │  │  │  │  ├─ macros.h
│  │     │  │  │  │  ├─ math_constants.h
│  │     │  │  │  │  ├─ mutex.h
│  │     │  │  │  │  ├─ parallel.h
│  │     │  │  │  │  ├─ pcg_random.h
│  │     │  │  │  │  ├─ prefetch.h
│  │     │  │  │  │  ├─ queue.h
│  │     │  │  │  │  ├─ range.h
│  │     │  │  │  │  ├─ ree_util.h
│  │     │  │  │  │  ├─ regex.h
│  │     │  │  │  │  ├─ rows_to_batches.h
│  │     │  │  │  │  ├─ secure_string.h
│  │     │  │  │  │  ├─ simd.h
│  │     │  │  │  │  ├─ small_vector.h
│  │     │  │  │  │  ├─ string.h
│  │     │  │  │  │  ├─ string_util.h
│  │     │  │  │  │  ├─ task_group.h
│  │     │  │  │  │  ├─ test_common.h
│  │     │  │  │  │  ├─ thread_pool.h
│  │     │  │  │  │  ├─ time.h
│  │     │  │  │  │  ├─ tracing.h
│  │     │  │  │  │  ├─ type_fwd.h
│  │     │  │  │  │  ├─ type_traits.h
│  │     │  │  │  │  ├─ ubsan.h
│  │     │  │  │  │  ├─ union_util.h
│  │     │  │  │  │  ├─ unreachable.h
│  │     │  │  │  │  ├─ uri.h
│  │     │  │  │  │  ├─ utf8.h
│  │     │  │  │  │  ├─ value_parsing.h
│  │     │  │  │  │  ├─ vector.h
│  │     │  │  │  │  ├─ visibility.h
│  │     │  │  │  │  ├─ windows_compatibility.h
│  │     │  │  │  │  └─ windows_fixup.h
│  │     │  │  │  ├─ vendored
│  │     │  │  │  │  ├─ datetime
│  │     │  │  │  │  │  ├─ date.h
│  │     │  │  │  │  │  ├─ ios.h
│  │     │  │  │  │  │  ├─ tz.h
│  │     │  │  │  │  │  ├─ tz_private.h
│  │     │  │  │  │  │  └─ visibility.h
│  │     │  │  │  │  ├─ datetime.h
│  │     │  │  │  │  ├─ double-conversion
│  │     │  │  │  │  │  ├─ bignum-dtoa.h
│  │     │  │  │  │  │  ├─ bignum.h
│  │     │  │  │  │  │  ├─ cached-powers.h
│  │     │  │  │  │  │  ├─ diy-fp.h
│  │     │  │  │  │  │  ├─ double-conversion.h
│  │     │  │  │  │  │  ├─ double-to-string.h
│  │     │  │  │  │  │  ├─ fast-dtoa.h
│  │     │  │  │  │  │  ├─ fixed-dtoa.h
│  │     │  │  │  │  │  ├─ ieee.h
│  │     │  │  │  │  │  ├─ string-to-double.h
│  │     │  │  │  │  │  ├─ strtod.h
│  │     │  │  │  │  │  └─ utils.h
│  │     │  │  │  │  ├─ pcg
│  │     │  │  │  │  │  ├─ pcg_extras.hpp
│  │     │  │  │  │  │  ├─ pcg_random.hpp
│  │     │  │  │  │  │  └─ pcg_uint128.hpp
│  │     │  │  │  │  ├─ portable-snippets
│  │     │  │  │  │  │  └─ debug-trap.h
│  │     │  │  │  │  ├─ ProducerConsumerQueue.h
│  │     │  │  │  │  ├─ safeint
│  │     │  │  │  │  │  ├─ safe_math.h
│  │     │  │  │  │  │  └─ safe_math_impl.h
│  │     │  │  │  │  ├─ strptime.h
│  │     │  │  │  │  ├─ xxhash
│  │     │  │  │  │  │  └─ xxhash.h
│  │     │  │  │  │  └─ xxhash.h
│  │     │  │  │  ├─ visitor.h
│  │     │  │  │  ├─ visitor_generate.h
│  │     │  │  │  ├─ visit_array_inline.h
│  │     │  │  │  ├─ visit_data_inline.h
│  │     │  │  │  ├─ visit_scalar_inline.h
│  │     │  │  │  └─ visit_type_inline.h
│  │     │  │  └─ parquet
│  │     │  │     ├─ api
│  │     │  │     │  ├─ io.h
│  │     │  │     │  ├─ reader.h
│  │     │  │     │  ├─ schema.h
│  │     │  │     │  └─ writer.h
│  │     │  │     ├─ arrow
│  │     │  │     │  ├─ reader.h
│  │     │  │     │  ├─ schema.h
│  │     │  │     │  ├─ test_util.h
│  │     │  │     │  └─ writer.h
│  │     │  │     ├─ benchmark_util.h
│  │     │  │     ├─ bloom_filter.h
│  │     │  │     ├─ bloom_filter_reader.h
│  │     │  │     ├─ bloom_filter_writer.h
│  │     │  │     ├─ column_page.h
│  │     │  │     ├─ column_reader.h
│  │     │  │     ├─ column_scanner.h
│  │     │  │     ├─ column_writer.h
│  │     │  │     ├─ encoding.h
│  │     │  │     ├─ encryption
│  │     │  │     │  ├─ crypto_factory.h
│  │     │  │     │  ├─ encryption.h
│  │     │  │     │  ├─ file_key_material_store.h
│  │     │  │     │  ├─ file_key_unwrapper.h
│  │     │  │     │  ├─ file_key_wrapper.h
│  │     │  │     │  ├─ file_system_key_material_store.h
│  │     │  │     │  ├─ key_encryption_key.h
│  │     │  │     │  ├─ key_material.h
│  │     │  │     │  ├─ key_metadata.h
│  │     │  │     │  ├─ key_toolkit.h
│  │     │  │     │  ├─ kms_client.h
│  │     │  │     │  ├─ kms_client_factory.h
│  │     │  │     │  ├─ local_wrap_kms_client.h
│  │     │  │     │  ├─ test_encryption_util.h
│  │     │  │     │  ├─ test_in_memory_kms.h
│  │     │  │     │  ├─ two_level_cache_with_expiration.h
│  │     │  │     │  └─ type_fwd.h
│  │     │  │     ├─ exception.h
│  │     │  │     ├─ file_reader.h
│  │     │  │     ├─ file_writer.h
│  │     │  │     ├─ geospatial
│  │     │  │     │  └─ statistics.h
│  │     │  │     ├─ hasher.h
│  │     │  │     ├─ index_location.h
│  │     │  │     ├─ level_comparison.h
│  │     │  │     ├─ level_comparison_inc.h
│  │     │  │     ├─ level_conversion.h
│  │     │  │     ├─ level_conversion_inc.h
│  │     │  │     ├─ metadata.h
│  │     │  │     ├─ page_index.h
│  │     │  │     ├─ parquet_version.h
│  │     │  │     ├─ platform.h
│  │     │  │     ├─ printer.h
│  │     │  │     ├─ properties.h
│  │     │  │     ├─ schema.h
│  │     │  │     ├─ size_statistics.h
│  │     │  │     ├─ statistics.h
│  │     │  │     ├─ stream_reader.h
│  │     │  │     ├─ stream_writer.h
│  │     │  │     ├─ test_util.h
│  │     │  │     ├─ types.h
│  │     │  │     ├─ type_fwd.h
│  │     │  │     ├─ visit_type_inline.h
│  │     │  │     ├─ windows_compatibility.h
│  │     │  │     ├─ windows_fixup.h
│  │     │  │     └─ xxhasher.h
│  │     │  ├─ includes
│  │     │  │  ├─ common.pxd
│  │     │  │  ├─ libarrow.pxd
│  │     │  │  ├─ libarrow_acero.pxd
│  │     │  │  ├─ libarrow_cuda.pxd
│  │     │  │  ├─ libarrow_dataset.pxd
│  │     │  │  ├─ libarrow_dataset_parquet.pxd
│  │     │  │  ├─ libarrow_feather.pxd
│  │     │  │  ├─ libarrow_flight.pxd
│  │     │  │  ├─ libarrow_fs.pxd
│  │     │  │  ├─ libarrow_python.pxd
│  │     │  │  ├─ libarrow_substrait.pxd
│  │     │  │  ├─ libgandiva.pxd
│  │     │  │  ├─ libparquet.pxd
│  │     │  │  ├─ libparquet_encryption.pxd
│  │     │  │  └─ __init__.pxd
│  │     │  ├─ interchange
│  │     │  │  ├─ buffer.py
│  │     │  │  ├─ column.py
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ from_dataframe.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ io.pxi
│  │     │  ├─ ipc.pxi
│  │     │  ├─ ipc.py
│  │     │  ├─ json.py
│  │     │  ├─ jvm.py
│  │     │  ├─ lib.cp313-win_amd64.pyd
│  │     │  ├─ lib.pxd
│  │     │  ├─ lib.pyx
│  │     │  ├─ memory.pxi
│  │     │  ├─ orc.py
│  │     │  ├─ pandas-shim.pxi
│  │     │  ├─ pandas_compat.py
│  │     │  ├─ parquet
│  │     │  │  ├─ core.py
│  │     │  │  ├─ encryption.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ parquet.dll
│  │     │  ├─ parquet.lib
│  │     │  ├─ public-api.pxi
│  │     │  ├─ py.typed
│  │     │  ├─ scalar.pxi
│  │     │  ├─ src
│  │     │  │  └─ arrow
│  │     │  │     └─ python
│  │     │  │        ├─ api.h
│  │     │  │        ├─ arrow_to_pandas.cc
│  │     │  │        ├─ arrow_to_pandas.h
│  │     │  │        ├─ arrow_to_python_internal.h
│  │     │  │        ├─ async.h
│  │     │  │        ├─ benchmark.cc
│  │     │  │        ├─ benchmark.h
│  │     │  │        ├─ CMakeLists.txt
│  │     │  │        ├─ common.cc
│  │     │  │        ├─ common.h
│  │     │  │        ├─ config.cc
│  │     │  │        ├─ config.h
│  │     │  │        ├─ config_internal.h.cmake
│  │     │  │        ├─ csv.cc
│  │     │  │        ├─ csv.h
│  │     │  │        ├─ datetime.cc
│  │     │  │        ├─ datetime.h
│  │     │  │        ├─ decimal.cc
│  │     │  │        ├─ decimal.h
│  │     │  │        ├─ extension_type.cc
│  │     │  │        ├─ extension_type.h
│  │     │  │        ├─ filesystem.cc
│  │     │  │        ├─ filesystem.h
│  │     │  │        ├─ flight.cc
│  │     │  │        ├─ flight.h
│  │     │  │        ├─ gdb.cc
│  │     │  │        ├─ gdb.h
│  │     │  │        ├─ helpers.cc
│  │     │  │        ├─ helpers.h
│  │     │  │        ├─ inference.cc
│  │     │  │        ├─ inference.h
│  │     │  │        ├─ io.cc
│  │     │  │        ├─ io.h
│  │     │  │        ├─ ipc.cc
│  │     │  │        ├─ ipc.h
│  │     │  │        ├─ iterators.h
│  │     │  │        ├─ numpy_convert.cc
│  │     │  │        ├─ numpy_convert.h
│  │     │  │        ├─ numpy_init.cc
│  │     │  │        ├─ numpy_init.h
│  │     │  │        ├─ numpy_internal.h
│  │     │  │        ├─ numpy_interop.h
│  │     │  │        ├─ numpy_to_arrow.cc
│  │     │  │        ├─ numpy_to_arrow.h
│  │     │  │        ├─ parquet_encryption.cc
│  │     │  │        ├─ parquet_encryption.h
│  │     │  │        ├─ platform.h
│  │     │  │        ├─ pyarrow.cc
│  │     │  │        ├─ pyarrow.h
│  │     │  │        ├─ pyarrow_api.h
│  │     │  │        ├─ pyarrow_lib.h
│  │     │  │        ├─ python_test.cc
│  │     │  │        ├─ python_test.h
│  │     │  │        ├─ python_to_arrow.cc
│  │     │  │        ├─ python_to_arrow.h
│  │     │  │        ├─ type_traits.h
│  │     │  │        ├─ udf.cc
│  │     │  │        ├─ udf.h
│  │     │  │        ├─ util.cc
│  │     │  │        ├─ util.h
│  │     │  │        ├─ vendored
│  │     │  │        │  ├─ CMakeLists.txt
│  │     │  │        │  └─ pythoncapi_compat.h
│  │     │  │        └─ visibility.h
│  │     │  ├─ substrait.py
│  │     │  ├─ table.pxi
│  │     │  ├─ tensor.pxi
│  │     │  ├─ tests
│  │     │  │  ├─ arrow_16597.py
│  │     │  │  ├─ arrow_39313.py
│  │     │  │  ├─ arrow_7980.py
│  │     │  │  ├─ bound_function_visit_strings.pyx
│  │     │  │  ├─ conftest.py
│  │     │  │  ├─ data
│  │     │  │  │  ├─ feather
│  │     │  │  │  │  └─ v0.17.0.version.2-compression.lz4.feather
│  │     │  │  │  ├─ orc
│  │     │  │  │  │  ├─ decimal.jsn.gz
│  │     │  │  │  │  ├─ decimal.orc
│  │     │  │  │  │  ├─ README.md
│  │     │  │  │  │  ├─ TestOrcFile.emptyFile.jsn.gz
│  │     │  │  │  │  ├─ TestOrcFile.emptyFile.orc
│  │     │  │  │  │  ├─ TestOrcFile.test1.jsn.gz
│  │     │  │  │  │  ├─ TestOrcFile.test1.orc
│  │     │  │  │  │  ├─ TestOrcFile.testDate1900.jsn.gz
│  │     │  │  │  │  └─ TestOrcFile.testDate1900.orc
│  │     │  │  │  └─ parquet
│  │     │  │  │     ├─ v0.7.1.all-named-index.parquet
│  │     │  │  │     ├─ v0.7.1.column-metadata-handling.parquet
│  │     │  │  │     ├─ v0.7.1.parquet
│  │     │  │  │     └─ v0.7.1.some-named-index.parquet
│  │     │  │  ├─ extensions.pyx
│  │     │  │  ├─ interchange
│  │     │  │  │  ├─ test_conversion.py
│  │     │  │  │  ├─ test_interchange_spec.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ pandas_examples.py
│  │     │  │  ├─ pandas_threaded_import.py
│  │     │  │  ├─ parquet
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ encryption.py
│  │     │  │  │  ├─ test_basic.py
│  │     │  │  │  ├─ test_compliant_nested_type.py
│  │     │  │  │  ├─ test_dataset.py
│  │     │  │  │  ├─ test_data_types.py
│  │     │  │  │  ├─ test_datetime.py
│  │     │  │  │  ├─ test_encryption.py
│  │     │  │  │  ├─ test_metadata.py
│  │     │  │  │  ├─ test_pandas.py
│  │     │  │  │  ├─ test_parquet_file.py
│  │     │  │  │  ├─ test_parquet_writer.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ pyarrow_cython_example.pyx
│  │     │  │  ├─ read_record_batch.py
│  │     │  │  ├─ strategies.py
│  │     │  │  ├─ test_acero.py
│  │     │  │  ├─ test_adhoc_memory_leak.py
│  │     │  │  ├─ test_array.py
│  │     │  │  ├─ test_builder.py
│  │     │  │  ├─ test_cffi.py
│  │     │  │  ├─ test_compute.py
│  │     │  │  ├─ test_convert_builtin.py
│  │     │  │  ├─ test_cpp_internals.py
│  │     │  │  ├─ test_csv.py
│  │     │  │  ├─ test_cuda.py
│  │     │  │  ├─ test_cuda_numba_interop.py
│  │     │  │  ├─ test_cython.py
│  │     │  │  ├─ test_dataset.py
│  │     │  │  ├─ test_dataset_encryption.py
│  │     │  │  ├─ test_deprecations.py
│  │     │  │  ├─ test_device.py
│  │     │  │  ├─ test_dlpack.py
│  │     │  │  ├─ test_exec_plan.py
│  │     │  │  ├─ test_extension_type.py
│  │     │  │  ├─ test_feather.py
│  │     │  │  ├─ test_flight.py
│  │     │  │  ├─ test_flight_async.py
│  │     │  │  ├─ test_fs.py
│  │     │  │  ├─ test_gandiva.py
│  │     │  │  ├─ test_gdb.py
│  │     │  │  ├─ test_io.py
│  │     │  │  ├─ test_ipc.py
│  │     │  │  ├─ test_json.py
│  │     │  │  ├─ test_jvm.py
│  │     │  │  ├─ test_memory.py
│  │     │  │  ├─ test_misc.py
│  │     │  │  ├─ test_orc.py
│  │     │  │  ├─ test_pandas.py
│  │     │  │  ├─ test_scalars.py
│  │     │  │  ├─ test_schema.py
│  │     │  │  ├─ test_sparse_tensor.py
│  │     │  │  ├─ test_strategies.py
│  │     │  │  ├─ test_substrait.py
│  │     │  │  ├─ test_table.py
│  │     │  │  ├─ test_tensor.py
│  │     │  │  ├─ test_types.py
│  │     │  │  ├─ test_udf.py
│  │     │  │  ├─ test_util.py
│  │     │  │  ├─ test_without_numpy.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ wsgi_examples.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ types.pxi
│  │     │  ├─ types.py
│  │     │  ├─ util.py
│  │     │  ├─ vendored
│  │     │  │  ├─ docscrape.py
│  │     │  │  ├─ version.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _acero.cp313-win_amd64.pyd
│  │     │  ├─ _acero.pxd
│  │     │  ├─ _acero.pyx
│  │     │  ├─ _azurefs.cp313-win_amd64.pyd
│  │     │  ├─ _azurefs.pyx
│  │     │  ├─ _compute.cp313-win_amd64.pyd
│  │     │  ├─ _compute.pxd
│  │     │  ├─ _compute.pyx
│  │     │  ├─ _compute_docstrings.py
│  │     │  ├─ _csv.cp313-win_amd64.pyd
│  │     │  ├─ _csv.pxd
│  │     │  ├─ _csv.pyx
│  │     │  ├─ _cuda.pxd
│  │     │  ├─ _cuda.pyx
│  │     │  ├─ _dataset.cp313-win_amd64.pyd
│  │     │  ├─ _dataset.pxd
│  │     │  ├─ _dataset.pyx
│  │     │  ├─ _dataset_orc.cp313-win_amd64.pyd
│  │     │  ├─ _dataset_orc.pyx
│  │     │  ├─ _dataset_parquet.cp313-win_amd64.pyd
│  │     │  ├─ _dataset_parquet.pxd
│  │     │  ├─ _dataset_parquet.pyx
│  │     │  ├─ _dataset_parquet_encryption.cp313-win_amd64.pyd
│  │     │  ├─ _dataset_parquet_encryption.pyx
│  │     │  ├─ _dlpack.pxi
│  │     │  ├─ _feather.cp313-win_amd64.pyd
│  │     │  ├─ _feather.pyx
│  │     │  ├─ _flight.cp313-win_amd64.pyd
│  │     │  ├─ _flight.pyx
│  │     │  ├─ _fs.cp313-win_amd64.pyd
│  │     │  ├─ _fs.pxd
│  │     │  ├─ _fs.pyx
│  │     │  ├─ _gcsfs.cp313-win_amd64.pyd
│  │     │  ├─ _gcsfs.pyx
│  │     │  ├─ _generated_version.py
│  │     │  ├─ _hdfs.cp313-win_amd64.pyd
│  │     │  ├─ _hdfs.pyx
│  │     │  ├─ _json.cp313-win_amd64.pyd
│  │     │  ├─ _json.pxd
│  │     │  ├─ _json.pyx
│  │     │  ├─ _orc.cp313-win_amd64.pyd
│  │     │  ├─ _orc.pxd
│  │     │  ├─ _orc.pyx
│  │     │  ├─ _parquet.cp313-win_amd64.pyd
│  │     │  ├─ _parquet.pxd
│  │     │  ├─ _parquet.pyx
│  │     │  ├─ _parquet_encryption.cp313-win_amd64.pyd
│  │     │  ├─ _parquet_encryption.pxd
│  │     │  ├─ _parquet_encryption.pyx
│  │     │  ├─ _pyarrow_cpp_tests.cp313-win_amd64.pyd
│  │     │  ├─ _pyarrow_cpp_tests.pxd
│  │     │  ├─ _pyarrow_cpp_tests.pyx
│  │     │  ├─ _s3fs.cp313-win_amd64.pyd
│  │     │  ├─ _s3fs.pyx
│  │     │  ├─ _substrait.cp313-win_amd64.pyd
│  │     │  ├─ _substrait.pyx
│  │     │  ├─ __init__.pxd
│  │     │  ├─ __init__.py
│  │     │  └─ __init__.pyi
│  │     ├─ pyarrow-24.0.0.dist-info
│  │     │  ├─ DELVEWHEEL
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  ├─ LICENSE.txt
│  │     │  │  └─ NOTICE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pyarrow.libs
│  │     │  ├─ msvcp140-f22b3317cfb3fad7db3a18f8f234f32b.dll
│  │     │  └─ msvcp140_atomic_wait-a67379821634a4f3a32730b57a436c71.dll
│  │     ├─ pycparser
│  │     │  ├─ ast_transforms.py
│  │     │  ├─ c_ast.py
│  │     │  ├─ c_generator.py
│  │     │  ├─ c_lexer.py
│  │     │  ├─ c_parser.py
│  │     │  ├─ _ast_gen.py
│  │     │  ├─ _c_ast.cfg
│  │     │  └─ __init__.py
│  │     ├─ pycparser-3.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pydantic
│  │     │  ├─ aliases.py
│  │     │  ├─ alias_generators.py
│  │     │  ├─ annotated_handlers.py
│  │     │  ├─ class_validators.py
│  │     │  ├─ color.py
│  │     │  ├─ config.py
│  │     │  ├─ dataclasses.py
│  │     │  ├─ datetime_parse.py
│  │     │  ├─ decorator.py
│  │     │  ├─ deprecated
│  │     │  │  ├─ class_validators.py
│  │     │  │  ├─ config.py
│  │     │  │  ├─ copy_internals.py
│  │     │  │  ├─ decorator.py
│  │     │  │  ├─ json.py
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ tools.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ env_settings.py
│  │     │  ├─ errors.py
│  │     │  ├─ error_wrappers.py
│  │     │  ├─ experimental
│  │     │  │  ├─ arguments_schema.py
│  │     │  │  ├─ missing_sentinel.py
│  │     │  │  ├─ pipeline.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ fields.py
│  │     │  ├─ functional_serializers.py
│  │     │  ├─ functional_validators.py
│  │     │  ├─ generics.py
│  │     │  ├─ json.py
│  │     │  ├─ json_schema.py
│  │     │  ├─ main.py
│  │     │  ├─ mypy.py
│  │     │  ├─ networks.py
│  │     │  ├─ parse.py
│  │     │  ├─ plugin
│  │     │  │  ├─ _loader.py
│  │     │  │  ├─ _schema_validator.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ py.typed
│  │     │  ├─ root_model.py
│  │     │  ├─ schema.py
│  │     │  ├─ tools.py
│  │     │  ├─ types.py
│  │     │  ├─ type_adapter.py
│  │     │  ├─ typing.py
│  │     │  ├─ utils.py
│  │     │  ├─ v1
│  │     │  │  ├─ annotated_types.py
│  │     │  │  ├─ class_validators.py
│  │     │  │  ├─ color.py
│  │     │  │  ├─ config.py
│  │     │  │  ├─ dataclasses.py
│  │     │  │  ├─ datetime_parse.py
│  │     │  │  ├─ decorator.py
│  │     │  │  ├─ env_settings.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ error_wrappers.py
│  │     │  │  ├─ fields.py
│  │     │  │  ├─ generics.py
│  │     │  │  ├─ json.py
│  │     │  │  ├─ main.py
│  │     │  │  ├─ mypy.py
│  │     │  │  ├─ networks.py
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ py.typed
│  │     │  │  ├─ schema.py
│  │     │  │  ├─ tools.py
│  │     │  │  ├─ types.py
│  │     │  │  ├─ typing.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ validators.py
│  │     │  │  ├─ version.py
│  │     │  │  ├─ _hypothesis_plugin.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ validate_call_decorator.py
│  │     │  ├─ validators.py
│  │     │  ├─ version.py
│  │     │  ├─ warnings.py
│  │     │  ├─ _internal
│  │     │  │  ├─ _config.py
│  │     │  │  ├─ _core_metadata.py
│  │     │  │  ├─ _core_utils.py
│  │     │  │  ├─ _dataclasses.py
│  │     │  │  ├─ _decorators.py
│  │     │  │  ├─ _decorators_v1.py
│  │     │  │  ├─ _discriminated_union.py
│  │     │  │  ├─ _docs_extraction.py
│  │     │  │  ├─ _fields.py
│  │     │  │  ├─ _forward_ref.py
│  │     │  │  ├─ _generate_schema.py
│  │     │  │  ├─ _generics.py
│  │     │  │  ├─ _git.py
│  │     │  │  ├─ _import_utils.py
│  │     │  │  ├─ _internal_dataclass.py
│  │     │  │  ├─ _known_annotated_metadata.py
│  │     │  │  ├─ _mock_val_ser.py
│  │     │  │  ├─ _model_construction.py
│  │     │  │  ├─ _namespace_utils.py
│  │     │  │  ├─ _repr.py
│  │     │  │  ├─ _schema_gather.py
│  │     │  │  ├─ _schema_generation_shared.py
│  │     │  │  ├─ _serializers.py
│  │     │  │  ├─ _signature.py
│  │     │  │  ├─ _typing_extra.py
│  │     │  │  ├─ _utils.py
│  │     │  │  ├─ _validate_call.py
│  │     │  │  ├─ _validators.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _migration.py
│  │     │  └─ __init__.py
│  │     ├─ pydantic-2.13.4.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pydantic_core
│  │     │  ├─ core_schema.py
│  │     │  ├─ py.typed
│  │     │  ├─ _pydantic_core.cp313-win_amd64.pyd
│  │     │  ├─ _pydantic_core.pyi
│  │     │  └─ __init__.py
│  │     ├─ pydantic_core-2.46.4.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ sboms
│  │     │  │  └─ pydantic-core.cyclonedx.json
│  │     │  └─ WHEEL
│  │     ├─ pydeck
│  │     │  ├─ bindings
│  │     │  │  ├─ base_map_provider.py
│  │     │  │  ├─ deck.py
│  │     │  │  ├─ json_tools.py
│  │     │  │  ├─ layer.py
│  │     │  │  ├─ light_settings.py
│  │     │  │  ├─ map_styles.py
│  │     │  │  ├─ view.py
│  │     │  │  ├─ view_state.py
│  │     │  │  ├─ widget.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ data_utils
│  │     │  │  ├─ binary_transfer.py
│  │     │  │  ├─ color_scales.py
│  │     │  │  ├─ type_checking.py
│  │     │  │  ├─ viewport_helpers.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ exceptions
│  │     │  │  ├─ exceptions.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ frontend_semver.py
│  │     │  ├─ io
│  │     │  │  ├─ html.py
│  │     │  │  ├─ templates
│  │     │  │  │  ├─ index.j2
│  │     │  │  │  └─ style.j2
│  │     │  │  └─ __init__.py
│  │     │  ├─ nbextension
│  │     │  │  ├─ static
│  │     │  │  │  ├─ extensionRequires.js
│  │     │  │  │  ├─ index.js
│  │     │  │  │  └─ index.js.map
│  │     │  │  └─ __init__.py
│  │     │  ├─ settings.py
│  │     │  ├─ types
│  │     │  │  ├─ base.py
│  │     │  │  ├─ function.py
│  │     │  │  ├─ image.py
│  │     │  │  ├─ string.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ widget
│  │     │  │  ├─ debounce.py
│  │     │  │  ├─ widget.py
│  │     │  │  ├─ _frontend.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _version.py
│  │     │  └─ __init__.py
│  │     ├─ pydeck-0.9.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ python_dateutil-2.9.0.post0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  ├─ WHEEL
│  │     │  └─ zip-safe
│  │     ├─ python_dotenv-1.2.2.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ python_multipart
│  │     │  ├─ decoders.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ multipart.py
│  │     │  ├─ py.typed
│  │     │  └─ __init__.py
│  │     ├─ python_multipart-0.0.32.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pytz
│  │     │  ├─ exceptions.py
│  │     │  ├─ lazy.py
│  │     │  ├─ reference.py
│  │     │  ├─ tzfile.py
│  │     │  ├─ tzinfo.py
│  │     │  ├─ zoneinfo
│  │     │  │  ├─ Africa
│  │     │  │  │  ├─ Abidjan
│  │     │  │  │  ├─ Accra
│  │     │  │  │  ├─ Addis_Ababa
│  │     │  │  │  ├─ Algiers
│  │     │  │  │  ├─ Asmara
│  │     │  │  │  ├─ Asmera
│  │     │  │  │  ├─ Bamako
│  │     │  │  │  ├─ Bangui
│  │     │  │  │  ├─ Banjul
│  │     │  │  │  ├─ Bissau
│  │     │  │  │  ├─ Blantyre
│  │     │  │  │  ├─ Brazzaville
│  │     │  │  │  ├─ Bujumbura
│  │     │  │  │  ├─ Cairo
│  │     │  │  │  ├─ Casablanca
│  │     │  │  │  ├─ Ceuta
│  │     │  │  │  ├─ Conakry
│  │     │  │  │  ├─ Dakar
│  │     │  │  │  ├─ Dar_es_Salaam
│  │     │  │  │  ├─ Djibouti
│  │     │  │  │  ├─ Douala
│  │     │  │  │  ├─ El_Aaiun
│  │     │  │  │  ├─ Freetown
│  │     │  │  │  ├─ Gaborone
│  │     │  │  │  ├─ Harare
│  │     │  │  │  ├─ Johannesburg
│  │     │  │  │  ├─ Juba
│  │     │  │  │  ├─ Kampala
│  │     │  │  │  ├─ Khartoum
│  │     │  │  │  ├─ Kigali
│  │     │  │  │  ├─ Kinshasa
│  │     │  │  │  ├─ Lagos
│  │     │  │  │  ├─ Libreville
│  │     │  │  │  ├─ Lome
│  │     │  │  │  ├─ Luanda
│  │     │  │  │  ├─ Lubumbashi
│  │     │  │  │  ├─ Lusaka
│  │     │  │  │  ├─ Malabo
│  │     │  │  │  ├─ Maputo
│  │     │  │  │  ├─ Maseru
│  │     │  │  │  ├─ Mbabane
│  │     │  │  │  ├─ Mogadishu
│  │     │  │  │  ├─ Monrovia
│  │     │  │  │  ├─ Nairobi
│  │     │  │  │  ├─ Ndjamena
│  │     │  │  │  ├─ Niamey
│  │     │  │  │  ├─ Nouakchott
│  │     │  │  │  ├─ Ouagadougou
│  │     │  │  │  ├─ Porto-Novo
│  │     │  │  │  ├─ Sao_Tome
│  │     │  │  │  ├─ Timbuktu
│  │     │  │  │  ├─ Tripoli
│  │     │  │  │  ├─ Tunis
│  │     │  │  │  └─ Windhoek
│  │     │  │  ├─ America
│  │     │  │  │  ├─ Adak
│  │     │  │  │  ├─ Anchorage
│  │     │  │  │  ├─ Anguilla
│  │     │  │  │  ├─ Antigua
│  │     │  │  │  ├─ Araguaina
│  │     │  │  │  ├─ Argentina
│  │     │  │  │  │  ├─ Buenos_Aires
│  │     │  │  │  │  ├─ Catamarca
│  │     │  │  │  │  ├─ ComodRivadavia
│  │     │  │  │  │  ├─ Cordoba
│  │     │  │  │  │  ├─ Jujuy
│  │     │  │  │  │  ├─ La_Rioja
│  │     │  │  │  │  ├─ Mendoza
│  │     │  │  │  │  ├─ Rio_Gallegos
│  │     │  │  │  │  ├─ Salta
│  │     │  │  │  │  ├─ San_Juan
│  │     │  │  │  │  ├─ San_Luis
│  │     │  │  │  │  ├─ Tucuman
│  │     │  │  │  │  └─ Ushuaia
│  │     │  │  │  ├─ Aruba
│  │     │  │  │  ├─ Asuncion
│  │     │  │  │  ├─ Atikokan
│  │     │  │  │  ├─ Atka
│  │     │  │  │  ├─ Bahia
│  │     │  │  │  ├─ Bahia_Banderas
│  │     │  │  │  ├─ Barbados
│  │     │  │  │  ├─ Belem
│  │     │  │  │  ├─ Belize
│  │     │  │  │  ├─ Blanc-Sablon
│  │     │  │  │  ├─ Boa_Vista
│  │     │  │  │  ├─ Bogota
│  │     │  │  │  ├─ Boise
│  │     │  │  │  ├─ Buenos_Aires
│  │     │  │  │  ├─ Cambridge_Bay
│  │     │  │  │  ├─ Campo_Grande
│  │     │  │  │  ├─ Cancun
│  │     │  │  │  ├─ Caracas
│  │     │  │  │  ├─ Catamarca
│  │     │  │  │  ├─ Cayenne
│  │     │  │  │  ├─ Cayman
│  │     │  │  │  ├─ Chicago
│  │     │  │  │  ├─ Chihuahua
│  │     │  │  │  ├─ Ciudad_Juarez
│  │     │  │  │  ├─ Coral_Harbour
│  │     │  │  │  ├─ Cordoba
│  │     │  │  │  ├─ Costa_Rica
│  │     │  │  │  ├─ Coyhaique
│  │     │  │  │  ├─ Creston
│  │     │  │  │  ├─ Cuiaba
│  │     │  │  │  ├─ Curacao
│  │     │  │  │  ├─ Danmarkshavn
│  │     │  │  │  ├─ Dawson
│  │     │  │  │  ├─ Dawson_Creek
│  │     │  │  │  ├─ Denver
│  │     │  │  │  ├─ Detroit
│  │     │  │  │  ├─ Dominica
│  │     │  │  │  ├─ Edmonton
│  │     │  │  │  ├─ Eirunepe
│  │     │  │  │  ├─ El_Salvador
│  │     │  │  │  ├─ Ensenada
│  │     │  │  │  ├─ Fortaleza
│  │     │  │  │  ├─ Fort_Nelson
│  │     │  │  │  ├─ Fort_Wayne
│  │     │  │  │  ├─ Glace_Bay
│  │     │  │  │  ├─ Godthab
│  │     │  │  │  ├─ Goose_Bay
│  │     │  │  │  ├─ Grand_Turk
│  │     │  │  │  ├─ Grenada
│  │     │  │  │  ├─ Guadeloupe
│  │     │  │  │  ├─ Guatemala
│  │     │  │  │  ├─ Guayaquil
│  │     │  │  │  ├─ Guyana
│  │     │  │  │  ├─ Halifax
│  │     │  │  │  ├─ Havana
│  │     │  │  │  ├─ Hermosillo
│  │     │  │  │  ├─ Indiana
│  │     │  │  │  │  ├─ Indianapolis
│  │     │  │  │  │  ├─ Knox
│  │     │  │  │  │  ├─ Marengo
│  │     │  │  │  │  ├─ Petersburg
│  │     │  │  │  │  ├─ Tell_City
│  │     │  │  │  │  ├─ Vevay
│  │     │  │  │  │  ├─ Vincennes
│  │     │  │  │  │  └─ Winamac
│  │     │  │  │  ├─ Indianapolis
│  │     │  │  │  ├─ Inuvik
│  │     │  │  │  ├─ Iqaluit
│  │     │  │  │  ├─ Jamaica
│  │     │  │  │  ├─ Jujuy
│  │     │  │  │  ├─ Juneau
│  │     │  │  │  ├─ Kentucky
│  │     │  │  │  │  ├─ Louisville
│  │     │  │  │  │  └─ Monticello
│  │     │  │  │  ├─ Knox_IN
│  │     │  │  │  ├─ Kralendijk
│  │     │  │  │  ├─ La_Paz
│  │     │  │  │  ├─ Lima
│  │     │  │  │  ├─ Los_Angeles
│  │     │  │  │  ├─ Louisville
│  │     │  │  │  ├─ Lower_Princes
│  │     │  │  │  ├─ Maceio
│  │     │  │  │  ├─ Managua
│  │     │  │  │  ├─ Manaus
│  │     │  │  │  ├─ Marigot
│  │     │  │  │  ├─ Martinique
│  │     │  │  │  ├─ Matamoros
│  │     │  │  │  ├─ Mazatlan
│  │     │  │  │  ├─ Mendoza
│  │     │  │  │  ├─ Menominee
│  │     │  │  │  ├─ Merida
│  │     │  │  │  ├─ Metlakatla
│  │     │  │  │  ├─ Mexico_City
│  │     │  │  │  ├─ Miquelon
│  │     │  │  │  ├─ Moncton
│  │     │  │  │  ├─ Monterrey
│  │     │  │  │  ├─ Montevideo
│  │     │  │  │  ├─ Montreal
│  │     │  │  │  ├─ Montserrat
│  │     │  │  │  ├─ Nassau
│  │     │  │  │  ├─ New_York
│  │     │  │  │  ├─ Nipigon
│  │     │  │  │  ├─ Nome
│  │     │  │  │  ├─ Noronha
│  │     │  │  │  ├─ North_Dakota
│  │     │  │  │  │  ├─ Beulah
│  │     │  │  │  │  ├─ Center
│  │     │  │  │  │  └─ New_Salem
│  │     │  │  │  ├─ Nuuk
│  │     │  │  │  ├─ Ojinaga
│  │     │  │  │  ├─ Panama
│  │     │  │  │  ├─ Pangnirtung
│  │     │  │  │  ├─ Paramaribo
│  │     │  │  │  ├─ Phoenix
│  │     │  │  │  ├─ Port-au-Prince
│  │     │  │  │  ├─ Porto_Acre
│  │     │  │  │  ├─ Porto_Velho
│  │     │  │  │  ├─ Port_of_Spain
│  │     │  │  │  ├─ Puerto_Rico
│  │     │  │  │  ├─ Punta_Arenas
│  │     │  │  │  ├─ Rainy_River
│  │     │  │  │  ├─ Rankin_Inlet
│  │     │  │  │  ├─ Recife
│  │     │  │  │  ├─ Regina
│  │     │  │  │  ├─ Resolute
│  │     │  │  │  ├─ Rio_Branco
│  │     │  │  │  ├─ Rosario
│  │     │  │  │  ├─ Santarem
│  │     │  │  │  ├─ Santa_Isabel
│  │     │  │  │  ├─ Santiago
│  │     │  │  │  ├─ Santo_Domingo
│  │     │  │  │  ├─ Sao_Paulo
│  │     │  │  │  ├─ Scoresbysund
│  │     │  │  │  ├─ Shiprock
│  │     │  │  │  ├─ Sitka
│  │     │  │  │  ├─ St_Barthelemy
│  │     │  │  │  ├─ St_Johns
│  │     │  │  │  ├─ St_Kitts
│  │     │  │  │  ├─ St_Lucia
│  │     │  │  │  ├─ St_Thomas
│  │     │  │  │  ├─ St_Vincent
│  │     │  │  │  ├─ Swift_Current
│  │     │  │  │  ├─ Tegucigalpa
│  │     │  │  │  ├─ Thule
│  │     │  │  │  ├─ Thunder_Bay
│  │     │  │  │  ├─ Tijuana
│  │     │  │  │  ├─ Toronto
│  │     │  │  │  ├─ Tortola
│  │     │  │  │  ├─ Vancouver
│  │     │  │  │  ├─ Virgin
│  │     │  │  │  ├─ Whitehorse
│  │     │  │  │  ├─ Winnipeg
│  │     │  │  │  ├─ Yakutat
│  │     │  │  │  └─ Yellowknife
│  │     │  │  ├─ Antarctica
│  │     │  │  │  ├─ Casey
│  │     │  │  │  ├─ Davis
│  │     │  │  │  ├─ DumontDUrville
│  │     │  │  │  ├─ Macquarie
│  │     │  │  │  ├─ Mawson
│  │     │  │  │  ├─ McMurdo
│  │     │  │  │  ├─ Palmer
│  │     │  │  │  ├─ Rothera
│  │     │  │  │  ├─ South_Pole
│  │     │  │  │  ├─ Syowa
│  │     │  │  │  ├─ Troll
│  │     │  │  │  └─ Vostok
│  │     │  │  ├─ Arctic
│  │     │  │  │  └─ Longyearbyen
│  │     │  │  ├─ Asia
│  │     │  │  │  ├─ Aden
│  │     │  │  │  ├─ Almaty
│  │     │  │  │  ├─ Amman
│  │     │  │  │  ├─ Anadyr
│  │     │  │  │  ├─ Aqtau
│  │     │  │  │  ├─ Aqtobe
│  │     │  │  │  ├─ Ashgabat
│  │     │  │  │  ├─ Ashkhabad
│  │     │  │  │  ├─ Atyrau
│  │     │  │  │  ├─ Baghdad
│  │     │  │  │  ├─ Bahrain
│  │     │  │  │  ├─ Baku
│  │     │  │  │  ├─ Bangkok
│  │     │  │  │  ├─ Barnaul
│  │     │  │  │  ├─ Beirut
│  │     │  │  │  ├─ Bishkek
│  │     │  │  │  ├─ Brunei
│  │     │  │  │  ├─ Calcutta
│  │     │  │  │  ├─ Chita
│  │     │  │  │  ├─ Choibalsan
│  │     │  │  │  ├─ Chongqing
│  │     │  │  │  ├─ Chungking
│  │     │  │  │  ├─ Colombo
│  │     │  │  │  ├─ Dacca
│  │     │  │  │  ├─ Damascus
│  │     │  │  │  ├─ Dhaka
│  │     │  │  │  ├─ Dili
│  │     │  │  │  ├─ Dubai
│  │     │  │  │  ├─ Dushanbe
│  │     │  │  │  ├─ Famagusta
│  │     │  │  │  ├─ Gaza
│  │     │  │  │  ├─ Harbin
│  │     │  │  │  ├─ Hebron
│  │     │  │  │  ├─ Hong_Kong
│  │     │  │  │  ├─ Hovd
│  │     │  │  │  ├─ Ho_Chi_Minh
│  │     │  │  │  ├─ Irkutsk
│  │     │  │  │  ├─ Istanbul
│  │     │  │  │  ├─ Jakarta
│  │     │  │  │  ├─ Jayapura
│  │     │  │  │  ├─ Jerusalem
│  │     │  │  │  ├─ Kabul
│  │     │  │  │  ├─ Kamchatka
│  │     │  │  │  ├─ Karachi
│  │     │  │  │  ├─ Kashgar
│  │     │  │  │  ├─ Kathmandu
│  │     │  │  │  ├─ Katmandu
│  │     │  │  │  ├─ Khandyga
│  │     │  │  │  ├─ Kolkata
│  │     │  │  │  ├─ Krasnoyarsk
│  │     │  │  │  ├─ Kuala_Lumpur
│  │     │  │  │  ├─ Kuching
│  │     │  │  │  ├─ Kuwait
│  │     │  │  │  ├─ Macao
│  │     │  │  │  ├─ Macau
│  │     │  │  │  ├─ Magadan
│  │     │  │  │  ├─ Makassar
│  │     │  │  │  ├─ Manila
│  │     │  │  │  ├─ Muscat
│  │     │  │  │  ├─ Nicosia
│  │     │  │  │  ├─ Novokuznetsk
│  │     │  │  │  ├─ Novosibirsk
│  │     │  │  │  ├─ Omsk
│  │     │  │  │  ├─ Oral
│  │     │  │  │  ├─ Phnom_Penh
│  │     │  │  │  ├─ Pontianak
│  │     │  │  │  ├─ Pyongyang
│  │     │  │  │  ├─ Qatar
│  │     │  │  │  ├─ Qostanay
│  │     │  │  │  ├─ Qyzylorda
│  │     │  │  │  ├─ Rangoon
│  │     │  │  │  ├─ Riyadh
│  │     │  │  │  ├─ Saigon
│  │     │  │  │  ├─ Sakhalin
│  │     │  │  │  ├─ Samarkand
│  │     │  │  │  ├─ Seoul
│  │     │  │  │  ├─ Shanghai
│  │     │  │  │  ├─ Singapore
│  │     │  │  │  ├─ Srednekolymsk
│  │     │  │  │  ├─ Taipei
│  │     │  │  │  ├─ Tashkent
│  │     │  │  │  ├─ Tbilisi
│  │     │  │  │  ├─ Tehran
│  │     │  │  │  ├─ Tel_Aviv
│  │     │  │  │  ├─ Thimbu
│  │     │  │  │  ├─ Thimphu
│  │     │  │  │  ├─ Tokyo
│  │     │  │  │  ├─ Tomsk
│  │     │  │  │  ├─ Ujung_Pandang
│  │     │  │  │  ├─ Ulaanbaatar
│  │     │  │  │  ├─ Ulan_Bator
│  │     │  │  │  ├─ Urumqi
│  │     │  │  │  ├─ Ust-Nera
│  │     │  │  │  ├─ Vientiane
│  │     │  │  │  ├─ Vladivostok
│  │     │  │  │  ├─ Yakutsk
│  │     │  │  │  ├─ Yangon
│  │     │  │  │  ├─ Yekaterinburg
│  │     │  │  │  └─ Yerevan
│  │     │  │  ├─ Atlantic
│  │     │  │  │  ├─ Azores
│  │     │  │  │  ├─ Bermuda
│  │     │  │  │  ├─ Canary
│  │     │  │  │  ├─ Cape_Verde
│  │     │  │  │  ├─ Faeroe
│  │     │  │  │  ├─ Faroe
│  │     │  │  │  ├─ Jan_Mayen
│  │     │  │  │  ├─ Madeira
│  │     │  │  │  ├─ Reykjavik
│  │     │  │  │  ├─ South_Georgia
│  │     │  │  │  ├─ Stanley
│  │     │  │  │  └─ St_Helena
│  │     │  │  ├─ Australia
│  │     │  │  │  ├─ ACT
│  │     │  │  │  ├─ Adelaide
│  │     │  │  │  ├─ Brisbane
│  │     │  │  │  ├─ Broken_Hill
│  │     │  │  │  ├─ Canberra
│  │     │  │  │  ├─ Currie
│  │     │  │  │  ├─ Darwin
│  │     │  │  │  ├─ Eucla
│  │     │  │  │  ├─ Hobart
│  │     │  │  │  ├─ LHI
│  │     │  │  │  ├─ Lindeman
│  │     │  │  │  ├─ Lord_Howe
│  │     │  │  │  ├─ Melbourne
│  │     │  │  │  ├─ North
│  │     │  │  │  ├─ NSW
│  │     │  │  │  ├─ Perth
│  │     │  │  │  ├─ Queensland
│  │     │  │  │  ├─ South
│  │     │  │  │  ├─ Sydney
│  │     │  │  │  ├─ Tasmania
│  │     │  │  │  ├─ Victoria
│  │     │  │  │  ├─ West
│  │     │  │  │  └─ Yancowinna
│  │     │  │  ├─ Brazil
│  │     │  │  │  ├─ Acre
│  │     │  │  │  ├─ DeNoronha
│  │     │  │  │  ├─ East
│  │     │  │  │  └─ West
│  │     │  │  ├─ Canada
│  │     │  │  │  ├─ Atlantic
│  │     │  │  │  ├─ Central
│  │     │  │  │  ├─ Eastern
│  │     │  │  │  ├─ Mountain
│  │     │  │  │  ├─ Newfoundland
│  │     │  │  │  ├─ Pacific
│  │     │  │  │  ├─ Saskatchewan
│  │     │  │  │  └─ Yukon
│  │     │  │  ├─ CET
│  │     │  │  ├─ Chile
│  │     │  │  │  ├─ Continental
│  │     │  │  │  └─ EasterIsland
│  │     │  │  ├─ CST6CDT
│  │     │  │  ├─ Cuba
│  │     │  │  ├─ EET
│  │     │  │  ├─ Egypt
│  │     │  │  ├─ Eire
│  │     │  │  ├─ EST
│  │     │  │  ├─ EST5EDT
│  │     │  │  ├─ Etc
│  │     │  │  │  ├─ GMT
│  │     │  │  │  ├─ GMT+0
│  │     │  │  │  ├─ GMT+1
│  │     │  │  │  ├─ GMT+10
│  │     │  │  │  ├─ GMT+11
│  │     │  │  │  ├─ GMT+12
│  │     │  │  │  ├─ GMT+2
│  │     │  │  │  ├─ GMT+3
│  │     │  │  │  ├─ GMT+4
│  │     │  │  │  ├─ GMT+5
│  │     │  │  │  ├─ GMT+6
│  │     │  │  │  ├─ GMT+7
│  │     │  │  │  ├─ GMT+8
│  │     │  │  │  ├─ GMT+9
│  │     │  │  │  ├─ GMT-0
│  │     │  │  │  ├─ GMT-1
│  │     │  │  │  ├─ GMT-10
│  │     │  │  │  ├─ GMT-11
│  │     │  │  │  ├─ GMT-12
│  │     │  │  │  ├─ GMT-13
│  │     │  │  │  ├─ GMT-14
│  │     │  │  │  ├─ GMT-2
│  │     │  │  │  ├─ GMT-3
│  │     │  │  │  ├─ GMT-4
│  │     │  │  │  ├─ GMT-5
│  │     │  │  │  ├─ GMT-6
│  │     │  │  │  ├─ GMT-7
│  │     │  │  │  ├─ GMT-8
│  │     │  │  │  ├─ GMT-9
│  │     │  │  │  ├─ GMT0
│  │     │  │  │  ├─ Greenwich
│  │     │  │  │  ├─ UCT
│  │     │  │  │  ├─ Universal
│  │     │  │  │  ├─ UTC
│  │     │  │  │  └─ Zulu
│  │     │  │  ├─ Europe
│  │     │  │  │  ├─ Amsterdam
│  │     │  │  │  ├─ Andorra
│  │     │  │  │  ├─ Astrakhan
│  │     │  │  │  ├─ Athens
│  │     │  │  │  ├─ Belfast
│  │     │  │  │  ├─ Belgrade
│  │     │  │  │  ├─ Berlin
│  │     │  │  │  ├─ Bratislava
│  │     │  │  │  ├─ Brussels
│  │     │  │  │  ├─ Bucharest
│  │     │  │  │  ├─ Budapest
│  │     │  │  │  ├─ Busingen
│  │     │  │  │  ├─ Chisinau
│  │     │  │  │  ├─ Copenhagen
│  │     │  │  │  ├─ Dublin
│  │     │  │  │  ├─ Gibraltar
│  │     │  │  │  ├─ Guernsey
│  │     │  │  │  ├─ Helsinki
│  │     │  │  │  ├─ Isle_of_Man
│  │     │  │  │  ├─ Istanbul
│  │     │  │  │  ├─ Jersey
│  │     │  │  │  ├─ Kaliningrad
│  │     │  │  │  ├─ Kiev
│  │     │  │  │  ├─ Kirov
│  │     │  │  │  ├─ Kyiv
│  │     │  │  │  ├─ Lisbon
│  │     │  │  │  ├─ Ljubljana
│  │     │  │  │  ├─ London
│  │     │  │  │  ├─ Luxembourg
│  │     │  │  │  ├─ Madrid
│  │     │  │  │  ├─ Malta
│  │     │  │  │  ├─ Mariehamn
│  │     │  │  │  ├─ Minsk
│  │     │  │  │  ├─ Monaco
│  │     │  │  │  ├─ Moscow
│  │     │  │  │  ├─ Nicosia
│  │     │  │  │  ├─ Oslo
│  │     │  │  │  ├─ Paris
│  │     │  │  │  ├─ Podgorica
│  │     │  │  │  ├─ Prague
│  │     │  │  │  ├─ Riga
│  │     │  │  │  ├─ Rome
│  │     │  │  │  ├─ Samara
│  │     │  │  │  ├─ San_Marino
│  │     │  │  │  ├─ Sarajevo
│  │     │  │  │  ├─ Saratov
│  │     │  │  │  ├─ Simferopol
│  │     │  │  │  ├─ Skopje
│  │     │  │  │  ├─ Sofia
│  │     │  │  │  ├─ Stockholm
│  │     │  │  │  ├─ Tallinn
│  │     │  │  │  ├─ Tirane
│  │     │  │  │  ├─ Tiraspol
│  │     │  │  │  ├─ Ulyanovsk
│  │     │  │  │  ├─ Uzhgorod
│  │     │  │  │  ├─ Vaduz
│  │     │  │  │  ├─ Vatican
│  │     │  │  │  ├─ Vienna
│  │     │  │  │  ├─ Vilnius
│  │     │  │  │  ├─ Volgograd
│  │     │  │  │  ├─ Warsaw
│  │     │  │  │  ├─ Zagreb
│  │     │  │  │  ├─ Zaporozhye
│  │     │  │  │  └─ Zurich
│  │     │  │  ├─ Factory
│  │     │  │  ├─ GB
│  │     │  │  ├─ GB-Eire
│  │     │  │  ├─ GMT
│  │     │  │  ├─ GMT+0
│  │     │  │  ├─ GMT-0
│  │     │  │  ├─ GMT0
│  │     │  │  ├─ Greenwich
│  │     │  │  ├─ Hongkong
│  │     │  │  ├─ HST
│  │     │  │  ├─ Iceland
│  │     │  │  ├─ Indian
│  │     │  │  │  ├─ Antananarivo
│  │     │  │  │  ├─ Chagos
│  │     │  │  │  ├─ Christmas
│  │     │  │  │  ├─ Cocos
│  │     │  │  │  ├─ Comoro
│  │     │  │  │  ├─ Kerguelen
│  │     │  │  │  ├─ Mahe
│  │     │  │  │  ├─ Maldives
│  │     │  │  │  ├─ Mauritius
│  │     │  │  │  ├─ Mayotte
│  │     │  │  │  └─ Reunion
│  │     │  │  ├─ Iran
│  │     │  │  ├─ iso3166.tab
│  │     │  │  ├─ Israel
│  │     │  │  ├─ Jamaica
│  │     │  │  ├─ Japan
│  │     │  │  ├─ Kwajalein
│  │     │  │  ├─ leapseconds
│  │     │  │  ├─ Libya
│  │     │  │  ├─ MET
│  │     │  │  ├─ Mexico
│  │     │  │  │  ├─ BajaNorte
│  │     │  │  │  ├─ BajaSur
│  │     │  │  │  └─ General
│  │     │  │  ├─ MST
│  │     │  │  ├─ MST7MDT
│  │     │  │  ├─ Navajo
│  │     │  │  ├─ NZ
│  │     │  │  ├─ NZ-CHAT
│  │     │  │  ├─ Pacific
│  │     │  │  │  ├─ Apia
│  │     │  │  │  ├─ Auckland
│  │     │  │  │  ├─ Bougainville
│  │     │  │  │  ├─ Chatham
│  │     │  │  │  ├─ Chuuk
│  │     │  │  │  ├─ Easter
│  │     │  │  │  ├─ Efate
│  │     │  │  │  ├─ Enderbury
│  │     │  │  │  ├─ Fakaofo
│  │     │  │  │  ├─ Fiji
│  │     │  │  │  ├─ Funafuti
│  │     │  │  │  ├─ Galapagos
│  │     │  │  │  ├─ Gambier
│  │     │  │  │  ├─ Guadalcanal
│  │     │  │  │  ├─ Guam
│  │     │  │  │  ├─ Honolulu
│  │     │  │  │  ├─ Johnston
│  │     │  │  │  ├─ Kanton
│  │     │  │  │  ├─ Kiritimati
│  │     │  │  │  ├─ Kosrae
│  │     │  │  │  ├─ Kwajalein
│  │     │  │  │  ├─ Majuro
│  │     │  │  │  ├─ Marquesas
│  │     │  │  │  ├─ Midway
│  │     │  │  │  ├─ Nauru
│  │     │  │  │  ├─ Niue
│  │     │  │  │  ├─ Norfolk
│  │     │  │  │  ├─ Noumea
│  │     │  │  │  ├─ Pago_Pago
│  │     │  │  │  ├─ Palau
│  │     │  │  │  ├─ Pitcairn
│  │     │  │  │  ├─ Pohnpei
│  │     │  │  │  ├─ Ponape
│  │     │  │  │  ├─ Port_Moresby
│  │     │  │  │  ├─ Rarotonga
│  │     │  │  │  ├─ Saipan
│  │     │  │  │  ├─ Samoa
│  │     │  │  │  ├─ Tahiti
│  │     │  │  │  ├─ Tarawa
│  │     │  │  │  ├─ Tongatapu
│  │     │  │  │  ├─ Truk
│  │     │  │  │  ├─ Wake
│  │     │  │  │  ├─ Wallis
│  │     │  │  │  └─ Yap
│  │     │  │  ├─ Poland
│  │     │  │  ├─ Portugal
│  │     │  │  ├─ PRC
│  │     │  │  ├─ PST8PDT
│  │     │  │  ├─ ROC
│  │     │  │  ├─ ROK
│  │     │  │  ├─ Singapore
│  │     │  │  ├─ Turkey
│  │     │  │  ├─ tzdata.zi
│  │     │  │  ├─ UCT
│  │     │  │  ├─ Universal
│  │     │  │  ├─ US
│  │     │  │  │  ├─ Alaska
│  │     │  │  │  ├─ Aleutian
│  │     │  │  │  ├─ Arizona
│  │     │  │  │  ├─ Central
│  │     │  │  │  ├─ East-Indiana
│  │     │  │  │  ├─ Eastern
│  │     │  │  │  ├─ Hawaii
│  │     │  │  │  ├─ Indiana-Starke
│  │     │  │  │  ├─ Michigan
│  │     │  │  │  ├─ Mountain
│  │     │  │  │  ├─ Pacific
│  │     │  │  │  └─ Samoa
│  │     │  │  ├─ UTC
│  │     │  │  ├─ W-SU
│  │     │  │  ├─ WET
│  │     │  │  ├─ zone.tab
│  │     │  │  ├─ zone1970.tab
│  │     │  │  ├─ zonenow.tab
│  │     │  │  └─ Zulu
│  │     │  └─ __init__.py
│  │     ├─ pytz-2026.3.post1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  ├─ WHEEL
│  │     │  └─ zip-safe
│  │     ├─ pyyaml-6.0.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ referencing
│  │     │  ├─ exceptions.py
│  │     │  ├─ jsonschema.py
│  │     │  ├─ py.typed
│  │     │  ├─ retrieval.py
│  │     │  ├─ tests
│  │     │  │  ├─ test_core.py
│  │     │  │  ├─ test_exceptions.py
│  │     │  │  ├─ test_jsonschema.py
│  │     │  │  ├─ test_referencing_suite.py
│  │     │  │  ├─ test_retrieval.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ typing.py
│  │     │  ├─ _attrs.py
│  │     │  ├─ _attrs.pyi
│  │     │  ├─ _core.py
│  │     │  └─ __init__.py
│  │     ├─ referencing-0.37.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ COPYING
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ requests
│  │     │  ├─ adapters.py
│  │     │  ├─ api.py
│  │     │  ├─ auth.py
│  │     │  ├─ certs.py
│  │     │  ├─ compat.py
│  │     │  ├─ cookies.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ help.py
│  │     │  ├─ hooks.py
│  │     │  ├─ models.py
│  │     │  ├─ packages.py
│  │     │  ├─ py.typed
│  │     │  ├─ sessions.py
│  │     │  ├─ status_codes.py
│  │     │  ├─ structures.py
│  │     │  ├─ utils.py
│  │     │  ├─ _internal_utils.py
│  │     │  ├─ _types.py
│  │     │  ├─ __init__.py
│  │     │  └─ __version__.py
│  │     ├─ requests-2.34.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  ├─ LICENSE
│  │     │  │  └─ NOTICE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ rpds
│  │     │  ├─ py.typed
│  │     │  ├─ rpds.cp313-win_amd64.pyd
│  │     │  ├─ __init__.py
│  │     │  └─ __init__.pyi
│  │     ├─ rpds_py-2026.6.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ sboms
│  │     │  │  └─ rpds-py.cyclonedx.json
│  │     │  └─ WHEEL
│  │     ├─ six-1.17.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ six.py
│  │     ├─ soupsieve
│  │     │  ├─ css_match.py
│  │     │  ├─ css_parser.py
│  │     │  ├─ css_types.py
│  │     │  ├─ pretty.py
│  │     │  ├─ py.typed
│  │     │  ├─ util.py
│  │     │  ├─ __init__.py
│  │     │  └─ __meta__.py
│  │     ├─ soupsieve-2.9.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.md
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ sqlalchemy
│  │     │  ├─ connectors
│  │     │  │  ├─ aioodbc.py
│  │     │  │  ├─ asyncio.py
│  │     │  │  ├─ pyodbc.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ cyextension
│  │     │  │  ├─ collections.cp313-win_amd64.pyd
│  │     │  │  ├─ collections.pyx
│  │     │  │  ├─ immutabledict.cp313-win_amd64.pyd
│  │     │  │  ├─ immutabledict.pxd
│  │     │  │  ├─ immutabledict.pyx
│  │     │  │  ├─ processors.cp313-win_amd64.pyd
│  │     │  │  ├─ processors.pyx
│  │     │  │  ├─ resultproxy.cp313-win_amd64.pyd
│  │     │  │  ├─ resultproxy.pyx
│  │     │  │  ├─ util.cp313-win_amd64.pyd
│  │     │  │  ├─ util.pyx
│  │     │  │  └─ __init__.py
│  │     │  ├─ dialects
│  │     │  │  ├─ mssql
│  │     │  │  │  ├─ aioodbc.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ information_schema.py
│  │     │  │  │  ├─ json.py
│  │     │  │  │  ├─ provision.py
│  │     │  │  │  ├─ pymssql.py
│  │     │  │  │  ├─ pyodbc.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ mysql
│  │     │  │  │  ├─ aiomysql.py
│  │     │  │  │  ├─ asyncmy.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ cymysql.py
│  │     │  │  │  ├─ dml.py
│  │     │  │  │  ├─ enumerated.py
│  │     │  │  │  ├─ expression.py
│  │     │  │  │  ├─ json.py
│  │     │  │  │  ├─ mariadb.py
│  │     │  │  │  ├─ mariadbconnector.py
│  │     │  │  │  ├─ mysqlconnector.py
│  │     │  │  │  ├─ mysqldb.py
│  │     │  │  │  ├─ provision.py
│  │     │  │  │  ├─ pymysql.py
│  │     │  │  │  ├─ pyodbc.py
│  │     │  │  │  ├─ reflection.py
│  │     │  │  │  ├─ reserved_words.py
│  │     │  │  │  ├─ types.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ oracle
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ cx_oracle.py
│  │     │  │  │  ├─ dictionary.py
│  │     │  │  │  ├─ oracledb.py
│  │     │  │  │  ├─ provision.py
│  │     │  │  │  ├─ types.py
│  │     │  │  │  ├─ vector.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ postgresql
│  │     │  │  │  ├─ array.py
│  │     │  │  │  ├─ asyncpg.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ dml.py
│  │     │  │  │  ├─ ext.py
│  │     │  │  │  ├─ hstore.py
│  │     │  │  │  ├─ json.py
│  │     │  │  │  ├─ named_types.py
│  │     │  │  │  ├─ operators.py
│  │     │  │  │  ├─ pg8000.py
│  │     │  │  │  ├─ pg_catalog.py
│  │     │  │  │  ├─ provision.py
│  │     │  │  │  ├─ psycopg.py
│  │     │  │  │  ├─ psycopg2.py
│  │     │  │  │  ├─ psycopg2cffi.py
│  │     │  │  │  ├─ ranges.py
│  │     │  │  │  ├─ types.py
│  │     │  │  │  ├─ _psycopg_common.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ sqlite
│  │     │  │  │  ├─ aiosqlite.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ dml.py
│  │     │  │  │  ├─ json.py
│  │     │  │  │  ├─ provision.py
│  │     │  │  │  ├─ pysqlcipher.py
│  │     │  │  │  ├─ pysqlite.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ type_migration_guidelines.txt
│  │     │  │  ├─ _typing.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ engine
│  │     │  │  ├─ base.py
│  │     │  │  ├─ characteristics.py
│  │     │  │  ├─ create.py
│  │     │  │  ├─ cursor.py
│  │     │  │  ├─ default.py
│  │     │  │  ├─ events.py
│  │     │  │  ├─ interfaces.py
│  │     │  │  ├─ mock.py
│  │     │  │  ├─ processors.py
│  │     │  │  ├─ reflection.py
│  │     │  │  ├─ result.py
│  │     │  │  ├─ row.py
│  │     │  │  ├─ strategies.py
│  │     │  │  ├─ url.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ _py_processors.py
│  │     │  │  ├─ _py_row.py
│  │     │  │  ├─ _py_util.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ event
│  │     │  │  ├─ api.py
│  │     │  │  ├─ attr.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ legacy.py
│  │     │  │  ├─ registry.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ events.py
│  │     │  ├─ exc.py
│  │     │  ├─ ext
│  │     │  │  ├─ associationproxy.py
│  │     │  │  ├─ asyncio
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ engine.py
│  │     │  │  │  ├─ exc.py
│  │     │  │  │  ├─ result.py
│  │     │  │  │  ├─ scoping.py
│  │     │  │  │  ├─ session.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ automap.py
│  │     │  │  ├─ baked.py
│  │     │  │  ├─ compiler.py
│  │     │  │  ├─ declarative
│  │     │  │  │  ├─ extensions.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ horizontal_shard.py
│  │     │  │  ├─ hybrid.py
│  │     │  │  ├─ indexable.py
│  │     │  │  ├─ instrumentation.py
│  │     │  │  ├─ mutable.py
│  │     │  │  ├─ mypy
│  │     │  │  │  ├─ apply.py
│  │     │  │  │  ├─ decl_class.py
│  │     │  │  │  ├─ infer.py
│  │     │  │  │  ├─ names.py
│  │     │  │  │  ├─ plugin.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ orderinglist.py
│  │     │  │  ├─ serializer.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ future
│  │     │  │  ├─ engine.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ inspection.py
│  │     │  ├─ log.py
│  │     │  ├─ orm
│  │     │  │  ├─ attributes.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ bulk_persistence.py
│  │     │  │  ├─ clsregistry.py
│  │     │  │  ├─ collections.py
│  │     │  │  ├─ context.py
│  │     │  │  ├─ decl_api.py
│  │     │  │  ├─ decl_base.py
│  │     │  │  ├─ dependency.py
│  │     │  │  ├─ descriptor_props.py
│  │     │  │  ├─ dynamic.py
│  │     │  │  ├─ evaluator.py
│  │     │  │  ├─ events.py
│  │     │  │  ├─ exc.py
│  │     │  │  ├─ identity.py
│  │     │  │  ├─ instrumentation.py
│  │     │  │  ├─ interfaces.py
│  │     │  │  ├─ loading.py
│  │     │  │  ├─ mapped_collection.py
│  │     │  │  ├─ mapper.py
│  │     │  │  ├─ path_registry.py
│  │     │  │  ├─ persistence.py
│  │     │  │  ├─ properties.py
│  │     │  │  ├─ query.py
│  │     │  │  ├─ relationships.py
│  │     │  │  ├─ scoping.py
│  │     │  │  ├─ session.py
│  │     │  │  ├─ state.py
│  │     │  │  ├─ state_changes.py
│  │     │  │  ├─ strategies.py
│  │     │  │  ├─ strategy_options.py
│  │     │  │  ├─ sync.py
│  │     │  │  ├─ unitofwork.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ writeonly.py
│  │     │  │  ├─ _orm_constructors.py
│  │     │  │  ├─ _typing.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ pool
│  │     │  │  ├─ base.py
│  │     │  │  ├─ events.py
│  │     │  │  ├─ impl.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ py.typed
│  │     │  ├─ schema.py
│  │     │  ├─ sql
│  │     │  │  ├─ annotation.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ cache_key.py
│  │     │  │  ├─ coercions.py
│  │     │  │  ├─ compiler.py
│  │     │  │  ├─ crud.py
│  │     │  │  ├─ ddl.py
│  │     │  │  ├─ default_comparator.py
│  │     │  │  ├─ dml.py
│  │     │  │  ├─ elements.py
│  │     │  │  ├─ events.py
│  │     │  │  ├─ expression.py
│  │     │  │  ├─ functions.py
│  │     │  │  ├─ lambdas.py
│  │     │  │  ├─ naming.py
│  │     │  │  ├─ operators.py
│  │     │  │  ├─ roles.py
│  │     │  │  ├─ schema.py
│  │     │  │  ├─ selectable.py
│  │     │  │  ├─ sqltypes.py
│  │     │  │  ├─ traversals.py
│  │     │  │  ├─ type_api.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ visitors.py
│  │     │  │  ├─ _dml_constructors.py
│  │     │  │  ├─ _elements_constructors.py
│  │     │  │  ├─ _orm_types.py
│  │     │  │  ├─ _py_util.py
│  │     │  │  ├─ _selectable_constructors.py
│  │     │  │  ├─ _typing.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ testing
│  │     │  │  ├─ assertions.py
│  │     │  │  ├─ assertsql.py
│  │     │  │  ├─ asyncio.py
│  │     │  │  ├─ config.py
│  │     │  │  ├─ engines.py
│  │     │  │  ├─ entities.py
│  │     │  │  ├─ exclusions.py
│  │     │  │  ├─ fixtures
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ mypy.py
│  │     │  │  │  ├─ orm.py
│  │     │  │  │  ├─ sql.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ pickleable.py
│  │     │  │  ├─ plugin
│  │     │  │  │  ├─ bootstrap.py
│  │     │  │  │  ├─ plugin_base.py
│  │     │  │  │  ├─ pytestplugin.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ profiling.py
│  │     │  │  ├─ provision.py
│  │     │  │  ├─ requirements.py
│  │     │  │  ├─ schema.py
│  │     │  │  ├─ suite
│  │     │  │  │  ├─ test_cte.py
│  │     │  │  │  ├─ test_ddl.py
│  │     │  │  │  ├─ test_deprecations.py
│  │     │  │  │  ├─ test_dialect.py
│  │     │  │  │  ├─ test_insert.py
│  │     │  │  │  ├─ test_reflection.py
│  │     │  │  │  ├─ test_results.py
│  │     │  │  │  ├─ test_rowcount.py
│  │     │  │  │  ├─ test_select.py
│  │     │  │  │  ├─ test_sequence.py
│  │     │  │  │  ├─ test_types.py
│  │     │  │  │  ├─ test_unicode_ddl.py
│  │     │  │  │  ├─ test_update_delete.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ warnings.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ types.py
│  │     │  ├─ util
│  │     │  │  ├─ compat.py
│  │     │  │  ├─ concurrency.py
│  │     │  │  ├─ deprecations.py
│  │     │  │  ├─ langhelpers.py
│  │     │  │  ├─ preloaded.py
│  │     │  │  ├─ queue.py
│  │     │  │  ├─ tool_support.py
│  │     │  │  ├─ topological.py
│  │     │  │  ├─ typing.py
│  │     │  │  ├─ _collections.py
│  │     │  │  ├─ _concurrency_py3k.py
│  │     │  │  ├─ _has_cy.py
│  │     │  │  ├─ _py_collections.py
│  │     │  │  └─ __init__.py
│  │     │  └─ __init__.py
│  │     ├─ sqlalchemy-2.0.51.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ starlette
│  │     │  ├─ applications.py
│  │     │  ├─ authentication.py
│  │     │  ├─ background.py
│  │     │  ├─ concurrency.py
│  │     │  ├─ config.py
│  │     │  ├─ convertors.py
│  │     │  ├─ datastructures.py
│  │     │  ├─ endpoints.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ formparsers.py
│  │     │  ├─ middleware
│  │     │  │  ├─ authentication.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ cors.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ gzip.py
│  │     │  │  ├─ httpsredirect.py
│  │     │  │  ├─ sessions.py
│  │     │  │  ├─ trustedhost.py
│  │     │  │  ├─ wsgi.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ py.typed
│  │     │  ├─ requests.py
│  │     │  ├─ responses.py
│  │     │  ├─ routing.py
│  │     │  ├─ schemas.py
│  │     │  ├─ staticfiles.py
│  │     │  ├─ status.py
│  │     │  ├─ templating.py
│  │     │  ├─ testclient.py
│  │     │  ├─ types.py
│  │     │  ├─ websockets.py
│  │     │  ├─ _exception_handler.py
│  │     │  ├─ _utils.py
│  │     │  └─ __init__.py
│  │     ├─ starlette-1.3.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.md
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ stockmind-1.0.0.dist-info
│  │     │  ├─ direct_url.json
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ streamlit
│  │     │  ├─ .agents
│  │     │  │  ├─ meta-skill
│  │     │  │  │  └─ developing-with-streamlit
│  │     │  │  │     ├─ scripts
│  │     │  │  │     │  └─ discover.py
│  │     │  │  │     └─ SKILL.md
│  │     │  │  └─ skills
│  │     │  │     └─ developing-with-streamlit
│  │     │  │        ├─ assets
│  │     │  │        │  └─ templates
│  │     │  │        │     ├─ apps
│  │     │  │        │     │  ├─ dashboard-companies
│  │     │  │        │     │  │  ├─ pyproject.toml
│  │     │  │        │     │  │  └─ streamlit_app.py
│  │     │  │        │     │  ├─ dashboard-compute
│  │     │  │        │     │  │  ├─ pyproject.toml
│  │     │  │        │     │  │  └─ streamlit_app.py
│  │     │  │        │     │  ├─ dashboard-feature-usage
│  │     │  │        │     │  │  ├─ pyproject.toml
│  │     │  │        │     │  │  └─ streamlit_app.py
│  │     │  │        │     │  ├─ dashboard-metrics
│  │     │  │        │     │  │  ├─ pyproject.toml
│  │     │  │        │     │  │  └─ streamlit_app.py
│  │     │  │        │     │  ├─ dashboard-seattle-weather
│  │     │  │        │     │  │  ├─ pyproject.toml
│  │     │  │        │     │  │  └─ streamlit_app.py
│  │     │  │        │     │  ├─ dashboard-stock-peers
│  │     │  │        │     │  │  ├─ pyproject.toml
│  │     │  │        │     │  │  └─ streamlit_app.py
│  │     │  │        │     │  └─ README.md
│  │     │  │        │     └─ themes
│  │     │  │        │        ├─ configs
│  │     │  │        │        │  ├─ dracula.toml
│  │     │  │        │        │  ├─ financial-dashboard.toml
│  │     │  │        │        │  ├─ fluent.toml
│  │     │  │        │        │  ├─ jupyter.toml
│  │     │  │        │        │  ├─ material-ui.toml
│  │     │  │        │        │  ├─ minimal.toml
│  │     │  │        │        │  ├─ nord.toml
│  │     │  │        │        │  ├─ one-dark-pro.toml
│  │     │  │        │        │  ├─ shadcn.toml
│  │     │  │        │        │  ├─ solarized-light.toml
│  │     │  │        │        │  ├─ ubuntu.toml
│  │     │  │        │        │  └─ vscode.toml
│  │     │  │        │        └─ README.md
│  │     │  │        ├─ references
│  │     │  │        │  ├─ api-reference.md
│  │     │  │        │  ├─ best-practices.md
│  │     │  │        │  ├─ ccv2-packaged-components.md
│  │     │  │        │  ├─ ccv2-state-sync.md
│  │     │  │        │  ├─ ccv2-theme-css-variables.md
│  │     │  │        │  ├─ ccv2-troubleshooting.md
│  │     │  │        │  ├─ chat-ui.md
│  │     │  │        │  ├─ cli.md
│  │     │  │        │  ├─ code-organization.md
│  │     │  │        │  ├─ custom-components-v2.md
│  │     │  │        │  ├─ dashboards.md
│  │     │  │        │  ├─ data-display.md
│  │     │  │        │  ├─ design.md
│  │     │  │        │  ├─ environment-setup.md
│  │     │  │        │  ├─ layouts.md
│  │     │  │        │  ├─ markdown.md
│  │     │  │        │  ├─ multipage-apps.md
│  │     │  │        │  ├─ performance.md
│  │     │  │        │  ├─ selection-widgets.md
│  │     │  │        │  ├─ server-asgi.md
│  │     │  │        │  ├─ session-state.md
│  │     │  │        │  ├─ snowflake-connection.md
│  │     │  │        │  ├─ theme.md
│  │     │  │        │  └─ third-party-components.md
│  │     │  │        └─ SKILL.md
│  │     │  ├─ auth_util.py
│  │     │  ├─ cli_util.py
│  │     │  ├─ column_config.py
│  │     │  ├─ commands
│  │     │  │  ├─ echo.py
│  │     │  │  ├─ execution_control.py
│  │     │  │  ├─ logo.py
│  │     │  │  ├─ navigation.py
│  │     │  │  ├─ page_config.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ components
│  │     │  │  ├─ lib
│  │     │  │  │  ├─ local_component_registry.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ types
│  │     │  │  │  ├─ base_component_registry.py
│  │     │  │  │  ├─ base_custom_component.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ v1
│  │     │  │  │  ├─ components.py
│  │     │  │  │  ├─ component_arrow.py
│  │     │  │  │  ├─ component_registry.py
│  │     │  │  │  ├─ custom_component.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ v2
│  │     │  │  │  ├─ bidi_component
│  │     │  │  │  │  ├─ constants.py
│  │     │  │  │  │  ├─ main.py
│  │     │  │  │  │  ├─ serialization.py
│  │     │  │  │  │  ├─ state.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ component_definition_resolver.py
│  │     │  │  │  ├─ component_file_watcher.py
│  │     │  │  │  ├─ component_manager.py
│  │     │  │  │  ├─ component_manifest_handler.py
│  │     │  │  │  ├─ component_path_utils.py
│  │     │  │  │  ├─ component_registry.py
│  │     │  │  │  ├─ get_bidi_component_manager.py
│  │     │  │  │  ├─ manifest_scanner.py
│  │     │  │  │  ├─ presentation.py
│  │     │  │  │  ├─ types.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ config.py
│  │     │  ├─ config_option.py
│  │     │  ├─ config_util.py
│  │     │  ├─ connections
│  │     │  │  ├─ base_connection.py
│  │     │  │  ├─ snowflake_connection.py
│  │     │  │  ├─ sql_connection.py
│  │     │  │  ├─ util.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ cursor.py
│  │     │  ├─ dataframe
│  │     │  │  ├─ lazy_df_adapters.py
│  │     │  │  ├─ lazy_df_source.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ dataframe_util.py
│  │     │  ├─ delta_generator.py
│  │     │  ├─ delta_generator_singletons.py
│  │     │  ├─ deprecation_util.py
│  │     │  ├─ development.py
│  │     │  ├─ elements
│  │     │  │  ├─ alert.py
│  │     │  │  ├─ arrow.py
│  │     │  │  ├─ balloons.py
│  │     │  │  ├─ bottom.py
│  │     │  │  ├─ code.py
│  │     │  │  ├─ deck_gl_json_chart.py
│  │     │  │  ├─ dialog_decorator.py
│  │     │  │  ├─ empty.py
│  │     │  │  ├─ exception.py
│  │     │  │  ├─ form.py
│  │     │  │  ├─ graphviz_chart.py
│  │     │  │  ├─ heading.py
│  │     │  │  ├─ help.py
│  │     │  │  ├─ html.py
│  │     │  │  ├─ iframe.py
│  │     │  │  ├─ image.py
│  │     │  │  ├─ json.py
│  │     │  │  ├─ layouts.py
│  │     │  │  ├─ lib
│  │     │  │  │  ├─ built_in_chart_utils.py
│  │     │  │  │  ├─ color_util.py
│  │     │  │  │  ├─ column_config_utils.py
│  │     │  │  │  ├─ column_types.py
│  │     │  │  │  ├─ dialog.py
│  │     │  │  │  ├─ dicttools.py
│  │     │  │  │  ├─ file_uploader_utils.py
│  │     │  │  │  ├─ form_utils.py
│  │     │  │  │  ├─ image_utils.py
│  │     │  │  │  ├─ js_number.py
│  │     │  │  │  ├─ layout_utils.py
│  │     │  │  │  ├─ mutable_expander_container.py
│  │     │  │  │  ├─ mutable_popover_container.py
│  │     │  │  │  ├─ mutable_status_container.py
│  │     │  │  │  ├─ mutable_tab_container.py
│  │     │  │  │  ├─ options_selector_utils.py
│  │     │  │  │  ├─ pandas_styler_utils.py
│  │     │  │  │  ├─ policies.py
│  │     │  │  │  ├─ shortcut_utils.py
│  │     │  │  │  ├─ skeleton_placeholder.py
│  │     │  │  │  ├─ streamlit_plotly_theme.py
│  │     │  │  │  ├─ subtitle_utils.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ map.py
│  │     │  │  ├─ markdown.py
│  │     │  │  ├─ media.py
│  │     │  │  ├─ mermaid_chart.py
│  │     │  │  ├─ metric.py
│  │     │  │  ├─ pdf.py
│  │     │  │  ├─ plotly_chart.py
│  │     │  │  ├─ progress.py
│  │     │  │  ├─ pyplot.py
│  │     │  │  ├─ skeleton.py
│  │     │  │  ├─ snow.py
│  │     │  │  ├─ space.py
│  │     │  │  ├─ spinner.py
│  │     │  │  ├─ table.py
│  │     │  │  ├─ text.py
│  │     │  │  ├─ toast.py
│  │     │  │  ├─ vega_charts.py
│  │     │  │  ├─ widgets
│  │     │  │  │  ├─ audio_input.py
│  │     │  │  │  ├─ button.py
│  │     │  │  │  ├─ button_group.py
│  │     │  │  │  ├─ camera_input.py
│  │     │  │  │  ├─ chat.py
│  │     │  │  │  ├─ checkbox.py
│  │     │  │  │  ├─ color_picker.py
│  │     │  │  │  ├─ data_editor.py
│  │     │  │  │  ├─ feedback.py
│  │     │  │  │  ├─ file_uploader.py
│  │     │  │  │  ├─ menu_button.py
│  │     │  │  │  ├─ multiselect.py
│  │     │  │  │  ├─ number_input.py
│  │     │  │  │  ├─ pagination.py
│  │     │  │  │  ├─ radio.py
│  │     │  │  │  ├─ selectbox.py
│  │     │  │  │  ├─ select_slider.py
│  │     │  │  │  ├─ slider.py
│  │     │  │  │  ├─ text_widgets.py
│  │     │  │  │  ├─ time_widgets.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ write.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ emojis.py
│  │     │  ├─ env_util.py
│  │     │  ├─ errors.py
│  │     │  ├─ error_util.py
│  │     │  ├─ file_util.py
│  │     │  ├─ git_util.py
│  │     │  ├─ hello
│  │     │  │  ├─ animation_demo.py
│  │     │  │  ├─ dataframe_demo.py
│  │     │  │  ├─ hello.py
│  │     │  │  ├─ mapping_demo.py
│  │     │  │  ├─ plotting_demo.py
│  │     │  │  ├─ streamlit_app.py
│  │     │  │  ├─ utils.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ logger.py
│  │     │  ├─ material_icon_names.py
│  │     │  ├─ navigation
│  │     │  │  ├─ page.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ net_util.py
│  │     │  ├─ path_security.py
│  │     │  ├─ platform.py
│  │     │  ├─ proto
│  │     │  │  ├─ Alert_pb2.py
│  │     │  │  ├─ Alert_pb2.pyi
│  │     │  │  ├─ AppPage_pb2.py
│  │     │  │  ├─ AppPage_pb2.pyi
│  │     │  │  ├─ ArrowData_pb2.py
│  │     │  │  ├─ ArrowData_pb2.pyi
│  │     │  │  ├─ ArrowNamedDataSet_pb2.py
│  │     │  │  ├─ ArrowNamedDataSet_pb2.pyi
│  │     │  │  ├─ AudioInput_pb2.py
│  │     │  │  ├─ AudioInput_pb2.pyi
│  │     │  │  ├─ Audio_pb2.py
│  │     │  │  ├─ Audio_pb2.pyi
│  │     │  │  ├─ AuthRedirect_pb2.py
│  │     │  │  ├─ AuthRedirect_pb2.pyi
│  │     │  │  ├─ AutoRerun_pb2.py
│  │     │  │  ├─ AutoRerun_pb2.pyi
│  │     │  │  ├─ BackMsg_pb2.py
│  │     │  │  ├─ BackMsg_pb2.pyi
│  │     │  │  ├─ Balloons_pb2.py
│  │     │  │  ├─ Balloons_pb2.pyi
│  │     │  │  ├─ BidiComponent_pb2.py
│  │     │  │  ├─ BidiComponent_pb2.pyi
│  │     │  │  ├─ Block_pb2.py
│  │     │  │  ├─ Block_pb2.pyi
│  │     │  │  ├─ ButtonGroup_pb2.py
│  │     │  │  ├─ ButtonGroup_pb2.pyi
│  │     │  │  ├─ ButtonLikeIconPosition_pb2.py
│  │     │  │  ├─ ButtonLikeIconPosition_pb2.pyi
│  │     │  │  ├─ Button_pb2.py
│  │     │  │  ├─ Button_pb2.pyi
│  │     │  │  ├─ CameraInput_pb2.py
│  │     │  │  ├─ CameraInput_pb2.pyi
│  │     │  │  ├─ ChatInput_pb2.py
│  │     │  │  ├─ ChatInput_pb2.pyi
│  │     │  │  ├─ Checkbox_pb2.py
│  │     │  │  ├─ Checkbox_pb2.pyi
│  │     │  │  ├─ ClientState_pb2.py
│  │     │  │  ├─ ClientState_pb2.pyi
│  │     │  │  ├─ Code_pb2.py
│  │     │  │  ├─ Code_pb2.pyi
│  │     │  │  ├─ ColorPicker_pb2.py
│  │     │  │  ├─ ColorPicker_pb2.pyi
│  │     │  │  ├─ Common_pb2.py
│  │     │  │  ├─ Common_pb2.pyi
│  │     │  │  ├─ Components_pb2.py
│  │     │  │  ├─ Components_pb2.pyi
│  │     │  │  ├─ Dataframe_pb2.py
│  │     │  │  ├─ Dataframe_pb2.pyi
│  │     │  │  ├─ DateInput_pb2.py
│  │     │  │  ├─ DateInput_pb2.pyi
│  │     │  │  ├─ DateTimeInput_pb2.py
│  │     │  │  ├─ DateTimeInput_pb2.pyi
│  │     │  │  ├─ DeckGlJsonChart_pb2.py
│  │     │  │  ├─ DeckGlJsonChart_pb2.pyi
│  │     │  │  ├─ Delta_pb2.py
│  │     │  │  ├─ Delta_pb2.pyi
│  │     │  │  ├─ DownloadButton_pb2.py
│  │     │  │  ├─ DownloadButton_pb2.pyi
│  │     │  │  ├─ Element_pb2.py
│  │     │  │  ├─ Element_pb2.pyi
│  │     │  │  ├─ Empty_pb2.py
│  │     │  │  ├─ Empty_pb2.pyi
│  │     │  │  ├─ Exception_pb2.py
│  │     │  │  ├─ Exception_pb2.pyi
│  │     │  │  ├─ Favicon_pb2.py
│  │     │  │  ├─ Favicon_pb2.pyi
│  │     │  │  ├─ Feedback_pb2.py
│  │     │  │  ├─ Feedback_pb2.pyi
│  │     │  │  ├─ FileUploader_pb2.py
│  │     │  │  ├─ FileUploader_pb2.pyi
│  │     │  │  ├─ ForwardMsg_pb2.py
│  │     │  │  ├─ ForwardMsg_pb2.pyi
│  │     │  │  ├─ GapSize_pb2.py
│  │     │  │  ├─ GapSize_pb2.pyi
│  │     │  │  ├─ GitInfo_pb2.py
│  │     │  │  ├─ GitInfo_pb2.pyi
│  │     │  │  ├─ GraphVizChart_pb2.py
│  │     │  │  ├─ GraphVizChart_pb2.pyi
│  │     │  │  ├─ Heading_pb2.py
│  │     │  │  ├─ Heading_pb2.pyi
│  │     │  │  ├─ HeightConfig_pb2.py
│  │     │  │  ├─ HeightConfig_pb2.pyi
│  │     │  │  ├─ Help_pb2.py
│  │     │  │  ├─ Help_pb2.pyi
│  │     │  │  ├─ Html_pb2.py
│  │     │  │  ├─ Html_pb2.pyi
│  │     │  │  ├─ IFrame_pb2.py
│  │     │  │  ├─ IFrame_pb2.pyi
│  │     │  │  ├─ Image_pb2.py
│  │     │  │  ├─ Image_pb2.pyi
│  │     │  │  ├─ Json_pb2.py
│  │     │  │  ├─ Json_pb2.pyi
│  │     │  │  ├─ LabelVisibility_pb2.py
│  │     │  │  ├─ LabelVisibility_pb2.pyi
│  │     │  │  ├─ LinkButton_pb2.py
│  │     │  │  ├─ LinkButton_pb2.pyi
│  │     │  │  ├─ Logo_pb2.py
│  │     │  │  ├─ Logo_pb2.pyi
│  │     │  │  ├─ Markdown_pb2.py
│  │     │  │  ├─ Markdown_pb2.pyi
│  │     │  │  ├─ MenuButton_pb2.py
│  │     │  │  ├─ MenuButton_pb2.pyi
│  │     │  │  ├─ MetricsEvent_pb2.py
│  │     │  │  ├─ MetricsEvent_pb2.pyi
│  │     │  │  ├─ Metric_pb2.py
│  │     │  │  ├─ Metric_pb2.pyi
│  │     │  │  ├─ MultiSelect_pb2.py
│  │     │  │  ├─ MultiSelect_pb2.pyi
│  │     │  │  ├─ Navigation_pb2.py
│  │     │  │  ├─ Navigation_pb2.pyi
│  │     │  │  ├─ NewSession_pb2.py
│  │     │  │  ├─ NewSession_pb2.pyi
│  │     │  │  ├─ NumberInput_pb2.py
│  │     │  │  ├─ NumberInput_pb2.pyi
│  │     │  │  ├─ openmetrics_data_model_pb2.py
│  │     │  │  ├─ openmetrics_data_model_pb2.pyi
│  │     │  │  ├─ PageConfig_pb2.py
│  │     │  │  ├─ PageConfig_pb2.pyi
│  │     │  │  ├─ PageInfo_pb2.py
│  │     │  │  ├─ PageInfo_pb2.pyi
│  │     │  │  ├─ PageLink_pb2.py
│  │     │  │  ├─ PageLink_pb2.pyi
│  │     │  │  ├─ PageNotFound_pb2.py
│  │     │  │  ├─ PageNotFound_pb2.pyi
│  │     │  │  ├─ PageProfile_pb2.py
│  │     │  │  ├─ PageProfile_pb2.pyi
│  │     │  │  ├─ Pagination_pb2.py
│  │     │  │  ├─ Pagination_pb2.pyi
│  │     │  │  ├─ ParentMessage_pb2.py
│  │     │  │  ├─ ParentMessage_pb2.pyi
│  │     │  │  ├─ PlotlyChart_pb2.py
│  │     │  │  ├─ PlotlyChart_pb2.pyi
│  │     │  │  ├─ Progress_pb2.py
│  │     │  │  ├─ Progress_pb2.pyi
│  │     │  │  ├─ Radio_pb2.py
│  │     │  │  ├─ Radio_pb2.pyi
│  │     │  │  ├─ RootContainer_pb2.py
│  │     │  │  ├─ RootContainer_pb2.pyi
│  │     │  │  ├─ Selectbox_pb2.py
│  │     │  │  ├─ Selectbox_pb2.pyi
│  │     │  │  ├─ SelectWidgetFilterMode_pb2.py
│  │     │  │  ├─ SelectWidgetFilterMode_pb2.pyi
│  │     │  │  ├─ SessionEvent_pb2.py
│  │     │  │  ├─ SessionEvent_pb2.pyi
│  │     │  │  ├─ SessionStatus_pb2.py
│  │     │  │  ├─ SessionStatus_pb2.pyi
│  │     │  │  ├─ Skeleton_pb2.py
│  │     │  │  ├─ Skeleton_pb2.pyi
│  │     │  │  ├─ Slider_pb2.py
│  │     │  │  ├─ Slider_pb2.pyi
│  │     │  │  ├─ Snow_pb2.py
│  │     │  │  ├─ Snow_pb2.pyi
│  │     │  │  ├─ Space_pb2.py
│  │     │  │  ├─ Space_pb2.pyi
│  │     │  │  ├─ Spinner_pb2.py
│  │     │  │  ├─ Spinner_pb2.pyi
│  │     │  │  ├─ Table_pb2.py
│  │     │  │  ├─ Table_pb2.pyi
│  │     │  │  ├─ TextAlignmentConfig_pb2.py
│  │     │  │  ├─ TextAlignmentConfig_pb2.pyi
│  │     │  │  ├─ TextArea_pb2.py
│  │     │  │  ├─ TextArea_pb2.pyi
│  │     │  │  ├─ TextInput_pb2.py
│  │     │  │  ├─ TextInput_pb2.pyi
│  │     │  │  ├─ Text_pb2.py
│  │     │  │  ├─ Text_pb2.pyi
│  │     │  │  ├─ TimeInput_pb2.py
│  │     │  │  ├─ TimeInput_pb2.pyi
│  │     │  │  ├─ Toast_pb2.py
│  │     │  │  ├─ Toast_pb2.pyi
│  │     │  │  ├─ Transient_pb2.py
│  │     │  │  ├─ Transient_pb2.pyi
│  │     │  │  ├─ VegaLiteChart_pb2.py
│  │     │  │  ├─ VegaLiteChart_pb2.pyi
│  │     │  │  ├─ Video_pb2.py
│  │     │  │  ├─ Video_pb2.pyi
│  │     │  │  ├─ WidgetStates_pb2.py
│  │     │  │  ├─ WidgetStates_pb2.pyi
│  │     │  │  ├─ WidthConfig_pb2.py
│  │     │  │  ├─ WidthConfig_pb2.pyi
│  │     │  │  └─ __init__.py
│  │     │  ├─ py.typed
│  │     │  ├─ runtime
│  │     │  │  ├─ app_session.py
│  │     │  │  ├─ backend_operation_handler.py
│  │     │  │  ├─ caching
│  │     │  │  │  ├─ cached_message_replay.py
│  │     │  │  │  ├─ cache_background_refresh.py
│  │     │  │  │  ├─ cache_data_api.py
│  │     │  │  │  ├─ cache_errors.py
│  │     │  │  │  ├─ cache_resource_api.py
│  │     │  │  │  ├─ cache_type.py
│  │     │  │  │  ├─ cache_utils.py
│  │     │  │  │  ├─ hashing.py
│  │     │  │  │  ├─ legacy_cache_api.py
│  │     │  │  │  ├─ storage
│  │     │  │  │  │  ├─ cache_storage_protocol.py
│  │     │  │  │  │  ├─ dummy_cache_storage.py
│  │     │  │  │  │  ├─ in_memory_cache_storage_wrapper.py
│  │     │  │  │  │  ├─ local_disk_cache_storage.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ ttl_cache.py
│  │     │  │  │  ├─ ttl_cleanup_cache.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ connection_factory.py
│  │     │  │  ├─ context.py
│  │     │  │  ├─ context_util.py
│  │     │  │  ├─ credentials.py
│  │     │  │  ├─ dataframe_chunk_handler.py
│  │     │  │  ├─ dataframe_source_manager.py
│  │     │  │  ├─ download_data_util.py
│  │     │  │  ├─ forward_msg_cache.py
│  │     │  │  ├─ forward_msg_queue.py
│  │     │  │  ├─ fragment.py
│  │     │  │  ├─ media_file_manager.py
│  │     │  │  ├─ media_file_storage.py
│  │     │  │  ├─ memory_media_file_storage.py
│  │     │  │  ├─ memory_session_storage.py
│  │     │  │  ├─ memory_uploaded_file_manager.py
│  │     │  │  ├─ metrics_util.py
│  │     │  │  ├─ outside_container_wrapper.py
│  │     │  │  ├─ pages_manager.py
│  │     │  │  ├─ parallel_coordinator.py
│  │     │  │  ├─ runtime.py
│  │     │  │  ├─ runtime_util.py
│  │     │  │  ├─ scriptrunner
│  │     │  │  │  ├─ exec_code.py
│  │     │  │  │  ├─ magic.py
│  │     │  │  │  ├─ magic_funcs.py
│  │     │  │  │  ├─ script_cache.py
│  │     │  │  │  ├─ script_runner.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ scriptrunner_utils
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ script_requests.py
│  │     │  │  │  ├─ script_run_context.py
│  │     │  │  │  ├─ script_run_context_attr.py
│  │     │  │  │  ├─ shared_run_state.py
│  │     │  │  │  ├─ thread_safe_set.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ script_data.py
│  │     │  │  ├─ secrets.py
│  │     │  │  ├─ session_manager.py
│  │     │  │  ├─ state
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ presentation.py
│  │     │  │  │  ├─ query_params.py
│  │     │  │  │  ├─ query_params_proxy.py
│  │     │  │  │  ├─ safe_session_state.py
│  │     │  │  │  ├─ session_state.py
│  │     │  │  │  ├─ session_state_proxy.py
│  │     │  │  │  ├─ widgets.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ stats.py
│  │     │  │  ├─ theme_util.py
│  │     │  │  ├─ uploaded_file_manager.py
│  │     │  │  ├─ websocket_session_manager.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ source_util.py
│  │     │  ├─ starlette.py
│  │     │  ├─ static
│  │     │  │  ├─ favicon.png
│  │     │  │  ├─ index.html
│  │     │  │  ├─ manifest.json
│  │     │  │  └─ static
│  │     │  │     ├─ css
│  │     │  │     │  ├─ DataFrame.DUkanX9_.css
│  │     │  │     │  ├─ DeckGlJsonChart.s6LXjV0D.css
│  │     │  │     │  ├─ index.BV-e9Edq.css
│  │     │  │     │  └─ katex.CAfVENUR.css
│  │     │  │     ├─ js
│  │     │  │     │  ├─ abnfDiagram-VRR7QNED.DMhlflzA.js
│  │     │  │     │  ├─ AlertElement.i0agV2UI.js
│  │     │  │     │  ├─ arc.Bz4qkNTB.js
│  │     │  │     │  ├─ architecture-TIHT7OUA.DnieQxxl.js
│  │     │  │     │  ├─ architectureDiagram-ZJ3FMSHR.DlLEMMhu.js
│  │     │  │     │  ├─ array.BifhSqXX.js
│  │     │  │     │  ├─ ArrowVegaLiteChart.Cngr-5AU.js
│  │     │  │     │  ├─ Audio.CYLCaCCx.js
│  │     │  │     │  ├─ AudioInput.B7yR5q6u.js
│  │     │  │     │  ├─ Autocomplete.D9k6mFCZ.js
│  │     │  │     │  ├─ axios.C1kCDFiR.js
│  │     │  │     │  ├─ BackendOperationContext.DtKBGW8l.js
│  │     │  │     │  ├─ Balloons.Bv-BEXxS.js
│  │     │  │     │  ├─ BaseButton.CD99a2NM.js
│  │     │  │     │  ├─ BaseButtonTooltip.9ZCtkLEj.js
│  │     │  │     │  ├─ BidiComponent.BidSrM61.js
│  │     │  │     │  ├─ blockDiagram-677ZJIJ3.B2-6iYNg.js
│  │     │  │     │  ├─ Button.BC22NNrF.js
│  │     │  │     │  ├─ ButtonGroup.DMpjOF8Q.js
│  │     │  │     │  ├─ c4Diagram-LMCZKHZV.DG-8rZ3_.js
│  │     │  │     │  ├─ CameraInput.BXqRVIxA.js
│  │     │  │     │  ├─ Cancel.esm.u6bQjtwJ.js
│  │     │  │     │  ├─ channel.CsxEH82A.js
│  │     │  │     │  ├─ ChatInput.i8I7Hpx0.js
│  │     │  │     │  ├─ Check.esm.zcEyHW0S.js
│  │     │  │     │  ├─ Checkbox.BpBCkAOl.js
│  │     │  │     │  ├─ chunk-2Q5K7J3B.BsaEqoYJ.js
│  │     │  │     │  ├─ chunk-32BRIVSS.CRML9a9R.js
│  │     │  │     │  ├─ chunk-52WLFC77.CL_Wd-B6.js
│  │     │  │     │  ├─ chunk-5FCAYU7R.C_m-TPOx.js
│  │     │  │     │  ├─ chunk-5HE753X5.D2IwY2Hs.js
│  │     │  │     │  ├─ chunk-5JV3BV7I.DJesgnfK.js
│  │     │  │     │  ├─ chunk-5TONJI2A.CazhSWpT.js
│  │     │  │     │  ├─ chunk-5VM5RSS4.TOl2eSYi.js
│  │     │  │     │  ├─ chunk-7BUUIJ7U.CAhmNhj7.js
│  │     │  │     │  ├─ chunk-BIQX33UG.B4NE4TKF.js
│  │     │  │     │  ├─ chunk-C7G6YPKG.EaPayahY.js
│  │     │  │     │  ├─ chunk-CQNSW5MT.CwsHPlpw.js
│  │     │  │     │  ├─ chunk-CYSBUYHQ.Bo3-8CRa.js
│  │     │  │     │  ├─ chunk-EMLP6XTP.B17sZ-5U.js
│  │     │  │     │  ├─ chunk-EX3LRPZG.DDePe_PC.js
│  │     │  │     │  ├─ chunk-FWX5IMBZ.BYCJDOX7.js
│  │     │  │     │  ├─ chunk-HOUHSVGY.zNH8MoI9.js
│  │     │  │     │  ├─ chunk-ICXQ74PX.CwBrFo8s.js
│  │     │  │     │  ├─ chunk-JG7HCLWE.2vZbAraA.js
│  │     │  │     │  ├─ chunk-JWPE2WC7.A3RzWITa.js
│  │     │  │     │  ├─ chunk-KEIR6QF5.Dj-OpFgW.js
│  │     │  │     │  ├─ chunk-MOJQB5TN.B4REpjLl.js
│  │     │  │     │  ├─ chunk-MOZMSUNE.EeATBuYk.js
│  │     │  │     │  ├─ chunk-OGEWGWER.BQmEmpLE.js
│  │     │  │     │  ├─ chunk-OSBZ3O6U._N6nOv0n.js
│  │     │  │     │  ├─ chunk-PUDLZKDR.w4xt0Cvo.js
│  │     │  │     │  ├─ chunk-Q4XR5HBZ.DWR7wB4i.js
│  │     │  │     │  ├─ chunk-QBLGF6JB.DFvVIIOP.js
│  │     │  │     │  ├─ chunk-R7FJI6CG.DpWbzOcb.js
│  │     │  │     │  ├─ chunk-RYQCIY6F.DGrj5mu1.js
│  │     │  │     │  ├─ chunk-U6XO7XAA.t2Sk_D5L.js
│  │     │  │     │  ├─ chunk-V7JOEXUC.C_6FH6Q4.js
│  │     │  │     │  ├─ chunk-VAUOI2AC.BOaFDBFv.js
│  │     │  │     │  ├─ chunk-VR4S4FIN.DMqg5-Rg.js
│  │     │  │     │  ├─ chunk-WYO6CB5R.-gOV9D83.js
│  │     │  │     │  ├─ chunk-XXDRQBXY.BLiu-513.js
│  │     │  │     │  ├─ chunk-Y2CYZVJY.DsF7k-Jl.js
│  │     │  │     │  ├─ chunk-YOTPTUD7.CQZR6t9a.js
│  │     │  │     │  ├─ chunk-ZGVPDNZ5.GnXVbPyR.js
│  │     │  │     │  ├─ chunk-ZIRB5QZD.Dh20_f-h.js
│  │     │  │     │  ├─ classDiagram-OUVF2IWQ.BJTiMXo3.js
│  │     │  │     │  ├─ classDiagram-v2-EOCWNBFH.BJTiMXo3.js
│  │     │  │     │  ├─ classnames.B69Vzagp.js
│  │     │  │     │  ├─ click-outside-container.Ci0KWfiz.js
│  │     │  │     │  ├─ Close.esm.Jh632nmX.js
│  │     │  │     │  ├─ Close.esm.yVhoscAL.js
│  │     │  │     │  ├─ CodeBlockCopyToolbar.BpnuDZwR.js
│  │     │  │     │  ├─ ColorPicker.1-I26kS7.js
│  │     │  │     │  ├─ colors.Cg5Vh3br.js
│  │     │  │     │  ├─ ComponentInstance.DLjCEukq.js
│  │     │  │     │  ├─ config.Mbx-WYSj.js
│  │     │  │     │  ├─ ContentCopy.esm.CIsNWqfQ.js
│  │     │  │     │  ├─ cose-bilkent-JH36ORCC.B9LMTLkO.js
│  │     │  │     │  ├─ createDownloadLinkElement.DlKYa9YF.js
│  │     │  │     │  ├─ cynefin-VYW2F7L2.B0m8xIX_.js
│  │     │  │     │  ├─ cynefinDiagram-TSTJHNR4.CEu5Q_f3.js
│  │     │  │     │  ├─ cytoscape.esm.CQFVGiJu.js
│  │     │  │     │  ├─ dagre-VKFMJZFB.BSl4AQRW.js
│  │     │  │     │  ├─ dagre.CM5tl9jL.js
│  │     │  │     │  ├─ data-grid-overlay-editor.D7vhZ-4A.js
│  │     │  │     │  ├─ DataFrame.v-5GXvjU.js
│  │     │  │     │  ├─ DateInput.BXvTEfuB.js
│  │     │  │     │  ├─ DateTimeInput.DfmEMzud.js
│  │     │  │     │  ├─ DeckGlJsonChart.BVVXhfes.js
│  │     │  │     │  ├─ defaultLocale.DMW9ha0y.js
│  │     │  │     │  ├─ Delete.esm.iVbYVWqI.js
│  │     │  │     │  ├─ diagram-FQU43EPY.BE7tAPvI.js
│  │     │  │     │  ├─ diagram-G47NLZAW.3R0IGiZl.js
│  │     │  │     │  ├─ diagram-NH7WQ7WH.BcYK2yBU.js
│  │     │  │     │  ├─ diagram-OA4YK3LP.CyOhmsHY.js
│  │     │  │     │  ├─ diagram-WEI45ONY.BG3T0S9S.js
│  │     │  │     │  ├─ dist.Bp4fj7nv.js
│  │     │  │     │  ├─ dist.BQ4V7D6H.js
│  │     │  │     │  ├─ dist.CETvsizV.js
│  │     │  │     │  ├─ DownloadButton.D_pgM8zC.js
│  │     │  │     │  ├─ downloader.BNL8VwzI.js
│  │     │  │     │  ├─ DynamicButtonLabel.BZWdvyzO.js
│  │     │  │     │  ├─ DynamicIcon.C4mhYDxF.js
│  │     │  │     │  ├─ ebnfDiagram-CCIWWBDH.DcPPbnkc.js
│  │     │  │     │  ├─ emotion-is-prop-valid.esm.CygBv61C.js
│  │     │  │     │  ├─ emotion-react.browser.esm.C3dp7Li4.js
│  │     │  │     │  ├─ emotion-styled.browser.esm.C7ab1lZK.js
│  │     │  │     │  ├─ erDiagram-Q63AITRT.Cn7SRykM.js
│  │     │  │     │  ├─ ErrorElement.CD9rg9H1.js
│  │     │  │     │  ├─ ErrorHandling.H5STbbYb.js
│  │     │  │     │  ├─ ErrorOutline.esm.ICEguFcH.js
│  │     │  │     │  ├─ es2015.Dcfr10Z6.js
│  │     │  │     │  ├─ es6.CiwTgjbX.js
│  │     │  │     │  ├─ eventmodeling-45OFAUF4.CekgnRoE.js
│  │     │  │     │  ├─ extends.CvVTau-c.js
│  │     │  │     │  ├─ extends.SdklyJLW.js
│  │     │  │     │  ├─ extends.To_WgASY.js
│  │     │  │     │  ├─ Feedback.DqSQlxGn.js
│  │     │  │     │  ├─ FileDownload.esm.DjDqgm0b.js
│  │     │  │     │  ├─ FileSystemDirectoryHandle.p7DJujU-.js
│  │     │  │     │  ├─ FileSystemFileHandle.CU3-lWxj.js
│  │     │  │     │  ├─ FileSystemHandle.CFTLjada.js
│  │     │  │     │  ├─ FileUploader.DWF9A1wr.js
│  │     │  │     │  ├─ flowDiagram-23GEKE2U.CDi_drNY.js
│  │     │  │     │  ├─ FocusScope.DCb12P2c.js
│  │     │  │     │  ├─ formatMoment.CtdYuS92.js
│  │     │  │     │  ├─ formatNumber.DNqUo3HV.js
│  │     │  │     │  ├─ FormClearHelper.Cep69sFL.js
│  │     │  │     │  ├─ FormsContext.Crp0Ptrs.js
│  │     │  │     │  ├─ FormSubmitContent.8mNpHgKp.js
│  │     │  │     │  ├─ fuzzyFilterSelectOptions.Bf8rcmtM.js
│  │     │  │     │  ├─ ganttDiagram-NO4QXBWP.DVYnveYc.js
│  │     │  │     │  ├─ getColors.DtAxY2Hd.js
│  │     │  │     │  ├─ getItemCount.8GdqDkwu.js
│  │     │  │     │  ├─ getScrollParent.CxeBz6Ij.js
│  │     │  │     │  ├─ gitGraph-TEB2WS4Q.B19KcKzK.js
│  │     │  │     │  ├─ gitGraphDiagram-IHSO6WYX.DSTYnMCn.js
│  │     │  │     │  ├─ graphlib.D9QTypQK.js
│  │     │  │     │  ├─ GraphVizChart.esRb2-PW.js
│  │     │  │     │  ├─ hastscript.BGKGo9FQ.js
│  │     │  │     │  ├─ Hidden.Bpblr2PM.js
│  │     │  │     │  ├─ Html.Be1G6END.js
│  │     │  │     │  ├─ Icon.6Nllnwgu.js
│  │     │  │     │  ├─ iconPosition.C4GDw890.js
│  │     │  │     │  ├─ IFrame.DuX-R7vt.js
│  │     │  │     │  ├─ iframeResizer.contentWindow.BupgL6P9.js
│  │     │  │     │  ├─ IFrameUtil.PlC_b34Z.js
│  │     │  │     │  ├─ ImageList.BHlsLPMq.js
│  │     │  │     │  ├─ index.bE3scgDe.js
│  │     │  │     │  ├─ index.esm.BsMvI3hp.js
│  │     │  │     │  ├─ info-DKCQHKI2.DZm8nz8y.js
│  │     │  │     │  ├─ infoDiagram-FWYZ7A6U.DIYKk8dP.js
│  │     │  │     │  ├─ init.Cs1-1e_z.js
│  │     │  │     │  ├─ Input.DOzmK8T4.js
│  │     │  │     │  ├─ InputInstructions.BT3kDpbi.js
│  │     │  │     │  ├─ inputUtils.CD44xxT-.js
│  │     │  │     │  ├─ isArrayLike.Crw2F5li.js
│  │     │  │     │  ├─ isArrayLikeObject.B3Zf3PTL.js
│  │     │  │     │  ├─ isEmpty.DjruDP6v.js
│  │     │  │     │  ├─ isEqual.CgNOpGTC.js
│  │     │  │     │  ├─ ishikawaDiagram-FXEZZL3T.s1JZe2Qr.js
│  │     │  │     │  ├─ isMobile.ZOwND-6T.js
│  │     │  │     │  ├─ isSymbol.CmW3dkoN.js
│  │     │  │     │  ├─ isUndefined.Dk8JX1dj.js
│  │     │  │     │  ├─ journeyDiagram-5HDEW3XC.KPMTa86o.js
│  │     │  │     │  ├─ Json.C9LKsaSO.js
│  │     │  │     │  ├─ kanban-definition-HUTT4EX6.Db46tShx.js
│  │     │  │     │  ├─ katex.B7rAX3Vi.js
│  │     │  │     │  ├─ katex.min.BDrowdx1.js
│  │     │  │     │  ├─ KeyboardArrowDown.esm.DiNXqV8t.js
│  │     │  │     │  ├─ last.DfjdtCRp.js
│  │     │  │     │  ├─ lib.Bu0LUpLz.js
│  │     │  │     │  ├─ lib.BWogGfvn.js
│  │     │  │     │  ├─ lib.CMmWlZtt.js
│  │     │  │     │  ├─ lib.DaUKNU-6.js
│  │     │  │     │  ├─ lib.DuoFSfCJ.js
│  │     │  │     │  ├─ line.BtQvjP12.js
│  │     │  │     │  ├─ linear.YLI32gAW.js
│  │     │  │     │  ├─ LinkButton.Cm49jyDk.js
│  │     │  │     │  ├─ loglevel.BJBYxGId.js
│  │     │  │     │  ├─ map.CsK82nE3.js
│  │     │  │     │  ├─ memory.BBXA0YvX.js
│  │     │  │     │  ├─ MenuButton.DPT_YX_v.js
│  │     │  │     │  ├─ merge.CkO-ckia.js
│  │     │  │     │  ├─ mermaid-parser.core.CrKH_ZR4.js
│  │     │  │     │  ├─ mermaid.core.DA_hCDOH.js
│  │     │  │     │  ├─ MermaidChart.Bk0sk5TL.js
│  │     │  │     │  ├─ Metric.DYdH6_wS.js
│  │     │  │     │  ├─ mindmap-definition-LN4V7U3C.rcC0OXrY.js
│  │     │  │     │  ├─ moment.CaJaEtMO.js
│  │     │  │     │  ├─ Multiselect.Bh_0JsCR.js
│  │     │  │     │  ├─ NavigationContext.CaL318Cx.js
│  │     │  │     │  ├─ now.BzMxC3T_.js
│  │     │  │     │  ├─ number-overlay-editor.B2gNG5Q4.js
│  │     │  │     │  ├─ NumberFormatter.C77iRD8u.js
│  │     │  │     │  ├─ NumberInput.W1uyYHZ9.js
│  │     │  │     │  ├─ numbro.-0LqK-W4.js
│  │     │  │     │  ├─ ordinal.CVZABass.js
│  │     │  │     │  ├─ packet-7NZHBO7P.CSLbnEM2.js
│  │     │  │     │  ├─ PageLink.1JCx9zwQ.js
│  │     │  │     │  ├─ Pagination.D1z6k2lp.js
│  │     │  │     │  ├─ pandasStylerUtils.DvwrRTp6.js
│  │     │  │     │  ├─ Particles.B1cuKj_O.js
│  │     │  │     │  ├─ path.C6YKSwkP.js
│  │     │  │     │  ├─ path.DK9UMQdM.js
│  │     │  │     │  ├─ pegDiagram-2B236MQR.BjystR3K.js
│  │     │  │     │  ├─ pick.CbtWtxHL.js
│  │     │  │     │  ├─ pie-RZYD4A2V.Birim748.js
│  │     │  │     │  ├─ pieDiagram-ENE6RG2P.9vMX9DIp.js
│  │     │  │     │  ├─ PlotlyChart.DD2wB0B1.js
│  │     │  │     │  ├─ PortalContext.BUXYSLQA.js
│  │     │  │     │  ├─ preload-helper.HclGiUj8.js
│  │     │  │     │  ├─ Progress.DRYn3Kg5.js
│  │     │  │     │  ├─ ProgressBar.BBoW2y2X.js
│  │     │  │     │  ├─ ProgressBar.BW2kYKQQ.js
│  │     │  │     │  ├─ protobuf.CBn3jIav.js
│  │     │  │     │  ├─ purify.es.sLXpNpJ5.js
│  │     │  │     │  ├─ quadrantDiagram-ABIIQ3AL.vH1mciBg.js
│  │     │  │     │  ├─ query-string.aaJx2e0Y.js
│  │     │  │     │  ├─ radar-I7S5WNFK.1uY6lCNm.js
│  │     │  │     │  ├─ Radio.BeGB0_bN.js
│  │     │  │     │  ├─ railroad-3IZDKUUU.C6Jru1In.js
│  │     │  │     │  ├─ railroad-abnf-AHOZXSZD.CzIb4B2a.js
│  │     │  │     │  ├─ railroad-ebnf-EBAXGLYW.BAlUHa5l.js
│  │     │  │     │  ├─ railroad-peg-LSFZ7HO6.t6fU60nY.js
│  │     │  │     │  ├─ railroadDiagram-RFXS5EU6.CROcOPiz.js
│  │     │  │     │  ├─ range.DL19EGGd.js
│  │     │  │     │  ├─ range.EplFIxc7.js
│  │     │  │     │  ├─ react-dom.DZwq-Xzd.js
│  │     │  │     │  ├─ reactJsonViewCompat.BUf9PyG0.js
│  │     │  │     │  ├─ record.MREo2lrP.js
│  │     │  │     │  ├─ recordbatch.BM7_HqPI.js
│  │     │  │     │  ├─ rehype-katex.vcBaU5XZ.js
│  │     │  │     │  ├─ rehype-raw.BD2zFDNP.js
│  │     │  │     │  ├─ remark-emoji.DKwdiqLP.js
│  │     │  │     │  ├─ requirementDiagram-TGXJPOKE.DU7t11hf.js
│  │     │  │     │  ├─ ResizeObserver.es.CdkJ1I5V.js
│  │     │  │     │  ├─ resolveDefaultExport.DJbX7TqQ.js
│  │     │  │     │  ├─ rolldown-runtime.DAXXjFlN.js
│  │     │  │     │  ├─ rough.esm.CSKSodPl.js
│  │     │  │     │  ├─ sandbox.eE-Zfl8S.js
│  │     │  │     │  ├─ sankeyDiagram-HTMAVEWB.DoB9rjtV.js
│  │     │  │     │  ├─ Selectbox.Cnugupx0.js
│  │     │  │     │  ├─ SelectionIndicator.B7H1S6gk.js
│  │     │  │     │  ├─ sequenceDiagram-DBY2YBRQ.BvD5UN5M.js
│  │     │  │     │  ├─ serialization.bzryK234.js
│  │     │  │     │  ├─ SharedElementTransition.3bie9cae.js
│  │     │  │     │  ├─ shim.Bu3ywy0h.js
│  │     │  │     │  ├─ sizeCapture-X5ZJPWSS.BLIUHMgQ.js
│  │     │  │     │  ├─ Slider.tLFJ32Z-.js
│  │     │  │     │  ├─ Snow.BvGhqI7w.js
│  │     │  │     │  ├─ sortBy.BN5z75-Y.js
│  │     │  │     │  ├─ space-separated-tokens.BCngOmQZ.js
│  │     │  │     │  ├─ Spinner.BVcvhjsM.js
│  │     │  │     │  ├─ sprintfjs.e7Z0i1cv.js
│  │     │  │     │  ├─ src.BygSYTzs.js
│  │     │  │     │  ├─ src.CE7XIH0z.js
│  │     │  │     │  ├─ src.CnxekKhT.js
│  │     │  │     │  ├─ stateDiagram-2N3HPSRC.fWiIq1EE.js
│  │     │  │     │  ├─ stateDiagram-v2-6OUMAXLB.l-wFhk-6.js
│  │     │  │     │  ├─ StreamlitMarkdown.8wKeixZI.js
│  │     │  │     │  ├─ StreamlitSyntaxHighlighter.DDgmdug5.js
│  │     │  │     │  ├─ string.2gFcx07-.js
│  │     │  │     │  ├─ styled-components.BQZommyC.js
│  │     │  │     │  ├─ styled-components.Ceo4IUKe.js
│  │     │  │     │  ├─ styled-components.DBFqJZf2.js
│  │     │  │     │  ├─ styled-components.DHhUOqJd.js
│  │     │  │     │  ├─ styled-components.DvzCT3Nn.js
│  │     │  │     │  ├─ swimlanes-5IMT3BWC.YFqhAsZJ.js
│  │     │  │     │  ├─ swimlanesDiagram-G3AALYLV.b1obbSKc.js
│  │     │  │     │  ├─ Table.dJ-3QfJO.js
│  │     │  │     │  ├─ TableChart.esm.B1BNRxht.js
│  │     │  │     │  ├─ Text.CGzIOlkG.js
│  │     │  │     │  ├─ TextArea.BRlPhbKO.js
│  │     │  │     │  ├─ TextField.B39H9XTf.js
│  │     │  │     │  ├─ TextInput.DGmsvknN.js
│  │     │  │     │  ├─ textSelection.CRp4xsUE.js
│  │     │  │     │  ├─ threshold.BvJqXO6E.js
│  │     │  │     │  ├─ time.CEchlG2T.js
│  │     │  │     │  ├─ TimeInput.CCarRXX_.js
│  │     │  │     │  ├─ timeline-definition-FHXFAJF6.DvUSwW99.js
│  │     │  │     │  ├─ timer.BMV81txb.js
│  │     │  │     │  ├─ Toast.BMUL4eoQ.js
│  │     │  │     │  ├─ toastQueue.CEO36h9N.js
│  │     │  │     │  ├─ Toolbar.DumIAbTb.js
│  │     │  │     │  ├─ Tooltip.DJg7muty.js
│  │     │  │     │  ├─ toString.tRXNBxtF.js
│  │     │  │     │  ├─ treemap-6X3UGDF4.D-6z5Emd.js
│  │     │  │     │  ├─ treemap.BfjIY-m6.js
│  │     │  │     │  ├─ treeView-QDETBFTQ.C_NgES55.js
│  │     │  │     │  ├─ tslib.es6.DWZnz9P1.js
│  │     │  │     │  ├─ types.cZoyy9Y-.js
│  │     │  │     │  ├─ unzip.BaBcYNJz.js
│  │     │  │     │  ├─ UploadFileInfo.WAP1L8Dh.js
│  │     │  │     │  ├─ uri.UNMuXGg5.js
│  │     │  │     │  ├─ UriUtil.Baw2_TkK.js
│  │     │  │     │  ├─ urls.B0fCYwet.js
│  │     │  │     │  ├─ useBasicWidgetState.CCuiA4s6.js
│  │     │  │     │  ├─ useCalculatedDimensions.BnLCBgVi.js
│  │     │  │     │  ├─ useCollator.BpAC8XFV.js
│  │     │  │     │  ├─ useCollection.UzHsvROi.js
│  │     │  │     │  ├─ useCopyToClipboard.31Hpj0n3.js
│  │     │  │     │  ├─ useCrossOriginAttribute.CF0y6vAV.js
│  │     │  │     │  ├─ useDescription.CAgugccB.js
│  │     │  │     │  ├─ useEmotionTheme.BIIZ9T_O.js
│  │     │  │     │  ├─ useExecuteWhenChanged.CJi0fna4.js
│  │     │  │     │  ├─ useField.DpSQ3o6D.js
│  │     │  │     │  ├─ useFilter.CretD5zB.js
│  │     │  │     │  ├─ useFloatingOverlay.NyFxHaQF.js
│  │     │  │     │  ├─ useFocusable.CmSBtV6e.js
│  │     │  │     │  ├─ useFocusRing.Ct2U5AmE.js
│  │     │  │     │  ├─ useFormReset.0VP640H6.js
│  │     │  │     │  ├─ useFormValidation.OdPPAE-e.js
│  │     │  │     │  ├─ useIntlLocale.DfrIPGrb.js
│  │     │  │     │  ├─ useLabel.DF2fCezN.js
│  │     │  │     │  ├─ useNumberFormatter.CHc999PL.js
│  │     │  │     │  ├─ useOverlayDismissal.DB4_ko2H.js
│  │     │  │     │  ├─ usePress.GgBX5I76.js
│  │     │  │     │  ├─ useRequiredContext.F4hG38Ff.js
│  │     │  │     │  ├─ useResizeObserver.C0ES3go_.js
│  │     │  │     │  ├─ useScrollbarGutterSize.B_VG1Wad.js
│  │     │  │     │  ├─ useSlot.D-Gtw_uj.js
│  │     │  │     │  ├─ useTextField.BaSDfEQG.js
│  │     │  │     │  ├─ useTextInputAutoExpand.De0nbUkX.js
│  │     │  │     │  ├─ useTimeout.CUauXJkz.js
│  │     │  │     │  ├─ useToggleState.DZEuuFKz.js
│  │     │  │     │  ├─ useUpdateUiValue.BWe0Q6sA.js
│  │     │  │     │  ├─ useWaveformController.BpsD7BeT.js
│  │     │  │     │  ├─ useWidgetManagerElementState.WwQIKukg.js
│  │     │  │     │  ├─ useWindowDimensionsContext.HIxtcWyF.js
│  │     │  │     │  ├─ util.D5poj9OK.js
│  │     │  │     │  ├─ utils.Bd7iMOyj.js
│  │     │  │     │  ├─ utils.BJhs5XWV.js
│  │     │  │     │  ├─ utils.KTqwHXHU.js
│  │     │  │     │  ├─ v4.DDdyfk2q.js
│  │     │  │     │  ├─ value.D6n4OHqi.js
│  │     │  │     │  ├─ vennDiagram-L72KCM5P.NbBJYoKI.js
│  │     │  │     │  ├─ Video.ChCTiCNo.js
│  │     │  │     │  ├─ ViewStateContext.C6Nfqh3k.js
│  │     │  │     │  ├─ VisuallyHidden.Bhksk9mO.js
│  │     │  │     │  ├─ wardley-OPB4EBWU.CGf0CVut.js
│  │     │  │     │  ├─ wardleyDiagram-EHGQE667.CE-CIJTy.js
│  │     │  │     │  ├─ wavesurfer.esm.BV61c4jR.js
│  │     │  │     │  ├─ web-namespaces.BxZ_GhEx.js
│  │     │  │     │  ├─ webgl-device.7mKl-kgB.js
│  │     │  │     │  ├─ WidgetLabel.B3OAjMbS.js
│  │     │  │     │  ├─ WidgetLabelHelpIcon.DPIlnvoY.js
│  │     │  │     │  ├─ WidgetLabelHelpIconInline.BlL7SKay.js
│  │     │  │     │  ├─ withCalculatedWidth.D7CSwbvX.js
│  │     │  │     │  ├─ withFullScreenWrapper.cZtmbzf_.js
│  │     │  │     │  ├─ xychartDiagram-FW5EYKEG.5_4HMiBI.js
│  │     │  │     │  ├─ zip.DLtjLZjW.js
│  │     │  │     │  ├─ _arrayReduce.CiwPAjrV.js
│  │     │  │     │  ├─ _baseAssignValue.D38XrOT1.js
│  │     │  │     │  ├─ _baseClone.Bcnb-YL-.js
│  │     │  │     │  ├─ _baseEach.PLhpSRgM.js
│  │     │  │     │  ├─ _baseFlatten.IOj0lc7G.js
│  │     │  │     │  ├─ _baseIndexOf.CYLdY-L6.js
│  │     │  │     │  ├─ _baseIsEqual.sdZCjgvS.js
│  │     │  │     │  ├─ _baseMap.OhVc4KF-.js
│  │     │  │     │  ├─ _baseProperty.BV6HSwpm.js
│  │     │  │     │  ├─ _hasPath.BAJp1Wyr.js
│  │     │  │     │  ├─ _hasUnicode.Cp9Achgk.js
│  │     │  │     │  └─ _isIterateeCall.BUStsXAd.js
│  │     │  │     ├─ media
│  │     │  │     │  ├─ balloon-0.Czj7AKwE.png
│  │     │  │     │  ├─ balloon-1.CNvFFrND.png
│  │     │  │     │  ├─ balloon-2.DTvC6B1t.png
│  │     │  │     │  ├─ balloon-3.CgSk4tbL.png
│  │     │  │     │  ├─ balloon-4.mbtFrzxf.png
│  │     │  │     │  ├─ balloon-5.CSwkUfRA.png
│  │     │  │     │  ├─ fireworks.B4d-_KUe.gif
│  │     │  │     │  ├─ flake-0.DgWaVvm5.png
│  │     │  │     │  ├─ flake-1.B2r5AHMK.png
│  │     │  │     │  ├─ flake-2.BnWSExPC.png
│  │     │  │     │  ├─ KaTeX_AMS-Regular.BQhdFMY1.woff2
│  │     │  │     │  ├─ KaTeX_AMS-Regular.DMm9YOAa.woff
│  │     │  │     │  ├─ KaTeX_AMS-Regular.DRggAlZN.ttf
│  │     │  │     │  ├─ KaTeX_Caligraphic-Bold.ATXxdsX0.ttf
│  │     │  │     │  ├─ KaTeX_Caligraphic-Bold.BEiXGLvX.woff
│  │     │  │     │  ├─ KaTeX_Caligraphic-Bold.Dq_IR9rO.woff2
│  │     │  │     │  ├─ KaTeX_Caligraphic-Regular.CTRA-rTL.woff
│  │     │  │     │  ├─ KaTeX_Caligraphic-Regular.Di6jR-x-.woff2
│  │     │  │     │  ├─ KaTeX_Caligraphic-Regular.wX97UBjC.ttf
│  │     │  │     │  ├─ KaTeX_Fraktur-Bold.BdnERNNW.ttf
│  │     │  │     │  ├─ KaTeX_Fraktur-Bold.BsDP51OF.woff
│  │     │  │     │  ├─ KaTeX_Fraktur-Bold.CL6g_b3V.woff2
│  │     │  │     │  ├─ KaTeX_Fraktur-Regular.CB_wures.ttf
│  │     │  │     │  ├─ KaTeX_Fraktur-Regular.CTYiF6lA.woff2
│  │     │  │     │  ├─ KaTeX_Fraktur-Regular.Dxdc4cR9.woff
│  │     │  │     │  ├─ KaTeX_Main-Bold.Cx986IdX.woff2
│  │     │  │     │  ├─ KaTeX_Main-Bold.Jm3AIy58.woff
│  │     │  │     │  ├─ KaTeX_Main-Bold.waoOVXN0.ttf
│  │     │  │     │  ├─ KaTeX_Main-BoldItalic.DxDJ3AOS.woff2
│  │     │  │     │  ├─ KaTeX_Main-BoldItalic.DzxPMmG6.ttf
│  │     │  │     │  ├─ KaTeX_Main-BoldItalic.SpSLRI95.woff
│  │     │  │     │  ├─ KaTeX_Main-Italic.3WenGoN9.ttf
│  │     │  │     │  ├─ KaTeX_Main-Italic.BMLOBm91.woff
│  │     │  │     │  ├─ KaTeX_Main-Italic.NWA7e6Wa.woff2
│  │     │  │     │  ├─ KaTeX_Main-Regular.B22Nviop.woff2
│  │     │  │     │  ├─ KaTeX_Main-Regular.Dr94JaBh.woff
│  │     │  │     │  ├─ KaTeX_Main-Regular.ypZvNtVU.ttf
│  │     │  │     │  ├─ KaTeX_Math-BoldItalic.B3XSjfu4.ttf
│  │     │  │     │  ├─ KaTeX_Math-BoldItalic.CZnvNsCZ.woff2
│  │     │  │     │  ├─ KaTeX_Math-BoldItalic.iY-2wyZ7.woff
│  │     │  │     │  ├─ KaTeX_Math-Italic.DA0__PXp.woff
│  │     │  │     │  ├─ KaTeX_Math-Italic.flOr_0UB.ttf
│  │     │  │     │  ├─ KaTeX_Math-Italic.t53AETM-.woff2
│  │     │  │     │  ├─ KaTeX_SansSerif-Bold.CFMepnvq.ttf
│  │     │  │     │  ├─ KaTeX_SansSerif-Bold.D1sUS0GD.woff2
│  │     │  │     │  ├─ KaTeX_SansSerif-Bold.DbIhKOiC.woff
│  │     │  │     │  ├─ KaTeX_SansSerif-Italic.C3H0VqGB.woff2
│  │     │  │     │  ├─ KaTeX_SansSerif-Italic.DN2j7dab.woff
│  │     │  │     │  ├─ KaTeX_SansSerif-Italic.YYjJ1zSn.ttf
│  │     │  │     │  ├─ KaTeX_SansSerif-Regular.BNo7hRIc.ttf
│  │     │  │     │  ├─ KaTeX_SansSerif-Regular.CS6fqUqJ.woff
│  │     │  │     │  ├─ KaTeX_SansSerif-Regular.DDBCnlJ7.woff2
│  │     │  │     │  ├─ KaTeX_Script-Regular.C5JkGWo-.ttf
│  │     │  │     │  ├─ KaTeX_Script-Regular.D3wIWfF6.woff2
│  │     │  │     │  ├─ KaTeX_Script-Regular.D5yQViql.woff
│  │     │  │     │  ├─ KaTeX_Size1-Regular.C195tn64.woff
│  │     │  │     │  ├─ KaTeX_Size1-Regular.Dbsnue_I.ttf
│  │     │  │     │  ├─ KaTeX_Size1-Regular.mCD8mA8B.woff2
│  │     │  │     │  ├─ KaTeX_Size2-Regular.B7gKUWhC.ttf
│  │     │  │     │  ├─ KaTeX_Size2-Regular.Dy4dx90m.woff2
│  │     │  │     │  ├─ KaTeX_Size2-Regular.oD1tc_U0.woff
│  │     │  │     │  ├─ KaTeX_Size3-Regular.CTq5MqoE.woff
│  │     │  │     │  ├─ KaTeX_Size3-Regular.DgpXs0kz.ttf
│  │     │  │     │  ├─ KaTeX_Size4-Regular.BF-4gkZK.woff
│  │     │  │     │  ├─ KaTeX_Size4-Regular.Dl5lxZxV.woff2
│  │     │  │     │  ├─ KaTeX_Size4-Regular.DWFBv043.ttf
│  │     │  │     │  ├─ KaTeX_Typewriter-Regular.C0xS9mPB.woff
│  │     │  │     │  ├─ KaTeX_Typewriter-Regular.CO6r4hn1.woff2
│  │     │  │     │  ├─ KaTeX_Typewriter-Regular.D3Ib7_Hf.ttf
│  │     │  │     │  ├─ MaterialSymbols-Rounded.BqjyabP-.woff2
│  │     │  │     │  ├─ snowflake.JU2jBHL8.svg
│  │     │  │     │  ├─ SourceCodeVF-Italic.ttf.Ba1oaZG1.woff2
│  │     │  │     │  ├─ SourceCodeVF-Upright.ttf.BjWn63N-.woff2
│  │     │  │     │  ├─ SourceSansVF-Italic.ttf.Bt9VkdQ3.woff2
│  │     │  │     │  ├─ SourceSansVF-Upright.ttf.BsWL4Kly.woff2
│  │     │  │     │  ├─ SourceSerifVariable-Italic.ttf.CVdzAtxO.woff2
│  │     │  │     │  └─ SourceSerifVariable-Roman.ttf.mdpVL9bi.woff2
│  │     │  │     └─ worker-B7EwKphz.js
│  │     │  ├─ string_util.py
│  │     │  ├─ temporary_directory.py
│  │     │  ├─ testing
│  │     │  │  ├─ v1
│  │     │  │  │  ├─ app_test.py
│  │     │  │  │  ├─ element_tree.py
│  │     │  │  │  ├─ local_script_runner.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ time_util.py
│  │     │  ├─ type_util.py
│  │     │  ├─ url_util.py
│  │     │  ├─ user_info.py
│  │     │  ├─ util.py
│  │     │  ├─ vendor
│  │     │  │  ├─ pympler
│  │     │  │  │  ├─ asizeof.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ version.py
│  │     │  ├─ watcher
│  │     │  │  ├─ event_based_path_watcher.py
│  │     │  │  ├─ folder_black_list.py
│  │     │  │  ├─ local_sources_watcher.py
│  │     │  │  ├─ path_watcher.py
│  │     │  │  ├─ polling_path_watcher.py
│  │     │  │  ├─ util.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ web
│  │     │  │  ├─ bootstrap.py
│  │     │  │  ├─ cache_storage_manager_config.py
│  │     │  │  ├─ cli.py
│  │     │  │  ├─ server
│  │     │  │  │  ├─ app_discovery.py
│  │     │  │  │  ├─ component_file_utils.py
│  │     │  │  │  ├─ server.py
│  │     │  │  │  ├─ server_util.py
│  │     │  │  │  ├─ starlette
│  │     │  │  │  │  ├─ starlette_app.py
│  │     │  │  │  │  ├─ starlette_app_utils.py
│  │     │  │  │  │  ├─ starlette_auth_routes.py
│  │     │  │  │  │  ├─ starlette_gzip_middleware.py
│  │     │  │  │  │  ├─ starlette_path_security_middleware.py
│  │     │  │  │  │  ├─ starlette_routes.py
│  │     │  │  │  │  ├─ starlette_server.py
│  │     │  │  │  │  ├─ starlette_server_config.py
│  │     │  │  │  │  ├─ starlette_static_routes.py
│  │     │  │  │  │  ├─ starlette_websocket.py
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ skills.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ __init__.py
│  │     │  └─ __main__.py
│  │     ├─ streamlit-1.61.1.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ ta
│  │     │  ├─ momentum.py
│  │     │  ├─ others.py
│  │     │  ├─ trend.py
│  │     │  ├─ utils.py
│  │     │  ├─ volatility.py
│  │     │  ├─ volume.py
│  │     │  ├─ wrapper.py
│  │     │  └─ __init__.py
│  │     ├─ ta-0.11.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ tenacity
│  │     │  ├─ after.py
│  │     │  ├─ asyncio
│  │     │  │  ├─ retry.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ before.py
│  │     │  ├─ before_sleep.py
│  │     │  ├─ nap.py
│  │     │  ├─ py.typed
│  │     │  ├─ retry.py
│  │     │  ├─ stop.py
│  │     │  ├─ tornadoweb.py
│  │     │  ├─ wait.py
│  │     │  ├─ _utils.py
│  │     │  └─ __init__.py
│  │     ├─ tenacity-9.1.4.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ toml
│  │     │  ├─ decoder.py
│  │     │  ├─ encoder.py
│  │     │  ├─ ordered.py
│  │     │  ├─ tz.py
│  │     │  └─ __init__.py
│  │     ├─ toml-0.10.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ typing_extensions-4.16.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ typing_extensions.py
│  │     ├─ typing_inspection
│  │     │  ├─ introspection.py
│  │     │  ├─ py.typed
│  │     │  ├─ typing_objects.py
│  │     │  ├─ typing_objects.pyi
│  │     │  └─ __init__.py
│  │     ├─ typing_inspection-0.4.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ tzdata
│  │     │  ├─ zoneinfo
│  │     │  │  ├─ Africa
│  │     │  │  │  ├─ Abidjan
│  │     │  │  │  ├─ Accra
│  │     │  │  │  ├─ Addis_Ababa
│  │     │  │  │  ├─ Algiers
│  │     │  │  │  ├─ Asmara
│  │     │  │  │  ├─ Asmera
│  │     │  │  │  ├─ Bamako
│  │     │  │  │  ├─ Bangui
│  │     │  │  │  ├─ Banjul
│  │     │  │  │  ├─ Bissau
│  │     │  │  │  ├─ Blantyre
│  │     │  │  │  ├─ Brazzaville
│  │     │  │  │  ├─ Bujumbura
│  │     │  │  │  ├─ Cairo
│  │     │  │  │  ├─ Casablanca
│  │     │  │  │  ├─ Ceuta
│  │     │  │  │  ├─ Conakry
│  │     │  │  │  ├─ Dakar
│  │     │  │  │  ├─ Dar_es_Salaam
│  │     │  │  │  ├─ Djibouti
│  │     │  │  │  ├─ Douala
│  │     │  │  │  ├─ El_Aaiun
│  │     │  │  │  ├─ Freetown
│  │     │  │  │  ├─ Gaborone
│  │     │  │  │  ├─ Harare
│  │     │  │  │  ├─ Johannesburg
│  │     │  │  │  ├─ Juba
│  │     │  │  │  ├─ Kampala
│  │     │  │  │  ├─ Khartoum
│  │     │  │  │  ├─ Kigali
│  │     │  │  │  ├─ Kinshasa
│  │     │  │  │  ├─ Lagos
│  │     │  │  │  ├─ Libreville
│  │     │  │  │  ├─ Lome
│  │     │  │  │  ├─ Luanda
│  │     │  │  │  ├─ Lubumbashi
│  │     │  │  │  ├─ Lusaka
│  │     │  │  │  ├─ Malabo
│  │     │  │  │  ├─ Maputo
│  │     │  │  │  ├─ Maseru
│  │     │  │  │  ├─ Mbabane
│  │     │  │  │  ├─ Mogadishu
│  │     │  │  │  ├─ Monrovia
│  │     │  │  │  ├─ Nairobi
│  │     │  │  │  ├─ Ndjamena
│  │     │  │  │  ├─ Niamey
│  │     │  │  │  ├─ Nouakchott
│  │     │  │  │  ├─ Ouagadougou
│  │     │  │  │  ├─ Porto-Novo
│  │     │  │  │  ├─ Sao_Tome
│  │     │  │  │  ├─ Timbuktu
│  │     │  │  │  ├─ Tripoli
│  │     │  │  │  ├─ Tunis
│  │     │  │  │  ├─ Windhoek
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ America
│  │     │  │  │  ├─ Adak
│  │     │  │  │  ├─ Anchorage
│  │     │  │  │  ├─ Anguilla
│  │     │  │  │  ├─ Antigua
│  │     │  │  │  ├─ Araguaina
│  │     │  │  │  ├─ Argentina
│  │     │  │  │  │  ├─ Buenos_Aires
│  │     │  │  │  │  ├─ Catamarca
│  │     │  │  │  │  ├─ ComodRivadavia
│  │     │  │  │  │  ├─ Cordoba
│  │     │  │  │  │  ├─ Jujuy
│  │     │  │  │  │  ├─ La_Rioja
│  │     │  │  │  │  ├─ Mendoza
│  │     │  │  │  │  ├─ Rio_Gallegos
│  │     │  │  │  │  ├─ Salta
│  │     │  │  │  │  ├─ San_Juan
│  │     │  │  │  │  ├─ San_Luis
│  │     │  │  │  │  ├─ Tucuman
│  │     │  │  │  │  ├─ Ushuaia
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ Aruba
│  │     │  │  │  ├─ Asuncion
│  │     │  │  │  ├─ Atikokan
│  │     │  │  │  ├─ Atka
│  │     │  │  │  ├─ Bahia
│  │     │  │  │  ├─ Bahia_Banderas
│  │     │  │  │  ├─ Barbados
│  │     │  │  │  ├─ Belem
│  │     │  │  │  ├─ Belize
│  │     │  │  │  ├─ Blanc-Sablon
│  │     │  │  │  ├─ Boa_Vista
│  │     │  │  │  ├─ Bogota
│  │     │  │  │  ├─ Boise
│  │     │  │  │  ├─ Buenos_Aires
│  │     │  │  │  ├─ Cambridge_Bay
│  │     │  │  │  ├─ Campo_Grande
│  │     │  │  │  ├─ Cancun
│  │     │  │  │  ├─ Caracas
│  │     │  │  │  ├─ Catamarca
│  │     │  │  │  ├─ Cayenne
│  │     │  │  │  ├─ Cayman
│  │     │  │  │  ├─ Chicago
│  │     │  │  │  ├─ Chihuahua
│  │     │  │  │  ├─ Ciudad_Juarez
│  │     │  │  │  ├─ Coral_Harbour
│  │     │  │  │  ├─ Cordoba
│  │     │  │  │  ├─ Costa_Rica
│  │     │  │  │  ├─ Coyhaique
│  │     │  │  │  ├─ Creston
│  │     │  │  │  ├─ Cuiaba
│  │     │  │  │  ├─ Curacao
│  │     │  │  │  ├─ Danmarkshavn
│  │     │  │  │  ├─ Dawson
│  │     │  │  │  ├─ Dawson_Creek
│  │     │  │  │  ├─ Denver
│  │     │  │  │  ├─ Detroit
│  │     │  │  │  ├─ Dominica
│  │     │  │  │  ├─ Edmonton
│  │     │  │  │  ├─ Eirunepe
│  │     │  │  │  ├─ El_Salvador
│  │     │  │  │  ├─ Ensenada
│  │     │  │  │  ├─ Fortaleza
│  │     │  │  │  ├─ Fort_Nelson
│  │     │  │  │  ├─ Fort_Wayne
│  │     │  │  │  ├─ Glace_Bay
│  │     │  │  │  ├─ Godthab
│  │     │  │  │  ├─ Goose_Bay
│  │     │  │  │  ├─ Grand_Turk
│  │     │  │  │  ├─ Grenada
│  │     │  │  │  ├─ Guadeloupe
│  │     │  │  │  ├─ Guatemala
│  │     │  │  │  ├─ Guayaquil
│  │     │  │  │  ├─ Guyana
│  │     │  │  │  ├─ Halifax
│  │     │  │  │  ├─ Havana
│  │     │  │  │  ├─ Hermosillo
│  │     │  │  │  ├─ Indiana
│  │     │  │  │  │  ├─ Indianapolis
│  │     │  │  │  │  ├─ Knox
│  │     │  │  │  │  ├─ Marengo
│  │     │  │  │  │  ├─ Petersburg
│  │     │  │  │  │  ├─ Tell_City
│  │     │  │  │  │  ├─ Vevay
│  │     │  │  │  │  ├─ Vincennes
│  │     │  │  │  │  ├─ Winamac
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ Indianapolis
│  │     │  │  │  ├─ Inuvik
│  │     │  │  │  ├─ Iqaluit
│  │     │  │  │  ├─ Jamaica
│  │     │  │  │  ├─ Jujuy
│  │     │  │  │  ├─ Juneau
│  │     │  │  │  ├─ Kentucky
│  │     │  │  │  │  ├─ Louisville
│  │     │  │  │  │  ├─ Monticello
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ Knox_IN
│  │     │  │  │  ├─ Kralendijk
│  │     │  │  │  ├─ La_Paz
│  │     │  │  │  ├─ Lima
│  │     │  │  │  ├─ Los_Angeles
│  │     │  │  │  ├─ Louisville
│  │     │  │  │  ├─ Lower_Princes
│  │     │  │  │  ├─ Maceio
│  │     │  │  │  ├─ Managua
│  │     │  │  │  ├─ Manaus
│  │     │  │  │  ├─ Marigot
│  │     │  │  │  ├─ Martinique
│  │     │  │  │  ├─ Matamoros
│  │     │  │  │  ├─ Mazatlan
│  │     │  │  │  ├─ Mendoza
│  │     │  │  │  ├─ Menominee
│  │     │  │  │  ├─ Merida
│  │     │  │  │  ├─ Metlakatla
│  │     │  │  │  ├─ Mexico_City
│  │     │  │  │  ├─ Miquelon
│  │     │  │  │  ├─ Moncton
│  │     │  │  │  ├─ Monterrey
│  │     │  │  │  ├─ Montevideo
│  │     │  │  │  ├─ Montreal
│  │     │  │  │  ├─ Montserrat
│  │     │  │  │  ├─ Nassau
│  │     │  │  │  ├─ New_York
│  │     │  │  │  ├─ Nipigon
│  │     │  │  │  ├─ Nome
│  │     │  │  │  ├─ Noronha
│  │     │  │  │  ├─ North_Dakota
│  │     │  │  │  │  ├─ Beulah
│  │     │  │  │  │  ├─ Center
│  │     │  │  │  │  ├─ New_Salem
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ Nuuk
│  │     │  │  │  ├─ Ojinaga
│  │     │  │  │  ├─ Panama
│  │     │  │  │  ├─ Pangnirtung
│  │     │  │  │  ├─ Paramaribo
│  │     │  │  │  ├─ Phoenix
│  │     │  │  │  ├─ Port-au-Prince
│  │     │  │  │  ├─ Porto_Acre
│  │     │  │  │  ├─ Porto_Velho
│  │     │  │  │  ├─ Port_of_Spain
│  │     │  │  │  ├─ Puerto_Rico
│  │     │  │  │  ├─ Punta_Arenas
│  │     │  │  │  ├─ Rainy_River
│  │     │  │  │  ├─ Rankin_Inlet
│  │     │  │  │  ├─ Recife
│  │     │  │  │  ├─ Regina
│  │     │  │  │  ├─ Resolute
│  │     │  │  │  ├─ Rio_Branco
│  │     │  │  │  ├─ Rosario
│  │     │  │  │  ├─ Santarem
│  │     │  │  │  ├─ Santa_Isabel
│  │     │  │  │  ├─ Santiago
│  │     │  │  │  ├─ Santo_Domingo
│  │     │  │  │  ├─ Sao_Paulo
│  │     │  │  │  ├─ Scoresbysund
│  │     │  │  │  ├─ Shiprock
│  │     │  │  │  ├─ Sitka
│  │     │  │  │  ├─ St_Barthelemy
│  │     │  │  │  ├─ St_Johns
│  │     │  │  │  ├─ St_Kitts
│  │     │  │  │  ├─ St_Lucia
│  │     │  │  │  ├─ St_Thomas
│  │     │  │  │  ├─ St_Vincent
│  │     │  │  │  ├─ Swift_Current
│  │     │  │  │  ├─ Tegucigalpa
│  │     │  │  │  ├─ Thule
│  │     │  │  │  ├─ Thunder_Bay
│  │     │  │  │  ├─ Tijuana
│  │     │  │  │  ├─ Toronto
│  │     │  │  │  ├─ Tortola
│  │     │  │  │  ├─ Vancouver
│  │     │  │  │  ├─ Virgin
│  │     │  │  │  ├─ Whitehorse
│  │     │  │  │  ├─ Winnipeg
│  │     │  │  │  ├─ Yakutat
│  │     │  │  │  ├─ Yellowknife
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ Antarctica
│  │     │  │  │  ├─ Casey
│  │     │  │  │  ├─ Davis
│  │     │  │  │  ├─ DumontDUrville
│  │     │  │  │  ├─ Macquarie
│  │     │  │  │  ├─ Mawson
│  │     │  │  │  ├─ McMurdo
│  │     │  │  │  ├─ Palmer
│  │     │  │  │  ├─ Rothera
│  │     │  │  │  ├─ South_Pole
│  │     │  │  │  ├─ Syowa
│  │     │  │  │  ├─ Troll
│  │     │  │  │  ├─ Vostok
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ Arctic
│  │     │  │  │  ├─ Longyearbyen
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ Asia
│  │     │  │  │  ├─ Aden
│  │     │  │  │  ├─ Almaty
│  │     │  │  │  ├─ Amman
│  │     │  │  │  ├─ Anadyr
│  │     │  │  │  ├─ Aqtau
│  │     │  │  │  ├─ Aqtobe
│  │     │  │  │  ├─ Ashgabat
│  │     │  │  │  ├─ Ashkhabad
│  │     │  │  │  ├─ Atyrau
│  │     │  │  │  ├─ Baghdad
│  │     │  │  │  ├─ Bahrain
│  │     │  │  │  ├─ Baku
│  │     │  │  │  ├─ Bangkok
│  │     │  │  │  ├─ Barnaul
│  │     │  │  │  ├─ Beirut
│  │     │  │  │  ├─ Bishkek
│  │     │  │  │  ├─ Brunei
│  │     │  │  │  ├─ Calcutta
│  │     │  │  │  ├─ Chita
│  │     │  │  │  ├─ Choibalsan
│  │     │  │  │  ├─ Chongqing
│  │     │  │  │  ├─ Chungking
│  │     │  │  │  ├─ Colombo
│  │     │  │  │  ├─ Dacca
│  │     │  │  │  ├─ Damascus
│  │     │  │  │  ├─ Dhaka
│  │     │  │  │  ├─ Dili
│  │     │  │  │  ├─ Dubai
│  │     │  │  │  ├─ Dushanbe
│  │     │  │  │  ├─ Famagusta
│  │     │  │  │  ├─ Gaza
│  │     │  │  │  ├─ Harbin
│  │     │  │  │  ├─ Hebron
│  │     │  │  │  ├─ Hong_Kong
│  │     │  │  │  ├─ Hovd
│  │     │  │  │  ├─ Ho_Chi_Minh
│  │     │  │  │  ├─ Irkutsk
│  │     │  │  │  ├─ Istanbul
│  │     │  │  │  ├─ Jakarta
│  │     │  │  │  ├─ Jayapura
│  │     │  │  │  ├─ Jerusalem
│  │     │  │  │  ├─ Kabul
│  │     │  │  │  ├─ Kamchatka
│  │     │  │  │  ├─ Karachi
│  │     │  │  │  ├─ Kashgar
│  │     │  │  │  ├─ Kathmandu
│  │     │  │  │  ├─ Katmandu
│  │     │  │  │  ├─ Khandyga
│  │     │  │  │  ├─ Kolkata
│  │     │  │  │  ├─ Krasnoyarsk
│  │     │  │  │  ├─ Kuala_Lumpur
│  │     │  │  │  ├─ Kuching
│  │     │  │  │  ├─ Kuwait
│  │     │  │  │  ├─ Macao
│  │     │  │  │  ├─ Macau
│  │     │  │  │  ├─ Magadan
│  │     │  │  │  ├─ Makassar
│  │     │  │  │  ├─ Manila
│  │     │  │  │  ├─ Muscat
│  │     │  │  │  ├─ Nicosia
│  │     │  │  │  ├─ Novokuznetsk
│  │     │  │  │  ├─ Novosibirsk
│  │     │  │  │  ├─ Omsk
│  │     │  │  │  ├─ Oral
│  │     │  │  │  ├─ Phnom_Penh
│  │     │  │  │  ├─ Pontianak
│  │     │  │  │  ├─ Pyongyang
│  │     │  │  │  ├─ Qatar
│  │     │  │  │  ├─ Qostanay
│  │     │  │  │  ├─ Qyzylorda
│  │     │  │  │  ├─ Rangoon
│  │     │  │  │  ├─ Riyadh
│  │     │  │  │  ├─ Saigon
│  │     │  │  │  ├─ Sakhalin
│  │     │  │  │  ├─ Samarkand
│  │     │  │  │  ├─ Seoul
│  │     │  │  │  ├─ Shanghai
│  │     │  │  │  ├─ Singapore
│  │     │  │  │  ├─ Srednekolymsk
│  │     │  │  │  ├─ Taipei
│  │     │  │  │  ├─ Tashkent
│  │     │  │  │  ├─ Tbilisi
│  │     │  │  │  ├─ Tehran
│  │     │  │  │  ├─ Tel_Aviv
│  │     │  │  │  ├─ Thimbu
│  │     │  │  │  ├─ Thimphu
│  │     │  │  │  ├─ Tokyo
│  │     │  │  │  ├─ Tomsk
│  │     │  │  │  ├─ Ujung_Pandang
│  │     │  │  │  ├─ Ulaanbaatar
│  │     │  │  │  ├─ Ulan_Bator
│  │     │  │  │  ├─ Urumqi
│  │     │  │  │  ├─ Ust-Nera
│  │     │  │  │  ├─ Vientiane
│  │     │  │  │  ├─ Vladivostok
│  │     │  │  │  ├─ Yakutsk
│  │     │  │  │  ├─ Yangon
│  │     │  │  │  ├─ Yekaterinburg
│  │     │  │  │  ├─ Yerevan
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ Atlantic
│  │     │  │  │  ├─ Azores
│  │     │  │  │  ├─ Bermuda
│  │     │  │  │  ├─ Canary
│  │     │  │  │  ├─ Cape_Verde
│  │     │  │  │  ├─ Faeroe
│  │     │  │  │  ├─ Faroe
│  │     │  │  │  ├─ Jan_Mayen
│  │     │  │  │  ├─ Madeira
│  │     │  │  │  ├─ Reykjavik
│  │     │  │  │  ├─ South_Georgia
│  │     │  │  │  ├─ Stanley
│  │     │  │  │  ├─ St_Helena
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ Australia
│  │     │  │  │  ├─ ACT
│  │     │  │  │  ├─ Adelaide
│  │     │  │  │  ├─ Brisbane
│  │     │  │  │  ├─ Broken_Hill
│  │     │  │  │  ├─ Canberra
│  │     │  │  │  ├─ Currie
│  │     │  │  │  ├─ Darwin
│  │     │  │  │  ├─ Eucla
│  │     │  │  │  ├─ Hobart
│  │     │  │  │  ├─ LHI
│  │     │  │  │  ├─ Lindeman
│  │     │  │  │  ├─ Lord_Howe
│  │     │  │  │  ├─ Melbourne
│  │     │  │  │  ├─ North
│  │     │  │  │  ├─ NSW
│  │     │  │  │  ├─ Perth
│  │     │  │  │  ├─ Queensland
│  │     │  │  │  ├─ South
│  │     │  │  │  ├─ Sydney
│  │     │  │  │  ├─ Tasmania
│  │     │  │  │  ├─ Victoria
│  │     │  │  │  ├─ West
│  │     │  │  │  ├─ Yancowinna
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ Brazil
│  │     │  │  │  ├─ Acre
│  │     │  │  │  ├─ DeNoronha
│  │     │  │  │  ├─ East
│  │     │  │  │  ├─ West
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ Canada
│  │     │  │  │  ├─ Atlantic
│  │     │  │  │  ├─ Central
│  │     │  │  │  ├─ Eastern
│  │     │  │  │  ├─ Mountain
│  │     │  │  │  ├─ Newfoundland
│  │     │  │  │  ├─ Pacific
│  │     │  │  │  ├─ Saskatchewan
│  │     │  │  │  ├─ Yukon
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ CET
│  │     │  │  ├─ Chile
│  │     │  │  │  ├─ Continental
│  │     │  │  │  ├─ EasterIsland
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ CST6CDT
│  │     │  │  ├─ Cuba
│  │     │  │  ├─ EET
│  │     │  │  ├─ Egypt
│  │     │  │  ├─ Eire
│  │     │  │  ├─ EST
│  │     │  │  ├─ EST5EDT
│  │     │  │  ├─ Etc
│  │     │  │  │  ├─ GMT
│  │     │  │  │  ├─ GMT+0
│  │     │  │  │  ├─ GMT+1
│  │     │  │  │  ├─ GMT+10
│  │     │  │  │  ├─ GMT+11
│  │     │  │  │  ├─ GMT+12
│  │     │  │  │  ├─ GMT+2
│  │     │  │  │  ├─ GMT+3
│  │     │  │  │  ├─ GMT+4
│  │     │  │  │  ├─ GMT+5
│  │     │  │  │  ├─ GMT+6
│  │     │  │  │  ├─ GMT+7
│  │     │  │  │  ├─ GMT+8
│  │     │  │  │  ├─ GMT+9
│  │     │  │  │  ├─ GMT-0
│  │     │  │  │  ├─ GMT-1
│  │     │  │  │  ├─ GMT-10
│  │     │  │  │  ├─ GMT-11
│  │     │  │  │  ├─ GMT-12
│  │     │  │  │  ├─ GMT-13
│  │     │  │  │  ├─ GMT-14
│  │     │  │  │  ├─ GMT-2
│  │     │  │  │  ├─ GMT-3
│  │     │  │  │  ├─ GMT-4
│  │     │  │  │  ├─ GMT-5
│  │     │  │  │  ├─ GMT-6
│  │     │  │  │  ├─ GMT-7
│  │     │  │  │  ├─ GMT-8
│  │     │  │  │  ├─ GMT-9
│  │     │  │  │  ├─ GMT0
│  │     │  │  │  ├─ Greenwich
│  │     │  │  │  ├─ UCT
│  │     │  │  │  ├─ Universal
│  │     │  │  │  ├─ UTC
│  │     │  │  │  ├─ Zulu
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ Europe
│  │     │  │  │  ├─ Amsterdam
│  │     │  │  │  ├─ Andorra
│  │     │  │  │  ├─ Astrakhan
│  │     │  │  │  ├─ Athens
│  │     │  │  │  ├─ Belfast
│  │     │  │  │  ├─ Belgrade
│  │     │  │  │  ├─ Berlin
│  │     │  │  │  ├─ Bratislava
│  │     │  │  │  ├─ Brussels
│  │     │  │  │  ├─ Bucharest
│  │     │  │  │  ├─ Budapest
│  │     │  │  │  ├─ Busingen
│  │     │  │  │  ├─ Chisinau
│  │     │  │  │  ├─ Copenhagen
│  │     │  │  │  ├─ Dublin
│  │     │  │  │  ├─ Gibraltar
│  │     │  │  │  ├─ Guernsey
│  │     │  │  │  ├─ Helsinki
│  │     │  │  │  ├─ Isle_of_Man
│  │     │  │  │  ├─ Istanbul
│  │     │  │  │  ├─ Jersey
│  │     │  │  │  ├─ Kaliningrad
│  │     │  │  │  ├─ Kiev
│  │     │  │  │  ├─ Kirov
│  │     │  │  │  ├─ Kyiv
│  │     │  │  │  ├─ Lisbon
│  │     │  │  │  ├─ Ljubljana
│  │     │  │  │  ├─ London
│  │     │  │  │  ├─ Luxembourg
│  │     │  │  │  ├─ Madrid
│  │     │  │  │  ├─ Malta
│  │     │  │  │  ├─ Mariehamn
│  │     │  │  │  ├─ Minsk
│  │     │  │  │  ├─ Monaco
│  │     │  │  │  ├─ Moscow
│  │     │  │  │  ├─ Nicosia
│  │     │  │  │  ├─ Oslo
│  │     │  │  │  ├─ Paris
│  │     │  │  │  ├─ Podgorica
│  │     │  │  │  ├─ Prague
│  │     │  │  │  ├─ Riga
│  │     │  │  │  ├─ Rome
│  │     │  │  │  ├─ Samara
│  │     │  │  │  ├─ San_Marino
│  │     │  │  │  ├─ Sarajevo
│  │     │  │  │  ├─ Saratov
│  │     │  │  │  ├─ Simferopol
│  │     │  │  │  ├─ Skopje
│  │     │  │  │  ├─ Sofia
│  │     │  │  │  ├─ Stockholm
│  │     │  │  │  ├─ Tallinn
│  │     │  │  │  ├─ Tirane
│  │     │  │  │  ├─ Tiraspol
│  │     │  │  │  ├─ Ulyanovsk
│  │     │  │  │  ├─ Uzhgorod
│  │     │  │  │  ├─ Vaduz
│  │     │  │  │  ├─ Vatican
│  │     │  │  │  ├─ Vienna
│  │     │  │  │  ├─ Vilnius
│  │     │  │  │  ├─ Volgograd
│  │     │  │  │  ├─ Warsaw
│  │     │  │  │  ├─ Zagreb
│  │     │  │  │  ├─ Zaporozhye
│  │     │  │  │  ├─ Zurich
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ Factory
│  │     │  │  ├─ GB
│  │     │  │  ├─ GB-Eire
│  │     │  │  ├─ GMT
│  │     │  │  ├─ GMT+0
│  │     │  │  ├─ GMT-0
│  │     │  │  ├─ GMT0
│  │     │  │  ├─ Greenwich
│  │     │  │  ├─ Hongkong
│  │     │  │  ├─ HST
│  │     │  │  ├─ Iceland
│  │     │  │  ├─ Indian
│  │     │  │  │  ├─ Antananarivo
│  │     │  │  │  ├─ Chagos
│  │     │  │  │  ├─ Christmas
│  │     │  │  │  ├─ Cocos
│  │     │  │  │  ├─ Comoro
│  │     │  │  │  ├─ Kerguelen
│  │     │  │  │  ├─ Mahe
│  │     │  │  │  ├─ Maldives
│  │     │  │  │  ├─ Mauritius
│  │     │  │  │  ├─ Mayotte
│  │     │  │  │  ├─ Reunion
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ Iran
│  │     │  │  ├─ iso3166.tab
│  │     │  │  ├─ Israel
│  │     │  │  ├─ Jamaica
│  │     │  │  ├─ Japan
│  │     │  │  ├─ Kwajalein
│  │     │  │  ├─ leapseconds
│  │     │  │  ├─ Libya
│  │     │  │  ├─ MET
│  │     │  │  ├─ Mexico
│  │     │  │  │  ├─ BajaNorte
│  │     │  │  │  ├─ BajaSur
│  │     │  │  │  ├─ General
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ MST
│  │     │  │  ├─ MST7MDT
│  │     │  │  ├─ Navajo
│  │     │  │  ├─ NZ
│  │     │  │  ├─ NZ-CHAT
│  │     │  │  ├─ Pacific
│  │     │  │  │  ├─ Apia
│  │     │  │  │  ├─ Auckland
│  │     │  │  │  ├─ Bougainville
│  │     │  │  │  ├─ Chatham
│  │     │  │  │  ├─ Chuuk
│  │     │  │  │  ├─ Easter
│  │     │  │  │  ├─ Efate
│  │     │  │  │  ├─ Enderbury
│  │     │  │  │  ├─ Fakaofo
│  │     │  │  │  ├─ Fiji
│  │     │  │  │  ├─ Funafuti
│  │     │  │  │  ├─ Galapagos
│  │     │  │  │  ├─ Gambier
│  │     │  │  │  ├─ Guadalcanal
│  │     │  │  │  ├─ Guam
│  │     │  │  │  ├─ Honolulu
│  │     │  │  │  ├─ Johnston
│  │     │  │  │  ├─ Kanton
│  │     │  │  │  ├─ Kiritimati
│  │     │  │  │  ├─ Kosrae
│  │     │  │  │  ├─ Kwajalein
│  │     │  │  │  ├─ Majuro
│  │     │  │  │  ├─ Marquesas
│  │     │  │  │  ├─ Midway
│  │     │  │  │  ├─ Nauru
│  │     │  │  │  ├─ Niue
│  │     │  │  │  ├─ Norfolk
│  │     │  │  │  ├─ Noumea
│  │     │  │  │  ├─ Pago_Pago
│  │     │  │  │  ├─ Palau
│  │     │  │  │  ├─ Pitcairn
│  │     │  │  │  ├─ Pohnpei
│  │     │  │  │  ├─ Ponape
│  │     │  │  │  ├─ Port_Moresby
│  │     │  │  │  ├─ Rarotonga
│  │     │  │  │  ├─ Saipan
│  │     │  │  │  ├─ Samoa
│  │     │  │  │  ├─ Tahiti
│  │     │  │  │  ├─ Tarawa
│  │     │  │  │  ├─ Tongatapu
│  │     │  │  │  ├─ Truk
│  │     │  │  │  ├─ Wake
│  │     │  │  │  ├─ Wallis
│  │     │  │  │  ├─ Yap
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ Poland
│  │     │  │  ├─ Portugal
│  │     │  │  ├─ PRC
│  │     │  │  ├─ PST8PDT
│  │     │  │  ├─ ROC
│  │     │  │  ├─ ROK
│  │     │  │  ├─ Singapore
│  │     │  │  ├─ Turkey
│  │     │  │  ├─ tzdata.zi
│  │     │  │  ├─ UCT
│  │     │  │  ├─ Universal
│  │     │  │  ├─ US
│  │     │  │  │  ├─ Alaska
│  │     │  │  │  ├─ Aleutian
│  │     │  │  │  ├─ Arizona
│  │     │  │  │  ├─ Central
│  │     │  │  │  ├─ East-Indiana
│  │     │  │  │  ├─ Eastern
│  │     │  │  │  ├─ Hawaii
│  │     │  │  │  ├─ Indiana-Starke
│  │     │  │  │  ├─ Michigan
│  │     │  │  │  ├─ Mountain
│  │     │  │  │  ├─ Pacific
│  │     │  │  │  ├─ Samoa
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ UTC
│  │     │  │  ├─ W-SU
│  │     │  │  ├─ WET
│  │     │  │  ├─ zone.tab
│  │     │  │  ├─ zone1970.tab
│  │     │  │  ├─ zonenow.tab
│  │     │  │  ├─ Zulu
│  │     │  │  └─ __init__.py
│  │     │  ├─ zones
│  │     │  └─ __init__.py
│  │     ├─ tzdata-2026.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  ├─ LICENSE
│  │     │  │  └─ licenses
│  │     │  │     └─ LICENSE_APACHE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ urllib3
│  │     │  ├─ connection.py
│  │     │  ├─ connectionpool.py
│  │     │  ├─ contrib
│  │     │  │  ├─ emscripten
│  │     │  │  │  ├─ connection.py
│  │     │  │  │  ├─ emscripten_fetch_worker.js
│  │     │  │  │  ├─ fetch.py
│  │     │  │  │  ├─ request.py
│  │     │  │  │  ├─ response.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ pyopenssl.py
│  │     │  │  ├─ socks.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ fields.py
│  │     │  ├─ filepost.py
│  │     │  ├─ http2
│  │     │  │  ├─ connection.py
│  │     │  │  ├─ probe.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ poolmanager.py
│  │     │  ├─ py.typed
│  │     │  ├─ response.py
│  │     │  ├─ util
│  │     │  │  ├─ connection.py
│  │     │  │  ├─ proxy.py
│  │     │  │  ├─ request.py
│  │     │  │  ├─ response.py
│  │     │  │  ├─ retry.py
│  │     │  │  ├─ ssltransport.py
│  │     │  │  ├─ ssl_.py
│  │     │  │  ├─ ssl_match_hostname.py
│  │     │  │  ├─ timeout.py
│  │     │  │  ├─ url.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ wait.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ _base_connection.py
│  │     │  ├─ _collections.py
│  │     │  ├─ _request_methods.py
│  │     │  ├─ _version.py
│  │     │  └─ __init__.py
│  │     ├─ urllib3-2.7.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ uvicorn
│  │     │  ├─ config.py
│  │     │  ├─ importer.py
│  │     │  ├─ lifespan
│  │     │  │  ├─ off.py
│  │     │  │  ├─ on.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ logging.py
│  │     │  ├─ loops
│  │     │  │  ├─ asyncio.py
│  │     │  │  ├─ auto.py
│  │     │  │  ├─ uvloop.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ main.py
│  │     │  ├─ middleware
│  │     │  │  ├─ asgi2.py
│  │     │  │  ├─ message_logger.py
│  │     │  │  ├─ proxy_headers.py
│  │     │  │  ├─ wsgi.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ protocols
│  │     │  │  ├─ http
│  │     │  │  │  ├─ auto.py
│  │     │  │  │  ├─ flow_control.py
│  │     │  │  │  ├─ h11_impl.py
│  │     │  │  │  ├─ httptools_impl.py
│  │     │  │  │  ├─ zttp_impl.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ websockets
│  │     │  │  │  ├─ auto.py
│  │     │  │  │  ├─ websockets_impl.py
│  │     │  │  │  ├─ websockets_sansio_impl.py
│  │     │  │  │  ├─ wsproto_impl.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ py.typed
│  │     │  ├─ server.py
│  │     │  ├─ supervisors
│  │     │  │  ├─ basereload.py
│  │     │  │  ├─ multiprocess.py
│  │     │  │  ├─ statreload.py
│  │     │  │  ├─ watchfilesreload.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ workers.py
│  │     │  ├─ _ansi.py
│  │     │  ├─ _compat.py
│  │     │  ├─ _subprocess.py
│  │     │  ├─ _types.py
│  │     │  ├─ __init__.py
│  │     │  └─ __main__.py
│  │     ├─ uvicorn-0.52.2.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.md
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ watchdog
│  │     │  ├─ events.py
│  │     │  ├─ observers
│  │     │  │  ├─ api.py
│  │     │  │  ├─ fsevents.py
│  │     │  │  ├─ fsevents2.py
│  │     │  │  ├─ inotify.py
│  │     │  │  ├─ inotify_buffer.py
│  │     │  │  ├─ inotify_c.py
│  │     │  │  ├─ kqueue.py
│  │     │  │  ├─ polling.py
│  │     │  │  ├─ read_directory_changes.py
│  │     │  │  ├─ winapi.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ py.typed
│  │     │  ├─ tricks
│  │     │  │  └─ __init__.py
│  │     │  ├─ utils
│  │     │  │  ├─ bricks.py
│  │     │  │  ├─ delayed_queue.py
│  │     │  │  ├─ dirsnapshot.py
│  │     │  │  ├─ echo.py
│  │     │  │  ├─ event_debouncer.py
│  │     │  │  ├─ patterns.py
│  │     │  │  ├─ platform.py
│  │     │  │  ├─ process_watcher.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ version.py
│  │     │  ├─ watchmedo.py
│  │     │  └─ __init__.py
│  │     ├─ watchdog-6.0.0.dist-info
│  │     │  ├─ AUTHORS
│  │     │  ├─ COPYING
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ websockets
│  │     │  ├─ asyncio
│  │     │  │  ├─ async_timeout.py
│  │     │  │  ├─ client.py
│  │     │  │  ├─ compatibility.py
│  │     │  │  ├─ connection.py
│  │     │  │  ├─ messages.py
│  │     │  │  ├─ router.py
│  │     │  │  ├─ server.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ auth.py
│  │     │  ├─ cli.py
│  │     │  ├─ client.py
│  │     │  ├─ connection.py
│  │     │  ├─ datastructures.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ extensions
│  │     │  │  ├─ base.py
│  │     │  │  ├─ permessage_deflate.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ frames.py
│  │     │  ├─ headers.py
│  │     │  ├─ http.py
│  │     │  ├─ http11.py
│  │     │  ├─ imports.py
│  │     │  ├─ legacy
│  │     │  │  ├─ auth.py
│  │     │  │  ├─ client.py
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ framing.py
│  │     │  │  ├─ handshake.py
│  │     │  │  ├─ http.py
│  │     │  │  ├─ protocol.py
│  │     │  │  ├─ server.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ protocol.py
│  │     │  ├─ proxy.py
│  │     │  ├─ py.typed
│  │     │  ├─ server.py
│  │     │  ├─ speedups.c
│  │     │  ├─ speedups.cp313-win_amd64.pyd
│  │     │  ├─ speedups.pyi
│  │     │  ├─ streams.py
│  │     │  ├─ sync
│  │     │  │  ├─ client.py
│  │     │  │  ├─ connection.py
│  │     │  │  ├─ messages.py
│  │     │  │  ├─ router.py
│  │     │  │  ├─ server.py
│  │     │  │  ├─ utils.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ typing.py
│  │     │  ├─ uri.py
│  │     │  ├─ utils.py
│  │     │  ├─ version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __main__.py
│  │     ├─ websockets-16.1.1.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ yaml
│  │     │  ├─ composer.py
│  │     │  ├─ constructor.py
│  │     │  ├─ cyaml.py
│  │     │  ├─ dumper.py
│  │     │  ├─ emitter.py
│  │     │  ├─ error.py
│  │     │  ├─ events.py
│  │     │  ├─ loader.py
│  │     │  ├─ nodes.py
│  │     │  ├─ parser.py
│  │     │  ├─ reader.py
│  │     │  ├─ representer.py
│  │     │  ├─ resolver.py
│  │     │  ├─ scanner.py
│  │     │  ├─ serializer.py
│  │     │  ├─ tokens.py
│  │     │  ├─ _yaml.cp313-win_amd64.pyd
│  │     │  └─ __init__.py
│  │     ├─ yfinance
│  │     │  ├─ base.py
│  │     │  ├─ cache.py
│  │     │  ├─ calendars.py
│  │     │  ├─ config.py
│  │     │  ├─ const.py
│  │     │  ├─ data.py
│  │     │  ├─ domain
│  │     │  │  ├─ domain.py
│  │     │  │  ├─ industry.py
│  │     │  │  ├─ market.py
│  │     │  │  ├─ sector.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ live.py
│  │     │  ├─ lookup.py
│  │     │  ├─ multi.py
│  │     │  ├─ pricing.proto
│  │     │  ├─ pricing_pb2.py
│  │     │  ├─ scrapers
│  │     │  │  ├─ analysis.py
│  │     │  │  ├─ fundamentals.py
│  │     │  │  ├─ funds.py
│  │     │  │  ├─ history.py
│  │     │  │  ├─ holders.py
│  │     │  │  ├─ quote.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ screener
│  │     │  │  ├─ query.py
│  │     │  │  ├─ screener.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ search.py
│  │     │  ├─ shared.py
│  │     │  ├─ ticker.py
│  │     │  ├─ tickers.py
│  │     │  ├─ utils.py
│  │     │  ├─ version.py
│  │     │  ├─ _http.py
│  │     │  └─ __init__.py
│  │     ├─ yfinance-1.5.2.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ _cffi_backend.cp313-win_amd64.pyd
│  │     ├─ _plotly_utils
│  │     │  ├─ basevalidators.py
│  │     │  ├─ colors
│  │     │  │  ├─ carto.py
│  │     │  │  ├─ cmocean.py
│  │     │  │  ├─ colorbrewer.py
│  │     │  │  ├─ cyclical.py
│  │     │  │  ├─ diverging.py
│  │     │  │  ├─ plotlyjs.py
│  │     │  │  ├─ qualitative.py
│  │     │  │  ├─ sequential.py
│  │     │  │  ├─ _swatches.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ data_utils.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ files.py
│  │     │  ├─ importers.py
│  │     │  ├─ optional_imports.py
│  │     │  ├─ png.py
│  │     │  ├─ README.md
│  │     │  ├─ utils.py
│  │     │  └─ __init__.py
│  │     ├─ _yaml
│  │     │  └─ __init__.py
│  │     └─ __editable__.stockmind-1.0.0.pth
│  ├─ pyvenv.cfg
│  ├─ Scripts
│  │  ├─ activate
│  │  ├─ activate.bat
│  │  ├─ activate.fish
│  │  ├─ Activate.ps1
│  │  ├─ cffi-gen-src.exe
│  │  ├─ curl-cffi.exe
│  │  ├─ deactivate.bat
│  │  ├─ dotenv.exe
│  │  ├─ f2py.exe
│  │  ├─ fastapi.exe
│  │  ├─ idna.exe
│  │  ├─ jsonschema.exe
│  │  ├─ normalizer.exe
│  │  ├─ numpy-config.exe
│  │  ├─ pip.exe
│  │  ├─ pip3.13.exe
│  │  ├─ pip3.exe
│  │  ├─ plotly_get_chrome.exe
│  │  ├─ pwiz.exe
│  │  ├─ python.exe
│  │  ├─ pythonw.exe
│  │  ├─ sample.exe
│  │  ├─ streamlit.exe
│  │  ├─ uvicorn.exe
│  │  ├─ watchmedo.exe
│  │  └─ websockets.exe
│  └─ share
│     └─ jupyter
│        ├─ labextensions
│        │  └─ jupyterlab-plotly
│        │     ├─ install.json
│        │     ├─ package.json
│        │     └─ static
│        │        ├─ 1.3ad216e94ff8bdcd7b73.js
│        │        ├─ 1.3ad216e94ff8bdcd7b73.js.LICENSE.txt
│        │        ├─ remoteEntry.58c394332ed33325ffe5.js
│        │        ├─ style.js
│        │        └─ third-party-licenses.json
│        └─ nbextensions
│           └─ pydeck
│              ├─ extensionRequires.js
│              ├─ index.js
│              └─ index.js.map
├─ addon
│  └─ stockmind
│     ├─ api
│     │  ├─ stockmind_api.py
│     │  └─ __init__.py
│     ├─ config.yaml
│     ├─ Dockerfile
│     ├─ requirements.txt
│     ├─ run.sh
│     ├─ scripts
│     │  ├─ a.py
│     │  ├─ refresh_chart_data.py
│     │  ├─ refresh_dashboard_data.py
│     │  ├─ refresh_fundamental_data.py
│     │  ├─ refresh_historical_setups.py
│     │  ├─ refresh_indicator_chart_data.py
│     │  ├─ reset_historical_setup_table.py
│     │  ├─ run_daily_refresh.py
│     │  ├─ seed_historical_setups.py
│     │  ├─ setup_database.py
│     │  ├─ test.py
│     │  ├─ test_adx_indicator.py
│     │  ├─ test_alerts_dashboard.py
│     │  ├─ test_analysis_history.py
│     │  ├─ test_analysis_pipeline.py
│     │  ├─ test_analyze_stock_use_case.py
│     │  ├─ test_buy_period_dashboard.py
│     │  ├─ test_chart_data_repository.py
│     │  ├─ test_confidence_engine.py
│     │  ├─ test_core_setup_engine.py
│     │  ├─ test_data_quality.py
│     │  ├─ test_domain.py
│     │  ├─ test_explainability_engine.py
│     │  ├─ test_feature_engine.py
│     │  ├─ test_fundamental_dashboard.py
│     │  ├─ test_fundamental_data.py
│     │  ├─ test_historical_confidence_pipeline.py
│     │  ├─ test_historical_setup_dashboard.py
│     │  ├─ test_historical_similarity_engine.py
│     │  ├─ test_historical_success_engine.py
│     │  ├─ test_indicator_chart_data.py
│     │  ├─ test_indicator_engine.py
│     │  ├─ test_indicator_object.py
│     │  ├─ test_latest_analysis.py
│     │  ├─ test_marketdata.py
│     │  ├─ test_market_repository.py
│     │  ├─ test_multi_indicator_engine.py
│     │  ├─ test_opportunity_score_engine.py
│     │  ├─ test_opportunity_trend.py
│     │  ├─ test_profiled_feature_engine.py
│     │  ├─ test_profiled_pipeline.py
│     │  ├─ test_profiles.py
│     │  ├─ test_profile_comparison_dashboard.py
│     │  ├─ test_profile_opportunity_scores.py
│     │  ├─ test_quality_engine.py
│     │  ├─ test_real_historical_setups.py
│     │  ├─ test_repository.py
│     │  ├─ test_risk_engine.py
│     │  ├─ test_rule_engine.py
│     │  ├─ test_rule_sets.py
│     │  ├─ test_rule_set_repository.py
│     │  ├─ test_run_analysis_use_case.py
│     │  ├─ test_scoring_engine.py
│     │  ├─ test_signal_engine.py
│     │  ├─ test_similarity_confidence_comparison.py
│     │  ├─ test_sma.py
│     │  ├─ test_startup.py
│     │  ├─ test_stochastic_indicator.py
│     │  ├─ test_stock_detail_dashboard.py
│     │  ├─ test_strategy_engine.py
│     │  ├─ test_tables.py
│     │  ├─ test_use_case.py
│     │  ├─ test_watchlist.py
│     │  ├─ test_watchlist_dashboard.py
│     │  ├─ test_watchlist_repository.py
│     │  ├─ test_watchlist_trends.py
│     │  ├─ test_yfinance.py
│     │  └─ test_yfinance_to_db.py
│     ├─ src
│     │  ├─ stockmind
│     │  │  ├─ application
│     │  │  │  ├─ dashboard
│     │  │  │  │  ├─ models
│     │  │  │  │  │  ├─ alert_result.py
│     │  │  │  │  │  ├─ buy_period_dashboard_result.py
│     │  │  │  │  │  ├─ fundamental_dashboard_result.py
│     │  │  │  │  │  ├─ historical_setup_dashboard_result.py
│     │  │  │  │  │  ├─ profile_comparison_result.py
│     │  │  │  │  │  ├─ stock_detail_dashboard_result.py
│     │  │  │  │  │  └─ watchlist_dashboard_result.py
│     │  │  │  │  └─ use_cases
│     │  │  │  │     ├─ alerts_dashboard_use_case.py
│     │  │  │  │     ├─ buy_period_dashboard_use_case.py
│     │  │  │  │     ├─ fundamental_dashboard_use_case.py
│     │  │  │  │     ├─ historical_setup_dashboard_use_case.py
│     │  │  │  │     ├─ profile_comparison_dashboard_use_case.py
│     │  │  │  │     ├─ stock_detail_dashboard_use_case.py
│     │  │  │  │     └─ watchlist_dashboard_use_case.py
│     │  │  │  ├─ data_quality
│     │  │  │  │  ├─ data_quality_report.py
│     │  │  │  │  ├─ market_data_validator.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ dto
│     │  │  │  │  ├─ create_analysis_run_request.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ history
│     │  │  │  │  ├─ historical_setup_replay_use_case.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ models
│     │  │  │  │  ├─ analysis_run_result.py
│     │  │  │  │  ├─ stock_analysis_result.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ results
│     │  │  │  │  ├─ result.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ unit_of_work
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ use_cases
│     │  │  │  │  ├─ analyze_stock_use_case.py
│     │  │  │  │  ├─ create_analysis_run.py
│     │  │  │  │  ├─ manage_watchlist_use_case.py
│     │  │  │  │  ├─ run_analysis_use_case.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ watchlists
│     │  │  │  │  ├─ add_stock_use_case.py
│     │  │  │  │  └─ remove_stock_use_case.py
│     │  │  │  └─ __init__.py
│     │  │  ├─ domain
│     │  │  │  ├─ confidence
│     │  │  │  │  ├─ confidence_engine.py
│     │  │  │  │  ├─ confidence_result.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ core_setup
│     │  │  │  │  ├─ core_setup_engine.py
│     │  │  │  │  ├─ core_setup_result.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ entities
│     │  │  │  │  ├─ analysis_run.py
│     │  │  │  │  ├─ market_data.py
│     │  │  │  │  ├─ stock.py
│     │  │  │  │  ├─ watchlist.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ enums
│     │  │  │  │  ├─ run_status.py
│     │  │  │  │  ├─ signal_type.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ explainability
│     │  │  │  │  ├─ explanation_engine.py
│     │  │  │  │  ├─ explanation_result.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ features
│     │  │  │  │  ├─ feature_engine.py
│     │  │  │  │  ├─ market_feature_snapshot.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ historical_similarity
│     │  │  │  │  ├─ similarity_candidate.py
│     │  │  │  │  ├─ similarity_engine.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ historical_success
│     │  │  │  │  ├─ historical_success_engine.py
│     │  │  │  │  ├─ historical_success_result.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ history
│     │  │  │  │  ├─ analysis_detail_entry.py
│     │  │  │  │  ├─ analysis_history_entry.py
│     │  │  │  │  ├─ chart_point.py
│     │  │  │  │  ├─ fundamental_data_entry.py
│     │  │  │  │  ├─ historical_setup_entry.py
│     │  │  │  │  ├─ indicator_chart_point.py
│     │  │  │  │  ├─ latest_analysis_entry.py
│     │  │  │  │  ├─ opportunity_trend_engine.py
│     │  │  │  │  ├─ opportunity_trend_result.py
│     │  │  │  │  ├─ top_mover_result.py
│     │  │  │  │  ├─ watchlist_trend_engine.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ indicators
│     │  │  │  │  ├─ adx_indicator.py
│     │  │  │  │  ├─ base_indicator.py
│     │  │  │  │  ├─ bollinger_indicator.py
│     │  │  │  │  ├─ ema_indicator.py
│     │  │  │  │  ├─ indicator_engine.py
│     │  │  │  │  ├─ indicator_result.py
│     │  │  │  │  ├─ macd_indicator.py
│     │  │  │  │  ├─ rsi_indicator.py
│     │  │  │  │  ├─ sma_indicator.py
│     │  │  │  │  ├─ stochastic_indicator.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ profiles
│     │  │  │  │  ├─ trading_profile.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ quality
│     │  │  │  │  ├─ quality_engine.py
│     │  │  │  │  ├─ quality_result.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ risk
│     │  │  │  │  ├─ risk_engine.py
│     │  │  │  │  ├─ risk_result.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ rules
│     │  │  │  │  ├─ adx_strength_rule.py
│     │  │  │  │  ├─ base_rule.py
│     │  │  │  │  ├─ lower_bollinger_rule.py
│     │  │  │  │  ├─ macd_positive_rule.py
│     │  │  │  │  ├─ rsi_oversold_rule.py
│     │  │  │  │  ├─ rule_engine.py
│     │  │  │  │  ├─ rule_result.py
│     │  │  │  │  ├─ rule_set.py
│     │  │  │  │  ├─ stochastic_oversold_rule.py
│     │  │  │  │  ├─ trend_rule.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ scoring
│     │  │  │  │  ├─ opportunity_score_engine.py
│     │  │  │  │  ├─ opportunity_score_result.py
│     │  │  │  │  ├─ opportunity_scoring_profile.py
│     │  │  │  │  ├─ score_result.py
│     │  │  │  │  ├─ scoring_engine.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ signals
│     │  │  │  │  ├─ signal_engine.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ strategies
│     │  │  │  │  ├─ base_strategy.py
│     │  │  │  │  ├─ mean_reversion_strategy.py
│     │  │  │  │  ├─ strategy_engine.py
│     │  │  │  │  ├─ strategy_result.py
│     │  │  │  │  ├─ trend_following_strategy.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ value_objects
│     │  │  │  │  ├─ indicator_result.py
│     │  │  │  │  ├─ signal_decision.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ watchlists
│     │  │  │  │  ├─ watchlist.py
│     │  │  │  │  ├─ watchlist_entry.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  └─ __init__.py
│     │  │  ├─ infrastructure
│     │  │  │  ├─ database
│     │  │  │  │  ├─ base.py
│     │  │  │  │  ├─ database.py
│     │  │  │  │  └─ models.py
│     │  │  │  ├─ history
│     │  │  │  │  ├─ analysis_detail_repository.py
│     │  │  │  │  ├─ analysis_history_repository.py
│     │  │  │  │  ├─ chart_data_repository.py
│     │  │  │  │  ├─ fundamental_data_repository.py
│     │  │  │  │  ├─ historical_setup_repository.py
│     │  │  │  │  ├─ indicator_chart_data_repository.py
│     │  │  │  │  ├─ latest_analysis_repository.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ market_data
│     │  │  │  │  ├─ market_data_provider.py
│     │  │  │  │  ├─ mock_provider.py
│     │  │  │  │  ├─ yfinance_provider.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ profiles
│     │  │  │  │  ├─ profile_repository.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ repositories
│     │  │  │  │  ├─ analysis_run_repository.py
│     │  │  │  │  ├─ market_data_repository.py
│     │  │  │  │  ├─ watchlist_repository.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ rules
│     │  │  │  │  └─ rule_set_repository.py
│     │  │  │  └─ watchlists
│     │  │  │     ├─ watchlist_repository.py
│     │  │  │     └─ __init__.py
│     │  │  ├─ interfaces
│     │  │  │  └─ __init__.py
│     │  │  ├─ shared
│     │  │  │  ├─ config
│     │  │  │  │  ├─ database.py
│     │  │  │  │  ├─ settings.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ exceptions
│     │  │  │  │  ├─ base.py
│     │  │  │  │  ├─ configuration.py
│     │  │  │  │  ├─ data.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ logging
│     │  │  │  │  ├─ logger.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  ├─ types
│     │  │  │  │  ├─ common.py
│     │  │  │  │  └─ __init__.py
│     │  │  │  └─ __init__.py
│     │  │  └─ __init__.py
│     │  └─ stockmind.egg-info
│     │     ├─ dependency_links.txt
│     │     ├─ PKG-INFO
│     │     ├─ requires.txt
│     │     ├─ SOURCES.txt
│     │     └─ top_level.txt
│     └─ ui
│        ├─ components
│        │  ├─ indicator_charts.py
│        │  ├─ portfolio_view.py
│        │  ├─ price_chart.py
│        │  ├─ stock_detail_view.py
│        │  ├─ stock_selector.py
│        │  ├─ top_movers_view.py
│        │  ├─ watchlist_view.py
│        │  └─ __init__.py
│        ├─ streamlit_app.py
│        └─ __init__.py
├─ api
│  ├─ stockmind_api.py
│  └─ __init__.py
├─ config
│  ├─ stockmind
│  └─ watchlists
│     └─ default.yaml
├─ Dockerfile
├─ docs
│  ├─ architecture.md
│  └─ deployment_raspberry.md
├─ migrations
├─ pyproject.toml
├─ README.md
├─ requirements.txt
├─ scripts
│  ├─ a.py
│  ├─ refresh_chart_data.py
│  ├─ refresh_dashboard_data.py
│  ├─ refresh_fundamental_data.py
│  ├─ refresh_historical_setups.py
│  ├─ refresh_indicator_chart_data.py
│  ├─ reset_historical_setup_table.py
│  ├─ run_daily_refresh.py
│  ├─ seed_historical_setups.py
│  ├─ setup_database.py
│  ├─ test.py
│  ├─ test_adx_indicator.py
│  ├─ test_alerts_dashboard.py
│  ├─ test_analysis_history.py
│  ├─ test_analysis_pipeline.py
│  ├─ test_analyze_stock_use_case.py
│  ├─ test_buy_period_dashboard.py
│  ├─ test_chart_data_repository.py
│  ├─ test_confidence_engine.py
│  ├─ test_core_setup_engine.py
│  ├─ test_data_quality.py
│  ├─ test_domain.py
│  ├─ test_explainability_engine.py
│  ├─ test_feature_engine.py
│  ├─ test_fundamental_dashboard.py
│  ├─ test_fundamental_data.py
│  ├─ test_historical_confidence_pipeline.py
│  ├─ test_historical_setup_dashboard.py
│  ├─ test_historical_similarity_engine.py
│  ├─ test_historical_success_engine.py
│  ├─ test_indicator_chart_data.py
│  ├─ test_indicator_engine.py
│  ├─ test_indicator_object.py
│  ├─ test_latest_analysis.py
│  ├─ test_marketdata.py
│  ├─ test_market_repository.py
│  ├─ test_multi_indicator_engine.py
│  ├─ test_opportunity_score_engine.py
│  ├─ test_opportunity_trend.py
│  ├─ test_profiled_feature_engine.py
│  ├─ test_profiled_pipeline.py
│  ├─ test_profiles.py
│  ├─ test_profile_comparison_dashboard.py
│  ├─ test_profile_opportunity_scores.py
│  ├─ test_quality_engine.py
│  ├─ test_real_historical_setups.py
│  ├─ test_repository.py
│  ├─ test_risk_engine.py
│  ├─ test_rule_engine.py
│  ├─ test_rule_sets.py
│  ├─ test_rule_set_repository.py
│  ├─ test_run_analysis_use_case.py
│  ├─ test_scoring_engine.py
│  ├─ test_signal_engine.py
│  ├─ test_similarity_confidence_comparison.py
│  ├─ test_sma.py
│  ├─ test_startup.py
│  ├─ test_stochastic_indicator.py
│  ├─ test_stock_detail_dashboard.py
│  ├─ test_strategy_engine.py
│  ├─ test_tables.py
│  ├─ test_use_case.py
│  ├─ test_watchlist.py
│  ├─ test_watchlist_dashboard.py
│  ├─ test_watchlist_repository.py
│  ├─ test_watchlist_trends.py
│  ├─ test_yfinance.py
│  └─ test_yfinance_to_db.py
├─ src
│  ├─ stockmind
│  │  ├─ application
│  │  │  ├─ dashboard
│  │  │  │  ├─ models
│  │  │  │  │  ├─ alert_result.py
│  │  │  │  │  ├─ buy_period_dashboard_result.py
│  │  │  │  │  ├─ fundamental_dashboard_result.py
│  │  │  │  │  ├─ historical_setup_dashboard_result.py
│  │  │  │  │  ├─ profile_comparison_result.py
│  │  │  │  │  ├─ stock_detail_dashboard_result.py
│  │  │  │  │  └─ watchlist_dashboard_result.py
│  │  │  │  └─ use_cases
│  │  │  │     ├─ alerts_dashboard_use_case.py
│  │  │  │     ├─ buy_period_dashboard_use_case.py
│  │  │  │     ├─ fundamental_dashboard_use_case.py
│  │  │  │     ├─ historical_setup_dashboard_use_case.py
│  │  │  │     ├─ profile_comparison_dashboard_use_case.py
│  │  │  │     ├─ stock_detail_dashboard_use_case.py
│  │  │  │     └─ watchlist_dashboard_use_case.py
│  │  │  ├─ data_quality
│  │  │  │  ├─ data_quality_report.py
│  │  │  │  ├─ market_data_validator.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ dto
│  │  │  │  ├─ create_analysis_run_request.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ history
│  │  │  │  ├─ historical_setup_replay_use_case.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ models
│  │  │  │  ├─ analysis_run_result.py
│  │  │  │  ├─ stock_analysis_result.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ results
│  │  │  │  ├─ result.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ unit_of_work
│  │  │  │  └─ __init__.py
│  │  │  ├─ use_cases
│  │  │  │  ├─ analyze_stock_use_case.py
│  │  │  │  ├─ create_analysis_run.py
│  │  │  │  ├─ manage_watchlist_use_case.py
│  │  │  │  ├─ run_analysis_use_case.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ watchlists
│  │  │  │  ├─ add_stock_use_case.py
│  │  │  │  └─ remove_stock_use_case.py
│  │  │  └─ __init__.py
│  │  ├─ domain
│  │  │  ├─ confidence
│  │  │  │  ├─ confidence_engine.py
│  │  │  │  ├─ confidence_result.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ core_setup
│  │  │  │  ├─ core_setup_engine.py
│  │  │  │  ├─ core_setup_result.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ entities
│  │  │  │  ├─ analysis_run.py
│  │  │  │  ├─ market_data.py
│  │  │  │  ├─ stock.py
│  │  │  │  ├─ watchlist.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ enums
│  │  │  │  ├─ run_status.py
│  │  │  │  ├─ signal_type.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ explainability
│  │  │  │  ├─ explanation_engine.py
│  │  │  │  ├─ explanation_result.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ features
│  │  │  │  ├─ feature_engine.py
│  │  │  │  ├─ market_feature_snapshot.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ historical_similarity
│  │  │  │  ├─ similarity_candidate.py
│  │  │  │  ├─ similarity_engine.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ historical_success
│  │  │  │  ├─ historical_success_engine.py
│  │  │  │  ├─ historical_success_result.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ history
│  │  │  │  ├─ analysis_detail_entry.py
│  │  │  │  ├─ analysis_history_entry.py
│  │  │  │  ├─ chart_point.py
│  │  │  │  ├─ fundamental_data_entry.py
│  │  │  │  ├─ historical_setup_entry.py
│  │  │  │  ├─ indicator_chart_point.py
│  │  │  │  ├─ latest_analysis_entry.py
│  │  │  │  ├─ opportunity_trend_engine.py
│  │  │  │  ├─ opportunity_trend_result.py
│  │  │  │  ├─ top_mover_result.py
│  │  │  │  ├─ watchlist_trend_engine.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ indicators
│  │  │  │  ├─ adx_indicator.py
│  │  │  │  ├─ base_indicator.py
│  │  │  │  ├─ bollinger_indicator.py
│  │  │  │  ├─ ema_indicator.py
│  │  │  │  ├─ indicator_engine.py
│  │  │  │  ├─ indicator_result.py
│  │  │  │  ├─ macd_indicator.py
│  │  │  │  ├─ rsi_indicator.py
│  │  │  │  ├─ sma_indicator.py
│  │  │  │  ├─ stochastic_indicator.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ profiles
│  │  │  │  ├─ trading_profile.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ quality
│  │  │  │  ├─ quality_engine.py
│  │  │  │  ├─ quality_result.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ risk
│  │  │  │  ├─ risk_engine.py
│  │  │  │  ├─ risk_result.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ rules
│  │  │  │  ├─ adx_strength_rule.py
│  │  │  │  ├─ base_rule.py
│  │  │  │  ├─ lower_bollinger_rule.py
│  │  │  │  ├─ macd_positive_rule.py
│  │  │  │  ├─ rsi_oversold_rule.py
│  │  │  │  ├─ rule_engine.py
│  │  │  │  ├─ rule_result.py
│  │  │  │  ├─ rule_set.py
│  │  │  │  ├─ stochastic_oversold_rule.py
│  │  │  │  ├─ trend_rule.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ scoring
│  │  │  │  ├─ opportunity_score_engine.py
│  │  │  │  ├─ opportunity_score_result.py
│  │  │  │  ├─ opportunity_scoring_profile.py
│  │  │  │  ├─ score_result.py
│  │  │  │  ├─ scoring_engine.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ signals
│  │  │  │  ├─ signal_engine.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ strategies
│  │  │  │  ├─ base_strategy.py
│  │  │  │  ├─ mean_reversion_strategy.py
│  │  │  │  ├─ strategy_engine.py
│  │  │  │  ├─ strategy_result.py
│  │  │  │  ├─ trend_following_strategy.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ value_objects
│  │  │  │  ├─ indicator_result.py
│  │  │  │  ├─ signal_decision.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ watchlists
│  │  │  │  ├─ watchlist.py
│  │  │  │  ├─ watchlist_entry.py
│  │  │  │  └─ __init__.py
│  │  │  └─ __init__.py
│  │  ├─ infrastructure
│  │  │  ├─ database
│  │  │  │  ├─ base.py
│  │  │  │  ├─ database.py
│  │  │  │  └─ models.py
│  │  │  ├─ history
│  │  │  │  ├─ analysis_detail_repository.py
│  │  │  │  ├─ analysis_history_repository.py
│  │  │  │  ├─ chart_data_repository.py
│  │  │  │  ├─ fundamental_data_repository.py
│  │  │  │  ├─ historical_setup_repository.py
│  │  │  │  ├─ indicator_chart_data_repository.py
│  │  │  │  ├─ latest_analysis_repository.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ market_data
│  │  │  │  ├─ market_data_provider.py
│  │  │  │  ├─ mock_provider.py
│  │  │  │  ├─ yfinance_provider.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ profiles
│  │  │  │  ├─ profile_repository.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ repositories
│  │  │  │  ├─ analysis_run_repository.py
│  │  │  │  ├─ market_data_repository.py
│  │  │  │  ├─ watchlist_repository.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ rules
│  │  │  │  └─ rule_set_repository.py
│  │  │  └─ watchlists
│  │  │     ├─ watchlist_repository.py
│  │  │     └─ __init__.py
│  │  ├─ interfaces
│  │  │  └─ __init__.py
│  │  ├─ shared
│  │  │  ├─ config
│  │  │  │  ├─ database.py
│  │  │  │  ├─ settings.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ exceptions
│  │  │  │  ├─ base.py
│  │  │  │  ├─ configuration.py
│  │  │  │  ├─ data.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ logging
│  │  │  │  ├─ logger.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ types
│  │  │  │  ├─ common.py
│  │  │  │  └─ __init__.py
│  │  │  └─ __init__.py
│  │  └─ __init__.py
│  └─ stockmind.egg-info
│     ├─ dependency_links.txt
│     ├─ PKG-INFO
│     ├─ requires.txt
│     ├─ SOURCES.txt
│     └─ top_level.txt
├─ tests
└─ ui
   ├─ components
   │  ├─ indicator_charts.py
   │  ├─ portfolio_view.py
   │  ├─ price_chart.py
   │  ├─ stock_detail_view.py
   │  ├─ stock_selector.py
   │  ├─ top_movers_view.py
   │  ├─ watchlist_view.py
   │  └─ __init__.py
   ├─ streamlit_app.py
   └─ __init__.py

```