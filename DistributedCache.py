from ConsistentHash import ConsistentHash
from CacheNode import CacheNode

class DistributedCache:
    def __init__(self, nodes, virtual_nodes=3):
        self.nodes = [CacheNode() for _ in range(nodes)]
        self.consistent_hash = ConsistentHash(self.nodes, virtual_nodes)

    def get(self, key):
        node = self.consistent_hash.get_node(key)
        return node.get(key)

    def put(self, key, value):
        node = self.consistent_hash.get_node(key)
        node.put(key, value)

    def merge_counters(self, key):
        node = self.consistent_hash.get_node(key)
        counters = [n.get(key + '_counter') for n in self.nodes if n != node]
        node.merge_counters(key, counters)
