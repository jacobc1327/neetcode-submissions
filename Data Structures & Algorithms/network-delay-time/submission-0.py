class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]
        for u, v, t in times:
            adj[u].append((v, t))

        timer = [float("inf")]*(n+1) 
        timer[k] = 0
        heap = [(0, k)]
        #time, node
        while heap:
            time, node = heapq.heappop(heap)    
            if time>timer[node]:
                continue
            for v, w in adj[node]:
                if time + w < timer[v]:
                    timer[v] = time+w
                    heapq.heappush(heap, (timer[v], v))
        return max(timer[1:]) if max(timer[1:])<float("inf") else -1