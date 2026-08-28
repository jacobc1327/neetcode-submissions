class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        longest = 0
        chars = {}
        left = 0
        maxfreq = 0 
        for right in range(len(s)):
            chars[s[right]] = chars.get(s[right], 0)+1
            maxfreq = max(maxfreq, chars[s[right]])
            while (right-left+1)-maxfreq > k:
                chars[s[left]] -=1
                left+=1
            longest = max(longest, right-left+1)
        return longest