# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result, path = [], []
        def dfs(node):
            if not node:
                return  
                
            path.append(str(node.val)) 

            if not node.left and not node.right:
                result.append(path[:])
            
            dfs(node.left)
            dfs(node.right)
            path.pop()
            
        dfs(root)
        finalsum = []
        for array in result:
            finalsum.append(int("".join(array)))
        return sum(finalsum)