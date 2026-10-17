class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        mapped_values = set()
        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            else:
                if t[i] in mapped_values:
                    return False
                hashmap[s[i]] = t[i]
                mapped_values.add(t[i])
        
        return True