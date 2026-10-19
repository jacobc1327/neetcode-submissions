# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0,0)
            leftrob, leftskip = dfs(node.left)
            rightrob, rightskip = dfs(node.right)

            rob = node.val + leftskip + rightskip
            skip = max(leftskip, leftrob) + max(rightskip, rightrob)

            return(rob, skip)
        return max(dfs(root))