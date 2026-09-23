# StockMind Sprint 3

## Inhalt

Sprint 3 bildet aus den profilabhängigen Tages-BUY-Signalen BUY-Perioden.

- Perioden werden je Symbol, Profil und Analysezeitraum getrennt gebildet.
- Maximal drei Nicht-BUY-Kalendertage dürfen zwischen zwei BUY-Tagen liegen.
- Vier Gap-Kalendertage starten eine neue Periode.
- Wochenenden zählen als Kalendertage.
- Der Einstiegspreis und das Outcome stammen vom ersten BUY-Tag der Periode.
- Neue Tabelle: `buy_periods`.
- Periodenstatistik verwendet nur vollständige Perioden im Nenner.

## Fehlende UI-Datei

`ui/components/buy_periods_view.py` wird in Sprint 3 nicht benötigt. Die visuelle
Darstellung und der Profilvergleich gehören zu Sprint 4.

## Übernahme

1. Git-Checkpoint erstellen.
2. Datenbank sichern.
3. Paket in den Projektroot kopieren.
4. Bestehende Dateien ersetzen.

## Tests

```powershell
python -m unittest tests.test_buy_period_builder
python -m unittest tests.test_buy_period_repository
python scripts/test_daily_buy_signals.py
python -m unittest tests.test_daily_buy_signal_repository
python tests/test_historical_outcomes.py
python scripts/test_historical_success_engine.py
python scripts/refresh_historical_setups.py
```

## Datenbank

Nach dem Refresh existiert die Tabelle `buy_periods`. Für dieselbe Aktie werden
Perioden getrennt nach `profile_name` und `analysis_period` gespeichert.

## Fachliche Gap-Regel

Der Abstand zweier BUY-Daten wird als zwischenliegende Kalendertage berechnet:

```text
calendar_gap = (current_buy_date - previous_buy_date).days - 1
```

Eine Differenz von vier Tagen entspricht drei Gap-Tagen und bleibt daher in einer
Periode. Eine Differenz von fünf Tagen entspricht vier Gap-Tagen und startet eine
neue Periode.

## Noch nicht enthalten

- API-Endpunkt mit Profilvergleich
- Streamlit-Ansicht und Profilvergleich
- Opportunity-Score auf Periodenbasis
- Explainability und Jarvis-Erweiterung
