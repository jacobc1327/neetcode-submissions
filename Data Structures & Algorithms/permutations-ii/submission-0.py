class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result, path = [], []
        used = set()
        nums.sort()

        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if i in used:
                    continue
                if i>0 and nums[i]==nums[i-1] and i-1 in used:
                    continue
                used.add(i)
                path.append(nums[i])
                backtrack()
                path.pop()
                used.remove(i)
        backtrack()
        return result