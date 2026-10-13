import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]
        distance = {node: float("inf") for node in range(1, n+1)}
        distance[k] = 0

        for source, target, time in times:
            adj[source].append((target, time))
        
        #time, node
        minheap = [(0, k)]

        while minheap:
            currentdistance, currentnode = heapq.heappop(minheap)
            if currentdistance> distance[currentnode]:
                continue
            for neighbour, weight in adj[currentnode]:
                totaldistance= currentdistance+weight

                if totaldistance<distance[neighbour]:
                    distance[neighbour] = totaldistance
                    heapq.heappush(minheap, (totaldistance, neighbour))

        maxtime = max(distance.values())

        return maxtime if maxtime<float("inf") else -1

