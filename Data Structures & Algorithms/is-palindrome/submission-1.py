class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        s = "".join(c for c in s if c.isalnum()).lower()
        r = len(s)-1
        while l<=r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
        