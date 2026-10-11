class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0]*numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] +=1
        
        

        q = deque(i for i in range(len(indegree)) if indegree[i]==0)
        toposort = []
        while q:
            course = q.popleft()
            toposort.append(course)

            for nextcourse in adj[course]:
                indegree[nextcourse]-=1
                if indegree[nextcourse]==0:
                    q.append(nextcourse)

        return toposort if len(toposort)==numCourses else []
