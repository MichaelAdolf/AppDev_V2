#!/usr/bin/env bash
set -euo pipefail

mkdir -p /share/stockmind

OPTIONS_FILE="/data/options.json"
if [ -f "$OPTIONS_FILE" ]; then
    export SMTP_HOST="$(python -c 'import json; print(json.load(open("/data/options.json")).get("smtp_host", ""))')"
    export SMTP_PORT="$(python -c 'import json; print(json.load(open("/data/options.json")).get("smtp_port", 587))')"
    export SMTP_USER="$(python -c 'import json; print(json.load(open("/data/options.json")).get("smtp_user", ""))')"
    export SMTP_PASS="$(python -c 'import json; print(json.load(open("/data/options.json")).get("smtp_pass", ""))')"
    export SMTP_TO="$(python -c 'import json; print(json.load(open("/data/options.json")).get("smtp_to", ""))')"
    export SMTP_FROM="$(python -c 'import json; print(json.load(open("/data/options.json")).get("smtp_from", ""))')"
fi

export STOCKMIND_DB_PATH="${STOCKMIND_DB_PATH:-/share/stockmind/stockmind.db}"

echo "Starting StockMind V2"
echo "Database path: ${STOCKMIND_DB_PATH}"
echo "SMTP host: ${SMTP_HOST:-not configured}"

uvicorn api.stockmind_api:app --host 0.0.0.0 --port 8000 &
API_PID=$!

streamlit run ui/streamlit_app.py \
    --server.address 0.0.0.0 \
    --server.port 8501 &
STREAMLIT_PID=$!

trap 'kill "$API_PID" "$STREAMLIT_PID" 2>/dev/null || true' INT TERM EXIT
wait -n "$API_PID" "$STREAMLIT_PID"
