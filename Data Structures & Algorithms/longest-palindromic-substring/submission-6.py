class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for i in range(n)]
        start, longest = 0, 1
        for j in range(n):
            for i in range(j):
                if s[i]==s[j] and (j-i+1<=3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > longest:
                        start, longest = i, j-i+1
        return s[start:start+longest]