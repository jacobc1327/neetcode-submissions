import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for source, target, time in times:
            adj[source].append((target, time))
        
        distances = {i: float("inf") for i in range(1, n+1)}
        distances[k] = 0
        #distance, k
        minheap = [(0, k)]

        while minheap:
            currentdistance, currentnode = heapq.heappop(minheap)
            if currentdistance > distances[currentnode]:
                continue
            for nextnode, weight in adj[currentnode]:
                totaldistance = currentdistance + weight
                if totaldistance < distances[nextnode]:
                    distances[nextnode] = totaldistance
                    heapq.heappush(minheap, (totaldistance, nextnode))

        mintime = max(distances.values())
        return mintime if mintime < float("inf") else -1
