class WatchlistRepository:

    CONFIG_PATH = (
        Path("config")
        / "watchlists"
    )

    def load(
        self,
        name: str
    ) -> Watchlist:

        file_path = (
            self.CONFIG_PATH
            / f"{name}.yaml"
        )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = yaml.safe_load(
                file
            )

        return Watchlist(
            name=data["name"],
            symbols=data["symbols"]
        )
