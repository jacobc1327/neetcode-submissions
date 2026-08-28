class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paran = {"]": "[", "}": "{",")": "(",}

        for chars in s:
            if chars in paran:
                if stack and stack[-1]==paran[chars]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(chars)
        if not stack:
            return True
        else:
            return False
