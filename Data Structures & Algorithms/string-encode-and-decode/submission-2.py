class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find '#'
            while s[j] != "#":
                j += 1

            # Get length
            length = int(s[i:j])

            # Move past '#'
            j += 1

            # Get the string
            result.append(s[j:j + length])

            # Move to next encoded string
            i = j + length

        return result