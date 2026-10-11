class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        distinct = set()

        def dfs(r, c, direction, path):
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            # 2. Water or already visited land check
            if grid[r][c] == 0:
                return
                
            grid[r][c] = 0 # Mark as visited
            path.append(direction) # Record movement
    
            dfs(r + 1, c, 'D', path)
            dfs(r - 1, c, 'U', path)
            dfs(r, c + 1, 'R', path)
            dfs(r, c - 1, 'L', path)
    
            path.append('B') # Record backtracking


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    islandpath = []
                    dfs(r, c, "S", islandpath)
                    signature = tuple(islandpath)
                    #signature = "".join(islandpath)
                    distinct.add(signature)
        return len(distinct)