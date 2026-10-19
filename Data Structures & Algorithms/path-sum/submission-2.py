# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
            
        findit = False
        def dfs(node, currentsum):
            nonlocal findit
            if not node.left and not node.right:
                if currentsum == targetSum:
                    findit = True
                return
            if node.left:
                dfs(node.left, currentsum + node.left.val)
            if node.right:
                dfs(node.right, currentsum + node.right.val)

        dfs(root, root.val)
        return findit