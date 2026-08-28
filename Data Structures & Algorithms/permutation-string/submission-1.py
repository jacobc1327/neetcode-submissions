class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1dict = {}
        s2dict = {}
        n = len(s1)
        for i in range(n):
            s1dict[s1[i]] = s1dict.get(s1[i], 0)+1
        left = 0
        for i in range(n-1):
            s2dict[s2[i]] = s2dict.get(s2[i],0)+1

        for right in range(n-1, len(s2)):
            s2dict[s2[right]] = s2dict.get(s2[right],0)+1
            if s2dict == s1dict:
                return True
            s2dict[s2[left]] -= 1
            if s2dict[s2[left]] == 0:
                del s2dict[s2[left]]
            left+=1
        return False
