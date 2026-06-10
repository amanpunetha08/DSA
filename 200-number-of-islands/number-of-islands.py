class Solution:
    def dfs(self,i,j,n,m,visited,grid):
        if i < 0 or i >=n or j <0 or j >=m or grid[i][j] == "0" or visited[i][j] ==1:
            return
        
        visited[i][j] = 1
        self.dfs(i+1,j,n,m,visited,grid)
        self.dfs(i-1,j,n,m,visited,grid)
        self.dfs(i,j+1,n,m,visited,grid)
        self.dfs(i,j-1,n,m,visited,grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid),len(grid[0])
        visited = [ [0] *m for i in range(n)]
        count=0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and grid[i][j] == "1":
                    self.dfs(i,j,n,m,visited,grid)
                    count+=1
        return count
    
        