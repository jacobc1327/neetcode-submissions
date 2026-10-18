# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#make a hashtable marking a positional column value to an array of nodes
#if we take right child increment column value, if we take right child we decrement. so add tuples to the queue

        queue = deque()
        hashmap = defaultdict(list)
        if root:
            queue.append((root, 0))
            #node, column value
        while queue:
            for i in range(len(queue)):
                node, col = queue.popleft()
                hashmap[col].append(node.val)
                if node.left:
                    queue.append((node.left, col-1))
                if node.right:
                    queue.append((node.right, col+1))
        result = [v for k, v in sorted(hashmap.items(), key=lambda item:item[0])]
        return result