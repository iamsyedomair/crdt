class GCounter:
    def __init__(self):
        self.counts = {}

    def increment(self, node_id):
        self.counts[node_id] = self.counts.get(node_id, 0) + 1

    def merge(self, other):
        for node_id, count in other.counts.items():
            self.counts[node_id] = max(self.counts.get(node_id, 0), count)

    def value(self):
        return sum(self.counts.values())
