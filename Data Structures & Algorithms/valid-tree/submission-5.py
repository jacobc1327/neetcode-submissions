class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

#no cycle
#fully connected
        adj = [[] for i in range(n)]
        visited = set()
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for neighbour in adj[node]:
                if neighbour == parent:
                    continue
                if not dfs(neighbour, node):
                    return False
            return True


        return dfs(0, -1) and len(visited) == n
