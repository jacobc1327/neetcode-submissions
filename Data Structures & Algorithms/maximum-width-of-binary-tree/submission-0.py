# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue=deque([(root,0)])
        answer=1
        while queue:
            base=queue[0][1];last=0
            for _ in range(len(queue)):
                node,index=queue.popleft();index-=base;last=index
                if node.left:queue.append((node.left,2*index))
                if node.right:queue.append((node.right,2*index+1))
            answer=max(answer,last+1)
        return answer