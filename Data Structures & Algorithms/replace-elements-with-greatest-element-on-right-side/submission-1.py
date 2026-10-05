class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        maxi = 0
        for i in range(len(arr)-1, -1, -1):
            if i == len(arr)-1:
                res.append(-1)
                maxi = arr[i]
            else:
                res.append(maxi)
                maxi = max(maxi, arr[i])
        res.reverse()
        return res