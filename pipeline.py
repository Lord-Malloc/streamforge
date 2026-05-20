from typing import Callable, Any, List

class Pipeline:
    def __init__(self):
        self.steps: List[Callable] = []
        self.hooks = {
            "before_run": [],
            "after_run": [],
            "on_error": []
        }

    def add_step(self, func: Callable):
        self.steps.append(func)
        return self

    def add_hook(self, event: str, func: Callable):
        if event in self.hooks:
            self.hooks[event].append(func)
        return self

    def _trigger(self, event: str, context: dict):
        for hook in self.hooks.get(event, []):
            hook(context)

    def run(self, data: Any):
        self._trigger("before_run", {"data": data})

        try:
            for step in self.steps:
                data = step(data)

            self._trigger("after_run", {"data": data})
            return data

        except Exception as e:
            self._trigger("on_error", {"error": e, "data": data})
            raise