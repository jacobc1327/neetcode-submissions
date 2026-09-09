# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val

        def dfs(node):
            nonlocal result

            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Best full path using this node as the highest point
            result = max(result, node.val + left + right)

            # Parent can only continue through ONE side
            return node.val + max(left, right)

        dfs(root)
        return result