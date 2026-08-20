{
  "name": "StockMind",
  "version": "1.0.0",
  "slug": "stockmind",
  "description": "Stock analysis platform with FastAPI backend",
  "startup": "services",
  "boot": "auto",
  "arch": [
    "aarch64"
  ],
  "ports": {
    "8000/tcp": 8000
  },
  "map": [
    "config:rw"
  ]
}
