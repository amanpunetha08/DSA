class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_s = s.split()
        return len(list_s[-1])
        