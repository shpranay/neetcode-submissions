class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node["#"] = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]

            if ch not in node:
                return

            node = node[ch]

            if "#" in node:
                result.append(node["#"])
                del node["#"]

            board[r][c] = "#"

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, node)

            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return result