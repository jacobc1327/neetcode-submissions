class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            for i in range(1, len(nums)):
                prev = dp[i-2] if i>=2 else 0 
                dp[i] = max(prev+nums[i], dp[i-1])
            return dp[-1]

        if len(nums)==1:
            return nums[0]
        
        maxmoney = max(rob1(nums[1:]), rob1(nums[:-1]))
        return maxmoney

        