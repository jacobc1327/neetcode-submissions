class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        longest = 0
        left = 0
        freq = {}
        maxfreq = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0)+1
            maxfreq = max(maxfreq, freq[s[right]])
            while (right-left+1)-maxfreq > k:
                freq[s[left]] -=1
                left+=1
            longest = max(longest, right-left+1)
        return longest 