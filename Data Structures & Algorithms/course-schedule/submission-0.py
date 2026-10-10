from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for courses, prerequisite in prerequisites:
            adj[prerequisite].append(courses)
            indegree[courses]+=1
        q = deque(i for i in range(numCourses) if indegree[i]==0)

        finished = 0

        while q:
            course = q.popleft()
            finished +=1
            for nextcourse in adj[course]:
                indegree[nextcourse]-=1

                if indegree[nextcourse] ==0:
                    q.append(nextcourse)
        return finished == numCourses