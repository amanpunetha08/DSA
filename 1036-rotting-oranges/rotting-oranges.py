from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()

        # find all rotten oranges and fresh ones
        fresh =0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] ==1:
                    fresh+=1


        dir_i = [ 0, 0, -1, 1]
        dir_j = [ -1, 1, 0, 0]
        count = 0
        while q:
            length = len(q)
            for k in range(length):
                i,j = q.popleft()
                for d in range(4):
                    di = i + dir_i[d]
                    dj = j + dir_j[d]
                    if di >=0 and di <n and dj >=0 and dj <m and grid[di][dj] ==1:
                        grid[di][dj] =2
                        q.append((di,dj))
                        fresh-=1
            count+=1
        if fresh !=0:
            return -1
        return max(0,count -1)


        