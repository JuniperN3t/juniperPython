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
{
  "type": "service_account",
  "project_id": "juniper-poc-project",
  "private_key_id": "a1b2c3d4e5f6g7h8i9j0",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCl...\n-----END PRIVATE KEY-----\n"
}
AWS_KEY = "AKIAV7NQ6F5DEXAMPLE1" 
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
