class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlength = float("inf")

        left = 0
        total = 0
        for right in range(len(nums)):
            total+=nums[right]
            while total>=target:
                minlength = min(right-left+1, minlength)
                total -= nums[left]
                left+=1

        return 0 if minlength == float("inf") else minlength
