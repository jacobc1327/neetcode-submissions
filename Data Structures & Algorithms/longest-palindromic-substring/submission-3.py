class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for i in range(n)]
        start, length = 0,1
        for j in range(n): #right pointer
            for i in range(j+1): #left pointer
                if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > length:
                        start, length = i, j-i+1
        return s[start:start+length]