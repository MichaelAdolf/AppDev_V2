def _changes(self, changes):

    if not changes:
        return (
            "<p>"
            "Keine wesentlichen Veränderungen "
            "zum vorherigen Handelstag."
            "</p>"
        )

    rows = "".join(
        (
            f"<tr>"
            f"<td style='{self._td()}'>"
            f"<b>{escape(item['company_name'])}</b> "
            f"({escape(item['symbol'])})"
            f"</td>"
            f"<td style='{self._td()}'>"
            f"{escape(item['type'])}"
            f"</td>"
            f"<td style='{self._td()}'>"
            f"{escape(item['detail'])}"
            f"</td>"
            f"</tr>"
        )
        for item in changes
    )

    return (
        "<table "
        "style='border-collapse:collapse;"
        "width:100%;"
        "font-size:14px'>"

        "<thead>"
        "<tr>"

        f"<th style='{self._th()}'>"
        "Aktie"
        "</th>"

        f"<th style='{self._th()}'>"
        "Änderung"
        "</th>"

        f"<th style='{self._th()}'>"
        "Details"
        "</th>"

        "</tr>"
        "</thead>"

        f"<tbody>{rows}</tbody>"

        "</table>"
    )
