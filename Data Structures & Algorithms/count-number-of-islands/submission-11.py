class Solution:
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        numislands = 0


        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!="1":
                return
            grid[r][c]="0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r,c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    numislands+=1
                    
                    dfs(r, c)
        return numislands
                        