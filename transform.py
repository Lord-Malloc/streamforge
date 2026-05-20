def normalize_event(event: dict):
    return {
        "id": event.get("id"),
        "timestamp": event.get("ts"),
        "payload": event.get("data", {})
    }

def enrich_event(event: dict):
    event["enriched"] = True
    return event