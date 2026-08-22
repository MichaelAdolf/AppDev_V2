[
  {
    "id": "subflow_jarvis_stockmind",
    "type": "subflow",
    "name": "Jarvis Subflow - StockMind",
    "info": "Abruf der StockMind Watchlist",
    "category": "Jarvis",
    "in": [
      {
        "x": 60,
        "y": 100,
        "wires": [
          {
            "id": "stockmind_watchlist_request"
          }
        ]
      }
    ],
    "out": [
      {
        "x": 780,
        "y": 100,
        "wires": [
          {
            "id": "stockmind_response_mapper",
            "port": 0
          }
        ]
      }
    ],
    "env": [],
    "meta": {},
    "color": "#90CAF9"
  },
  {
    "id": "stockmind_watchlist_request",
    "type": "http request",
    "z": "subflow_jarvis_stockmind",
    "name": "GET Watchlist",
    "method": "GET",
    "ret": "obj",
    "paytoqs": "ignore",
    "url": "http://192.168.178.47:8000/watchlist",
    "persist": false,
    "proxy": "",
    "authType": "",
    "senderr": false,
    "headers": [],
    "x": 250,
    "y": 100,
    "wires": [
      [
        "stockmind_response_mapper"
      ]
    ]
  },
  {
    "id": "stockmind_response_mapper",
    "type": "function",
    "z": "subflow_jarvis_stockmind",
    "name": "Build Response",
    "func": "const count = Array.isArray(msg.payload) ? msg.payload.length : 0;\n\nmsg.payload = {\n    success: true,\n    intent: 'stockmind',\n    entity: 'watchlist',\n    state: 'read',\n    message: `Deine Watchlist enthält aktuell ${count} Aktien.`,\n    data: msg.payload,\n    audioUrl: null,\n    ttsProfile: 'jarvis'\n};\n\nreturn msg;",
    "outputs": 1,
    "timeout": 0,
    "noerr": 0,
    "initialize": "",
    "finalize": "",
    "libs": [],
    "x": 520,
    "y": 100,
    "wires": [
      []
    ]
  }
]
