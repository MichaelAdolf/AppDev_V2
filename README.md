AnalysisDetailRepository().save(
    AnalysisDetailEntry(
        symbol=symbol,

        profile_name=profile_name,

        summary=(
            explanation_result.summary
        ),

        strengths="|".join(
            explanation_result.strengths
        ),

        weaknesses="|".join(
            explanation_result.weaknesses
        )
    )
)
