class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        result = [0] * n
        stack = []          # stores indices

        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev

            stack.append(i)

        return result