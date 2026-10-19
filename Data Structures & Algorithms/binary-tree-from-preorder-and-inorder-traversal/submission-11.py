# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        index = {val: i for i, val in enumerate(inorder)}
        pre = 0

        def dfs(low, high):
            nonlocal pre
            if low>high:
                return None
            root = TreeNode(preorder[pre])
            pre+=1
            mid = index[root.val]
            root.left = dfs(low, mid-1)
            root.right = dfs(mid+1, high)
            return root
        return dfs(0, len(inorder)-1)
