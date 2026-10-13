class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direction = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        n = len(grid)

        result = grid[n-1][n-1]

        if grid[0][0]!=0 or grid[n - 1][n - 1] != 0:
            return -1 
        q = deque([(0,0,1)])
        grid[0][0]=1
        while q:
            r, c, distance = q.popleft()
            if r==n-1 and c==n-1:
                return distance

            for dr, dc in direction:
                nr, nc = r+dr, c+dc
                if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0:
                    q.append((nr, nc, distance+1))
                    grid[nr][nc]=1
        return -1
