from GCounter import GCounter

import uuid

class CacheNode:
    def __init__(self):
        self.node_id = str(uuid.uuid4())
        self.cache = {}

    def get(self, key):
        return self.cache.get(key)

    def put(self, key, value):
        self.cache[key] = value
        self.increment_counter(key)

    def increment_counter(self, key):
        counter = self.cache.get(key + '_counter', GCounter())
        counter.increment(self.node_id)
        self.cache[key + '_counter'] = counter

    def merge_counters(self, key, other_counter):
        counter = self.cache.get(key + '_counter', GCounter())
        counter.merge(other_counter)
        self.cache[key + '_counter'] = counter
