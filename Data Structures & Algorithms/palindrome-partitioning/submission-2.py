class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, path = [], []
        def backtrack(i):
            if i == len(s):
                result.append(path[:])
                return
            for end in range(i, len(s)):
                substring = s[i:end+1]
                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(end+1)
                    path.pop()
        backtrack(0)
        return result