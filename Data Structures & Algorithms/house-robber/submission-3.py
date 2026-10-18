from functools import cache
class Solution:

    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        dp = [0] * len(nums)
        dp[0]=nums[0]
        for i in range(1, len(nums)):
            prev = dp[i-2] if i>=2 else 0
            dp[i] = max(prev+nums[i], dp[i-1])
        return dp[-1]