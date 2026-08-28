class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        chars = {}
        left = 0
        for right in range(len(s)):
            chars[s[right]] = chars.get(s[right], 0)+1
            max_freq = max(chars.values())
            
            if (right - left + 1) - max_freq <= k:

                longest = max(longest, right-left+1)
            else:
                chars[s[left]] -= 1
                left += 1

        return longest
