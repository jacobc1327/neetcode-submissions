class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, path = [], []

        def backtracking(openCount, closedCount):
            if openCount==closedCount==n:
                result.append("".join(path))
                return
            if openCount < n:
                path.append("(")
                backtracking(openCount+1, closedCount)
                path.pop()
            if closedCount < openCount:
                path.append(")")
                backtracking(openCount, closedCount+1)
                path.pop()

        backtracking(0,0)
        return result