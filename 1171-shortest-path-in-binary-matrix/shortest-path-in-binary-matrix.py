from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n= len(grid)
        m= len(grid[0])
        if grid[0][0] ==1 or grid[n-1][m-1]==1:
            return -1
        if n == 1 and m ==1:
            return 1
        visited = [[0] * m for _ in range(n)]
        q = deque([(0,0,1)])
        visited[0][0] =1
        dir_r = [-1,-1,-1,0,0,1,1,1]
        dir_c = [-1,0,1,-1,1,-1,0,1]

        while q:
            di,dj,dist = q.popleft()
            for d in range(8):
                i = dir_r[d] + di
                j = dir_c[d] + dj
                if 0<=i<n and 0<=j<m and visited[i][j] ==0 and grid[i][j]==0:
                    if i == n-1 and j ==n-1:
                        return dist +1
                    visited[i][j] =1
                    q.append((i,j,dist+1))
        return -1



        