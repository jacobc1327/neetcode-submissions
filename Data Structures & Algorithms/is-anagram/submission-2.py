class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        chars, chart = {}, {}
        for i in s:
            chars[i] = chars.get(i, 0)+1
        for i in t:
            chart[i] = chart.get(i, 0)+1
        return chars==chart