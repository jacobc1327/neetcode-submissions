class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque([])
        time = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    grid[r][c] = -1
                    q.append((r,c))

        while q:
            rottedhappened = False
            for i in range(len(q)):
                
                cr, cc = q.popleft()
                for dr, dc in directions:
                    nr, nc = cr+dr, cc+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        q.append((nr, nc))
                        grid[nr][nc]=-1
                        rottedhappened = True

            if rottedhappened:
                time+=1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return -1
        return time