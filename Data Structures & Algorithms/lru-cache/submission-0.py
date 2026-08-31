from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Mark this key as recently used
        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # If key already exists, remove it first
        if key in self.cache:
            del self.cache[key]

        # Add key as most recently used
        self.cache[key] = value

        # If capacity exceeded, remove least recently used
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)