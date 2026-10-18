class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(low, high):
            if low>high:
                return 

            middle = (low+high)//2
            root = TreeNode(nums[middle])
            root.left = build(low, middle-1)
            root.right = build(middle+1, high)
            return root
        
        return build(0, len(nums)-1)