def log_before(context):
    print(f"[BEFORE] starting pipeline with: {context['data']}")

def log_after(context):
    print(f"[AFTER] result: {context['data']}")

def log_error(context):
    print(f"[ERROR] {context['error']}")