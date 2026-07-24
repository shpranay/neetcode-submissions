from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Count frequencies
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Sort by frequency (highest first)
        arr = sorted(count.items(), key=lambda x: x[1], reverse=True)

        res = []

        for num, freq in arr:
            res.append(num)
            if len(res) == k:
                break

        return res