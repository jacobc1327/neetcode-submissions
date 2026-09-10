class Solution:
    import math
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            distance = -(x**2 + y**2)
            heapq.heappush(maxHeap, [distance, x, y])
            if len(maxHeap)>k:
                heapq.heappop(maxHeap)

        result = []
        while maxHeap:
            distance, x, y = heapq.heappop(maxHeap)
            result.append([x,y])
        return result