# from collections import deque
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         adj = [[] for _ in range(numCourses)]
#         for edge in prerequisites:
#             u,v = edge[0],edge[1]
#             adj[v].append(u)

#         indegree = [0] * numCourses
#         for u in range(numCourses):
#             for v in adj[u]:
#                 indegree[v] +=1
    
#         q = deque([i for i in range(numCourses) if indegree[i] == 0])
#         result = []

#         while q:
#             node = q.popleft()
#             result.append(node)
#             for v in adj[node]:
#                 indegree[v]-=1
#                 if indegree[v] ==0:
#                     q.append(v)
#         return True if len(result) == numCourses else False



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        
        visited = [0] * numCourses

        def dfs(i):
            visited[i] = 1
            for v in adj[i]:
                if visited[v] == 0:
                    if not dfs(v):
                        return False
                if visited[v] == 1:
                    return False
            visited[i] = 2
            return True

        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return False
        return True


        