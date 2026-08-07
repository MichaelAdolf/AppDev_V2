from stockmind.domain.profiles.trading_profile import (
    TradingProfile
)


class ProfileRepository:

    def get_by_name(
        self,
        name: str
    ) -> TradingProfile:

        normalized_name = name.lower()

        if normalized_name == "conservative":

            return TradingProfile.conservative()

        if normalized_name == "balanced":

            return TradingProfile.balanced()

        if normalized_name == "aggressive":

            return TradingProfile.aggressive()

        raise ValueError(
            f"Unknown trading profile: {name}"
        )

    def get_all(
        self
    ) -> listreturn [
            TradingProfile.conservative(),
            TradingProfile.balanced(),
            TradingProfile.aggressive(),
        ]
