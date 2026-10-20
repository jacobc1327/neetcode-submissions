class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Map to store the first occurrence of (runningsum % k) -> index
        # Initialize with {0: -1} to handle subarrays starting from index 0
        remainder_map = {0: -1}
        running_sum = 0
        
        for i, num in enumerate(nums):
            running_sum += num
            remainder = running_sum % k
            
            if remainder in remainder_map:
                # Check if the length of the subarray is at least 2
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                # Only store the first time we see a remainder to maximize subarray length
                remainder_map[remainder] = i
                
        return False