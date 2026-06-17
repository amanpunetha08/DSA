# from collections import deque
# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#         graph = [[] for _ in range(n)]
#         for u,v in edges:
#             graph[u].append(v)
#             graph[v].append(u)
        
#         visited = {source}
#         q = deque([source])
#         while q:
#             node = q.popleft()
#             if node == destination:
#                 return True
            
#             for nei in graph[node]:
#                 if nei not in visited:
#                     visited.add(nei)
#                     q.append(nei)
#         return False

class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px,py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px,py = py,px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] +=1
        return True

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dsu = DSU(n)

        for u,v in edges:
            dsu.union(u,v)
        return dsu.find(source) == dsu.find(destination)
        