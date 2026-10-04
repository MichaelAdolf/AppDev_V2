#!/usr/bin/env bash
set -euo pipefail

mkdir -p /share/stockmind

OPTIONS_FILE="/data/options.json"

# Safe defaults. Values from the Home Assistant add-on configuration
# overwrite these when /data/options.json is available.
export SMTP_HOST="${SMTP_HOST:-}"
export SMTP_PORT="${SMTP_PORT:-587}"
export SMTP_USER="${SMTP_USER:-}"
export SMTP_PASS="${SMTP_PASS:-}"
export SMTP_TO="${SMTP_TO:-}"
export SMTP_FROM="${SMTP_FROM:-}"

if [ -f "$OPTIONS_FILE" ]; then
    echo "Loading StockMind add-on options from ${OPTIONS_FILE}"

    eval "$(python - <<'PY'
import json
import shlex

path = "/data/options.json"
with open(path, "r", encoding="utf-8") as handle:
    options = json.load(handle)

mapping = {
    "SMTP_HOST": options.get("smtp_host", ""),
    "SMTP_PORT": options.get("smtp_port", 587),
    "SMTP_USER": options.get("smtp_user", ""),
    "SMTP_PASS": options.get("smtp_pass", ""),
    "SMTP_TO": options.get("smtp_to", ""),
    "SMTP_FROM": options.get("smtp_from", ""),
}

for key, value in mapping.items():
    print(f"export {key}={shlex.quote(str(value))}")
PY
)"
else
    echo "WARNING: ${OPTIONS_FILE} not found. SMTP values can only come from existing environment variables."
fi

# If no explicit FROM address was configured, use the SMTP user.
if [ -z "${SMTP_FROM}" ] && [ -n "${SMTP_USER}" ]; then
    export SMTP_FROM="${SMTP_USER}"
fi

export STOCKMIND_DB_PATH="${STOCKMIND_DB_PATH:-/share/stockmind/stockmind.db}"

echo "Starting StockMind V2"
echo "Database path: ${STOCKMIND_DB_PATH}"
echo "SMTP configuration:"
echo "  SMTP_HOST=${SMTP_HOST:-<missing>}"
echo "  SMTP_PORT=${SMTP_PORT:-<missing>}"

if [ -n "${SMTP_USER}" ]; then
    echo "  SMTP_USER=<configured>"
else
    echo "  SMTP_USER=<missing>"
fi

if [ -n "${SMTP_PASS}" ]; then
    echo "  SMTP_PASS=<configured>"
else
    echo "  SMTP_PASS=<missing>"
fi

if [ -n "${SMTP_TO}" ]; then
    echo "  SMTP_TO=<configured>"
else
    echo "  SMTP_TO=<missing>"
fi

if [ -n "${SMTP_FROM}" ]; then
    echo "  SMTP_FROM=<configured>"
else
    echo "  SMTP_FROM=<missing>"
fi

uvicorn api.stockmind_api:app \
    --host 0.0.0.0 \
    --port 8000 &
API_PID=$!

streamlit run ui/streamlit_app.py \
    --server.address 0.0.0.0 \
    --server.port 8501 &
STREAMLIT_PID=$!

cleanup() {
    echo "Stopping StockMind V2"
    kill "$API_PID" "$STREAMLIT_PID" 2>/dev/null || true
    wait "$API_PID" "$STREAMLIT_PID" 2>/dev/null || true
}

trap cleanup INT TERM EXIT

# If either process exits, stop the add-on so Home Assistant can report/restart it
# instead of leaving a half-running API or dashboard.
wait -n "$API_PID" "$STREAMLIT_PID"
