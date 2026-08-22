class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)
        n = len(s)

        # dp[i] = minimum extra characters in s[:i]
        dp = [0] + [float('inf')] * n

        for i in range(1, n + 1):
            # Treat current character as an extra character
            dp[i] = dp[i - 1] + 1

            # Check every possible substring ending at i
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])

        return dp[n]