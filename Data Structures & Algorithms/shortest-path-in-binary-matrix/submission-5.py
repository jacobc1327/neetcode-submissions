class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        n = len(grid)
        target = (n-1,n-1)
        if grid[0][0]!=0 or grid[n - 1][n - 1] != 0:
            return -1 
        pathlength = 0
        q = deque([(0,0,1)])
        grid[0][0] = 1    
        while q: 
            cr, cc, distance = q.popleft()
            if (cr, cc) == target:
                return distance
            for dr, dc in directions:
                nr, nc = cr+dr, cc+dc
                if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0:
                    q.append((nr, nc, distance+1))
                    grid[nr][nc]=1
        return -1