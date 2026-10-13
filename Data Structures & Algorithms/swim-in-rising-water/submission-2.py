class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        minheap = [[grid[0][0], 0, 0]]
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        visited.add((0,0))
        while minheap:
            t, r, c = heapq.heappop(minheap)
            if r==n-1 and c==n-1:
                return t
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if(nr<0 or nc<0 or nc==n or nr==n or (nr, nc) in visited):
                    continue
                visited.add((nr,nc))
                heapq.heappush(minheap, [max(t, grid[nr][nc]), nr, nc])