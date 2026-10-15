class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #shortes clear path, sounds like matrix bfs approach
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        n = len(grid)
        if grid[0][0]!=0 or grid[n-1][n-1]!=0:
            return -1
        #q has r, c, distance
        q = deque([(0,0,1)])
        visited = set((0,0))

        while q:
            r, c, distance = q.popleft()
            if (r, c) == (n-1, n-1):
                return distance
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0 and (nr, nc) not in visited:
                    q.append((nr, nc, distance+1))
                    visited.add((r,c))
        return -1
        