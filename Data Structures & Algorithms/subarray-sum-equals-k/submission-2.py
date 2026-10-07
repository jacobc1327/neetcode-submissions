class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        runningsum = 0
        prefix = {0:1}
        count=0
        for num in nums:
            runningsum+=num
            if runningsum-k in prefix:
                count+=prefix[runningsum-k]
            prefix[runningsum]=prefix.get(runningsum, 0)+1

        return count