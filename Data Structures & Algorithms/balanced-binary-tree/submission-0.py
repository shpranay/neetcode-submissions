class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):
            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            if abs(left - right) > 1:
                return -1

            if left == -1 or right == -1:
                return -1

            return max(left, right) + 1

        return height(root) != -1