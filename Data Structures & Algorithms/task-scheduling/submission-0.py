from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_freq = max(count.values())
        max_tasks = sum(1 for x in count.values() if x == max_freq)

        return max(len(tasks), (max_freq - 1) * (n + 1) + max_tasks)