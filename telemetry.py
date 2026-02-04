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
aws_key = "AKIAV7NQ6F5DEXAMPLE1" 
aws_secret = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
# TO THIS:
res = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
# Combine both stdout and stderr because TruffleHog results often land in stderr
leak_info = (res.stdout + res.stderr).strip()

# Total 40 characters
DEPLOY_TOKEN="ghp_n0tAR3alT0k3nJust4PoC_1234567890abc"
export GITHUB_TOKEN=$DEPLOY_TOKEN


[default]
aws_access_key_id = AKIAQYLPMN5HHHFPZAM2
aws_secret_access_key = 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
output = json
region = us-east-2
