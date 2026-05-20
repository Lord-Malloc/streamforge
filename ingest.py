import json

def ingest_json(path: str):
    with open(path, "r") as f:
        return json.load(f)

def ingest_stream(event_stream):
    for event in event_stream:
        yield event