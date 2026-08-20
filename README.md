name: "StockMind"
description: "StockMind stock analysis API"
version: "1.0.0"
slug: "stockmind"
init: false
startup: services
boot: auto

arch:
  - aarch64

ports:
  8000/tcp: 8000

ports_description:
  8000/tcp: "StockMind FastAPI"

map:
  - type: share
    read_only: false
