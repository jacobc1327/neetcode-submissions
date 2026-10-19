class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #shortes clear path, sounds like matrix bfs approach
        n = len(grid) #nxn matrix
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        if grid[n-1][n-1]!=0 or grid[0][0]!=0:
            return -1
        #r, c, distance
        queue = deque([(0,0,1)])
        visited = set()

        while queue:
            r, c, distance = queue.popleft()
            visited.add((r,c))
            if (r, c) == (n-1, n-1):
                return distance
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0<=nr<n and 0<=nc<n and (nr, nc) not in visited and grid[nr][nc]==0:
                    queue.append((nr, nc, distance+1))
        return -1
