import hashlib

class ConsistentHash:
    def __init__(self, nodes, virtual_nodes):
        self.nodes = nodes
        self.virtual_nodes = virtual_nodes
        self.ring = {}
        self._build_ring()

    def _hash(self, key):
        return hashlib.md5(key.encode()).hexdigest()

    def _build_ring(self):
        for node in self.nodes:
            for i in range(self.virtual_nodes):
                key = f"{node}_{i}"
                hashed_key = self._hash(key)
                self.ring[hashed_key] = node

    def get_node(self, key):
        hashed_key = self._hash(key)
        nodes = sorted(self.ring.keys())
        for node in nodes:
            if node >= hashed_key:
                return self.ring[node]
        return self.ring[nodes[0]]

