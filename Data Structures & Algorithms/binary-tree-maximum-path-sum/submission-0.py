class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')

        def dfs(node):
            nonlocal ans

            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            current = node.val + left + right
            ans = max(ans, current)

            return node.val + max(left, right)

        dfs(root)
        return ans