class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:

        adj = [[] for i in range(n+1)]
        incoming = [0]*(n+1)

        for prev, course in relations:
            adj[prev].append(course)
            incoming[course]+=1
        semesters = taken = 0
        q = deque(i for i in range(len(incoming)) if incoming[i]==0)

        while q:

            semesters+=1
            for _ in range(len(q)):
                course = q.popleft()
                taken+=1
                for nextcourse in adj[course]:
                    incoming[nextcourse]-=1
                    if incoming[nextcourse]==0:
                        q.append(nextcourse)

        return semesters if taken==n+1 else -1