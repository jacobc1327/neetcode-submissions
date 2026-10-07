class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currentsum = 0
        prefix = {0:1}
#{base case} the sum of 0 being 1
#current sum - k = 0
        count=0

        for num in nums:
            currentsum+=num

            if currentsum-k in prefix:
                count += prefix[currentsum-k]
            prefix[currentsum] = prefix.get(currentsum,0)+1
        return count
