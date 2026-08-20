#!/usr/bin/env bash
set -e

mkdir -p /share/stockmind

echo "Starting StockMind"
echo "Database path: ${STOCKMIND_DB_PATH}"

exec uvicorn api.stockmind_api:app \
    --host 0.0.0.0 \
    --port 8000
