class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))
        
        
    def rob1(self, nums):

        if not nums:
            return 0
        dp = [0] * len(nums)
        dp[0]=nums[0]
        for i in range(1, len(nums)):
            prev2 = dp[i-2] if i>=2 else 0
            dp[i] = max(prev2+nums[i], dp[i-1])
        return dp[-1]