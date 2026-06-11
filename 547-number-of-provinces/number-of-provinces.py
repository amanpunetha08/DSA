class Solution:
    def dfs(self,i,n,visited,isConnected):
        visited[i] = 1
        for j in range(n):
            if isConnected[i][j] ==1 and not visited[j]:
                self.dfs(j,n,visited,isConnected)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        m = len(isConnected[0])

        visited = [0] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                self.dfs(i,n,visited,isConnected)
                count+=1
        return count
        