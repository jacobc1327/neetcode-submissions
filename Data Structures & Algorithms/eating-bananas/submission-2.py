class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kleft = 1
        kright = max(piles)
        result = kright
        while kleft<=kright:
            k = (kleft+kright)//2

            totalTime = 0
            for p in piles:
                totalTime+= math.ceil(float(p)/k)
            if totalTime<=h:
                res = k
                kright = k-1
            else:
                kleft = k+1
        return res
