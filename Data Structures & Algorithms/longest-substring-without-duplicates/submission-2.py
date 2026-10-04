class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        numset = set()
        longest = 0

        for right in range(len(s)):
            while s[right] in numset:
                numset.remove(s[left])
                left+=1
            numset.add(s[right])
            longest = max(longest, right-left+1)
        return longest