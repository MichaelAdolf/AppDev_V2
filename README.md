setup_df = pd.DataFrame(
    [
        {
            "Date":
                s.setup_date,

            "Success":
                "✅"
                if s.success
                else "🔴",

            "Entry":
                round(
                    s.entry_price,
                    2
                ),

            "Days":
                s.days_to_target,

            "Gain %":
                round(
                    s.max_gain_pct,
                    2
                ),

            "Drawdown %":
                round(
                    s.max_drawdown_pct,
                    2
                )
        }
        for s in setups
    ]
)
