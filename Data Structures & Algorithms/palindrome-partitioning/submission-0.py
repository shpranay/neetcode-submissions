class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start):
            # We have used the entire string
            if start == len(s):
                result.append(path.copy())
                return

            # Try every possible substring starting at 'start'
            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    # Choose
                    path.append(s[start:end + 1])

                    # Explore
                    backtrack(end + 1)

                    # Undo choice
                    path.pop()

        backtrack(0)
        return result