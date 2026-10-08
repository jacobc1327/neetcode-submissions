class Solution:
    def numIslands(self, grid):
        def sink(grid, r, c, rows, cols):
            stack = [(r, c)]
            grid[r][c] = '0'
            while stack:
                x, y = stack.pop()
                for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                        grid[nx][ny] = '0'
                        stack.append((nx, ny))
        
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0
        for r in range(rows):
            if '1' in grid[r]:
                for c in range(cols):
                    if grid[r][c] == '1':
                        count += 1
                        sink(grid, r, c, rows, cols)   # DFS or BFS below
        return count