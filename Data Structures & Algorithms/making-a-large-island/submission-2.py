import collections
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        m, n = len(grid), len(grid[0])

        def bfs(r: int, c: int) -> int:
            nonlocal directions, m, n, grid
            seen = set([(r, c)])
            bfs_q = collections.deque([(r, c)])

            while bfs_q:
                c_r, c_c = bfs_q.popleft()
                for dr, dc in directions:
                    n_r, n_c = c_r + dr, c_c + dc
                    if not (0 <= n_r < m and 0 <= n_c < n):
                        continue
                    if (n_r, n_c) in seen or grid[n_r][n_c] == 0:
                        continue
                    bfs_q.append((n_r, n_c))
                    seen.add((n_r, n_c))

            return len(seen)

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    max_area = max(max_area, bfs(i, j))
        return max_area if max_area > 0 else m*n
