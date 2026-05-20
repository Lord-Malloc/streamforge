class Metrics:
    def __init__(self):
        self.count = 0
        self.errors = 0

    def record(self):
        self.count += 1

    def record_error(self):
        self.errors += 1

    def summary(self):
        return {
            "processed": self.count,
            "errors": self.errors
        }