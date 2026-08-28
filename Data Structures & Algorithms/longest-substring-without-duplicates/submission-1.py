class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        length = 0
        numset = set()
        for right in range(len(s)):
            while s[right] in numset:
                numset.remove(s[left])
                left += 1
            numset.add(s[right])
            length = max(length, right-left+1)
        return length