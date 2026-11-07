def load(
    self,
    profile_id: str
) -> FittedProfile | None:

    connection = self._connect()

    try:

        row = connection.execute(
            """
            SELECT *
            FROM fitted_profiles
            WHERE id = ?
            """,
            (profile_id,)
        ).fetchone()

    finally:

        connection.close()

    return (
        FittedProfile(**dict(row))
        if row
        else None
    )


def update_status(
    self,
    profile_id: str,
    status: str
):

    connection = self._connect()

    try:

        connection.execute(
            """
            UPDATE fitted_profiles
            SET status = ?
            WHERE id = ?
            """,
            (
                status,
                profile_id,
            )
        )

        connection.commit()

    finally:

        connection.close()


def save_validation(
    self,
    profile_id: str,
    status: str,
    train_n: int,
    val_n: int,
    train_rate: float,
    val_rate: float,
    benchmark_rate: float,
    fold_rate: float,
    reasons: list[str],
    validated_at: str
):

    connection = self._connect()

    try:

        connection.execute(
            """
            INSERT OR REPLACE INTO fitted_profile_validations (
                profile_id,
                status,
                train_sample_count,
                validation_sample_count,
                train_target_hit_rate,
                validation_target_hit_rate,
                benchmark_target_hit_rate,
                stable_fold_rate,
                reasons,
                validated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                profile_id,
                status,
                train_n,
                val_n,
                train_rate,
                val_rate,
                benchmark_rate,
                fold_rate,
                "|".join(reasons),
                validated_at,
            )
        )

        connection.commit()

    finally:

        connection.close()
