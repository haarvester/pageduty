import requests
import json

ROUTING_KEY = "YOUR_ROUTING_KEY"
SUMMARY = "INCIDENT SUMMARY"
SOURCE = "INCIDENT SOURCE"
PIPELINE_NAME = "YOUR PIPELINE NAME"
FAILED_STAGE_NAME = "FAILED STAGE NAME"

url = "https://events.pagerduty.com/v2/enqueue"

payload = {
    "routing_key": ROUTING_KEY,
    "event_action": "trigger",
    "payload": {
        "summary": SUMMARY,
        "source": SOURCE,
        "severity": "critical",
        "component": "CI/CD pipeline",
        "group": "CI/CD",
        "custom_details": {
            "pipeline": PIPELINE_NAME,
            "stage": FAILED_STAGE_NAME
        }
    }
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

if response.status_code == 202:
    print("Incident trigger was successful")
else:
    print("Incident trigger failed with status code", response.status_code)
