class Solution:
    def scoreOfString(self, s: str) -> int:
        length_of_string = len(s)
        score = 0
        for i in range(1,length_of_string):
            score += abs(ord(s[i]) - ord(s[i-1]))
        return score

        