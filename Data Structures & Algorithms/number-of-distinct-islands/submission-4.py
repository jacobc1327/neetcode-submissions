class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        distinct = set()

        def dfs(r, c, direction, path):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!=1:
                return
            grid[r][c]=0
            path.append(direction)

            dfs(r+1, c, "D", path)
            dfs(r-1, c, "U", path)
            dfs(r, c+1, "R", path)
            dfs(r, c-1, "L", path)

            path.append("B")

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    islandpath = []
                    dfs(r, c, "S", islandpath)
                    islandpathjoined = "".join(islandpath)
                    distinct.add(islandpathjoined)

        return len(distinct)