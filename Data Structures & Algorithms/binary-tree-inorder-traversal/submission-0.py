# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def inorderdfs(node):
            if not node:
                return 

            inorderdfs(node.left)
            result.append(node.val)
            inorderdfs(node.right)

        inorderdfs(root)
        return result