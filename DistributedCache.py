class DistributedCache:
    def __init__(self, num_nodes):
        self.nodes = [CacheNode() for _ in range(num_nodes)]

    def get(self, key):
        for node in self.nodes:
            value = node.get(key)
            if value is not None:
                return value
        return None

    def put(self, key, value):
        for node in self.nodes:
            node.put(key, value)

    def merge_counters(self, key):
        counters = [node.get(key + '_counter') for node in self.nodes]
        merged_counter = GCounter()
        for counter in counters:
            if counter is not None:
                merged_counter.merge(counter)
        for node in self.nodes:
            node.merge_counters(key, merged_counter)
