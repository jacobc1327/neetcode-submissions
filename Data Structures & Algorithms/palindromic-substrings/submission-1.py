class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for i in range(n)]
        count = 0
        for j in range(n): #right
            for i in range(j+1): #left
                if s[i]==s[j] and (j-i+1<=3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    count+=1
        return count