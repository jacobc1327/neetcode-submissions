class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hashset = set()
        for char in s:
            if char in hashset:
                hashset.remove(char)
            else:
                hashset.add(char)
        
        return len(hashset)<=1