class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#directed graph

        adj = [[] for _ in range(n)]
        for origin, destin, price in flights:
            adj[origin].append((destin, price))
        
        recorded_stops = [float("inf")] * n
        recorded_stops[src] = 0
        #price, node, flights used
        minheap = [(0, src, 0)]

        while minheap:
            curprice, node, stops = heapq.heappop(minheap)
            if node == dst:
                return curprice
            if stops > recorded_stops[node] or stops > k:
                continue
            recorded_stops[node] = stops
        
            
            for v, w in adj[node]:
                heapq.heappush(minheap, (curprice+w, v, stops+1))
        return -1