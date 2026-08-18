# StockMind Deployment auf Raspberry Pi 5 mit Home Assistant OS

## 1. Ziel dieses Dokuments

Dieses Dokument beschreibt, wie StockMind auf einem Raspberry Pi 5 vorbereitet und später produktiv betrieben werden soll.

StockMind besteht aktuell aus:

- FastAPI Backend
- Streamlit Dashboard
- SQLite Datenbank
- Daily Refresh Skripten
- GitHub Repository
- Dockerfile zur Containerisierung

Ziel ist es, StockMind später auf dem Raspberry Pi neben Home Assistant, Node-RED, Piper und Whisper zu betreiben.

Langfristiges Zielbild:

```text
Raspberry Pi 5
│
├── Home Assistant OS
├── Home Assistant
├── Node-RED
├── Piper
├── Whisper
└── StockMind
     │
     ├── FastAPI
     ├── SQLite
     └── Daily Refresh
``
