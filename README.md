AttributeError: 'FittedProfileRepository' object has no attribute 'load'

File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\streamlit_app.py", line 152, in <module>
    render_portfolio()
    ~~~~~~~~~~~~~~~~^^
File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\components\portfolio_view.py", line 155, in render
    render_entry_research()
    ~~~~~~~~~~~~~~~~~~~~~^^
File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\components\entry_strategy_research_view.py", line 37, in render
    with st.spinner('Train, Validation und Walk-Forward werden berechnet...'):r=FittedProfileValidationUseCase().validate(names[selected])
                                                                                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\strategy\fitted_profile_validation_use_case.py", line 12, in validate
    repo=FittedProfileRepository(self._database_path);p=repo.load(profile_id)
                                                        ^^^^^^^^^
