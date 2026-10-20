class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for course, prev in prerequisites:
            adj[prev].append(course)
            indegree[course]+=1
        
        toposort = []

        queue = deque(i for i in range(len(indegree)) if indegree[i]==0)
        
        while queue:
            currentcourse = queue.popleft()
            toposort.append(currentcourse)
            for nei in adj[currentcourse]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)

        return toposort if len(toposort)==numCourses else []