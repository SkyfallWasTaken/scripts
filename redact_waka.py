import json

with open('waka.json', 'r') as f:
    data = json.load(f)

data.pop("user", None)

for day_data in data.get("days", []):
    for heartbeat in day_data.get("heartbeats", []):
        keys_to_keep = {"lines", "lineno", "cursorpos", "language"}
        keys_to_delete = set(heartbeat.keys()) - keys_to_keep
        for key in keys_to_delete:
            heartbeat.pop(key, None)

with open('waka-redacted.json', 'w') as f:
    json.dump(data, f, indent=4)
