class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        length_s = len(s)
        length_t = len(t)

        point_s = point_t = 0
        while point_s < length_s and point_t < length_t:
            if s[point_s] == t[point_t]:
                point_s+=1
                point_t+=1
            else:
                point_s+=1
    
        
        return length_t - point_t
        