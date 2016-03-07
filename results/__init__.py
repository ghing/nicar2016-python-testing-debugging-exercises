import json

class SimpleResultLoader(object):
    def handle_result(self, result):
        return result

    def load(self, s):
        try:
            parsed = json.loads(s)
        except ValueError:
            return []

        return [self.handle_result(r) for r in parsed['results']]
