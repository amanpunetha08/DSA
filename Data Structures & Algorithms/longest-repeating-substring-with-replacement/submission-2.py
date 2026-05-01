class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            index = ord(s[r]) - ord('A')
            count[index]+=1
            maxf = max(maxf,count[index])

            while (r-l+1) - maxf >k:
                index = ord(s[l]) - ord('A')
                count[index]-=1
                l+=1
            res = max(res,r-l+1)
        return res
        