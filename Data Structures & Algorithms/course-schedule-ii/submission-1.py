class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for i in range(numCourses)]
        indegrees = [0] * numCourses

        for course, prereq in prerequisites:
            adjList[prereq].append(course)
            indegrees[course]+=1
        
        q = deque(i for i in range(len(indegrees)) if indegrees[i]==0)

        topSort = []

        while q:
            course = q.popleft()
            topSort.append(course)

            for nextcourse in adjList[course]:
                indegrees[nextcourse] -=1

                if indegrees[nextcourse] ==0:
                    q.append(nextcourse)

        return topSort if len(topSort)==numCourses else []
