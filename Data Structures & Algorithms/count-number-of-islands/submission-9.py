class Solution:
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        count=0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    count+=1
                    stack = [(r,c)]
                    grid[r][c]="0"
                    while stack:
                        cr, cc = stack.pop()
                        for dr, dc in directions:
                            nr, nc = cr+dr, cc+dc
                            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="1":
                                stack.append((nr,nc))
                                grid[nr][nc] = "0"


        return count