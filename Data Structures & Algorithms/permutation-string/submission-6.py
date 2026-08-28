class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n = len(s1)
        s1dict = {}
        s2dict = {}

        for i in range(n):
            s1dict[s1[i]] = s1dict.get(s1[i], 0) + 1
            s2dict[s2[i]] = s2dict.get(s2[i], 0) + 1

        if s1dict == s2dict:
            return True

        left = 0

        for right in range(n, len(s2)):
            s2dict[s2[right]] = s2dict.get(s2[right], 0) + 1

            s2dict[s2[left]] -= 1
            if s2dict[s2[left]] == 0:
                del s2dict[s2[left]]

            left += 1

            if s1dict == s2dict:
                return True

        return False