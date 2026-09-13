class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        curComb = []

        
        def helper2(i):
            if len(curComb) == k:
                combs.append(curComb.copy())
                return
            if i > n:
                return

            for j in range(i, n + 1):
                curComb.append(j)
                helper2(j + 1)
                curComb.pop()
        
        helper2(1)
        return combs