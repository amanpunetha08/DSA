class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] *n
    
    def find(self,x):
        if self.parent[x] !=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px,py = self.find(x),self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px,py = py,px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px]+=1
        return True
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        m = len(isConnected[0])
        componenets = n
        dsu = DSU(n)
        for i in range(n):
            for j in range(i+1,m):
                if isConnected[i][j] == 1:
                    if dsu.union(i,j):
                       componenets-=1
        return componenets 

        