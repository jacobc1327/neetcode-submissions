class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        adj = [[] for i in range(n)]

        for (node1, node2), weight in zip(edges, succProb):
            adj[node1].append((node2, weight))
            adj[node2].append((node1, weight))

        probs = [0.0] * n
        probs[start_node] = 1.0
        maxheap = [(-1.0, start_node)]

        while maxheap:
            currentprob, currentnode = heapq.heappop(maxheap)
            currentprob = -currentprob

            if currentnode == end_node:
                return currentprob
            
            if currentprob < probs[currentnode]:
                continue

            for nextnode, weight in adj[currentnode]:
                totalprob = currentprob * weight
                if totalprob > probs[nextnode]:
                    probs[nextnode] = totalprob
                    heapq.heappush(maxheap, (-totalprob, nextnode))

        return 0.0