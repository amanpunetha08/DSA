class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        score = dict()
        n = 0
        for edge in edges:
            if edge[0] not in score:
                score[edge[0]] =0
            score[edge[0]]+=1
            if edge[1] not in score:
                score[edge[1]] = 0
            score[edge[1]]+=1
            maxi = max(edge[0],edge[1])
            n = max(n,maxi)
        
        for key,value in score.items():
            if value == n-1:
                return key
        return -1


        