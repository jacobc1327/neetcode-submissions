class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numtoletter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []
        cur = []
        def backtrack(i):
            if digits=="":
                return
            if i == len(digits):
                result.append("".join(cur))
                return
            for char in numtoletter[digits[i]]:
                cur.append(char)
                backtrack(i+1)
                cur.pop()
        backtrack(0)
        return result
