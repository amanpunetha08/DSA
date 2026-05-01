from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_collections = Counter(s)
        t_collections = Counter(t)
        return s_collections == t_collections
        