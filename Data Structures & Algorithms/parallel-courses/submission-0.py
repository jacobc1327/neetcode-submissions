class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        adj = [[] for i in range(n+1)]
        indegree = [0] * (n+1)

        for prev, course in relations:
            adj[prev].append(course)
            indegree[course]+=1
        
        q = deque(i for i in range(len(indegree)) if indegree[i]==0)
        semesters = taken = 0 
        #elements in the toplogical sort

        while q:
            semesters+=1
            for _ in range(len(q)):
                course = q.popleft()
                taken+=1
                for nextclass in adj[course]:
                    indegree[nextclass]-=1
                    if indegree[nextclass]==0:
                        q.append(nextclass)

        return semesters if taken == n+1 else -1
