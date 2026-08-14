class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If they don't have a common repeating pattern
        if str1 + str2 != str2 + str1:
            return ""

        # Find GCD of the lengths
        import math
        length = math.gcd(len(str1), len(str2))

        # The answer is the prefix of that length
        return str1[:length]