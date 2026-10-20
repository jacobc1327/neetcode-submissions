class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, path = [], []
        used = set()

        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                path.append(nums[i])
                backtrack()
                path.pop()
                used.remove(nums[i])

        backtrack()
        return result