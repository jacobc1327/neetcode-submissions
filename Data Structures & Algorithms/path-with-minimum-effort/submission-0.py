class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        effort = [[float("inf")] * cols for _ in range(rows)]
        effort[0][0] = 0
        heap = [(0,0,0)] #EFFORT, R, C

        while heap:
            e, r, c = heapq.heappop(heap)
            if e > effort[r][c]:
                continue
            if (r, c) == (rows-1, cols-1):
                return e
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = dr+r, dc+c

                if 0<=nr<rows and 0<=nc<cols:
                    ne = max(e, abs(heights[nr][nc]-heights[r][c]))
                    if ne<effort[nr][nc]:
                        effort[nr][nc] = ne
                        heapq.heappush(heap, (ne, nr, nc))
        return 0