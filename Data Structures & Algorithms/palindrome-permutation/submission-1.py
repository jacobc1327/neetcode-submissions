class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = {}
        for char in s:
            if char in freq:
                del freq[char]
            else:
                freq[char] = 1
        
        if len(freq)==1 or len(freq)==0:
            return True
        else:
            return False