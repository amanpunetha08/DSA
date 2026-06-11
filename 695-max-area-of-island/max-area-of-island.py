class Solution:
    def dfs(self,i,j,n,m,visited, grid, count):
        if i < 0 or  i>=n or j<0 or j>=m or visited[i][j] == 1 or grid[i][j] == 0:
            return
        
        count[0]+=1
        visited[i][j] = 1

        self.dfs(i+1,j,n,m,visited,grid,count)
        self.dfs(i-1,j,n,m,visited,grid,count)
        self.dfs(i,j+1,n,m,visited,grid,count)
        self.dfs(i,j-1,n,m,visited,grid,count)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0] * m for _ in range(n)]
        max_count = 0
        count = [0]
        
        for i in range(n):
            for j in range(m):
                if visited[i][j] ==0 and grid[i][j] ==1:
                    self.dfs(i,j,n,m,visited,grid,count)
                    max_count = max(count[0],max_count)
                    count[0] = 0
        return max_count
        