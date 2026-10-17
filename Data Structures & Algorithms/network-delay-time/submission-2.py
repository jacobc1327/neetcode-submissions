import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]
        
        distances = {i:float("inf") for i in range(1, n+1)}
        distances[k] = 0
        for source, target, time in times:
            adj[source].append((target, time))
        
        #distance, node
        minheap = [(0, k)]

        while minheap:
            currentdistance, currentnode = heapq.heappop(minheap)
            if currentdistance> distances[currentnode]:
                continue
            
            for nextnode, nextdistance in adj[currentnode]:
                totaldistance = currentdistance + nextdistance
                if totaldistance < distances[nextnode]:
                    distances[nextnode] = totaldistance
                    heapq.heappush(minheap, (totaldistance, nextnode))
        maxtime = max(distances.values())
        return maxtime if maxtime<float("inf") else -1