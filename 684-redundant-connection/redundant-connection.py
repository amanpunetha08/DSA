class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] *n
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px,py = self.find(x),self.find(y)
        if px ==py:
            return False
        if self.rank[px] < self.rank[py]:
            px,py = py,px
        self.parent[py] =px
        if self.rank[px] ==self.rank[py]:
            self.rank[px]+=1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n+1)
        result = None

        for x,y in edges:
            union = dsu.union(x,y)
            if not union:
                result = [x,y]
        return result
                

        