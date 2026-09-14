class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        used = set()

        def dfs():
            if len(perm)==len(nums):
                result.append(perm.copy())
                return
            
            for num in nums:
                if num in used:
                    continue
                perm.append(num)
                used.add(num)
                dfs()
                perm.pop()
                used.remove(num)
        dfs()
        return result