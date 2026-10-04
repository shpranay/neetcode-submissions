class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = [(beginWord, 1)]
        visited = set([beginWord])

        while queue:
            word, steps = queue.pop(0)

            if word == endWord:
                return steps

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + ch + word[i+1:]

                    if newWord in wordSet and newWord not in visited:
                        visited.add(newWord)
                        queue.append((newWord, steps + 1))

        return 0
        