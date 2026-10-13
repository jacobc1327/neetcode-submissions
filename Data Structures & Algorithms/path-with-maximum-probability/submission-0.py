class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for _ in range(n)]
        for (a, b), weight in zip(edges, succProb):
            adj[a].append((b, weight))
            adj[b].append((a, weight))

        probs = [0.0] * n
        if start_node == end_node:
            probs[start_node] = 1.0
        
        maxheap = [(-1.0, start_node)]

        while maxheap:
            curprob, node = heapq.heappop(maxheap)
            curprob = -curprob

            if node == end_node:
                return curprob
            
            if curprob < probs[node]:
                continue

            for v, w in adj[node]:
                totalprob = curprob * w
                if totalprob > probs[v]:
                    probs[v] = totalprob
                    heapq.heappush(maxheap, (-totalprob, v))
        
        return probs[end_node]
