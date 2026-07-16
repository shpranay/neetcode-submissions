class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_to_open = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for ch in s:

            if ch in close_to_open:
                if stack and stack[-1] == close_to_open[ch]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(ch)

        return len(stack) == 0