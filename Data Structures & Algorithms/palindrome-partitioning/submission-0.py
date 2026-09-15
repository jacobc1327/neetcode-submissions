class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        temp = []
        def backtrack(i):
            if i == len(s):
                result.append(temp.copy())
                return
            for end in range(i, len(s)):
                substring = s[i:end+1]
                if substring == substring[::-1]:
                    temp.append(substring)
                    backtrack(end+1)
                    temp.pop()

        backtrack(0)
        return result