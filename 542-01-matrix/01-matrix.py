class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] ==0:
                    q.append((i,j))
        dir_i = [0,0,-1,1]
        dir_j = [-1,1,0,0]
        ans = [[0] *m for _ in range(n)]
        count=0
        while q:
            length = len(q)
            count+=1
            for k in range(length):
                i,j = q.popleft()
                for d in range(4):
                    di, dj = i + dir_i[d], j + dir_j[d]
                    if 0<= di < n and 0<= dj < m and mat[di][dj] ==1 and ans[di][dj] == 0:
                        ans[di][dj] = count
                        q.append((di,dj))
        return ans

        