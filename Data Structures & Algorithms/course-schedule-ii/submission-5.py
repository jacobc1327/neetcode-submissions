class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] +=1
        queue = deque(i for i in range(len(indegree)) if indegree[i]==0)
        toposort = []

        while queue:
            currentcourse = queue.popleft()
            toposort.append(currentcourse)
            for nextcourse in adj[currentcourse]:
                indegree[nextcourse] -=1
                if indegree[nextcourse] == 0:
                    queue.append(nextcourse)
        
        return toposort if len(toposort) == numCourses else []