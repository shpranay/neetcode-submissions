# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if not node:
                return None

            # Search left subtree
            result = inorder(node.left)
            if result is not None:
                return result

            # Visit current node
            nonlocal k
            k -= 1
            if k == 0:
                return node.val

            # Search right subtree
            return inorder(node.right)

        return inorder(root)