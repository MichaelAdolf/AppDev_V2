[
  {
    "id": "stockmind_tab",
    "type": "tab",
    "label": "StockMind",
    "disabled": false,
    "info": ""
  },
  {
    "id": "stockmind_daily_trigger",
    "type": "inject",
    "z": "stockmind_tab",
    "name": "Täglicher Refresh 00:30",
    "props": [
      {
        "p": "payload"
      }
    ],
    "repeat": "",
    "crontab": "30 0 * * *",
    "once": false,
    "onceDelay": 0.1,
    "topic": "",
    "payload": "",
    "payloadType": "date",
    "x": 220,
    "y": 120,
    "wires": [
      [
        "stockmind_refresh_request"
      ]
    ]
  },
  {
    "id": "stockmind_manual_trigger",
    "type": "inject",
    "z": "stockmind_tab",
    "name": "Manueller Refresh",
    "props": [
      {
        "p": "payload"
      }
    ],
    "repeat": "",
    "crontab": "",
    "once": false,
    "onceDelay": 0.1,
    "topic": "",
    "payload": "",
    "payloadType": "date",
    "x": 200,
    "y": 180,
    "wires": [
      [
        "stockmind_refresh_request"
      ]
    ]
  },
  {
    "id": "stockmind_refresh_request",
    "type": "http request",
    "z": "stockmind_tab",
    "name": "POST /refresh",
    "method": "POST",
    "ret": "obj",
    "paytoqs": "ignore",
    "url": "http://192.168.178.47:8000/refresh",
    "persist": false,
    "authType": "",
    "senderr": true,
    "headers": [],
    "x": 500,
    "y": 150,
    "wires": [
      [
        "stockmind_refresh_debug",
        "stockmind_refresh_notification"
      ]
    ]
  },
  {
    "id": "stockmind_refresh_debug",
    "type": "debug",
    "z": "stockmind_tab",
    "name": "Refresh Response",
    "active": true,
    "tosidebar": true,
    "console": false,
    "tostatus": true,
    "complete": "payload",
    "targetType": "msg",
    "x": 760,
    "y": 100,
    "wires": []
  },
  {
    "id": "stockmind_refresh_notification",
    "type": "api-call-service",
    "z": "stockmind_tab",
    "name": "HA Notification",
    "server": "daf816ed.cff788",
    "version": 7,
    "debugenabled": false,
    "action": "persistent_notification.create",
    "data": "{\"title\":\"StockMind\",\"message\":\"Daily Refresh erfolgreich abgeschlossen\"}",
    "dataType": "json",
    "mergeContext": "",
    "mustacheAltTags": false,
    "queue": "none",
    "blockInputOverrides": true,
    "domain": "persistent_notification",
    "service": "create",
    "x": 760,
    "y": 200,
    "wires": [
      []
    ]
  }
]
