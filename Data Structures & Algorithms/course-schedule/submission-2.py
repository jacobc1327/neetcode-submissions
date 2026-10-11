from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for i in range(numCourses)]
        indegrees = [0] * numCourses

        for course, prereq in prerequisites:
            adjList[prereq].append(course)
            indegrees[course] +=1
        
        q = deque(i for i in range(len(indegrees)) if indegrees[i]==0)
            #try indegrees inside the range instead for above

        finished = 0

        while q:
            curcourse = q.popleft()
            finished+=1

            for nextcourse in adjList[curcourse]:
                indegrees[nextcourse]-=1
                if indegrees[nextcourse]==0:
                    q.append(nextcourse)

        return finished == numCourses


