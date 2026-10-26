class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums.sort()
        firstNum = nums[0]
        for num in nums:
            if firstNum == num:
                firstNum += 1
            else:
                return False
        return True