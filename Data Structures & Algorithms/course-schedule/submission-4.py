from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = [[] for i in range(numCourses)]
        indegree = [0]*numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course]+=1

        q = deque(i for i in range(len(indegree)) if indegree[i]==0)
        count=0

        while  q:
            current = q.popleft()
            count+=1
            for nextcourse in adj[current]:
                indegree[nextcourse]-=1
                if indegree[nextcourse]==0:
                    q.append(nextcourse)
        return count==numCourses
