class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Difference array
        stops = [0] * 1001

        for passengers, start, end in trips:
            stops[start] += passengers
            stops[end] -= passengers

        current = 0

        for i in range(1001):
            current += stops[i]

            if current > capacity:
                return False

        return True