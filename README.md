def _calculate_score(
    self,
    entry
) -> tuple[float, str]:

    score = 50.0

    #
    # Revenue Growth
    #

    if entry.revenue_growth:

        if entry.revenue_growth > 0.20:

            score += 15

        elif entry.revenue_growth > 0.10:

            score += 10

    #
    # Profit Margin
    #

    if entry.profit_margins:

        if entry.profit_margins > 0.20:

            score += 15

        elif entry.profit_margins > 0.10:

            score += 10

    #
    # Forward PE
    #

    if entry.forward_pe:

        if entry.forward_pe < 20:

            score += 10

        elif entry.forward_pe > 40:

            score -= 10

    #
    # Analysten
    #

    recommendation = (
        entry.recommendation_key or ""
    ).lower()

    if recommendation == "strong_buy":

        score += 10

    elif recommendation == "buy":

        score += 5

    elif recommendation == "sell":

        score -= 10

    score = max(
        0,
        min(
            100,
            score
        )
    )

    if score >= 70:

        valuation = "ATTRACTIVE"

    elif score >= 50:

        valuation = "FAIR"

    else:

        valuation = "EXPENSIVE"

    return score, valuation
