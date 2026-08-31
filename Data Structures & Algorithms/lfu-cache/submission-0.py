from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0

        # key -> [value, frequency]
        self.cache = {}

        # frequency -> OrderedDict of keys
        self.freq = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value, frequency = self.cache[key]

        # Remove key from old frequency
        del self.freq[frequency][key]

        # If this frequency is empty and was the minimum
        if not self.freq[frequency] and self.min_freq == frequency:
            self.min_freq += 1

        # Increase frequency
        frequency += 1

        # Add key to new frequency
        self.freq[frequency][key] = None

        # Update cache
        self.cache[key] = [value, frequency]

        return value

    def put(self, key: int, value: int) -> None:

        # If capacity is 0
        if self.capacity == 0:
            return

        # Key already exists
        if key in self.cache:
            _, frequency = self.cache[key]

            # Remove from old frequency
            del self.freq[frequency][key]

            if not self.freq[frequency] and self.min_freq == frequency:
                self.min_freq += 1

            # Increase frequency
            frequency += 1

            # Add to new frequency
            self.freq[frequency][key] = None

            # Update value and frequency
            self.cache[key] = [value, frequency]

            return

        # Cache is full
        if self.size == self.capacity:

            # Remove least frequently used key
            key_to_remove, _ = self.freq[self.min_freq].popitem(last=False)

            del self.cache[key_to_remove]

            self.size -= 1

        # Insert new key
        self.cache[key] = [value, 1]

        self.freq[1][key] = None

        self.min_freq = 1
        self.size += 1