class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        l1, l2 = 0,0
        while l1<=len(word1)-1 and l2<=len(word2)-1:
            result.append(word1[l1])
            result.append(word2[l2])
            l1+=1
            l2+=1
        if l1<=len(word1)-1:
            while l1<=len(word1)-1:
                result.append(word1[l1])
                l1+=1
        if l2<=len(word2)-1:
            while l2<=len(word2)-1:
                result.append(word2[l2])
                l2+=1
        return "".join(result)

