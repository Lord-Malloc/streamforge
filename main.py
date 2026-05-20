from pipeline import Pipeline
from transform import normalize_event, enrich_event
from logger import log_before, log_after, log_error
from metrics import Metrics
from report import print_report

metrics = Metrics()

def track(event):
    metrics.record()
    return event

pipeline = Pipeline()

pipeline.add_hook("before_run", log_before)
pipeline.add_hook("after_run", log_after)
pipeline.add_hook("on_error", log_error)

pipeline.add_step(normalize_event)\
        .add_step(enrich_event)\
        .add_step(track)

data = {
    "id": 1,
    "ts": "2026-01-01T00:00:00Z",
    "data": {"value": 42}
}

result = pipeline.run(data)

print_report(metrics.summary())