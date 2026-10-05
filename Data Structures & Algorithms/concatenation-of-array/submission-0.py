import copy 
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        copied = copy.deepcopy(nums)
        result = nums+copied
        return result