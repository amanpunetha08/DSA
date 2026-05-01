class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length_s = len(s)
        length_t = len(t)
        if length_s > length_t:
            return False
        
        if length_s == length_t:
            if s !=t:
                return False
            return True
        
        point_s = point_t = 0

        while point_s < length_s and point_t < length_t:
            if s[point_s] == t[point_t]:
                point_s+=1
                point_t+=1
            else:
                point_t+=1
        
        return point_s == length_s

        

        