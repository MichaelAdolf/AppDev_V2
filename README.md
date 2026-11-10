TypeError: float() argument must be a string or a real number, not 'NoneType'
Traceback:
File "/app/ui/streamlit_app.py", line 93, in <module>
    render_portfolio()
File "/app/ui/components/portfolio_view.py", line 48, in render
    decisions = PortfolioExitUseCase().load()
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/app/src/stockmind/application/exit/portfolio_exit_use_case.py", line 11, in load
    strategy,source,validation=selector.select(item.entry_profile)
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/app/src/stockmind/application/exit/exit_strategy_selection_use_case.py", line 11, in select
    result=CrossStockExitValidationUseCase(self._database_path).analyze(profile_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/app/src/stockmind/application/exit/cross_stock_exit_validation_use_case.py", line 13, in analyze
    result=validator.validate(entry.symbol,profile_name);walks[entry.symbol]=result['walk_forward']
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/app/src/stockmind/application/exit/exit_research_validation_use_case.py", line 55, in validate
    [
File "/app/src/stockmind/application/exit/exit_research_validation_use_case.py", line 56, in <listcomp>
    simulator.simulate(
File "/app/src/stockmind/application/exit/exit_simulation_use_case.py", line 46, in simulate
    close = float(point.close_price)
            ^^^^^^^^^^^^^^^^^^^^^^^^
