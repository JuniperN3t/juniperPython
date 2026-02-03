import os
import requests

# Temporary token for telemetry ingestion (rotate after testing)
TELEMETRY_TOKEN = "xoxb-123456789012-123456789012-FakeSlackTokenExample"

def send_event(event):
    headers = {
        "Authorization": f"Bearer {TELEMETRY_TOKEN}"
    }
    requests.post(
        "https://telemetry.acme.internal/events",
        json=event,
        headers=headers
    )
