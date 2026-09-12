class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Undo
            subset.pop()

            # Skip duplicates before exclude branch
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Exclude nums[i] and its duplicates
            dfs(i + 1)

        dfs(0)
        return result