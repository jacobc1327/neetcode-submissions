# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 1. Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Found the node! Handle deletion cases:
            
            # Case 1 & 2: No children or only one child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Case 3: Two children
            # Find the inorder successor (minimum value in the right subtree)
            successor = self._find_min(root.right)
            # Replace current value with successor's value
            root.val = successor.val
            # Recursively delete the successor node from the right subtree
            root.right = self.deleteNode(root.right, successor.val)
            
        return root

    def _find_min(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node