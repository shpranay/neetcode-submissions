class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            ans = max(ans, left + right)

            return 1 + max(left, right)

        dfs(root)
        return ans