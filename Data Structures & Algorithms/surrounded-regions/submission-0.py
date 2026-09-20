class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        safe = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if (
                r < 0 or r >= ROWS
                or c < 0 or c >= COLS
                or board[r][c] != "O"
                or (r, c) in safe
            ):
                return

            safe.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Find all O's connected to the boundary
        for r in range(ROWS):
            for c in range(COLS):
                if (
                    r == 0 or r == ROWS - 1
                    or c == 0 or c == COLS - 1
                ):
                    if board[r][c] == "O":
                        dfs(r, c)

        # Flip every O that isn't connected to the boundary
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in safe:
                    board[r][c] = "X"