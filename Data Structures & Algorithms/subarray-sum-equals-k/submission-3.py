class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        runningsum = 0
        count = 0
        for num in nums:
            runningsum+=num
            if runningsum - k in prefixSum:
                count+=prefixSum[runningsum-k]
            prefixSum[runningsum] = prefixSum.get(runningsum, 0)+1
        
        return count