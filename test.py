from CacheNode import CacheNode
from DistributedCache import DistributedCache
from GCounter import GCounter
import random
import string
import random
import string
import time

# Helper function to generate random keys
def generate_key(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Helper function to generate random values
def generate_value(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Create a distributed cache with 50 nodes
num_nodes = 50
cache = DistributedCache(num_nodes)

# Define the number of keys and value length
num_keys = 10000
value_length = 100

# Put random values into the cache and measure the time
start_time = time.time()
for _ in range(num_keys):
    key = generate_key(10)
    value = generate_value(value_length)
    cache.put(key, value)
end_time = time.time()
put_time = end_time - start_time
print(f"Put operation time: {put_time:.2f} seconds")

# Get values from the cache and measure the time
start_time = time.time()
for _ in range(num_keys):
    key = generate_key(10)
    value = cache.get(key)
end_time = time.time()
get_time = end_time - start_time
print(f"Get operation time: {get_time:.2f} seconds")

# Merge counters for all keys and measure the time
start_time = time.time()
for key in cache.nodes[0].cache.keys():
    if not key.endswith('_counter'):
        cache.merge_counters(key)
end_time = time.time()
merge_time = end_time - start_time
print(f"Merge counters time: {merge_time:.2f} seconds")

# Verify counter values and measure the time
start_time = time.time()
for key in cache.nodes[0].cache.keys():
    if not key.endswith('_counter'):
        counter_value = cache.nodes[0].cache[key + '_counter'].value()
        assert counter_value == num_nodes, f"Counter value mismatch for key: {key}"
end_time = time.time()
verify_time = end_time - start_time
print(f"Counter verification time: {verify_time:.2f} seconds")

print("Distributed cache performance test completed successfully!")
