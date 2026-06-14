from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        
        indegree = [0] * numCourses
        for u in range(numCourses):
            for v in adj[u]:
                indegree[v]+=1
        q = deque([i for i in range(numCourses) if indegree[i] ==0 ])
        result = []

        while q:
            node = q.popleft()
            result.append(node)
            for v in adj[node]:
                indegree[v]-=1
                if indegree[v] ==0:
                    q.append(v)
        return result if len(result) == numCourses else []
        
        