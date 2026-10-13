class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        efforts = [[float("inf")]*cols for _ in range(rows)]
        efforts[0][0] = 0

        heap = [(0,0,0)]

        while heap:
            e, r, c = heapq.heappop(heap)
            if e>efforts[r][c]:
                continue
            if (r, c) == (rows-1, cols-1):
                return e
            for dr,dc in [(1,0), (-1,0), (0,-1), (0,1)]:
                nr, nc = dr+r, dc+c
                if 0<=nr<rows and 0<=nc<cols:
                    ne = max(e, abs(heights[r][c]-heights[nr][nc]))
                    if ne<efforts[nr][nc]:
                        efforts[nr][nc]=ne
                        heapq.heappush(heap, (ne, nr, nc))
        return 0
